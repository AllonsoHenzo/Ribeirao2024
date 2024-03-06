def inverter_string(string):
    inverted_string = ''
    for char in string:
        inverted_string = char + inverted_string
    return inverted_string

input = input("Digite uma palavra para inverter: ")

inversao = inverter_string(input)

print("Palavra invertida:", inversao)