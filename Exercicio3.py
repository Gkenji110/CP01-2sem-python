from Exercicio1 import criar_mensagem, exibir_mensagens
from Exercicio2 import ordenar_por_destinatario

def busca_binaria_mensagens(lista_mensagens: list, destinatario_busca: str) -> list:
    ini = 0
    fim = len(lista_mensagens) - 1
    
    # Encontra o primeiro índice do destinatário
    primeiro_indice = -1
    while ini <= fim:
        meio = (ini + fim) // 2
        destinatario_atual = lista_mensagens[meio]['destinatario']
        
        if destinatario_atual == destinatario_busca:
            primeiro_indice = meio
            fim = meio - 1 
        elif destinatario_atual < destinatario_busca:
            ini = meio + 1
        else:
            fim = meio - 1
    
    if primeiro_indice == -1:
        return []
    
    # Encontra o último índice do destinatário
    ini = primeiro_indice
    fim = len(lista_mensagens) - 1
    ultimo_indice = primeiro_indice
    
    while ini <= fim:
        meio = (ini + fim) // 2
        destinatario_atual = lista_mensagens[meio]['destinatario']
        
        if destinatario_atual == destinatario_busca:
            ultimo_indice = meio
            ini = meio + 1 
        elif destinatario_atual < destinatario_busca:
            ini = meio + 1
        else:
            fim = meio - 1
    
    return lista_mensagens[primeiro_indice:ultimo_indice + 1]

def main():
    lista_mensagens = []
    
    remetentes = ['Ana', 'João', 'Gustavo', 'Flavia', 'Guilherme']
    destinatarios = ['Prof. Eduardo', 'Prof. Tiago', 'Prof. Leandro', 'Prof. Daniel', 'Prof. Willian']
    assuntos = ['Dúvida Exercício', 'Entrega Trabalho', 'Reunião', 'Prova', 'Projeto']
    
    for i in range(20):
        assunto = f"{assuntos[i % len(assuntos)]} {i + 1}"
        destinatario = destinatarios[i % len(destinatarios)]
        remetente = remetentes[i % len(remetentes)]
        conteudo = f"Conteúdo da mensagem {i + 1} enviada por {remetente}"
        
        mensagem = criar_mensagem(assunto, destinatario, remetente, conteudo)
        lista_mensagens.append(mensagem)
    
    mensagens_ordenadas = ordenar_por_destinatario(lista_mensagens)
    
    print("\n" + "=" * 50)
    exibir_mensagens(mensagens_ordenadas, "TODAS AS MENSAGENS (ORDENADAS):")
    
    destinatario_busca = "Prof. Eduardo"
    mensagens_encontradas = busca_binaria_mensagens(mensagens_ordenadas, destinatario_busca)
    
    print("\n" + "=" * 50)
    exibir_mensagens(mensagens_encontradas, f"MENSAGENS ENCONTRADAS PARA: {destinatario_busca}")

if __name__ == "__main__":
    main()
    