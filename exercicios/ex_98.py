import random
import sys
contador_Regressivo_1 = 10
soma_multiplicacao_1 = 0
nove_digitos = ''
for i in range(9):
    nove_digitos += str(random.randint(0,9))
for n in nove_digitos:
    if contador_Regressivo_1 >= 2:
        soma_multiplicacao_1 += int(n) * contador_Regressivo_1
        contador_Regressivo_1 -= 1
resto_divisao_1 = (soma_multiplicacao_1 * 10) % 11
primeiro_digito = resto_divisao_1 if resto_divisao_1 <= 9 else 0 #Mesma coisa que isso: if resto_divisao > 9:
    #                                                                                        primeiro_digito = 0
    #                                                                                     else:
    #                                                                                        primeiro_digito = resto_divisao                                                              
    #Cálculo do segundo digito verificador do CPF
contador_Regressivo_2 = 11
Soma_multiplicacao_2 = 0
for n in nove_digitos:
    if contador_Regressivo_2 > 2:
        Soma_multiplicacao_2 += int(n) * contador_Regressivo_2
        contador_Regressivo_2 -= 1
Soma_multiplicacao_2 += primeiro_digito * contador_Regressivo_2
resto_divisao_2 = (Soma_multiplicacao_2 * 10) % 11  
segundo_digito = resto_divisao_2 if resto_divisao_2 <= 9 else 0
novo_cpf = f'{nove_digitos}{primeiro_digito}{segundo_digito}'
print(novo_cpf)
#746.824.890-70
#74682489070    