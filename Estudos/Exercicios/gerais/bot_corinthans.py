import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.document_loaders import WebBaseLoader


load_dotenv()
os.environ['GROQ_API_KEY'] = os.getenv('api_key')
chat = ChatGroq(model='llama-3.3-70b-versatile')

loader = WebBaseLoader('https://blog.nubank.com.br/imposto-de-renda-ir/')
lista_documentos = loader.load()

#Deve-se passar cada documento para uma string - Tive que limitar em 6000 pois é a quantidade de token por minuto que o Groq aceita
documentos = "\n".join([doc.page_content[:6000] for doc in lista_documentos])
# print(documentos)

template = ChatPromptTemplate.from_messages([
    ("system", "Você é um assistente virtual amigável chamado Bmo e tem acesso às seguintes informações para dar suas respostas: {repertorio}"),
    ("human", "{pergunta}")
])
pergunta_user = input('Qual a sua pergunta sobre o corinthans?')
chain = template | chat
resposta2 = chain.invoke({'repertorio': documentos, 'pergunta': 'Se apresente, por favor?'})
resposta = chain.invoke({'repertorio': documentos, 'pergunta': pergunta_user})


print(resposta.content)
print(resposta2.content)