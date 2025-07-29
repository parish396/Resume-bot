# langchain_resume_bot.py
import os
import fitz  # PyMuPDF
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.chains import LLMChain

load_dotenv()
llm = ChatOpenAI(temperature=0, model_name="gpt-4")

def extract_text_from_pdf(file_path):
    doc = fitz.open(file_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def analyze_resume(text, question):
    prompt = ChatPromptTemplate.from_template(
        "You are an expert resume assistant. Given the following resume:\n\n{resume}\n\nAnswer this question:\n{question}"
    )
    chain = LLMChain(llm=llm, prompt=prompt)
    return chain.run({"resume": text, "question": question})
