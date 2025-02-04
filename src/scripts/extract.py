import pandas as pd
import logging

def extract_from_excel(file_path):
    """Extrai dados de um arquivo Excel."""
    logging.info(f"Extraindo dados do arquivo: {file_path}")
    return pd.read_excel(file_path)