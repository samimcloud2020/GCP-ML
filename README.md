# Question and Answering Application

This is a question-and-answering application. The user provides a link to a webpage on which they want to ask questions. After processing the link, the application automatically creates a 100 words summary, a Twitter tweet, and a LinkedIn post as per the content in the link. After this, users can ask their questions which are answered only from the information available in the webpage link provided.

This application uses:
- Google's Vertex AI PaLM API for text embedding and text answering
- Langchain framework for creating the embedding index and document retrieval
- StreamLit Framework for Application Development

******************************************************************************************************************
Nucleus sampling is a technique used in large language models to control the randomness and diversity of generated text. 
It works by sampling from only the most likely tokens in the model’s predicted distribution.

The key parameters are:

Temperature: Controls randomness, higher values increase diversity.

Top-p (nucleus): The cumulative probability cutoff for token selection. Lower values mean sampling from a smaller,
                more top-weighted nucleus.

Top-k: Sample from the k most likely next tokens at each step. Lower k focuses on higher probability tokens.
*********************************************************************************************************************
In general:

Higher temperature will make outputs more random and diverse.

Lower top-p values reduce diversity and focus on more probable tokens.

Lower top-k also concentrates sampling on the highest probability tokens for each step.

So temperature increases variety, while top-p and top-k reduce variety and focus samples on the model’s top predictions.
You have to balance diversity and relevance when tuning these parameters for different applications.
**********************************************************************************************************************
!pip install google-cloud-aiplatform --upgrade --user

!pip install langchain --upgrade

!pip install bs4

!pip install docarray

!pip install tiktoken

!pip install streamlit
*********************************************************************************************************************
For this implementation, I have installed Google Cloud CLI and authenticated using

#run in command line
gcloud auth application-default login
********************************************************************************************************************
Note: I am not using Langchain’s WebBaseLoader as it leads to wrong response using texts from ads and other texts 
from the webpage while in the above code, only the text from paragraphs are extracted.
*******************************************************************************************************************
LangChain Question & Answering

LangChain supports Question answering over documents — text files, CSV and pdf, etc. This Question & Answering 
refers to the Questions asked in the context of the document provided (not from public sources). 
Here are the steps involved in LangChain to perform this

1.Creates a Loader from the documents provided. It created multiple chunks of text data coming from the documents.

2.These text chunks are sent to the LLM model (in this case PaLM API text Embeddings model). 
Embeddings are nothing but a vector of numbers converted by the machine learning model, from the text data provided.

3.LangChain stores these embeddings in an in-memory database along with the chunks.
This whole process is called indexing and the VectorstoreIndexCreator method for indexing is used in the below code.

4.Once a question is asked by a user, embedding is created from the question text. 
Now the question embedding is searched over the database to find similar document embeddings.
Cosine-similarity is a known similarity search algorithm generally used.

5.Once the most appropriate documents are found, they are again sent to the LLM model with the question asked,
as a prompt, to synthesize the response.

I am using Streamlit Caching here to store objects across user interactions and multiple sessions. 
Streamlit provides two decorators @st.cache_resource and @st.cache_data.

Using @st.cache_data checks if the function is called with the same parameters and code, Streamlit will skip executing
the function altogether and return the cached value instead. The data is stored in a serialized manner in this case.

@st.cache_resource caches unserializable objects that you don’t want to load multiple times. 
Using it, you can share these resources across all reruns and sessions of an app without copying or duplication.
**********************************************************************************************************************
