import pandas as pd
from sqlalchemy import create_engine
from pymongo import MongoClient
import pyarrow.parquet as pq

def load_csv_to_postgres(file_path, db_url):
    df = pd.read_csv(file_path)
    engine = create_engine(db_url)
    df.to_sql('sample_table', engine, if_exists='append', index=False)

def load_csv_to_mongo(file_path, mongo_url):
    df = pd.read_csv(file_path)
    client = MongoClient(mongo_url)
    db = client['project_db']
    collection = db['sample_collection']
    collection.insert_many(df.to_dict('records'))

def transform_to_parquet(postgres_url, mongo_url, output_path):
    engine = create_engine(postgres_url)
    postgres_df = pd.read_sql('sample_table', engine)
    
    client = MongoClient(mongo_url)
    mongo_df = pd.DataFrame(list(client['project_db']['sample_collection'].find()))
    
    combined_df = pd.concat([postgres_df, mongo_df], ignore_index=True)
    combined_df.to_parquet(output_path)

if __name__ == "__main__":
    load_csv_to_postgres('/app/data/input/sample.csv', 'postgresql://user:password@project-postgres:5432/project_db')
    load_csv_to_mongo('/app/data/input/sample.csv', 'mongodb://user:password@project-mongo:27017/')
    transform_to_parquet('postgresql://user:password@project-postgres:5432/project_db', 'mongodb://user:password@project-mongo:27017/', '/app/data/output/transformed.parquet')
