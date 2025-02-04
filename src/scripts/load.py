import pandas as pd
import logging
import os

def load_to_excel(df, output_path):
    """Salva o DataFrame em um arquivo Excel."""
    logging.info(f"Salvando dados em: {output_path}")
    with pd.ExcelWriter(output_path, engine='xlsxwriter') as writer:
        df.to_excel(writer, index=False)

def salvar_em_partes(df, output_folder, base_filename, linhas_por_arquivo=500):
    """Divide o DataFrame em partes menores e salva em arquivos Excel separados."""
    total_linhas = len(df)
    num_partes = (total_linhas // linhas_por_arquivo) + (1 if total_linhas % linhas_por_arquivo > 0 else 0)
    
    for i in range(num_partes):
        # Dividir o DataFrame
        parte_df = df.iloc[i * linhas_por_arquivo : (i + 1) * linhas_por_arquivo]
        
        # Criar o nome do arquivo
        output_filename = f"{base_filename}_parte_{i + 1}.xlsx"
        output_path = os.path.join(output_folder, output_filename)
        
        # Salvar o DataFrame dividido
        logging.info(f"Salvando parte {i + 1} em: {output_path}")
        load_to_excel(parte_df, output_path)
