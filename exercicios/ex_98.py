#Cálculo do primeiro digito verificador do CPF
cpf = str(input('Insira o cpf: '))
Contador_Regressivo_1 = 10
Soma_multiplicacao_1 = 0
for n in cpf:
    if Contador_Regressivo_1 >= 2:
        cpf_int = int(n)
        Soma_multiplicacao_1 += cpf_int * Contador_Regressivo_1
        Contador_Regressivo_1 -= 1
print(Soma_multiplicacao_1)
resto_divisao_1 = (Soma_multiplicacao_1 * 10) % 11
primeiro_digito = resto_divisao_1 if resto_divisao_1 <= 9 else 0 #Mesma coisa que isso: if resto_divisao > 9:
#                                                                                        primeiro_digito = 0
#                                                                                     else:
#                                                                                        primeiro_digito = resto_divisao                                                              
print(f'Primeiro digito: {primeiro_digito}')
#Cálculo do segundo digito verificador do CPF
contador_Regressivo_2 = 11
Soma_multiplicacao_2 = 0
for n in cpf:
    if contador_Regressivo_2 >= 2:
        cpf_int = int(n)
        Soma_multiplicacao_2 += cpf_int * contador_Regressivo_2
        contador_Regressivo_2 -= 1
print(Soma_multiplicacao_2)
resto_divisao_2 = (Soma_multiplicacao_2 * 10) % 11
segundo_digito = resto_divisao_2 if resto_divisao_2 <= 9 else 0
print(f'Segundo digito: {segundo_digito}')
#746.824.890-70
#74682489070
