# Autores: Caio Guimarães RGM: 31319343
#          Giovanni Santos RGM: 631660754
#          Otávio Silva RGM: 31732330

# Professor: Giulio Guiyti Rossignolo Suzumura & Antonio Eduardo Marques Da Silva


# Funções de conversão de bases numéricas

import time


def bin_to_dec(num_binario):
    return int(num_binario, 2)

def hex_to_dec(num_hex):
    return int(num_hex, 16)

def oct_to_dec(num_octal):
    return int(num_octal, 8)

# ------------------------main------------------------    
opcao1 = 0

while opcao1 != 3:
    print('------------------------------ Menu ----------------------------')
    print('----------------------------------------------------------------')
    print('Bem-vindo ao conversor de bases numéricas! Selecione uma opção: ')
    print('----------------------------------------------------------------')

    
    print("1. Conversão de decimal para binário, hexadecimal e octal")
    print("2. Conversão de binário, hexadecimal e octal para decimal")
    print("3. Sair")
    
    
    escolha = input("Escolha uma opção: ")
   
    # Vamos fazer a conversão de decimal para binário, hexadecimal e octal 
    if escolha == "1":
        while True:
            num_decimal = input("Digite o número decimal: ")
            # Verifica se todos os caracteres são dígitos
            if all (digito in ['0','1','2','3','4','5','6','7','8','9'] for digito in str(num_decimal)):
                break
            else:
                print("Número decimal inválido. Por favor, digite apenas números.")
        
        #
        decimal_to_binary = bin(int(num_decimal))[2:]  # Removendo o prefixo '0b'
        decimal_to_hexadecimal = hex(int(num_decimal))[2:]  # Removendo o prefixo '0x'
        decimal_to_octal = oct(int(num_decimal))[2:] # Removendo o prefixo '0o'    
        print("Processando...")
        time.sleep(1)
        # Exibe os resultados1
    
        print(f"Resultado Binário: {decimal_to_binary}")
        print(f"Resultado Hexadecimal: {decimal_to_hexadecimal}")
        print(f"Resultado Octal: {decimal_to_octal}")
    
    
    # Vamos fazer a conversão de binário, hexadecimal e octal para decimal    
    if escolha == "2":
        while True:
            num_binario = input("Digite o número binário: ")
            
            # Verifica se todos os caracteres são '0' ou '1'
            if all(digito in ['0', '1'] for digito in num_binario):
                # Se todos os dígitos são '0' ou '1', sai do loop
                break
            else:
                print("Número binário inválido. Por favor, digite apenas '0' e '1'.")
        while True:
            num_hex= input("Digite o número hexadicimal: ")
            # Verifica se todos os caracteres são dígitos hexadecimais válidos
            if all(digito in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F','a','b','c','d','e','f'] for digito in num_hex):
            # Se todos os dígitos são válidos, sai do loop
                break
            else:
                print("Número hexadecimal inválido. Por favor, digite apenas '0' a '9' e 'A' a 'F'.")
        
        while True:
            num_octal= input("Digite o número octal: ")
            # Verifica se todos os caracteres são dígitos octais válidos
            if all(digito in ['0', '1', '2', '3', '4', '5', '6', '7'] for digito in num_octal):
            # Se todos os dígitos são válidos, sai do loop
                break
            else:
                print("Número octal inválido. Por favor, digite apenas '0' a '7'.")
        
        print("Processando...")
        time.sleep(1)   
        # Converte e exibe os resultados
        print(f"Conversão de binários para decimal: {bin_to_dec(num_binario)}")
        print(f"Conversão de hexadecimal para decimal: {hex_to_dec(num_hex)}")
        print(f"Conversão de octal para decimal: {oct_to_dec(num_octal)}")
      
    if escolha == "3":
        print("Saindo...")
        break
   