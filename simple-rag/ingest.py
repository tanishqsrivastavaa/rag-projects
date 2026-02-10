import os
from openai import AsyncOpenAI
import asyncpg
from pydantic import BaseModel

client = AsyncOpenAI(api_key="OPENAI_API_KEY")

#working on the ingesting first
async def get_embedding(text:str):
    response = await client.embeddings.create(
        model="text-embedding-3-large",
        input=text
        )
    
    return response.data[0].embedding

async def ingest_repo(repo_path:str):
    connection = await asyncpg.connect("postgresql://postgres:password@localhost/explain_it")

    #Setting up the table
    await connection.execute("CREATE EXTENSION IF NOT EXISTS vector;")
    await connection.execute("""
            CREATE TABLE IF NOT EXISTS code_vectors(
                             id SERIAL PRIMARY KEY,
                             file_path TEXT,
                             content TEXT,
                             embedding vector(3072)
                             );
                             """)
    

    