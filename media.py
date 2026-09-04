# Programa para calcular a média dos alunos 

nota1 = float(input("Digite sua 1° nota:"))
nota2 = float(input("Digite sua 2° nota:"))
nota3 = float(input("Digite sua 3° nota:"))
nota4 = float(input("Digite sua 4° nota:"))

media = (nota1 + nota2 + nota3 + nota4) /4

print(f"A sua média final é:{media:. 2f}")

if media >=7.0:
    print("Você foi aprovado!!!")

elif media >=5.0 and media <7.0:
    print("Você está de recuperação!!!")

elif media <5.0:
    print("Você está reprovado!!!")