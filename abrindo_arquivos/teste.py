caminho_arquivo = 'C:\\Users\\Pedro\\Documents\\GitHub\\Udemy_py\\abrindo_arquivos\\'
caminho_arquivo += 'criando_arquivo.txt'

# criando arquivo e escrevendo
with open(caminho_arquivo, 'w', encoding='utf-8') as arquivo: # 'w' apaga tudo que tem no arquivo e escreve tudo que vc quer, 'a' coloca o que vc quer no final do arquivo, sem apagar nada, 'encoding='utf-8'' serve para o vs code conseguir ler caracteres epeciais como acentuações 
    arquivo.write('AtenÃ§Ã£o\n')
    arquivo.write('linha 2\n')
    arquivo.writelines(('linha 3\n', 'linha 4 \n')) # escrever mais de uma linha
    arquivo.writelines(('Estou adicionando mais linhas parraa teste\n', 'hehehe\n'))
    #arquivo.seek(0, 0) # mover o cursor para o topo
    
   
    

# lendo arquivo
with open(caminho_arquivo, 'r') as arquivo:

    #print(arquivo.read())
    #print(arquivo.readline()) # lendo linha por linha
    for linha in arquivo.readlines():
        print(linha.strip())