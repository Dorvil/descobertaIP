import socket

def obter_endereco_ip(nome_host):
    try:
        endereco_ip = socket.gethostbyname(nome_host)
        return endereco_ip
    except socket.gaierror as e:
        return str(e)

def main():
    print("Descobridor de Endereço IP por David")
    print("------------------------------------")

    nome_host = input("Digite o nome do site (exemplo: www.exemplo.com): ")

    endereco_ip = obter_endereco_ip(nome_host)

    print("\nResultado:")
    print("-----------")
    
    if endereco_ip:
        print(f"O endereço IP associado ao site {nome_host} é: {endereco_ip}")
    else:
        print(f"Não foi possível obter o endereço IP para o site {nome_host}.")

if __name__ == "__main__":
    main()
