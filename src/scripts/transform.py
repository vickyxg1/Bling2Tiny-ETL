import pandas as pd
import logging


def transform_data(
    df: pd.DataFrame, mapeamento: dict, colunas_finais: list
) -> pd.DataFrame:
    """Transforma os dados conforme o mapeamento."""
    logging.info("Transformando dados.")
    df_transformado = pd.DataFrame(columns=colunas_finais)
    for coluna_final, coluna_origem in mapeamento.items():
        df_transformado[coluna_final] = (
            df[coluna_origem].fillna("") if coluna_origem in df.columns else ""
        )

    # Aplicar lógica do tipo de produto
    df_transformado = definir_tipo_produto(df_transformado)

    # Corrigir valores da coluna 'Estoque'
    df_transformado = corrigir_estoque(df_transformado)

    return df_transformado.fillna("")


def definir_tipo_produto(df: pd.DataFrame) -> pd.DataFrame:
    """
    Define o tipo do produto ('S' para filhos, 'V' para pais) sem alterar as descrições:
    """
    try:
        logging.info("Ajustando tipos de produto...")

        # Passo 1: Limpar espaços extras do código do produto pai
        df["Código do produto pai"] = df["Código do produto pai"].str.strip()

        # Passo 2: Identificar produtos filhos
        mask_filhos = df["Código do produto pai"].notna() & (
            df["Código do produto pai"] != ""
        )
        df.loc[mask_filhos, "Tipo do produto"] = "S"

        # Passo 3: Coletar códigos dos pais únicos
        codigos_pais = df.loc[mask_filhos, "Código do produto pai"].unique()

        # Passo 4: Mapear descrições dos pais
        parent_desc_dict = {}
        for codigo_pai in codigos_pais:
            codigo_pai_limpo = codigo_pai.strip()
            mask_pai = df["Código"].str.strip() == codigo_pai_limpo
            if mask_pai.any():
                parent_desc = df.loc[mask_pai, "Descrição"].iloc[0]
                parent_desc_dict[codigo_pai_limpo] = parent_desc
                df.loc[mask_pai, "Tipo do produto"] = "V"
            else:
                logging.warning(f"Código pai '{codigo_pai}' não encontrado.")

        # Passo 5: Definir 'S' para produtos não relacionados
        df["Tipo do produto"] = df["Tipo do produto"].fillna("S")

        return df
    except Exception as e:
        logging.error(f"Erro ao ajustar tipos de produto: {e}")
        raise

def corrigir_estoque(df: pd.DataFrame) -> pd.DataFrame:
    """Corrige a formatação da coluna 'Estoque', garantindo que os valores sejam inteiros corretamente formatados."""
    if "Estoque" in df.columns:
        logging.info("Corrigindo valores da coluna 'Estoque'.")
        df["Estoque"] = (
            df["Estoque"]
            .astype(str)
            .str.replace(".", "", regex=False)
            .str.replace(",", "", regex=False)
        )
        df["Estoque"] = pd.to_numeric(df["Estoque"], errors='coerce').fillna(0).astype(int)
    return df

