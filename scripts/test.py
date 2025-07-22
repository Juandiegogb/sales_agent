from langchain_postgres import PGVector
from sales_agent.settings import uri_connection
from langchain_openai.embeddings import OpenAIEmbeddings


embeddings = OpenAIEmbeddings(model="text-embedding-3-large")

vector_store = PGVector(
    embeddings=embeddings,
    collection_name="my_docs",
    connection=uri_connection,
    use_jsonb=True,
)
