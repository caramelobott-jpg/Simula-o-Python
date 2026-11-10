
import random

print("Bem vindo a simulacao")

while True:
    print("banana, maca, pera")
    escolha = input("Escolhe a fruta: ").lower()

    if escolha in ("maca", "banana", "pera"):
        print("Boa escolha")
        break
    else:
        print("Fruta invalida. Tente novamente.")

for i in range(2):
    print("Indo ao caixa")

print("Voce tem 100 reais de dinheiro")
print("Maca 8 reais | Banana 8 reais | Pera 8 reais")

saldo = 100
valor = 8

if valor <= saldo:
    saldo -= valor
    print("Seu saldo e", saldo)
else:
    print("Saldo insuficiente")

print("Saldo final:", saldo)

print("O sistema vai escolher quantos metros voce deve andar para chegar em casa")

def passos():
    casa = (120, 192, 130, 211)
    metros = 0

    for i in range(3):
        print("Gerando...")
        metros += random.choice(casa)

    return metros

distancia = passos()
print("Metros gerados:", distancia)

print("Se quiser pedir Uber, seu saldo e", saldo)

valor_uber = 60

uber_escolha = input(
    "Deseja ir de Uber? O Uber custa 60 reais. Sim ou Nao: "
).lower()

if uber_escolha == "sim":
    if valor_uber <= saldo:
        saldo -= valor_uber
        print("Voce foi de Uber!")
        print("Seu saldo agora e", saldo)
    else:
        print("Saldo insuficiente para o Uber.")

elif uber_escolha == "nao":
    print("Continue andando. Seu saldo e", saldo)

else:
    print("Escolha invalida.")

sede = True

def andamento():
    global sede

    if sede:
        print("Voce esta com sede.")

    escolha_parar = input(
        "Parar no posto a frente ou continuar? "
    ).lower()

    if escolha_parar == "continuar":
        print("Continuando andando")

    elif escolha_parar == "parar":
        print("Voce parou no posto a frente e bebeu agua")
        sede = False

    else:
        print("Escolha invalida.")

andamento()

while True:
    print("LIMITE DO GAME FOI CORTADO R: CAIXA")

    escolha_game = input(
        "O jogo foi fechado. Digite fechar para fechar: "
    ).lower()

    if escolha_game == "fechar":
        print("Jogo fechando...")
        break

    elif escolha_game == "nao":
        print("Game esta com problemas. Fale com o suporte")
        break

    else:
        print("Palavra invalida")

print("Restauracao do jogo 20/11/2026")
print("Parte 2 - Continuacao")

escolha_kop = input("Vai comparecer na parte 2? ").lower()

if escolha_kop == "sim":
    print("Que bom! Suas paginas voltarao")

elif escolha_kop == "nao":
    print("Espere que um dia volte")

else:
    print("Resposta invalida")

nome = input("Digite seu nome: ")
print("Muito obrigado por comparecer", nome)
print("Wow Game")
