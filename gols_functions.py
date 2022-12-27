"""
Arquivo com as funcoes criadas que foram utilizadas
"""
import pandas as pd
import numpy as np


def gols(team: str,
         category: pd.DataFrame,
         ) -> int:
    """
    Args:
        team: str com o nome da selecao
        cetegory: pd.DataFrame com a fase da copa a ser analisada
    Return:
        number: int com o numero de gols feitos pela selecao naquela fase da copa
    """
    number = 0
    games = category[["team1", "team2"]] == team
    for idx, value in enumerate(games.values):
        if any(value):
            if value[0]:
                number += category["number of goals team1"][idx]
            else:
                number += category["number of goals team2"][idx]
    return number


def gols_teams(group: np.ndarray,
               category: pd.DataFrame,
               ) -> np.ndarray:
    """
    Args:
        group: np.ndarray com nomes de selecoes
        category: pd.DataFrame com a fase da copa a ser analisada
    Return:
        np.ndarray com os gols marcados pelas selecoes naquela fase da copa
    """
    return np.array([gols(team, category) for team in group])
