# Conceitos   Notas
# A           De 10.0 á 9.1
# A-          De 9.0 á 8.1
# B           De 8.0 á 7.1
# B-          De 7.0 á 6.1
# C           De 6.0 á 5.1
# C-          De 5.0 á 4.1
# D           De 4.0 á 3.1
# D-          De 3.0 á 2.1
# E           De 2.0 á 1.1
# E-          De 1.0 á 0.0

# *Para notas maiores que 10 e menores que 0 será impresso "Nota inválida"
#!/usr/local/bin/python3


def nota_conceito(nota):
    if float(nota) <= 0 or float(nota) > 10:
        return 'Nota inválida'

    elif float(nota) >= 9.1:
        return 'A'

    elif float(nota) >= 8.1:
        return 'A-'

    elif float(nota) >= 7.1:
        return 'B'

    elif float(nota) >= 6.1:
        return 'B-'

    elif float(nota) >= 5.1:
        return 'C'

    elif float(nota) >= 4.1:
        return 'C-'

    elif float(nota) >= 3.1:
        return 'D'

    elif float(nota) >= 2.1:
        return 'D-'

    elif float(nota) >= 1.1:
        return 'E'

    else:
        return 'E-'


if __name__ == '__main__':
    valor_informado = input('Nota do aluno: ')
    conceito = nota_conceito(valor_informado)
    print(conceito)