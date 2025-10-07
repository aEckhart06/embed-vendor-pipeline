from google.cloud import aiplatform
from google.oauth2 import service_account
import vertexai

my_credentials = service_account.Credentials.from_service_account_file("../unvailed_service_account_key.json")
PROJECT_ID = "unvailed-466101"
LOCATION = "us-central1"
BUCKET_NAME = "unvailed_test_bucket_1"
aiplatform.init(
    project=PROJECT_ID, 
    location=LOCATION,
    staging_bucket=f"gs://{BUCKET_NAME}",
    credentials=my_credentials,

)
vertexai.init(project=PROJECT_ID, location=LOCATION)