from langchain_text_splitters import (
    RecursiveCharacterTextSplitter
)

from langchain_huggingface import (
    HuggingFaceEmbeddings
)

from langchain_community.vectorstores import (
    FAISS
)


def create_vector_store(text):
    """
    Create a FAISS vector store from transcript text.
    """


    # Split transcript


    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    documents = splitter.create_documents(
        [text]
    )


  
    # Create embeddings
 

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )


 
    # Create FAISS vector store
  

    vector_store = FAISS.from_documents(
        documents,
        embeddings
    )

    return vector_store