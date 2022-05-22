import random 

print("***** JOGO DE ADINHA *****")

numeroSecreto = random.randint(0, 12)

print(numeroSecreto)
total_de_tentativas = 5
rodada = 1

for rodadas in range(1, total_de_tentativas):
   print("Tentativa {} de {}".format(rodadas, total_de_tentativas))
   chute = int(input("Digite um numero: "))

   acertou = chute == numeroSecreto
   maiorQ = chute > numeroSecreto
   menorQ = chute < numeroSecreto

   if(acertou):
      print("Voce acertou o numero secreto")
      break
   else:
      if(maiorQ):
         print("Voce errou! Seu chute foi maior que o numero secreto")
      elif(menorQ):
         print("Voce errou! Seu chute foi menor que o numero secreto")
print("FIM DE JOGO")