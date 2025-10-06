import tqdm
import time
from embeddingModel import model

def get_embeddings_wrapper(split_texts: list[str]):
    embeddings = []
    for i in tqdm.tqdm(range(0, split_texts)):
        time.sleep(1) 
        texts = split_texts[i]
        text_embeddings = model.get_embeddings(texts)
        embeddings.extend([embedding.values for embedding in text_embeddings])
    return embeddings