import sqlite3

conector = sqlite3.connect("agenda.db")
cursor = conector.cursor()
print(''' Insira o número  da opçao desejada:
    1 - listar
    2 - cadastrar
    3 - alterar
    4 - excluir
    5 - sair
    ''')
Ler = int(input())

if Ler == 1:
    sql = "select *from contatos"
    cursor.execute(sql)
    dados = cursor.fetchall()

    print("-"*35)
    print("{:<12} {:25} {:12} {:10} {:20} {:>6}".format("NumContato","Nome","Cel","Tel","Email","Aniver"))
    print("-"*120)
    for d in dados:
        print("{:<12} {:25} {:12} {:10} {:20} {:>6}".format(d[0],d[1],d[2],d[3],d[4],d[5]))
    print("-"*120)

    print("Encontrados {} registros".format(len(dados)))
    conector.close()
if Ler == 2:
    Nome = input('Nome: ')
    Cel = input('Celular: ')
    Tel = input('Telefone: ')
    Email = input('Email: ')
    Aniver = input('Aniversário: ')

    sql = "insert into contatos(Nome,Cel,Tel,Email,Aniver) values (?,?,?,?,?)"

    cursor.execute(sql, (Nome, Cel, Tel, Email, Aniver))
    conector.commit()
    conector.close()

    print(f'{Nome} cadastrado com sucesso.')












