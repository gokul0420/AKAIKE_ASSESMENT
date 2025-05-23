# AKAIKE_ASSESSMENT - Document-Based Q&A Bot

This project is a **Retrieval-Augmented Generation (RAG)** powered Q&A bot designed to answer questions about a given document.

---

##  Features

- Document-specific Q&A from PDF
- Built with HuggingFace Transformers and Chroma for VectorDB
- Uses RAG pipeline with context retention
- Dynamic prompt generation for hybrid document + general knowledge responses

---

## 📄 Document

The current implementation is tailored to:


### 1. **Library Imports**
All necessary packages are imported as defined in `requirements.txt`.

### 2. **Document Splitting**
- Text from the document is extracted and split into **chunks**.
- Each chunk is of size 1000 with an overlap of 150 to maintain context flow.

### 3. **Model Initialization**
- **Embedding Model**: Converts document chunks into vector embeddings.
- **Text Generation Model**: Loaded using HuggingFace’s `pipeline`, runs locally.

### 4. **Embedding + Vector Storage**
- Chunks are embedded and stored in **Chroma VectorDB** for efficient similarity retrieval.

### 5. **Retriever Configuration**
- A retriever is set up to fetch top 4 chunks with the highest similarity to the user query.

### 6. **Prompt Template Design**
- Combines:
  - Prompt written by developer
  - Retrieved context chunks
  - User question

### 7. **Response Generation**
- The prompt is passed to the local generation model.
- Final response is based on the retrieved content get delivered.

---



