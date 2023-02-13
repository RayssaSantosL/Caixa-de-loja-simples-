#iniciando o programa e recebendo o usuário
print("Bem vindo a Loja * nome da loja* ")

def programa():
    #variaveis de entrada
    valor_original = float(input("Valor do produto: R$ "))
    quantidade = int(input("Quantidade: "))

    #sistema de descontos
    if (0 <= quantidade < 5):
        desconto = 0
    elif (5 <= quantidade < 20):
        desconto = 0.03
    elif (20 <= quantidade < 100):
        desconto = 0.06
    else:
        desconto = 0.1

    #variaveis de calculo de desconto
    sem_desconto = valor_original * quantidade
    com_desconto = sem_desconto - sem_desconto * desconto

    #resultado do desconto
    print("Valor sem desconto: R$ {:.2f} ".format(sem_desconto))
    print("Valor com desconto: R$ {:.2f}  (desconto{:.0f}%) ".format (com_desconto, 100*desconto))

repetir = str(input("Deseja somar produto? "))
#repetição
while repetir == "sim":
    programa()
    repetir = str(input("Deseja somar outro produto? "))
else:
    print("Obrigada pela preferência! Volte sempre!")