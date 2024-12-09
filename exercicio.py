import random
resultado = 0
def scoreboard():
  resultado =+ 1
  print (f"Scoreboard: {resultado}")
def main():
  numaleatorio = (random.randrange(1,21))
  tentativas = 6
  numescolhido = 0
  while numescolhido != numaleatorio:
      numescolhido = int(input("Escolha um número de 1 a 20: "))
      tentativas = tentativas - 1
      if numescolhido < numaleatorio:
        print ("O número é maior")
      elif numescolhido > numaleatorio:
        print ("O número é menor: ")
      elif numescolhido == numaleatorio:
        print ("Acertaste!")
        scoreboard()

  if tentativas == 0:
    print (f"Acabaram as tuas tentativas, o número era {numaleatorio}")
    quit()

if __name__ == "__main__":
  main()
