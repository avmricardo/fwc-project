"""
Plotando gols das quartas de final
"""
import numpy as np
import pandas as pd
import datas as dt
import gols_functions as func
import matplotlib.pyplot as plt

fig = plt.figure()
fig.suptitle("Gols quartas de final")

val = dt.quarter_finals.values

for i in range(4):
    ax = fig.add_subplot(2, 2, i+1)
    game = np.array([val[i][0], val[i][1]])
    ax.bar(
        game,
        func.gols_teams(game, dt.quarter_finals)
    )

plt.show()
