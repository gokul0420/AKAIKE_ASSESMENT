# AKAIKE_ASSESMENT

The have developed this Q/A bot by using RAG pipeline such that the system could answer user questions about the document content.

#Approach
1.I have impoted required libraries as mentioned in the requirements.txt
2.Initialized text splitter inorder to split doc's text into chunks.
3.Initialized models for embedding and text generation.
4.Loaded document("Here I've done for Acko-Health-Insurance.pdf").
5.Processed pdf in such a way that extracted all text and stored and using the text splitter these extracted text splitted into chunk where each chunk size is of 1000 and used overlap value 150 inorder to maintain context.
6.These splitted chunks get embedded and pushed to the vectordb(here I used chroma).
7.I've created retriever where it stores the most similarity chunks("Here I have used top 4 chunks with higher similarity scores")
8.For these retrieved chunks I would get appropriate text.
9.I have designed the prompt template in such a way that the system would answer for questions regarding Acko health insurance policy and for questions apart from this it tries to give answer from its previous trained knowledge.And also this prompt template consists of context text i.e retrieved text from above step and the prompt template

So,basically prompt_template=prompt(by_developer) + retrieved text from previous process + question(from_user)

10.This propmt_template would get passed through the generating model("Here I've used HuggingFace pipeline inorder to load model directly to my local system")
11.Finally,the system would return answer for the question asked based on the document content provided
