# 🧠 AKAIKE_ASSESSMENT - Document-Based Q&A Bot

This project is a **Retrieval-Augmented Generation (RAG)** powered Q&A bot designed to answer questions about a given document — in this case, the **Acko Health Insurance Policy PDF**. The bot uses advanced NLP techniques to extract, embed, and reason over document content, ensuring context-aware and accurate answers.

---

## 🚀 Features

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
- Each chunk is of size `1000` characters with an **overlap of 150** to maintain context flow.

### 3. **Model Initialization**
- **Embedding Model**: Converts document chunks into vector embeddings.
- **Text Generation Model**: Loaded using HuggingFace’s `pipeline`, runs locally.

### 4. **Embedding + Vector Storage**
- Chunks are embedded and stored in **Chroma VectorDB** for efficient similarity retrieval.

### 5. **Retriever Configuration**
- A retriever is set up to fetch **Top 4** chunks with the highest similarity to the user query.

### 6. **Prompt Template Design**
- Combines:
  - Developer-written prompt
  - Retrieved context chunks
  - User question

- This ensures the model answers accurately based on document content, and falls back to pretrained knowledge if needed.

### 7. **Response Generation**
- The assembled prompt is passed to the local generation model.
- Final response is based on the retrieved content and prompt configuration.

---



