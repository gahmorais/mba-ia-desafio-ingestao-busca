from langchain_openai import ChatOpenAI
from search import search_prompt
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from questionary import text
def main():
    load_dotenv()
    #Responderá com não tenho informações
    ##pergunta_1 = "Qual é a capital da França?"
    ##pergunta_2 = "Quantos clientes temos em 2024?"
    ##pergunta_3 = "Você acha isso bom ou ruim?"

    ###Perguntas com Respostas concretas
    ##pergunta_4 = "Qual o faturamento da Empresa Beta Financeira Indústria?"
    ##pergunta_5 = "Qual o faturamento da empresa Coral Energia Comércio?"
    ##pergunta_6 = "Quais as empresas mais velha?"
    ##pergunta_7 = "Quais as empresas mais novas?"
    ##pergunta_8 = "Qual o faturamento das empresas fundadas em 2024?"

    ###Perguntas com limitação técnica do RAG top k=10
    ##pergunta_9 = "Qual a soma de faturamento das empresas mais velha?"
    ##pergunta_10 = "Qual o maior faturamento do periodo?"
    ##pergunta_11 = "Qual a empresa com o maior faturamento?"

    while True:
        question = text("Faça sua pergunta sobre o relatório de faturamento ou digite 'sair' para encerrar").ask()
        if question == "sair":
            break
        chain = search_prompt(question=question)
        print("Iniciando processamento...")
        if not chain:
            print("Não foi possível processar a pergunta. Verifique os erros de inicialização.")
            return
        print("Enviando dados ao modelo...")
        model = ChatOpenAI(model="gpt-5-nano", temperature=0.5)
        answer_model = model.invoke(chain)
        print("Processando resposta...")
        print(f'Resposta: {answer_model.content}')
    print("Encerrando aplicação")
    

if __name__ == "__main__":
    main()