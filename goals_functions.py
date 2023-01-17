"""
Arquivo com as funcoes criadas que foram utilizadas
"""
import pandas as pd


def razoes_gols(df: pd.DataFrame, team: str) -> float:
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


def razoes_gols_selecoes(df: pd.DataFrame, selecoes: list) -> list:
    """
    Args:
        df: DataFrame da copa do mundo
        selecoes: lista com os nomes de todas as selecoes
    Return:
        razoes: lista com a razao entre gols feitos e tomados das selecoes contidas na lista informada
    """
    razoes = []
    for selecao in selecoes:
        razoes.append(razoes_gols(df, selecao))
    return razoes


def ordenar_lista(lista: list) -> list:
    """
    Função para ordenar a lista com as tuplas contendo as seleções e suas razões de gols
    """
    tamanho = len(lista)
    for i in range(tamanho):
        for j in range(i, tamanho):
            if lista[i][1] > lista[j][1]:
                auxiliar = lista[i]
                lista[i] = lista[j]
                lista[j] = auxiliar
    return lista


if __name__ == '__main__':
    """
    Testando as funcoes criadas
    """
    import datas as dt
    datas = pd.read_csv("FWC_data.csv")
    for i in range(len(dt.selecoes)):
        print(dt.selecoes[i], end=" ")
        print(razoes_gols_selecoes(datas, dt.selecoes)[i])
