PALAVRAS_PROIBIDAS = {'futebol', 'religião', 'política'}
textos = [
    'João gosta de futebol e política',
    'A praia foi divertida',
]

for texto in textos:
    intersecao = PALAVRAS_PROIBIDAS.intersection(set(texto.lower().split()))
    if intersecao:
        print('Texto possui palavras proíbidas:', intersecao)
    else:
        print('Texto autorizado:', texto)