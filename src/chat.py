from langchain_openai import ChatOpenAI
from search import search_prompt
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

def main():
    load_dotenv()
    pergunta_1 = "Qual é a capital da França?"
    pergunta_2 = "Quantos clientes temos em 2024?"
    pergunta_3 = "Você acha isso bom ou ruim?"
    pergunta_4 = "Qual o faturamento da Empresa Beta Financeira Indústria?"
    pergunta_5 = "Os dados presentes começam em qual ano e terminam em qual ano?"
    pergunta_6 = "Qual o maior faturamento do periodo"
    chain = search_prompt(question=pergunta_6)

    if not chain:
        print("Não foi possível iniciar o chat. Verifique os erros de inicialização.")
        return
    
    model = ChatOpenAI(model="gpt-5-nano", temperature=0.5)
    answer_model = model.invoke(chain)

    print(answer_model.content)

if __name__ == "__main__":
    main()