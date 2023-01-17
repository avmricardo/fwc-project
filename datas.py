"""
Arquivo com dados do grupos e das rodadas da copa
"""
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

groupA = ["QATAR", "ECUADOR", "SENEGAL", "NETHERLANDS"]
groupB = ["ENGLAND", "IRAN", "UNITED STATES", "WALES"]
groupC = ["ARGENTINA", "SAUDI ARABIA", "MEXICO", "POLAND"]
groupD = ["FRANCE", "AUSTRALIA", "DENMARK", "TUNISIA"]
groupE = ["SPAIN", "COSTA RICA", "GERMANY", "JAPAN"]
groupF = ["BELGIUM", "CANADA", "MOROCCO", "CROATIA"]
groupG = ["BRAZIL", "SERBIA", "SWITZERLAND", "CAMEROON"]
groupH = ["PORTUGAL", "GHANA", "URUGUAY", "KOREA REPUBLIC"]

selecoes = groupA + groupB + groupC + groupD + groupE + groupF + groupG + groupH
