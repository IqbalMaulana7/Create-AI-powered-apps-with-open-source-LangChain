# import os
# from langchain_openai import ChatOpenAI
# import gradio as gr

# # Memasukkan API key
# os.environ["OPENAI_API_KEY"] = "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"

# gpt3 = ChatOpenAI(model_name="gpt-3.5-turbo" )

# def chatbot(prompt):
#     return gpt3.invoke(prompt).content

# demo = gr.Interface(fn=chatbot, inputs="text", outputs="text")

# demo.launch(server_name="0.0.0.0", server_port= 7860, share=True)



# Menggunakan Hugging FaceHub
import os
from langchain_community.llms import HuggingFaceEndpoint
os.environ["HUGGINGFACEHUB_API_TOKEN"] = "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"
llm = HuggingFaceEndpoint(repo_id="google/flan-ul2")
text = "Beritahu fakta menarik tentang kentang!"
result = llm.invoke(text)
print(result)