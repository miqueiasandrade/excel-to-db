import pandas as pd
import re
from sqlalchemy import create_engine
import unicodedata


def normalize_column_name(col_name):
    """
    Normaliza o nome da coluna (remove acentos e converte para camelCase)
    """
    # Remove acentos
    col_name = unicodedata.normalize('NFKD', col_name).encode('ascii', 'ignore').decode('utf-8')
    
    # Substituir caracteres especiais, como espaços, por nada
    col_name = re.sub(r'[^a-zA-Z0-9\s]', '', col_name)

    # Converter para camelCase
    words = col_name.split()
    return words[0].lower() + ''.join(word.capitalize() for word in words[1:])


def process_column_names(df):
    """ Função para processar as colunas do DataFrame"""

    df.columns = [normalize_column_name(col) for col in df.columns]
    return df


def save_to_db(df, db_url, table_name):

    """ Função para salvar os dados no banco de dados (SQLite)"""

    # Criar conexão com o banco de dados SQLite
    engine = create_engine(db_url)
    
    # Salvar o DataFrame no banco de dados (substituindo a tabela se já existir)
    df.to_sql(table_name, con=engine, if_exists='append', index=False)


def main(excel_file, db_url, table_name):
    """ Carrega o arquivo Excel, processar as colunas e salvar no banco"""

    df = pd.read_excel(excel_file)
    df = process_column_names(df)
    save_to_db(df, db_url, table_name)

if __name__ == "__main__":
    excel_file = 'Exemplo.xlsx'
    db_url = 'sqlite:///exemplo.db' 
    table_name = 'Pessoas'
    
    main(excel_file, db_url, table_name)
