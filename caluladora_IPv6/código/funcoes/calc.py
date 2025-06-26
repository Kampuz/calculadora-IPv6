import funcoes.aux as aux
import random

def comprimir_endereco(endereco_com_prefixo : str) -> str:    
    
    # Separa endereço e prefixo
    endereco_expandido, prefixo = endereco_com_prefixo.strip().split('/')
    endereco_expandido = endereco_expandido.strip()
    prefixo = f"/{prefixo}"

    # Divide em blocos
    blocos = endereco_expandido.split(':')
    blocos_sem_zeros_esquerda = []

    #remove zeros à esquerda
    for bloco in blocos:
        bloco_sem_zeros_esquerda = bloco.lstrip('0')

        if bloco_sem_zeros_esquerda == '':
            bloco_sem_zeros_esquerda = '0'

        blocos_sem_zeros_esquerda.append(bloco_sem_zeros_esquerda)

    inicio_atual = -1
    tamanho_atual = 0
    melhor_inicio = -1
    melhor_tamanho = 0

    #Encontra a maior sequencia de '0000'
    for index, bloco in enumerate(blocos_sem_zeros_esquerda):
        if aux.inicio_sequencia(bloco, inicio_atual):
            inicio_atual = index
        elif aux.final_sequencia(bloco, inicio_atual) or aux.sequencia_nao_terminada(bloco, inicio_atual, index, len(blocos_sem_zeros_esquerda)):
            tamanho_atual = index - inicio_atual
            if tamanho_atual > melhor_tamanho:
                melhor_inicio, melhor_tamanho = inicio_atual, tamanho_atual
            inicio_atual = -1

    if melhor_tamanho < 2:
        endereco_comprimido = ':'.join(blocos_sem_zeros_esquerda) + prefixo
        return endereco_comprimido

    compactado = (blocos_sem_zeros_esquerda[:melhor_inicio] +
    [''] + blocos_sem_zeros_esquerda[melhor_inicio + melhor_tamanho:])

    print(compactado)

    resultado = ':'.join(compactado)

    print(resultado)

    resultado = resultado.replace(':::', '::')
    if resultado.startswith(':'):
        resultado = ':' + resultado
    if resultado.endswith(':'):
        resultado = resultado + ':'

    return resultado + prefixo

def expandir_endereco(endereco_ip : str) -> list[str]:
    
    # arruma o endereço ip
    endereco_ip = endereco_ip.strip().lower()

    # verifica se há uma "lacuna"
    if '::' in endereco_ip:

        #divide o endereco entre cabeca e cauda
        cabeca, cauda = endereco_ip.split('::')

        #divide a cabeca em blocos
        if cabeca:
            blocos_cabeca = cabeca.split(':')
        else:
            blocos_cabeca = []
        
        #divide a cauda em blocos
        if cauda:
            blocos_cauda = cauda.split(':')
        else:
            blocos_cauda = []

        # numeros de blocos que devem existir em um endereco ipv6
        blocos_num = 8

        # calcula o numero de blocos que existem na lacuna
        blocos_lacuna = blocos_num - (len(blocos_cabeca) + len(blocos_cauda))

        blocos = []

        #unifica os blocos
        for bloco in blocos_cabeca:
            blocos.append(bloco)
        for i in range(blocos_lacuna):
            blocos.append('0')
        for bloco in blocos_cauda:
            blocos.append(bloco)

    else:
        blocos = endereco_ip.split(':')

    for i in range(len(blocos)):
        blocos[i] = aux.adicionar_zeros(blocos[i])

    return blocos

def ipv6_para_binario(blocos : list[str]) -> str:
    string_binaria = ''

    for bloco in blocos:
        valor_inteiro = int(bloco, 16) #transforma o valor hexadecimal no bloco em inteiro
        valor_binario = f"{valor_inteiro:016b}" #transforma o valor inteiro em uma string binaria
        string_binaria = string_binaria + valor_binario
    
    return string_binaria

def binario_para_ipv6(string_binaria : str) -> list[str]:
    blocos : list[str] = []

    tamanho_bloco = 16
    comeco_string = 0

    for i in range(comeco_string, len(string_binaria), tamanho_bloco):
        comeco_segmento = i
        final_segmento = comeco_segmento + tamanho_bloco
        segmento_string = string_binaria[comeco_segmento : final_segmento]
        valor_binario = int(segmento_string, 2)
        bloco = f"{valor_binario:04x}"
        blocos.append(bloco)

    return blocos

def calcular_hosts(endereco_ip_com_prefixo : str) -> int:
    if '/' not in endereco_ip_com_prefixo:
        raise ValueError("Formato inválido: falta '/prefixo'.")
    endereco_ip, prefixo = endereco_ip_com_prefixo.split('/')

    try:
        prefixo = int(prefixo)
    except:
        raise ValueError("Prefixo inválido (não numérico).")
    
    if prefixo < 0 or prefixo > 128:
        raise ValueError("Prefixo fora do intervalo (0~128).")
    
    num_hosts = 2 ** (128 - prefixo)

    return num_hosts

def calcular_endereco_rede(endereco_ip_com_prefixo : str) -> str:
    if '/' not in endereco_ip_com_prefixo:
        raise ValueError("Formato inválido: falta '/prefixo'.")

    endereco, prefixo = endereco_ip_com_prefixo.strip().split('/')

    prefixo = int(prefixo)

    blocos = expandir_endereco(endereco)

    endereco_binario = ipv6_para_binario(blocos)
    
    rede_binaria = aux.aplicar_mascara(endereco_binario, prefixo)

    blocos_rede = binario_para_ipv6(rede_binaria)

    rede_expandida = ':'.join(blocos_rede) + f"/{prefixo}"

    rede_comprimida = comprimir_endereco(rede_expandida)

    return rede_comprimida

def gerar_ip_aleatorio(prefixo : int) -> str:
    NUM_BITS = 128

    if not (0 <= prefixo <= NUM_BITS):
        raise ValueError("Prefixo inválido para geração aleatória (0~128).")
    
    endereco_aleatorio = random.getrandbits(NUM_BITS)

    bits_hosts = NUM_BITS - prefixo
    parte_rede = random.getrandbits(prefixo) << bits_hosts
    parte_hosts = random.getrandbits(bits_hosts)

    endereco = parte_rede | parte_hosts

    endereco_binario = f"{endereco:0128b}"

    blocos = binario_para_ipv6(endereco_binario)
    
    endereco_ipv6 = ':'.join(blocos)

    return f"{endereco_ipv6}/{prefixo}"