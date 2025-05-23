import fitz
from langchain.docstore.document import Document
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from transformers import pipeline

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=150)

embedder = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2",
    model_kwargs={"device": "cpu"},
    encode_kwargs={"normalize_embeddings": False}
)


llm_pipe = pipeline(
    "text-generation",
    model="Qwen/Qwen1.5-0.5B",
    device=-1,  
    max_length=512,
    do_sample=True,
    top_p=0.95,
    temperature=0.7
)

data_given = "Acko-Group-Health-Insurance.pdf"

def process_pdf(data_given):
    doc = fitz.open(data_given)
    full_text = ""
    for page_num, page in enumerate(doc, start=1):
        page_text = page.get_text()
        full_text += page_text

    docs = [Document(page_content=full_text)]
    split_docs = text_splitter.split_documents(docs)
    print("SPLITTING DONE")

    stored_db = Chroma.from_documents(split_docs, embedding=embedder)
    print("CHROMA DONE")

    retriever = stored_db.as_retriever(search_kwargs={"k": 4})
    

    return retriever

def answer_query(query, retriever):
    retrieved_docs = retriever.get_relevant_documents(query)
    context_text = "\n".join([doc.page_content for doc in retrieved_docs])
    prompt = f"""You are a health insurance advisor. Answer the user's question clearly from the given context. If you can't find the answer in the context, infer from general knowledge.
Context:
{context_text}
Question: {query}
Answer:"""

    result = llm_pipe(prompt, max_new_tokens=300)
    generated_text = result[0]['generated_text']
    answer = generated_text.split("Answer:")[-1].strip()  
    return answer


if __name__ == "__main__":
    retriever = process_pdf(data_given)
    response = answer_query("Explain about the loss of pay due to hospitalization", retriever)
    print("\nFinal Answer:\n", response)
