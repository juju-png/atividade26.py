# Exercício Python 26: Desenvolva um programa que leia o primeiro termo e a razão de uma Pogreçao Aritimetica.
# No final, mostre os 10 primeiros termos dessa progressão.

primeiro_termo = float(input("Digite o primeiro termo da progressão aritmética: "))
razao = float(input("Digite a razão da progressão aritmética: "))
termos = []
for i in range(10):
    termo_atual = primeiro_termo + i * razao
    termos.append(termo_atual)

print("Os 10 primeiros termos da progressão aritmética são:")
for termo in termos:
    print(termo)
