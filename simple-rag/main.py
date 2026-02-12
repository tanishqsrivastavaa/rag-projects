import asyncio
import asyncpg

db_url= "postgresql://admin:password@localhost:5432/explainit"

async def main():
    try:
        conn = await asyncpg.connect(db_url)
        print("successfully connected to the database")
        version = await conn.fetchval("SELECT extversion FROM pg_extension WHERE extname = 'vector'")
        print(f"pgvector version: {version}")

        await conn.close()
    except Exception as e:
        print(f"{e}")

if __name__=="__main__":
    asyncio.run(main())