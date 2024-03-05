import os
from langchain_openai import ChatOpenAI
import gradio as gr
from langchain_community.llms import HuggingFaceEndpoint


# Memasukkan API key
os.environ["HUGGINGFACEHUB_API_TOKEN"] = "AKSES TOKEN KAMU"
llm = HuggingFaceEndpoint(repo_id="google/flan-ul2")

# gpt3 = ChatOpenAI(model_name="gpt-3.5-turbo" )


def chatbot(prompt):
    response = llm.invoke(prompt)
    return response


demo = gr.Interface(fn=chatbot, inputs="text", outputs="text")
demo.launch(server_name="0.0.0.0", server_port= 7860, share=True)