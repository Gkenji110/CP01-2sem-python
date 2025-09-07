def criar_mensagem(assunto, destinatario, remetente, conteudo):
    mensagem = {
        'assunto': assunto,
        'destinatario': destinatario,
        'remetente': remetente,
        'conteudo': conteudo
    }
    return mensagem

def exibir_mensagens(lista_mensagens, titulo="Mensagens:"):
    print(titulo)
    print("-" * 50)
    for i, mensagem in enumerate(lista_mensagens, 1):
        print(f"\nMensagem {i}:")
        print(f"Destinatário: {mensagem['destinatario']}")
        print(f"Assunto: {mensagem['assunto']}")
        print(f"De: {mensagem['remetente']}")
        print(f"Conteúdo: {mensagem['conteudo']}")
        print("-" * 50)

def main():
    remetentes = ['Ana', 'João', 'Gustavo', 'Flavia', 'Guilherme']
    destinatarios = ['Prof. Eduardo', 'Prof. Tiago', 'Prof. Leandro', 'Prof. Daniel', 'Prof. Willian']
    assuntos = ['Dúvida Exercício', 'Entrega Trabalho', 'Reunião', 'Prova', 'Projeto']
    
    lista_mensagens = []
    
    for i in range(20):
        assunto = f"{assuntos[i % len(assuntos)]} {i + 1}"
        destinatario = destinatarios[i % len(destinatarios)]
        remetente = remetentes[i % len(remetentes)]
        conteudo = f"Conteúdo da mensagem {i + 1} enviada por {remetente}"
        
        mensagem = criar_mensagem(assunto, destinatario, remetente, conteudo)
        lista_mensagens.append(mensagem)
    
    print("\n" + "=" * 50)
    exibir_mensagens(lista_mensagens, "MENSAGENS CRIADAS:")

if __name__ == "__main__":
    main()
