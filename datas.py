"""
Arquivo com dados do grupos e das rodadas da copa
"""
import numpy as np
import pandas as pd

data = pd.read_csv("FWC_data.csv")

group_stage = data[:48]
round_of_16 = data[48:56]
round_of_16.index = range(8)
quarter_finals = data[56:60]
quarter_finals.index = range(4)
semi_finals = data[60:62]
semi_finals.index = range(2)
third_place = data[62:63]
third_place.index = range(1)
final = data[63:]
final.index = range(1)

groupA = np.array(["QATAR", "ECUADOR", "SENEGAL", "NETHERLANDS"])
groupB = np.array(["ENGLAND", "IRAN", "UNITED STATES", "WALES"])
groupC = np.array(["ARGENTINA", "SAUDI ARABIA", "MEXICO", "POLAND"])
groupD = np.array(["FRANCE", "AUSTRALIA", "DENMARK", "TUNISIA"])
groupE = np.array(["SPAIN", "COSTA RICA", "GERMANY", "JAPAN"])
groupF = np.array(["BELGIUM", "CANADA", "MOROCCO", "CROATIA"])
groupG = np.array(["BRAZIL", "SERBIA", "SWITZERLAND", "CAMEROON"])
groupH = np.array(["PORTUGAL", "GHANA", "URUGUAY", "KOREA REPUBLIC"])
groups = {
    "Grupo A": groupA,
    "Grupo B": groupB,
    "Grupo C": groupC,
    "Grupo D": groupD,
    "Grupo E": groupE,
    "Grupo F": groupF,
    "Grupo G": groupG,
    "Grupo H": groupH
}
