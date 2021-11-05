arquivo = open('arquivo.txt','r+')

novoArquivo = []

for registro in arquivo:

    if registro[:6] == '|C190|': ##or '|C100|' :
        newFile = list(registro.split('|'))

        for dados in newFile:
            if dados == '1102' or dados == '6102' : ##or dados == '55':
                 newFile[2]  = '090'
                 newFile[6]  = '0,00'
                 newFile[7]  = '0,00'
                ##newFile[21] = '0,00'
                #newFile[22] = '0,00'
        x = ('|'.join(newFile))
        novoArquivo.append(x)
        continue
    novoArquivo.append(registro)

arquivo.close

novoSped = open ('Narquivo.txt', 'w')
for linha in novoArquivo:
    novoSped.writelines(linha)

novoSped.close()

print('concluido')
