def calcular_nivel(vitorias, derrotas):
    saldoVitorias = vitorias - derrotas  

    if saldoVitorias < 10:
        nivel = "Ferro"
    elif 11 <= saldoVitorias <= 20:
        nivel = "Bronze"
    elif 21 <= saldoVitorias <= 50:
        nivel = "Prata"
    elif 51 <= saldoVitorias <= 80:
        nivel = "Ouro"
    elif 81 <= saldoVitorias <= 90:
        nivel = "Diamante"
    elif 91 <= saldoVitorias <= 100:
        nivel = "Lendário"
    elif saldoVitorias >= 101:
        nivel = "Imortal"
    else:
        nivel = None  

    return saldoVitorias, nivel


def obter_valores_validos():
    while True:
        try:
            vitorias = int(input("Digite a quantidade de vitórias: "))
            derrotas = int(input("Digite a quantidade de derrotas: "))

            saldoVitorias, nivel = calcular_nivel(vitorias, derrotas)

            if nivel is None:
                print("O número de vitórias é insuficiente. Tente novamente.")
            else:
                return saldoVitorias, nivel

        except ValueError:
            print("Por favor, insira números inteiros válidos.")


saldoVitorias, nivel = obter_valores_validos()
print(f"O Herói tem um saldo de {saldoVitorias} e está no nível {nivel}.")
