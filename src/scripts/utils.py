import os
import logging
import yaml
from pathlib import Path
from typing import Dict, Any

def setup_logging(log_level: str = logging.INFO) -> None:
    """Configura o sistema de logging."""
    logging.basicConfig(
        level=log_level,
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=[
            logging.StreamHandler()  # Log no console
        ]
    )

def load_config(config_path: str = "config.yaml") -> Dict[str, Any]:
    """Carrega as configurações do arquivo YAML."""
    try:
        with open(config_path, "r") as f:
            config = yaml.safe_load(f)
        logging.info("Configurações carregadas com sucesso.")
        return config
    except Exception as e:
        logging.error(f"Erro ao carregar configurações: {e}")
        raise