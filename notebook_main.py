import pandas as pd
from google.cloud import storage, aiplatform
from vertexai.preview.language_models import TextEmbeddingModel
from google.oauth2 import service_account
import vertexai
import tqdm
import time
from langchain.text_splitter import RecursiveCharacterTextSplitter


PROJECT_ID = "unvailed-466101"
LOCATION = "us-central1"
BUCKET_NAME = "unvailed_test_bucket_1"
CSV_FILE_PATH = "Unvailed Vendors - Supported.csv"
MAX_CHUNK_SIZE = 2000
my_credentials = service_account.Credentials.from_service_account_file("unvailed-service-account.json")


aiplatform.init(
    project=PROJECT_ID, 
    location=LOCATION,
    staging_bucket=f"gs://{BUCKET_NAME}",
    credentials=my_credentials,

)
vertexai.init(project=PROJECT_ID, location=LOCATION)

df = pd.read_csv(CSV_FILE_PATH)
df['content'] = df['content'].str.replace(r"\(.*?\)", "", regex=True)
df['content'] = df['content'].str.replace(r"\n", " ", regex=True)

model = TextEmbeddingModel.from_pretrained("gemini-embedding-001")

def get_embeddings_wrapper(split_texts: list[str]):
    embeddings = []
    for i in tqdm.tqdm(range(0, split_texts)):
        time.sleep(1) 
        texts = split_texts[i]
        text_embeddings = model.get_embeddings(texts)
        embeddings.extend([embedding.values for embedding in text_embeddings])
    return embeddings

def split_text(content: str) -> list[str]:
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=MAX_CHUNK_SIZE, 
        chunk_overlap=100,
        length_function=len,
        )
    return text_splitter.split_text(content)

content = df['content'].tolist()
split_content = split_text(content)
df['embedding'] = get_embeddings_wrapper(split_content)

# Write to jsonl file
jsonl_string = df[["id", "url", "page_title", "content", "embedding"]].to_json(orient="records", lines=True)
with open("vendors_supported.json", "w") as f:
    f.write(jsonl_string)



# Copy jsonl file to GCS bucket
GCS_BUCKET_URI= f"gs://{BUCKET_NAME}"


# Create index
index_id = "projects/271286489289/locations/us-central1/indexes/4143788845227311104"
index = aiplatform.MatchingEngineIndex(index_id)

# Create index endpoint
index_endpoint_id = "projects/271286489289/locations/us-central1/indexEndpoints/8423862156717457408"
index_endpoint = aiplatform.MatchingEngineIndexEndpoint(index_endpoint_id)