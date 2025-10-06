from langchain.text_splitter import RecursiveCharacterTextSplitter

def split_text(content: str, MAX_CHUNK_SIZE) -> list[str]:
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=MAX_CHUNK_SIZE, 
        chunk_overlap=100,
        length_function=len,
        )
    return text_splitter.split_text(content)