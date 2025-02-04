# **Bling to Tiny - ETL em Python**

## **Descrição do Projeto**

Este projeto é um pipeline de ETL (Extract, Transform, Load) desenvolvido em Python para processar arquivos Excel contendo informações de produtos. Ele estrutura os dados para serem utilizados posteriormente de forma otimizada.

##**Atenção**

Seguindo contra as boas praticas, os comentarios no codigo sera mantido para poder ajudar na identificação de cada coisa e sua função, para auxiliar qualquer pessoa de qualquer nivel de conhecimento
O projeto ainda esta sendo desenvolvido entao algumas coisas precisarão ser feitas a mão, ex: se a descrição do produto filho vier no campo descrições, sera necessario fazer a mudança a mão

## **Estrutura do Projeto**

```
bling-to-tiny-py/
├── config.yaml               # Arquivo de configuração do projeto
├── data/
│   ├── raw/    # Arquivos originais (.xlsx) antes do processamento
│   └── ready/  # Arquivos processados e prontos para uso
├── src/
│   ├── main.py  # Script principal que orquestra o ETL
│   └── scripts/
│       ├── extract.py   # Responsável por carregar os arquivos
│       ├── transform.py # Responsável pela limpeza e transformação dos dados
│       ├── load.py      # Responsável por salvar os dados transformados
│       └── utils.py     # Funções auxiliares
├── requirements.txt  # Dependências do projeto
└── README.md         # Documentação geral
```

## **Configuração do Projeto**

O projeto utiliza um arquivo de configuração `config.yaml` para definir:

- Diretórios de entrada e saída.
- Mapeamento de colunas para transformação.
- Parâmetros adicionais para processamento de dados.

## **Regras de Transformação**

- **Identificação de produtos pais e filhos**
  - Produtos "pais" são marcados na coluna `"Tipo do produto"` com `"V"`.
  - Produtos "filhos" têm a coluna `"Código do produto pai"` preenchida e `"Tipo do produto"` como `"S"`.
- **Correção de descrições**
  - **Produtos filhos herdam a descrição do pai.**
  - **A coluna "Variações" do filho contém a descrição original antes da substituição.**
- **Preservação de códigos**
  - Os códigos de produtos são mantidos exatamente como no arquivo original (case-sensitive).

## **Como Clonar e Configurar o Projeto**

1. Clone o repositório:
   ```bash
   git clone https://github.com/vickyxg1/Bling2Tiny-ETL.git
   cd Bling2Tiny-ETL
   ```

2. Crie e ative um ambiente virtual (recomendado):
   ```bash
   # No Windows
   python -m venv venv
   venv\Scripts\activate

   # No macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

## **Execução**

1. Certifique-se de que o ambiente virtual está ativado.
2. Execute o pipeline:
   ```bash
   python src/main.py
   ```

## **Contribuição**

Sinta-se à vontade para contribuir abrindo um pull request ou reportando problemas na seção de issues.

## **Licença**

Este projeto é distribuído sob a licença MIT.

