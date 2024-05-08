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

