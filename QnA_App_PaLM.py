#DocArrayInMemorySearch is a document index provided by Docarray that stores documents in memory. 
#It is a great starting point for small datasets, where you may not want to launch a database server.

# import libraries
import streamlit as st
import requests
from bs4 import BeautifulSoup
from langchain.document_loaders import TextLoader          #reads in a file as text and places it all into one document.
from langchain.indexes import VectorstoreIndexCreator      #Logic for creating indexes.
from langchain.vectorstores import DocArrayInMemorySearch  #document index provided by Docarray that stores documents in memory.
import vertexai
from langchain.llms import VertexAI
from langchain.embeddings import VertexAIEmbeddings

vertexai.init(project=PROJECT, location=LOCATION)        #GCP PROJECT ID, LOCATION as region.

#The PaLM 2 for Text (text-bison, text-unicorn) foundation models are optimized for a variety of natural language 
#tasks such as sentiment analysis, entity extraction, and content creation. The types of content that the PaLM 2 for
#Text models can create include document summaries, answers to questions, and labels that classify content.

llm = VertexAI(
    model_name="text-bison@001",
    max_output_tokens=256,
    temperature=0.1,
    top_p=0.8,
    top_k=40,
    verbose=True,)
    
embeddings = VertexAIEmbeddings()

#The below code scrapes all the text data from the webpage link provided by the user and saves it in a text file.
def get_text(url):
    # Send a GET request to the URL
    response = requests.get(url)

    # Create a BeautifulSoup object with the HTML content
    soup = BeautifulSoup(response.content, "html.parser")

    # Find the specific element or elements containing the text you want to scrape
    # Here, we'll find all <p> tags and extract their text
    paragraphs = soup.find_all("p")

    # Loop through the paragraphs and print their text
    with open("text\\temp.txt", "w", encoding='utf-8') as file:
        # Loop through the paragraphs and write their text to the file
        for paragraph in paragraphs:
            file.write(paragraph.get_text() + "\n")

@st.cache_resource
def create_langchain_index(input_text):
    print("--indexing---")
    get_text(input_text)
    loader = TextLoader("text\\temp.txt", encoding='utf-8')
    # data = loader.load()

    index = VectorstoreIndexCreator(vectorstore_cls=DocArrayInMemorySearch,embedding=embeddings).from_loaders([loader])
    return index

# @st.cache_resource
# def get_basic_page_details(input_text,summary_query,tweet_query,ln_query):
#     index = create_langchain_index(input_text)
#     summary_response = index.query(summary_query)
#     tweet_response = index.query(tweet_query)
#     ln_response = index.query(ln_query)

#     return summary_response,tweet_response,ln_response


@st.cache_data
def get_response(input_text,query):
    print(f"--querying---{query}")
    response = index.query(query,llm=llm)
    return response

#The below code is a simple flow to accept the webpage link and process the queries
#using the get_response function created above. Using the cache, the same.

st.title('Webpage Question and Answering')


input_text=st.text_input("Provide the link to the webpage...")

summary_response = ""
tweet_response = ""
ln_response = ""
# if st.button("Load"):
if input_text:
    index = create_langchain_index(input_text)
    summary_query ="Write a 100 words summary of the document"
    summary_response = get_response(input_text,summary_query)

    tweet_query ="Write a twitter tweet"
    tweet_response =  get_response(input_text,tweet_query)

    ln_query ="Write a linkedin post for the document"
    ln_response = get_response(input_text,ln_query)


    with st.expander('Page Summary'): 
        st.info(summary_response)

    with st.expander('Tweet'): 
        st.info(tweet_response)

    with st.expander('LinkedIn Post'): 
        st.info(ln_response)


st.session_state.input_text = ''    
question=st.text_input("Ask a question from the link you shared...")
if st.button("Ask"):
        if question:
            index = create_langchain_index(input_text)
            response = get_response(input_text,question)
            st.write(response)
        else:
            st.warning("Please enter a question.")
    
