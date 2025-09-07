from Exercicio1 import criar_mensagem, exibir_mensagens
from Exercicio2 import ordenar_por_destinatario
from Exercicio3 import busca_binaria_mensagens

def exibir_menu():
    print("\n=== Sistema de Mensagens ===")
    print("1. Cadastrar nova mensagem")
    print("2. Buscar mensagens por destinatário")
    print("3. Sair")
    return input("\nEscolha uma opção: ")

def cadastrar_mensagem(lista_mensagens):
    print("\n=== Cadastro de Mensagem ===")
    remetente = input("Digite o nome do remetente: ")
    destinatario = input("Digite o nome do destinatário: ")
    assunto = input("Digite o assunto da mensagem: ")
    conteudo = input("Digite o conteúdo da mensagem: ")
    
    mensagem = criar_mensagem(assunto, destinatario, remetente, conteudo)
    lista_mensagens.append(mensagem)
    return ordenar_por_destinatario(lista_mensagens)

def buscar_mensagens(lista_mensagens):
    if not lista_mensagens:
        print("\nNão há mensagens cadastradas.")
        return
    
    destinatario = input("\nDigite o nome do destinatário para buscar: ")
    mensagens_encontradas = busca_binaria_mensagens(lista_mensagens, destinatario)
    
    if mensagens_encontradas:
        exibir_mensagens(mensagens_encontradas, f"=== Mensagens para {destinatario} ===")
    else:
        print(f"\nNenhuma mensagem encontrada para {destinatario}")

def main():
    lista_mensagens = []
    
    while True:
        opcao = exibir_menu()
        
        if opcao == '1':
            lista_mensagens = cadastrar_mensagem(lista_mensagens)
            print("\nMensagem cadastrada com sucesso!")
            
        elif opcao == '2':
            buscar_mensagens(lista_mensagens)
            
        elif opcao == '3':
            print("\nEncerrando o sistema...")
            break
            
        else:
            print("\nOpção inválida. Por favor, tente novamente.")

if __name__ == "__main__":
    main()
