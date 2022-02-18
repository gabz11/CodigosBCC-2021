# Calculadora/Conversora de bases númericas - TDE 1 - Grupo 7


# Inicio das funções de Conversão de base

# Conversões partindo do decimal

# Decimal para hexadecimal
def DecParaHex(x):
    x = int(x)
    novo_numero = ""
    # verifica se for 0 para retornar 0
    if x == 0:
        return x
    else:
        while x > 0:
            i = x % 16

            if i > 9:
                if i == 10:
                    novo_numero = novo_numero + "A"
                elif i == 11:
                    novo_numero = novo_numero + "B"
                elif i == 12:
                    novo_numero = novo_numero + "C"
                elif i == 13:
                    novo_numero = novo_numero + "D"
                elif i == 14:
                    novo_numero = novo_numero + "E"
                elif i == 15:
                    novo_numero = novo_numero + "F"

            else:
                novo_numero = novo_numero + str(i)

            x = x // 16

        novo_numero = novo_numero[::-1]
        return novo_numero

# Decimal para binário
def DecParaBi(x):
    x = int(x)
    novo_numero = ""
    # verifica se é 0 para retornar 0
    if x == 0:
        return x
    else:
        while x > 0:
            if x % 2 == 0:
                novo_numero = novo_numero + "0"
                x = x / 2
            else:
                novo_numero = novo_numero + "1"
                x = (x / 2) - 0.5
        novo_numero = novo_numero[::-1]
        return int(novo_numero)

# Decimal para octal
def DecParaOct(x):
    x = int(x)
    novo_numero = ""
    # verifica se é 0 para retornar 0
    if x == 0:
        return x
    else:
        while x > 0:
            i = x % 8

            novo_numero = novo_numero + str(i)

            x = x // 8

        novo_numero = novo_numero[::-1]
        return int(novo_numero)


# Conversões partindo do hexadecimal

# Hexadecimal para decimal.
def HexParaDec(x):
    x = str(x)
    novo_numero = 0
    exponente = len(x) - 1
    for i in x:
        if i == "0" or i == "1" or i == "2" or i == "3" or i == "4" or i == "5" or i == "6" or i == "7" or i == "8" or i == "9":
            novo_numero = novo_numero + int(i) * 16**exponente
        elif i == "A":
            novo_numero = novo_numero + 10 * 16**exponente
        elif i == "B":
            novo_numero = novo_numero + 11 * 16**exponente
        elif i == "C":
            novo_numero = novo_numero + 12 * 16**exponente
        elif i == "D":
            novo_numero = novo_numero + 13 * 16**exponente
        elif i == "E":
            novo_numero = novo_numero + 14 * 16**exponente
        elif i == "F":
            novo_numero = novo_numero + 15 * 16**exponente
        exponente = exponente - 1

    return novo_numero

# Hexadecimal para binário
def HexParaBi(x):
    x = str(x)
    x = x.upper()
    novo_numero = ""
    for i in x:
        if i == "0":
            novo_numero = novo_numero + "0000"
        elif i == "1":
            novo_numero = novo_numero + "0001"
        elif i == "2":
            novo_numero = novo_numero + "0010"
        elif i == "3":
            novo_numero = novo_numero + "0011"
        elif i == "4":
            novo_numero = novo_numero + "0100"
        elif i == "5":
            novo_numero = novo_numero + "0101"
        elif i == "6":
            novo_numero = novo_numero + "0110"
        elif i == "7":
            novo_numero = novo_numero + "0111"
        elif i == "8":
            novo_numero = novo_numero + "1000"
        elif i == "9":
            novo_numero = novo_numero + "1001"
        elif i == "A":
            novo_numero = novo_numero + "1010"
        elif i == "B":
            novo_numero = novo_numero + "1011"
        elif i == "C":
            novo_numero = novo_numero + "1100"
        elif i == "D":
            novo_numero = novo_numero + "1101"
        elif i == "E":
            novo_numero = novo_numero + "1110"
        elif i == "F":
            novo_numero = novo_numero + "1111"

    return int(novo_numero)

# Hexadecimal para Octal.
def HexParaOct(x):
    x = HexParaBi(x)
    novo_numero = BiParaOct(x)

    return novo_numero


#Conversão a partir de Binário

# Binário para decimal.
def BiParaDec(x):
    novo_numero = 0
    exponente = len(str(x)) - 1
    for i in str(x):
        if i == "1":
            novo_numero = novo_numero + 2**exponente
        exponente = exponente - 1
    return novo_numero

# Binario para hexadecimal.
def BiParaHex(x):
    x = str(x)
    novo_numero = ""
    lista = []
    prompt = len(x)
    while prompt % 4 != 0:
        lista.append("0")
        prompt = prompt + 1
    for i in x:
        lista.append(i)
    for i in range(0, len(lista) - 1, 4):
        if lista[i] == "0":
            if lista[i + 1] == "0":
                if lista[i + 2] == "0":
                    if lista[i + 3] == "0":
                        novo_numero = novo_numero + "0"
                    else:
                        novo_numero = novo_numero + "1"
                else:
                    if lista[i + 3] == "0":
                        novo_numero = novo_numero + "2"
                    else:
                        novo_numero = novo_numero + "3"
            else:
                if lista[i + 2] == "0":
                    if lista[i + 3] == "0":
                        novo_numero = novo_numero + "4"
                    else:
                        novo_numero = novo_numero + "5"
                else:
                    if lista[i + 3] == "0":
                        novo_numero = novo_numero + "6"
                    else:
                        novo_numero = novo_numero + "7"
        else:
            if lista[i + 1] == "0":
                if lista[i + 2] == "0":
                    if lista[i + 3] == "0":
                        novo_numero = novo_numero + "8"
                    else:
                        novo_numero = novo_numero + "9"
                else:
                    if lista[i + 3] == "0":
                        novo_numero = novo_numero + "A"
                    else:
                        novo_numero = novo_numero + "B"
            else:
                if lista[i + 2] == "0":
                    if lista[i + 3] == "0":
                        novo_numero = novo_numero + "C"
                    else:
                        novo_numero = novo_numero + "D"
                else:
                    if lista[i + 3] == "0":
                        novo_numero = novo_numero + "E"
                    else:
                        novo_numero = novo_numero + "F"

    return novo_numero

# Binário para octal
def BiParaOct(x):
    x = str(x)
    novo_numero = ""
    lista = []
    prompt = len(x)
    while prompt % 3 != 0:
        lista.append("0")
        prompt = prompt + 1
    for i in x:
        lista.append(i)
    for i in range(0, len(lista) - 1, 3):
        if lista[i] == "0":
            if lista[i + 1] == "0":
                if lista[i + 2] == "0":
                    novo_numero = novo_numero + "0"
                else:
                    novo_numero = novo_numero + "1"
            else:
                if lista[i + 2] == "0":
                    novo_numero = novo_numero + "2"
                else:
                    novo_numero = novo_numero + "3"
        else:
            if lista[i + 1] == "0":
                if lista[i + 2] == "0":
                    novo_numero = novo_numero + "4"
                else:
                    novo_numero = novo_numero + "5"
            else:
                if lista[i + 2] == "0":
                    novo_numero = novo_numero + "6"
                else:
                    novo_numero = novo_numero + "7"
    return int(novo_numero)


#Conversão a partir de Octadecimal

# Octal para decimal
def OctParaDec(x):
    x = str(x)
    novo_numero = 0
    exponente = len(x) - 1
    for i in x:
        novo_numero = novo_numero + int(i) * 8**exponente
        exponente = exponente - 1
    return novo_numero

# Octal para hexadecimal
def OctParaHex(x):
    x = OctParaBi(x)
    novo_numero = BiParaHex(x)

    return novo_numero

# Octal para binário
def OctParaBi(x):
    x = str(x)
    novo_numero = ""
    for i in x:
        if i == "0":
            novo_numero = novo_numero + "000"
        elif i == "1":
            novo_numero = novo_numero + "001"
        elif i == "2":
            novo_numero = novo_numero + "010"
        elif i == "3":
            novo_numero = novo_numero + "011"
        elif i == "4":
            novo_numero = novo_numero + "100"
        elif i == "5":
            novo_numero = novo_numero + "101"
        elif i == "6":
            novo_numero = novo_numero + "110"
        elif i == "7":
            novo_numero = novo_numero + "111"

    return int(novo_numero)

# Fim das funções de conversão

# Início de funções de operação/cálculo entre bases

# Retorna uma base de acordo com o que o usuário escolhe
def escolhaBase():
    # Retorna a base para operações
    # 1. Binário
    # 2. Octal
    # 3. Decimal
    # 4. Hexadecimal.
    while True:
        prompt = input(">> ")
        if prompt == "1":
            base = ["0", "1"]
            return base
        elif prompt == "2":
            base = ["0", "1", "2", "3", "4", "5", "6", "7"]
            return base
        elif prompt == "3":
            base = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
            return base
        elif prompt == "4":
            base = [
                "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", 'A', 'B',
                'C', 'D', 'E', 'F'
            ]
            return base
        else:
            print("\nOpção inválida...")

# Retorna a operação para fazer o calculo entre as bases
def escolhaOp():
    print("")
    print("=-" * 20)
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Resto")
    print("=-" * 20)
    print("")
    while True:
        prompt = input("Escolha uma operação: ")
        if prompt == "1":
            op = "+"
            return op
        elif prompt == "2":
            op = "-"
            return op
        elif prompt == "3":
            op = "*"
            return op
        elif prompt == "4":
            op = "%"
            return op
        else:
            print("Opção inválida")

# Retorna o número de entrada do usuário após verificar que ele pertence à base na qual o usuário escolheu.
def entradaNum(base):
    prompt = "\n>> "
    if len(base) == 2:
        # Binario
        flag = True
        while flag:
            numero = input(prompt)
            numero = numero.strip()
            numero_holder = list(numero)
            valores_invalidos = []
            for x in numero_holder:
                if x not in base:
                    valores_invalidos.append(x)
            if len(valores_invalidos) > 0:
                print("Número inválido")
            else:
                return numero
    elif len(base) == 8:
        # Octal
        flag = True
        while flag:
            numero = input(prompt)
            numero = numero.strip()
            numero_holder = list(numero)
            valores_invalidos = []
            for x in numero_holder:
                if x not in base:
                    valores_invalidos.append(x)
            if len(valores_invalidos) > 0:
                print("Número inválido")
            else:
                return numero
    elif len(base) == 10:
        # Decimal
        flag = True
        while flag:
            numero = input(prompt)
            numero = numero.strip()
            numero_holder = list(numero)
            valores_invalidos = []
            for x in numero_holder:
                if x not in base:
                    valores_invalidos.append(x)
            if len(valores_invalidos) > 0:
                print("Número inválido")
            else:
                return numero
    elif len(base) == 16:
        # Hex
        flag = True
        while flag:
            numero = input(prompt)
            numero = numero.strip()
            numero = numero.upper()
            numero_holder = list(numero)
            valores_invalidos = []
            for x in numero_holder:
                if x not in base:
                    valores_invalidos.append(x)
            if len(valores_invalidos) > 0:
                print("Número inválido")
            else:
                return numero

# Transforma a base em decimal para realizar à operação
def parseTermo(n, base):
    if len(base) == 2:
        numero = BiParaDec(n)
        return numero
    elif len(base) == 8:
        numero = OctParaDec(n)
        return numero
    elif len(base) == 10:
        numero = n
        return numero
    elif len(base) == 16:
        numero = HexParaDec(n)
        return numero

# Recebe 2 números de 2 diferentes bases que foram convertidos para decimal para realizar a operação e
# retorna o resultado em decimal
def opBases(num1_dec, num2_dec, operacao):
    # Operações entre bases
    if operacao == "+":
        # soma
        resultado = num1_dec + num2_dec
        return str(resultado)

    elif operacao == "-":
        # subtração
        resultado = num1_dec - num2_dec
        return str(resultado)

    elif operacao == "*":
        # multiplicação
        resultado = num1_dec * num2_dec
        return str(resultado)

    elif operacao == "%":
        # resto
        try:
            resultado = num1_dec % num2_dec
            int(resultado)
            return str(resultado)
        except (ZeroDivisionError):
            return print("Não se pode dividir por 0.")

# Retorna o tipo de base 'BIN' 'OCT' 'DEC' 'HEX' para estética
def tipoBase(base):
    # Identifica o tipo de base e retorna string para exibir na interface
    if len(base) == 2:
        tipo = "BIN"
        return tipo
    elif len(base) == 8:
        tipo = "OCT"
        return tipo
    elif len(base) == 10:
        tipo = "DEC"
        return tipo
    elif len(base) == 16:
        tipo = "HEX"
        return tipo

# Exibe o resultado da operação com as bases convertidas em decimais para as demais bases
def exibirResultado(b1_tipo, b2_tipo, resultado):
    print("=-" * 20)
    print(f"{num1}({b1_tipo}) {operacao} {num2}({b2_tipo})")
    print(
        f"Binário: {DecParaBi(num1_dec)} {operacao} {DecParaBi(num2_dec)} = {DecParaBi(resultado)}"
    )
    print(
        f"Octal: {DecParaOct(num1_dec)} {operacao} {DecParaOct(num2_dec)} = {DecParaOct(resultado)}"
    )
    print(f"Decimal: {num1_dec} {operacao} {num2_dec} = {resultado}")
    print(
        f"Hexadecimal: {DecParaHex(num1_dec)} {operacao} {DecParaHex(num2_dec)} = {DecParaHex(resultado)}"
    )
    print("=-" * 20)

# Fim das funções de operações

# MENU

while True:
    print("")
    print("=-" * 20)
    print("1. Conversão de bases.")
    print("2. Operações.")
    print("3. Sair.")
    print("=-" * 20)
    print("")

    escolha = input("Digite a operação desejada: ")
    if escolha == "1":
        # Conversão de bases
        opcoesBases = ["1", "2", "3", "4"]
        opcoesBinario = ["0", "1"]
        opcoesOctal = ["0", "1", "2", "3", "4", "5", "6", "7"]
        opcoesDecimal = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        opcoesHexa = [
            "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", 'A', 'B', 'C',
            'D', 'E', 'F'
        ]

        print("=-" * 20)
        print("1. Binário.")
        print("2. Octal.")
        print("3. Decimal.")
        print("4. Hexadecimal.")
        print("=-" * 20)

        escolhaBase1 = True
        while escolhaBase1:
            base_inicial = input("Escolha a base inicial: ")
            if base_inicial not in opcoesBases:
                print("Base inválida.")
            else:
                escolhaBase1 = False

        escolhaBase2 = True
        while escolhaBase2:
            base_final = input("Escolha a base a ser convertida: ")
            if base_final not in opcoesBases:
                print("Base inválida.")
            else:
                escolhaBase2 = False

        escolhaValor = True
        while escolhaValor:
            valor = input("Digite o valor desejado: ")
            valor = valor.strip()
            valor = valor.upper()
            sucessoValor = 1
            if base_inicial == "1":
                for i in valor:
                    if i not in opcoesBinario:
                        print("Valor não é binário.")
                        sucessoValor = 0
                        break

                if sucessoValor == 1:
                    if base_final == "1":
                        print("As bases são iguais.")
                        escolhaValor = False
                    elif base_final == "2":
                        resultado = BiParaOct(valor)
                        print(f"O resultado da conversão é: {resultado}")
                        escolhaValor = False
                    elif base_final == "3":
                        resultado = BiParaDec(valor)
                        print(f"O resultado da conversão é: {resultado}")
                        escolhaValor = False
                    else:
                        resultado = BiParaHex(valor)
                        print(f"O resultado da conversão é: {resultado}")
                        escolhaValor = False

            elif base_inicial == "2":
                for i in valor:
                    if i not in opcoesOctal:
                        print("Valor não é octal.")
                        sucessoValor = 0
                        break

                if sucessoValor == 1:
                    if base_final == "1":
                        resultado = OctParaBi(valor)
                        print(f"O resultado da conversão é: {resultado}")
                        escolhaValor = False
                    elif base_final == "2":
                        print("As bases são iguais.")
                        escolhaValor = False
                    elif base_final == "3":
                        resultado = OctParaDec(valor)
                        print(f"O resultado da conversão é: {resultado}")
                        escolhaValor = False
                    else:
                        resultado = OctParaHex(valor)
                        print(f"O resultado da conversão é: {resultado}")
                        escolhaValor = False

            elif base_inicial == "3":
                for i in valor:
                    if i not in opcoesDecimal:
                        print("Valor não é decimal.")
                        sucessoValor = 0
                        break

                if sucessoValor == 1:
                    if base_final == "1":
                        resultado = DecParaBi(valor)
                        print(f"O resultado da conversão é: {resultado}")
                        escolhaValor = False
                    elif base_final == "2":
                        resultado = DecParaOct(valor)
                        print(f"O resultado da conversão é: {resultado}")
                        escolhaValor = False
                    elif base_final == "3":
                        print("As bases são iguais.")
                        escolhaValor = False
                    else:
                        resultado = DecParaHex(valor)
                        print(f"O resultado da conversão é: {resultado}")
                        escolhaValor = False

            elif base_inicial == "4":
                for i in valor:
                    if i not in opcoesHexa:
                        print("Valor não é hexadecimal.")
                        sucessoValor = 0
                        break

                if sucessoValor == 1:
                    if base_final == "1":
                        resultado = HexParaBi(valor)
                        print(f"O resultado da conversão é: {resultado}")
                        escolhaValor = False
                    elif base_final == "2":
                        resultado = HexParaOct(valor)
                        print(f"O resultado da conversão é: {resultado}")
                        escolhaValor = False
                    elif base_final == "3":
                        resultado = HexParaDec(valor)
                        print(f"O resultado da conversão é: {resultado}")
                        escolhaValor = False
                    else:
                        print("As bases são iguais.")
                        escolhaValor = False

    elif escolha == "2":
        # Calculos de bases iguais ou diferentes

        operacao = escolhaOp()

        print("")
        print("=-" * 20)
        print("1. Binário.")
        print("2. Octal.")
        print("3. Decimal.")
        print("4. Hexadecimal.")
        print("=-" * 20)
        print("")

        print("Escolha a 1ra base.")
        base1 = escolhaBase()
        print("Escolha a 2da base.")
        base2 = escolhaBase()
        print("Entre o 1° número.")
        num1 = entradaNum(base1)
        print("Entre o 2° número.")
        num2 = entradaNum(base2)
        num1_dec = int(parseTermo(num1, base1))
        num2_dec = int(parseTermo(num2, base2))
        resultado = opBases(num1_dec, num2_dec, operacao)
        try:
            resultado = int(resultado)
            flagResultado = True
        except:
            flagResultado = False

        if flagResultado == True:
            if resultado >= 0:
                b1_tipo = tipoBase(base1)
                b2_tipo = tipoBase(base2)
                # chama a função para exibir o resultado
                exibirResultado(b1_tipo, b2_tipo, resultado)
            else:
                print(
                    "A calculadora de bases não funciona com números negativos, tente novamente!"
                )
        else:
            print("Tente novamente...")

    elif escolha == "3":
        # Encerra o programa
        print("Adeus!...")
        exit(0)

    else:
        # Caso prompt inválido
        print("Escolha inválida.")
