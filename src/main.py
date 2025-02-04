import glob
import logging
import pandas as pd
from pathlib import Path
from scripts.extract import extract_from_excel
from scripts.transform import transform_data, definir_tipo_produto
from scripts.load import salvar_em_partes
from scripts.utils import setup_logging, load_config

def main():
    # Configuração de logging
    setup_logging()
    logging.info("Iniciando processo de ETL.")

    # Carregar configurações
    config = load_config()
    
    # Extrair dados
    input_folder = Path(config["input_folder"])
    excel_files = list(input_folder.glob("*.xls*"))
    dfs = []
    
    for file in excel_files:
        # Após carregar as configurações:
        logging.info(f"Procurando arquivos em: {input_folder}")
        logging.info(f"Arquivos encontrados: {excel_files}")

        # Dentro do loop de extração:
        try:
            df = extract_from_excel(file)
            dfs.append(df)
            logging.info(f"Arquivo {file.name} processado com sucesso.")  # Novo log
        except Exception as e:
            logging.error(f"Erro ao processar {file.name}: {e}")

    # Transformar dados
    if dfs:
        # Concatenar todos os DataFrames em um único DataFrame
        df_final = pd.concat(dfs, ignore_index=True)

        # Aplicar transformações
        df_transformado = transform_data(
            df=df_final,
            mapeamento=config["mapeamento"],
            colunas_finais=config["colunas_finais"],
        )

        # Aplicar lógica do tipo de produto
        df_transformado = definir_tipo_produto(df_transformado)

        # Carregar dados em partes menores
        output_folder = Path(config["output_folder"])
        output_folder.mkdir(parents=True, exist_ok=True)
        base_filename = config["output_file"].replace(".xlsx", "")  # Remover extensão para adicionar "_parte_X"
        
        salvar_em_partes(df_transformado, output_folder, base_filename)
    else:
        logging.warning("Nenhum dado para salvar.")

if __name__ == "__main__":
    main()
