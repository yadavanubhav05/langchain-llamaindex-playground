import os
from dotenv import load_dotenv

# =========================
# Load Environment
# =========================
load_dotenv()

# =========================
# LlamaIndex Imports
# =========================
from llama_index.core import SimpleDirectoryReader, VectorStoreIndex, Settings
from llama_index.llms.google_genai import GoogleGenAI
from llama_index.embeddings.huggingface import HuggingFaceEmbedding

# =========================
# Configure Models
# =========================
Settings.llm = GoogleGenAI(
    model="gemini-2.5-flash"
)

Settings.embed_model = HuggingFaceEmbedding(
    model_name="BAAI/bge-small-en-v1.5"
)

# =========================
# Load Documents
# =========================
print("\n📂 Loading documents...\n")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DOCS_PATH = os.path.join(BASE_DIR, "docs")

documents = SimpleDirectoryReader(DOCS_PATH).load_data()

# =========================
# Build Index
# =========================
print("🔧 Building index...\n")

index = VectorStoreIndex.from_documents(documents)

print("✅ Index ready\n")

# =========================
# Query Engine
# =========================
query_engine = index.as_query_engine(
    similarity_top_k=3,
    response_mode="tree_summarize"
)

# =========================
# Run Query
# =========================
if __name__ == "__main__":
    query = "Summarize the document in simple points"

    print("🤖 Running query...\n")

    response = query_engine.query(query)

    print("\n=========== RESULT ===========\n")
    print(response)

    print("\n=========== METADATA ===========\n")
    print(response.metadata)