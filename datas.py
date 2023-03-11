"""
Arquivo com dados do grupos e das rodadas da copa
"""
import pandas as pd

df = pd.read_csv("FWC_data.csv")
valores = df.values.tolist()

groupA = ["QATAR", "ECUADOR", "SENEGAL", "NETHERLANDS"]
groupB = ["ENGLAND", "IRAN", "UNITED STATES", "WALES"]
groupC = ["ARGENTINA", "SAUDI ARABIA", "MEXICO", "POLAND"]
groupD = ["FRANCE", "AUSTRALIA", "DENMARK", "TUNISIA"]
groupE = ["SPAIN", "COSTA RICA", "GERMANY", "JAPAN"]
groupF = ["BELGIUM", "CANADA", "MOROCCO", "CROATIA"]
groupG = ["BRAZIL", "SERBIA", "SWITZERLAND", "CAMEROON"]
groupH = ["PORTUGAL", "GHANA", "URUGUAY", "KOREA REPUBLIC"]

selecoes = groupA + groupB + groupC + groupD + groupE + groupF + groupG + groupH

group_stage = valores[:48]  # 6 jogos por grupo *  8 grupos = 48 valores
round_of_16 = valores[48:56]  # 48 + 8 jogos das oitavas de final = 56
quarter_finals = valores[56:60]  # 56 + 4 jogos das quartas de final = 60
semi_finals = valores[60:62]  # 60 + 2 jogos da semi final
third_place = valores[62:63]  # 62 + 1 jogo da disputa de terceiro colocado
final = valores[63:64]  # último jogo da copa do mundo

fases_copa = [
    group_stage,
    round_of_16,
    quarter_finals,
    semi_finals,
    third_place,
    final
]

parametros = ["Fase de grupos",
              "Oitavas de final",
              "Quartas de final",
              "Semi finais",
              "Disputa de terceiro lugar",
              "Final"
              ]
