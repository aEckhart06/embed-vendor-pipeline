
sudo apt update
sudo install python3 python3-pip python3-venv git -y

cd /embed-vendor-pipeline/python_embedding_api
pip install -r requirements.txt

uvicorn app:app --host 0.0.0.0 --port 8080