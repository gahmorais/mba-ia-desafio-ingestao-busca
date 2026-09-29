from langchain_postgres.vectorstores import PGVector
from dotenv import load_dotenv
import os
from langchain_openai import OpenAIEmbeddings
PROMPT_TEMPLATE = """
CONTEXTO:
{contexto}

REGRAS:
- Responda somente com base no CONTEXTO.
- Se a informação não estiver explicitamente no CONTEXTO, responda:
  "Não tenho informações necessárias para responder sua pergunta."
- Nunca invente ou use conhecimento externo.
- Nunca produza opiniões ou interpretações além do que está escrito.

EXEMPLOS DE PERGUNTAS FORA DO CONTEXTO:
Pergunta: "Qual é a capital da França?"
Resposta: "Não tenho informações necessárias para responder sua pergunta."

Pergunta: "Quantos clientes temos em 2024?"
Resposta: "Não tenho informações necessárias para responder sua pergunta."

Pergunta: "Você acha isso bom ou ruim?"
Resposta: "Não tenho informações necessárias para responder sua pergunta."

PERGUNTA DO USUÁRIO:
{pergunta}

RESPONDA A "PERGUNTA DO USUÁRIO"
"""



def search_prompt(question=None):
    #VALIDA VARIAVEIS DE AMBIENTE
    try:
        load_dotenv()
        for k in ("OPENAI_API_KEY", "PG_VECTOR_COLLECTION_NAME", "DATABASE_URL"):
            if not os.getenv(k):
                raise RuntimeError(f"Environment variable {k} is not set")
        
        #CARREGA MODELOS DE IA
        embeddings = OpenAIEmbeddings(model=os.getenv("OPENAI_EMBEDDING_MODEL","text-embedding-3-small"))

        #INICIA CONEXÃO COM BANCO DE DADOS
        store = PGVector(
          embeddings=embeddings,
          collection_name=os.getenv("PG_VECTOR_COLLECTION_NAME"),
          connection=os.getenv("DATABASE_URL"),
          use_jsonb=True,
        )

        #REALIZA BUSCA NO BANCO DE DADOS
        results = store.similarity_search_with_score(question, k=10)

        #CARREGA OS RESULTADOS DO BANCO E FILTRA OS
        #10 RESULTADOS MAIS RELEVANTES
        contexto = ""
        for i, (doc, score) in enumerate(results, start=1):
          contexto += doc.page_content.strip() + ", "
          
        pergunta = question
        return f"""
CONTEXTO:
{contexto}

REGRAS:
- Responda somente com base no CONTEXTO.
- Se a informação não estiver explicitamente no CONTEXTO, responda:
  "Não tenho informações necessárias para responder sua pergunta."
- Nunca invente ou use conhecimento externo.
- Nunca produza opiniões ou interpretações além do que está escrito.

EXEMPLOS DE PERGUNTAS FORA DO CONTEXTO:
Pergunta: "Qual é a capital da França?"
Resposta: "Não tenho informações necessárias para responder sua pergunta."

Pergunta: "Quantos clientes temos em 2024?"
Resposta: "Não tenho informações necessárias para responder sua pergunta."

Pergunta: "Você acha isso bom ou ruim?"
Resposta: "Não tenho informações necessárias para responder sua pergunta."

PERGUNTA DO USUÁRIO:
{pergunta}

RESPONDA A "PERGUNTA DO USUÁRIO"
"""
        
    except Exception as e:
      print(f"ocorreu um erro - {e}")
