"""
Arquivo com dados do grupos e das rodadas da copa
"""
import pandas as pd

data = pd.read_csv("FWC_data.csv")

groupA = ["QATAR", "ECUADOR", "SENEGAL", "NETHERLANDS"]
groupB = ["ENGLAND", "IRAN", "UNITED STATES", "WALES"]
groupC = ["ARGENTINA", "SAUDI ARABIA", "MEXICO", "POLAND"]
groupD = ["FRANCE", "AUSTRALIA", "DENMARK", "TUNISIA"]
groupE = ["SPAIN", "COSTA RICA", "GERMANY", "JAPAN"]
groupF = ["BELGIUM", "CANADA", "MOROCCO", "CROATIA"]
groupG = ["BRAZIL", "SERBIA", "SWITZERLAND", "CAMEROON"]
groupH = ["PORTUGAL", "GHANA", "URUGUAY", "KOREA REPUBLIC"]

selecoes = groupA + groupB + groupC + groupD + groupE + groupF + groupG + groupH
