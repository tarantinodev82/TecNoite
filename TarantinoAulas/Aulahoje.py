cargo = input("Digite seu cargo: ").lower()  
salario = float(input("Digite seu salário: "))

if cargo == "vendedor":
    bonus = salario * 0.15
    print("Você é um Vendedor!")
    print(f"Seu bônus é de R$ {bonus:.2f}")

elif cargo == "analista":
    bonus = salario * 0.10
    print("Você é um Analista!")
    print(f"Seu bônus é de R$ {bonus:.2f}")

elif cargo == "gerente":
    bonus = salario * 0.20
    print("Você é o Gerente da loja!")
    print(f"Seu bônus é de R$ {bonus:.2f}")

else:
    print("Cargo não reconhecido.")
