def mostrar_dados(nome, email, idade, categoria):
    print("\n=== DADOS CADASTRADOS ===")
    print("Nome:", nome)
    print("E-mail:", email)
    print("Idade:", idade)
    print("Categoria:", categora)


nome = input("Digite seu nome: ")
email = input("Digite seu e-mail: ")
idade = int(input("Digite sua idade: "))

if idade <= 18:
    categoria = "Maior de idade"
else:
    categoria = "Menor de idade"

mostrar_dados(nome, email, idade, categoria)