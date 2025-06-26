def exibir_menu():
    print("=== Calculadora IPv6 =====")
    print("1) Calcular endereço de rede e número de hosts")
    print("2) Comprimir endereço IPv6 expandido")
    print("3) Gerar IPv6 aleatório /48")
    print("4) Gerar IPv6 aleatório /54")
    print("0) Sair")
    print("===========================")

    return

def continuar():
    input("aperte [ENTER] para continuar.")

    return

def sair():
    print("Saindo...\n")

    return

def adicionar_zeros(string : str) -> str:
    tamanho = len(string)
    zeros_faltando = 4 - tamanho

    i = 0
    for i in range(zeros_faltando):
        string = '0' + string
    
    return string

def aplicar_mascara(binario : str, prefixo : int) -> str:
    return binario[:prefixo] + '0' * (128 - prefixo)

def inicio_sequencia(bloco : str, valor_inicio : int):
    return ((bloco == '0') and (valor_inicio == -1))

def final_sequencia(bloco : str, valor_inicio : int):
    return ((bloco != '0') and (valor_inicio != -1))

def sequencia_nao_terminada(bloco : str, valor_inicio : int, index : int, tamanho_endereco : int):
    return (((bloco == '0') and (valor_inicio != -1)) and (index == (tamanho_endereco - 1)))