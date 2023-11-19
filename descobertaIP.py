import socket

def obter_enderecos_ip(nome_host):
    try:
        enderecos_ip = socket.gethostbyname_ex(nome_host)[2]
        return enderecos_ip
    except socket.gaierror as e:
        return str(e)

def main():
    nome_ferramenta = "DescobertaIP"
    linha_estrelas = "*" * 67

    print(linha_estrelas)
    print("/*                           DESCRIÇÃO DA FERRAMENTA                          */")
    print(f"*{'':<33}{nome_ferramenta.center(34)}{'':<33}*")
    print(f"*{'':<33}{'Coded by Davidson Dorvil'.center(34)}{'':<33}*")
    print(f"*{'':<33}{'GitHub: https://github.com/Dorvil'.center(34)}{'':<33}*")
    print(linha_estrelas)

    print("\nDescobridor de Endereços IP por David")
    print("------------------------------------")

    nome_host = input("Digite o nome do site (exemplo: www.exemplo.com): ")

    if not nome_host:
        print("Nome de host inválido. Por favor, forneça um nome de host válido.")
        return

    enderecos_ip = obter_enderecos_ip(nome_host)

    print("\nResultado:")
    print("-----------")

    if enderecos_ip:
        print(f"Os endereços IP associados ao site {nome_host} são: {', '.join(enderecos_ip)}")
    else:
        print(f"Não foi possível obter o endereço IP para o site {nome_host}.")

if __name__ == "__main__":
    main()
