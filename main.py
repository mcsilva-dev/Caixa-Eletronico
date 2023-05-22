from time import sleep

print("-"*50)
print("BEM-VINDO AO BANCO SILVA".center(50))
print("-"*50)
print("""CÉDULAS DISPONÍVEIS:
R$50.0
R$20.0
R$10.0
R$5.0
R$2.0
""")

while True:
  valor = input("INSIRA O VALOR DO SAQUE: R$")
  if valor[-1] not in '138':
    print(f"IMPRIMINDO R${int(valor):.1f}")
    print("AGUARDE...")
    sleep(3)
    print("-"*50)
    print("FORAM IMPRIMIDAS:")
    break
  else:
    print("TENTE NOVAMENTE.", end=" ")

saque = int(valor)
atual = 50
cedula = 0

while True:
  if atual <= saque:
    saque -= atual
    cedula += 1
  else:
    if cedula > 0:
      print(f"{cedula} CÉDULAS DE R${atual}.")
      cedula = 0
    if saque == 0:
      break
    if atual == 50:
      atual = 20
    elif atual == 20:
      atual = 10
    elif atual == 10:
      atual = 5
    elif atual == 5:
      atual = 2

print("-"*50)
print("RETIRE TODAS AS CÉDULAS\n")
sleep(3)
print("BANCO SILVA AGRADECE".center(50, '-'))
print("VOLTE SEMPRE".center(50, ">"))