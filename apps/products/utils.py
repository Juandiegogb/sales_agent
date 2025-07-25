from langchain_openai.embeddings import OpenAIEmbeddings
from langchain_postgres import PGVector
from sales_agent.settings import uri_connection


embeddings = OpenAIEmbeddings(model="text-embedding-3-large")

vector_store = PGVector(
    embeddings=embeddings,
    collection_name="products_embeddings",
    connection=uri_connection,
    use_jsonb=True,
)


def search_product(input_text):
    results = vector_store.search(
        input_text,
        search_type="similarity_score_threshold",
        score_threshold=0.3,
        k=4,
    )

    if not results:
        return results

    results = [
        {"Product description": result.page_content, "metadata": result.metadata}
        for result in results
    ]

    return results
