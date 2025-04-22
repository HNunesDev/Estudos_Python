import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.document_loaders import YoutubeLoader

load_dotenv()
os.environ['GROQ_API_KEY'] = os.getenv('api_key')
chat = ChatGroq(model='llama-3.3-70b-versatile')

url = 'https://www.youtube.com/watch?v=7c5yfAdmIEQ'
loader = YoutubeLoader.from_youtube_url(url, language = 'pt')
lista_documento = loader.load()

documentos = "\n".join([doc.page_content[:6000] for doc in lista_documento])

# print(documentos)

template = ChatPromptTemplate([
    ('system', 'Voce é um assistente amigavel chamado Bmo que responde com base no {video}'),
    ('user', '{pergunta}')
])

pergunta_usuario = input('Qual a sua pergunta referene ao video? ')
chain = template | chat

resposta1 = chain.invoke({'video': documentos, 'pergunta': pergunta_usuario})

print(resposta1.content)
