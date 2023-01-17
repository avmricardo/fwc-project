"""
Arquivo com as funcoes criadas que foram utilizadas
"""
import pandas as pd


def gols(df: pd.DataFrame, team: str) -> float:
    """
    Args:
        df: DataFrame da copa do mundo
        team: string com o nome de uma selecao
    Return:
        razao: float com a razao entre gols feitos e tomados por essa selecao
    """
    gols_feitos = 0
    gols_tomados = 0
    time1 = list(df["team1"])
    time2 = list(df["team2"])
    gols1 = list(df["number of goals team1"])
    gols2 = list(df["number of goals team2"])
    for i in range(len(time1)):
        if time1[i] == team:
            gols_feitos += gols1[i]
            gols_tomados += gols2[i]
        elif time2[i] == team:
            gols_feitos += gols2[i]
            gols_tomados += gols1[i]
    razao = gols_feitos / gols_tomados
    return razao


def gols_selecoes(df: pd.DataFrame, selecoes: list) -> list:
    """
    Args:
        df: DataFrame da copa do mundo
        selecoes: lista com os nomes de todas as selecoes
    Return:
        razoes: lista com a razao entre gols feitos e tomados das selecoes contidas na lista informada
    """
    razoes = []
    for selecao in selecoes:
        razoes.append(gols(df, selecao))
    return razoes


def max_min(lista: list) -> list:
    """
    Funcao para calular o valor maximo e minimo de uma lista
    """
    max = -9999
    min = 9999
    for i in lista:
        if i > max:
            max = i
        if i < min:
            min = i
    return [max, min]


if __name__ == '__main__':
    """
    Testando as funcoes
    """
    import datas as dt
    datas = pd.read_csv("FWC_data.csv")
    for i in range(32):
        print(dt.selecoes[i], end=" ")
        print(gols_selecoes(datas, dt.selecoes)[i])

    print("max():", max(gols_selecoes(datas, dt.selecoes)))
    print("min():", min(gols_selecoes(datas, dt.selecoes)))
    print("max_min():", max_min(gols_selecoes(datas, dt.selecoes)))
