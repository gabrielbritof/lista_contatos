contatos = []

# funções
def adicionar_contato(contatos, nome_contato, tel_contato, email_contato):
    contato_info = {"nome": nome_contato, "telefone": tel_contato, "email": email_contato, "favorito": True}
    contatos.append(contato_info)
    print(f"O contato de {nome_contato} foi adicionado!")
    return

def ver_contatos(contatos):
    print("\nLista de Contatos:")
    for indice, contato_info in enumerate(contatos):
        favorito = "⭐" if contato_info["favorito"] else "  "
        nome_contato = contato_info["nome"]
        print(f"{indice + 1}. {favorito} {nome_contato}: {tel_contato}, {email_contato}")
    return

def editar_nome_contato(contatos, indice_contato, novo_nome_contato):  
    indice_contato_ajustado = int(indice_contato) - 1
    if indice_contato_ajustado >= 0 and indice_contato_ajustado < len(contatos):
        contatos[indice_contato_ajustado]["nome"] = novo_nome_contato
        print(f"\nContato {indice_contato} atualizado para {novo_nome_contato}")
    else:
        print("\nÍndice da tarefa inválido.")
    return

def atualizar_favorito(contatos, indice_contato):
    indice_contato_ajustado = int(indice_contato) - 1
    if indice_contato_ajustado >= 0 and indice_contato_ajustado < len(contatos):
        if contatos[indice_contato_ajustado]["favorito"]:
            contatos[indice_contato_ajustado]["favorito"] = False
            print(f"\nContato {indice_contato} removido dos favoritos.")
        else:
            contatos[indice_contato_ajustado]["favorito"] = True
            print(f"\nContato {indice_contato} marcado como favorito.")
    else:
        print("\nÍndice de contato inválido.")
    return

def ver_contatos_favoritos(contatos):
    print("\nLista de Contatos Favoritos:")
    for indice, contato_info in enumerate(contatos):
        if contato_info["favorito"]:
            nome_contato = contato_info["nome"]
            print(f"{indice + 1}. ⭐ {nome_contato}: {tel_contato}, {email_contato}")
    return

def deletar_contato(contatos, indice):
    if indice >= 0 and indice < len(contatos):
        contato_removido = contatos.pop(indice)
        print(f"Contato {contato_removido['nome']} removido da sua lista")
    else:
        print("\nÍndice de contato inválido.")
    return

while True:
    print("\n----AGENDA DE CONTATOS----")
    print("1. Adicionar um contato")
    print("2. Ver contatos cadastrados")
    print("3. Editar contato")
    print("4. Marcar/Desmcarcar favorito")
    print("5. Ver lista de favoritos")
    print("6. Deletar contato")
    print("7. Sair")
    print("---------------------------")

    escolha = int(input("Digite a sua escolha: "))

    if escolha == 1:
        nome_contato = input("Digite o nome do novo contato: ")
        tel_contato = input("Digite o telefone: ")
        email_contato = input("Digite o e-mail: ")
        adicionar_contato(contatos, nome_contato, tel_contato, email_contato)
        favorito = input("Deseja salvar como favorito? (S/N) ").upper()
        if favorito == "S":
            contatos[-1]["favorito"] = True
        else:
            contatos[-1]["favorito"] = False
    
    elif escolha == 2:
        ver_contatos(contatos)

    elif escolha == 3:
        ver_contatos(contatos)
        indice_contato = input("Digite o índice do contato que deseja editar: ")
        novo_nome = input("Digite o novo nome do contato: ")
        editar_nome_contato(contatos, indice_contato, novo_nome)
    
    elif escolha == 4:
        ver_contatos(contatos)
        indice_contato = input("Qual o índice do contato que deseja marcar ou desmarcar como favorito? ")
        atualizar_favorito(contatos, indice_contato)

    elif escolha == 5:
        ver_contatos_favoritos(contatos)

    elif escolha == 6:
        ver_contatos(contatos)
        indice = int(input("Qual o índice do contato que deseja remover? ")) - 1
        deletar_contato(contatos, indice)

    elif escolha == 7:
        break