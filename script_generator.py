from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI

# Load environment variables from .env
load_dotenv()

# Create a Google Gemini model
model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

# Define the prompt template for script generation
prompt = ChatPromptTemplate.from_template("""
Write a full YouTube video script on the topic: "{topic}".  
Make it informative, engaging, and beginner-friendly.  
Include an intro, main content, and conclusion.
""")


script_chain = prompt | model | StrOutputParser()


def generate_script(topic:str)->str:
    return script_chain.invoke({"topic": topic})