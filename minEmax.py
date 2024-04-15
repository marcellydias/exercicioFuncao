vetor=[]
tamVetor = int(input("Digite o tamanho do seu vetor: "))
for i in range(tamVetor):
  vetor.append(float(input("digite um número: ")))

maior = vetor[0]
menor = vetor[0]

def max (vet):
  global maior
  for i in range(tamVetor):
    if(vet[i]>maior):
      maior=vetor[i]

def min (vet):
  global menor
  for i in range(tamVetor):
    if(vet[i]<menor):
      menor=vetor[i]


max(vetor)
min(vetor)
print("O maior número que você digitou foi: " , maior)
print("O menor número que você digitou foi: " , menor)
