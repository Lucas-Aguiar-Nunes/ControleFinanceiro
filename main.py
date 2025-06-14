from crud import *
from erros import *

def menu():
    while True:
        try:
            print("\t\tControle Financeiro")
            print("\t\tMenu")
            print("[1] - Inserir")
            print("[2] - Consultar")
            print("[3] - Atualizar")
            print("[4] - Deletar")
            print("[5] - Alterar Moeda")
            print("[0] - Sair ")
            print("\nDigite a Opção Desejada:")

            escolha = input("\nOpção: ")
            if escolha == "1":
                adicionar()
            elif escolha == "2":
                consultar()
            elif escolha == "3":
                atualizar()
            elif escolha == "4":
                deletar()
            elif escolha == "5":
                alterar_moeda()
            elif escolha == "0":
                break
            else:
                raise Escolha_Menu_Incorreta
        except Escolha_Menu_Incorreta:
            print('Opção inválida. Tente novamente.')
            sair = input("Pressione Qualquer Tecla Para Voltar...")
    print("Fechando Programa...")

def adicionar():
    while True:
        try:
            print("\t\tControle Financeiro")
            print("\t\tAdicionar no Banco de Dados")
            print("[1] - Usuario ")
            print("[2] - Meta ")
            print("[3] - Categoria ")
            print("[4] - Pagamento ")
            print("[5] - Provento ")
            print("[0] - Voltar ")
            print("\nDigite a Opção Desejada:")

            escolha = input("\nOpção: ")
            if escolha == "1":
                entrada_usuario()
            elif escolha == "2":
                entrada_meta()
            elif escolha == "3":
                entrada_categoria()
            elif escolha == "4":
                entrada_pagamento()
            elif escolha == "5":
                entrada_provento()
            elif escolha == "0":
                print("Voltando para Menu Principal")
            else:
                raise Escolha_Menu_Incorreta
        except Escolha_Menu_Incorreta:
            print('Opção inválida. Tente Novamente.')
        except ID_Incorreto:
            print("ID não Encontrado. Tente Novamente")
        else:
            break
        finally:
            sair = input("Pressione Qualquer Tecla Para Voltar...")

def consultar():
    while True:
        try:
            print("\t\tControle Financeiro\n")
            print("\t\t Consultar no Banco de Dados\n")
            print("[1] - Usuario ")
            print("[2] - Meta ")
            print("[3] - Categoria ")
            print("[4] - Pagamento ")
            print("[5] - Provento ")
            print("[0] - Voltar ")
            print("\nDigite a Opção Desejada:")

            escolha = input("\nOpção: ")
            if escolha == "1":
                listar_usuarios()
            elif escolha == "2":
                listar_metas()
            elif escolha == "3":
                listar_categorias()
            elif escolha == "4":
                listar_pagamentos()
            elif escolha == "5":
                listar_proventos()
            elif escolha == "0":
                print("Voltando para Menu Principal.")
            else:
                raise Escolha_Menu_Incorreta
        except Escolha_Menu_Incorreta:
            print('Opção inválida. Tente Novamente.')
        else:
            break
        finally:
            sair = input("Pressione Qualquer Tecla Para Voltar...")

def atualizar():
    while True:
        try:
            print("\t\tControle Financeiro\n")
            print("\t\t Atualizar no Banco de Dados\n")
            print("[1] - Usuario ")
            print("[2] - Meta ")
            print("[3] - Categoria ")
            print("[4] - Pagamento ")
            print("[5] - Provento ")
            print("[0] - Voltar ")
            print("\nDigite a Opção Desejada:")

            escolha = input("\nOpção: ")
            if escolha == "1":
                id = int(input("Informe o ID do Usuário: "))
                usuario = session.query(Usuario).filter_by(id=id).first()
                if usuario:
                    print(f"{usuario.id} - {usuario.nome}\t| Email: {usuario.email}\t| Saldo: {usuario.moeda}{usuario.saldo}")
                    entrada_usuario(usuario)
                else:
                    raise ID_Incorreto
            elif escolha == "2":
                id = int(input("Informe o ID da Meta: "))
                meta = session.query(Meta).filter_by(id=id).first()
                if meta:
                    print(f"{meta.id} - {meta.nome}\t| Conta: {meta.conta_id}\t| Valor: {meta.moeda}{meta.valor}\t| Saldo: {meta.moeda}{meta.saldo}\t Prazo: {meta.prazo}")
                    entrada_meta(meta)
                else:
                    raise ID_Incorreto
            elif escolha == "3":
                id = int(input("Informe o ID da Categoria: "))
                categoria = session.query(Categoria).filter_by(id=id).first()
                if categoria:
                    print(f"{categoria.id} - {categoria.nome}\t| Limite: {categoria.moeda}{categoria.limite}\t| Saldo: {categoria.moeda}{categoria.saldo}")
                    entrada_categoria(categoria)
                else:
                    raise ID_Incorreto
            elif escolha == "4":
                id = int(input("Informe o ID do Pagamento: "))
                pagamento = session.query(Pagamento).filter_by(id=id).first()
                if pagamento:
                    print(f"{pagamento.id} - {pagamento.nome}\t| Conta: {pagamento.conta_id}\t| Categoria: {pagamento.categoria_id}\t| Valor: {pagamento.moeda}{pagamento.valor}\t| Forma: {pagamento.forma_pagamento}")
                    entrada_pagamento(pagamento)
                else:
                    raise ID_Incorreto
            elif escolha == "5":
                id = int(input("Informe o ID do Provento: "))
                provento = session.query(Provento).filter_by(id=id).first()
                if provento:
                    print(f"{provento.id} - {provento.nome}\t| Conta: {provento.conta_id}\t| Fonte: {provento.fonte}\t| Valor: {provento.moeda}{provento.valor}")
                    entrada_provento(provento)
                else:
                    raise ID_Incorreto
            elif escolha == "0":
                print("Voltando para Menu Principal.")
            else:
                raise Escolha_Menu_Incorreta
        except Escolha_Menu_Incorreta:
            print('Opção inválida. Tente Novamente.')
        except ID_Incorreto:
            print("ID não Encontrado. Tente Novamente")
        else:
            break
        finally:
            sair = input("Pressione Qualquer Tecla Para Voltar...")

def deletar():
    while True:
        try:
            print("\t\tControle Financeiro\n")
            print("\t\t Deletar no Banco de Dados\n")
            print("[1] - Usuario ")
            print("[2] - Meta ")
            print("[3] - Categoria ")
            print("[4] - Pagamento ")
            print("[5] - Provento ")
            print("[0] - Voltar ")
            print("\nDigite a Opção Desejada:")

            escolha = input("\nOpção: ")
            if escolha == "1":
                id = int(input("Informe o ID do Usuário: "))
                usuario = session.query(Usuario).filter_by(id=id).first()
                if usuario:
                    session.delete(usuario)
                    session.commit()
                    print("Apagado com Sucesso.")
                else:
                    raise ID_Incorreto
            elif escolha == "2":
                id = int(input("Informe o ID da Meta: "))
                meta = session.query(Meta).filter_by(id=id).first()
                if meta:
                    session.delete(meta)
                    session.commit()
                    print("Apagado com Sucesso.")
                else:
                    raise ID_Incorreto
            elif escolha == "3":
                id = int(input("Informe o ID da Categoria: "))
                categoria = session.query(Categoria).filter_by(id=id).first()
                if categoria:
                    session.delete(categoria)
                    session.commit()
                    print("Apagado com Sucesso.")
                else:
                    raise ID_Incorreto
            elif escolha == "4":
                id = int(input("Informe o ID do Pagamento: "))
                pagamento = session.query(Pagamento).filter_by(id=id).first()
                if pagamento:
                    session.delete(pagamento)
                    session.commit()
                    print("Apagado com Sucesso.")
                else:
                    raise ID_Incorreto
            elif escolha == "5":
                id = int(input("Informe o ID do Provento: "))
                provento = session.query(Provento).filter_by(id=id).first()
                if provento:
                    session.delete(provento)
                    session.commit()
                    print("Apagado com Sucesso.")
                else:
                    raise ID_Incorreto
            elif escolha == "0":
                print("Voltando para Menu Principal.")
            else:
                raise Escolha_Menu_Incorreta
        except Escolha_Menu_Incorreta:
            print('Opção inválida. Tente Novamente.')
        except ID_Incorreto:
            print("ID não Encontrado. Tente Novamente")
        except ValueError:
            print("Valor Deve ser Numerico. Tente Novamente.")
        else:
            break
        finally:
            sair = input("Pressione Qualquer Tecla Para Voltar...")

def alterar_moeda():
    try:
        escolha = int(input("Digite [1] para Real (R$)\nDigite [2] para Dólar (U$)\n"))
        if escolha == 1:
            moeda = "RS"
        elif escolha == 2:
            moeda = 'U$'
        else:
            raise Escolha_Menu_Incorreta
    except Escolha_Menu_Incorreta:
        print("Entrada Invalida!")
    else:
        Usuario.alterar_moeda(moeda)
        Categoria.alterar_moeda(moeda)
        Pagamento.alterar_moeda(moeda)
        Provento.alterar_moeda(moeda)
        Meta.alterar_moeda(moeda)
    finally:
        sair = input("Pressione Qualquer Tecla Para Voltar...")   


if __name__ == "__main__":
    menu()