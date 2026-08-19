#ATIVIDADE1
alturas = []
alturas_masculino = []
quantidade_feminino = 0

print("=== Cadastro de 15 pessoas ===")

for i in range(15):
    print(f"\nPessoa {i + 1}")

    altura = float(input("Digite a altura (em metros): "))
    genero = input("Digite o gênero (Masculino/Feminino): ").strip().lower()

    alturas.append(altura)

    if genero == "masculino":
        alturas_masculino.append(altura)

    elif genero == "feminino":
        quantidade_feminino += 1

    else:
        print("Gênero inválido. Digite Masculino ou Feminino.")

# Maior e menor altura
maior_altura = max(alturas)
menor_altura = min(alturas)

# Média das alturas masculinas
if len(alturas_masculino) > 0:
    media_masculino = sum(alturas_masculino) / len(alturas_masculino)
else:
    media_masculino = 0

# Resultados
print("\n=== RESULTADOS ===")
print(f"Maior altura do grupo: {maior_altura:.2f} m")
print(f"Menor altura do grupo: {menor_altura:.2f} m")
print(f"Média de altura dos homens: {media_masculino:.2f} m")
print(f"Número de pessoas do gênero feminino: {quantidade_feminino}")
