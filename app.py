import os
import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
load_dotenv()

st.set_page_config(page_title="Language Translator")
st.title("Language Translation model")
input_text = st.text_input("Enter the language and the sentence to translate")

prompt_template = ChatPromptTemplate.from_messages(
     messages = [
         ("system","You are a helpful AI Translator who converts one language to another based on user preference, You dont the answer the question, just translate the given sentence."),
         ("human","{input_text}")
     ]
)

default_api_key = os.getenv("GOOGLE_API_KEY", "")
api_key = st.sidebar.text_input(
    "Enter your Google API key",
    value=default_api_key,
    type="password",
    help="The key is kept only for this session.",
)
st.sidebar.caption("Need a key? Visit makersuite.google.com for Gemini access.")

output_parser = StrOutputParser()
submit = st.button("Translate")

if submit:
    if not api_key:
        st.warning("Please provide your Google API key to continue.")
    elif not input_text:
        st.warning("Please enter text to translate.")
    else:
        try:
            model = ChatGoogleGenerativeAI(
                model="gemini-2.0-flash-001",
                api_key=api_key,
                temperature=1.0,
            )
            chain = prompt_template | model | output_parser
            response = chain.invoke({"input_text": input_text})
            st.subheader("The translated text is..")
            st.write(response)
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
