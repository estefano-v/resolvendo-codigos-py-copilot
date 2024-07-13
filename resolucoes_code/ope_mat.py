# Vamos solicitar como entrada dois numeros e depois vamos realizar uma operação simples entre eles.

# Solicitando os dois números.

num1 = int (input("Entre com o primeiro numero: "))

num2 = int (input("entre com o segundo número: "))

# Entrando com a escolha da operação.

operação = input("Entre com a operação que deseja estar realizando (+ ,-, *, /) : ")

# Realizando a condição da operação escolhida.
# Caso a operação seja diferente das anteriores retorna inválida.

if operação == "+":
    print(num1 + num2)
elif operação == "-":
    print(num1 - num2)
elif operação == "*":
    print(num1 * num2)
elif operação == "/":
    print(num1 / num2)
else:
    print("Operação inválida !")

# Peço licença para discordar do uso do código "abs" pois o problema pediu uma operação simples, como se fosse em uma calculadora.
