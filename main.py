# biblioteca
import random

# inserir nomes
nomes = []
quantidade = int(input("Quantos nomes você deseja inserir? "))

# lista de nomes 
for i in range(quantidade):
     nome = input(f"Insira o nome {i + 1}: ")
     nomes.append(nome)

# sortear nomes
nome_sorteado = random.choice(nomes)
print(f"O nome sorteado é: {nome_sorteado}")

