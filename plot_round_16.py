"""
Plotando gols das oitavas de final
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import gols_functions as func
import datas as dt

row = 2
column = 4
fig = plt.figure()
fig.suptitle("Gols oitavas de final")

val = dt.round_of_16.values

for i in range(8):
    ax = fig.add_subplot(row, column, i+1)
    game = np.array([val[i][0], val[i][1]])
    ax.bar(game, func.gols_teams(game, dt.round_of_16))
    ax.set_yticks(np.arange(7))

plt.show()
