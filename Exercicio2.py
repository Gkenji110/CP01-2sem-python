from Exercicio1 import criar_mensagem, exibir_mensagens

def ordenar_por_destinatario(lista_mensagens):
    return sorted(lista_mensagens, key=lambda x: x['destinatario'])

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
    
    print("\n" + "=" * 50)
    mensagens_ordenadas = ordenar_por_destinatario(lista_mensagens)
    exibir_mensagens(mensagens_ordenadas, "MENSAGENS ORDENADAS POR DESTINATÁRIO:")

if __name__ == "__main__":
    main()
