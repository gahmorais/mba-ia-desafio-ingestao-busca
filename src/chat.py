from langchain_openai import ChatOpenAI
from search import search_prompt
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

def main():
    load_dotenv()
    #Responderá com não tenho informações
    pergunta_1 = "Qual é a capital da França?"
    pergunta_2 = "Quantos clientes temos em 2024?"
    pergunta_3 = "Você acha isso bom ou ruim?"
    
    #Perguntas com Respostas concretas
    pergunta_4 = "Qual o faturamento da Empresa Beta Financeira Indústria?"
    pergunta_5 = "Qual o faturamento da empresa Coral Energia Comércio?"
    pergunta_6 = "Quais as empresas mais velha?"
    pergunta_7 = "Quais as empresas mais novas?"
    pergunta_8 = "Qual o faturamento das empresas fundadas em 2024?"
    
    
    #Perguntas com limitação técnica do RAG top k=10
    pergunta_9 = "Qual a soma de faturamento das empresas mais velha?"
    pergunta_10 = "Qual o maior faturamento do periodo?"
    pergunta_11 = "Qual a empresa com o maior faturamento?"
    
    chain = search_prompt(question=pergunta_8)

    if not chain:
        print("Não foi possível iniciar o chat. Verifique os erros de inicialização.")
        return
    
    model = ChatOpenAI(model="gpt-5-nano", temperature=0.5)
    answer_model = model.invoke(chain)

    print(answer_model.content)

if __name__ == "__main__":
    main()