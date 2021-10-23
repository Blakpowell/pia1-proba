# PIA_1 - Probabilidad Avanzada

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Importando los datos
a = pd.read_csv("muestras.csv")
b = a.iloc[:, 1:]
b.index = range(1, 21)
# b tiene el dataframe de las muestras

# b.mean() # tiene las medias
r = b.mean()

i = r.min()
dist = 1
ff = {'[{0} - {1})'.format(int(i), int(i+dist)): r[r>=np.floor(i)][r<np.floor(i+dist)].count()}
while (i < r.max()):
	ff.update({'[{0} - {1})'.format(int(i), int(i+dist)): r[r>=np.floor(i)][r<np.floor(i+dist)].count()})
	i = i + dist

tab_medias = pd.Series(ff)
print(tab_medias)

labels = tab_medias.index
tasas = list(tab_medias)

x = np.arange(len(labels))
width = 0.9

fig, ax = plt.subplots()
rects = ax.bar(x, tasas, width)

ax.set_title('Conteo de las medias en clases')
ax.set_ylabel('Cantidad')
ax.set_xticks(x)
ax.set_xticklabels(labels, rotation=30)
ax.bar_label(rects, padding=1)

plt.show()
