from random import randint

seu_nome = input('Qual é o seu nome? ')
print(f'Bem vindo (a) {seu_nome} ao jogo da adivinhação! Escolhi aleatoriamente um número entre 1 e 100, consegue adivinhar qual?')

numero_adivinhado = randint(1, 100)
numero_tentativas = 8

for tentativa in range(1, numero_tentativas + 1):
    print(f'Tentativa {tentativa} de {numero_tentativas}')
    chute = int(input('Escolha seu número: '))
    if chute == numero_adivinhado:
        print(f'Parabéns, você acertou em {tentativa} tentativas!')
        break
    elif chute > numero_adivinhado:
        print('Escolha um número menor!')
    else:
        print('Escolha um número maior!')

print(f'O número é {numero_adivinhado}! Obrigado {seu_nome} por jogar!')

'''if not acertou in range(1, numero_tentativas):
    print('Dessa vez foi quase! MAs não desanime, você pode tentar outras vezes!')'''

