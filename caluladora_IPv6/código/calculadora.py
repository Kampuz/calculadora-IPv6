import os
import funcoes.aux as aux
import funcoes.calc as calc

def main():
    while True:
        aux.exibir_menu()

        escolha = input("Escolha uma opção (0~4): ").strip()

        if escolha == '0':
            aux.sair()
            break

        elif escolha == '1':
            
            endereco_ip = input("Digite IPv6 c/ prefixo (ex:  2801:0390:0080:0000:0100:0000:0000:ff00 /64): ").strip()

            try:
                endereco_rede = calc.calcular_endereco_rede(endereco_ip)
                numero_hosts = calc.calcular_hosts(endereco_ip)

            except ValueError as e:
                print(f"Erro: {e}\n")

            print(f"\nEndereço de rede comprimido: {endereco_rede}")
            print(f"\nNúmero total de hosts: {numero_hosts:,}\n")
            
            aux.continuar()
        
        elif escolha == '2':

            endereco_ip = input("Digite IPv6 c/ prefixo (ex:  2801:0390:0080:0000:0100:0000:0000:ff00 /64): ").strip()
            
            try:
                endereco_ip_comprimido = calc.comprimir_endereco(endereco_ip) 

            except ValueError as e:
                print(f"Erro: {e}\n")

            print(f"\nEndereço de IP expandido: {endereco_ip}")                
            print(f"\nForma comprimida do endereço de IP: {endereco_ip_comprimido}")

            aux.continuar()
        
        elif escolha == '3':

            endereco_ip = input("Digite IPv6 comprimido c/ prefixo (ex:  2801:390:80:0:100::ff00 /64): ").strip()
            
            try:
                endereco_ip_expandido = calc.expandir_endereco(endereco_ip) 

            except ValueError as e:
                print(f"Erro: {e}\n")

            print(f"\nEndereço de IP expandido: {endereco_ip}")                
            print(f"\nForma comprimida do endereço de IP: {endereco_ip_comprimido}")

            aux.continuar()
            
        elif escolha == '4':
            print(f"Endereço IPV6 gerado: {calc.gerar_ip_aleatorio(48)}")
            aux.continuar()
        elif escolha == '5':
            print(f"Endereço IPV6 gerado: {calc.gerar_ip_aleatorio(54)}")
            aux.continuar()
        else:
            print("Opção Inválida!\n")
            aux.continuar()

        os.system('cls' if os.name == "nt" else 'clear')

if __name__ == "__main__":
    main()