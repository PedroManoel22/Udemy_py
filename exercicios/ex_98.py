#Cálculo do primeiro digito verificador do CPF
cpf = str(input('Insira o cpf: ').replace('.', ''))
cpf_formatado = cpf.replace('-', '')
soma = 0
a = 10
multiplicacao = 0
nove_digitos = []
for n in cpf_formatado:
    if a >= 2:
        cpf_int = int(n)
        multiplicacao = cpf_int * a
        soma += multiplicacao
        a -= 1
        nove_digitos.append(multiplicacao)
print(soma)
print(nove_digitos)
resto_divisao = (soma * 10) % 11
if resto_divisao > 9:
    primeiro_digito = 0
else:
    primeiro_digito = resto_divisao
print(f'Primeiro digito: {primeiro_digito}')
#746.824.890-70
#74682489070
