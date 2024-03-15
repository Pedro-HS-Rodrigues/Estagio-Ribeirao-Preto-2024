def string_inverter(string):
    array_de_caracteres = []
    for i in range(len(string) - 1, -1, -1):
        array_de_caracteres.append(string[i])
    string_invertida = ''.join(array_de_caracteres)
    return print(f"A palavra {string} invertida fica: {string_invertida}")

string = str(input("Digite aqui a string a ser invertida: "))
string_inverter(string)