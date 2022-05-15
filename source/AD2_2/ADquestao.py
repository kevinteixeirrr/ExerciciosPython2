import struct
dados = struct.Struct("20s 50s")

# subprograma
def decodificaDados1(bloco):
    desmpack = dados.unpack(bloco)  # desempacotou os arquivos

    bandeira1 = desmpack[0].decode("utf-8").rstrip(chr(0))
    taxa1 = desmpack[1].decode("utf-8").rstrip(chr(0))
    lista = []  # joguei os valores em lista para facilitar a substituição do \n para poder passar de string para float
    lista.append(bandeira1)
    lista.append(taxa1)
    # substitui a string com \n para uma sem \n
    lista = [elem.replace("\n", "")for elem in lista]
    # trasnformei a taxa da bandeira do cartão em numero flutuante
    lista[1] = float(lista[1])
    # calculo do preço a ser convertido
    precoConv = (precoInpt * taxaInpt) + lista[1]
    return precoConv


# programa principal
nomeArq = input()
bandeiraInpt = input()
try:
    taxaInpt = float(input())
except ValueError:
    exit('Você colocou uma taxa não correspondente')
try:
    precoInpt = float(input())
except ValueError:
    exit('Você colocou um valor não correspondente')

try:
    with open('arquivo.txt', 'r', encoding='utf-8') as arquivoTxt:  # leitura do arquivo txt
        with open(nomeArq, "wb") as arquivoBin:  # abri um arquivo bin
            linha = arquivoTxt.readline()
            arquivoTxt.seek(0)
            while linha != "": # comecei a ler as linhas para empacotar os arquivos
                linha = arquivoTxt.readline()
                separadas = linha.split("#")
                if len(separadas) > 1:
                    bandeira = separadas[0]
                    taxa = separadas[1]
                    bloco = dados.pack(bandeira.encode("utf-8"), taxa.encode("utf-8"))# parte onde empacotei os arquivos para binario
                    arquivoBin.write(bloco)
                    if bandeiraInpt == 'Visa' and taxa == '123.90\n':# condição para cada bandeira do cartao, se for a bandeira e a taxa dela faça
                        resul = decodificaDados1(bloco)
                        print(f'Como seu cartão é da bandeira {bandeiraInpt}, então você pagará {resul:.2f}')
                        break
                    elif bandeiraInpt == 'Mastercard' and taxa == '245.45\n':
                        resul = decodificaDados1(bloco)
                        print(f'Como seu cartão é da bandeira {bandeiraInpt}, então você pagará {resul:.2f}')
                        break
                    elif bandeiraInpt == 'Diners' and taxa == '367\n':
                        resul = decodificaDados1(bloco)
                        print(f'Como seu cartão é da bandeira {bandeiraInpt}, então você pagará {resul:.2f}')
                        break
                    elif bandeiraInpt == 'Elo' and taxa == '532\n':
                        resul = decodificaDados1(bloco)
                        print(f'Como seu cartão é da bandeira {bandeiraInpt}, então você pagará {resul:.2f}')
                        break
                else:#caso não encontre a bandeira do cartão ele ecerra e deixa a mensagem
                    print('Cartão não consta')
                    break
except IOError:#em caso de erro por não encontrar o arquivo
    print('Um dos arquivos não foi encontrado ou digitou errado.')
