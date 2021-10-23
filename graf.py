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
tabla = pd.Series(r)

def contar(dist = 1):
	global tabla
	i = r.min()
	clases = {}
	while i < r.max():
		clases.update({'[{0} - {1})'.format(int(i), int(i+dist)): r[r>=np.floor(i)][r<np.floor(i+dist)].count()})
		i = i + dist
	tabla = pd.Series(clases)
	
def plot_hist():
	global tabla
	labels = tabla.index
	tasas = list(tabla)
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

if __name__ == '__main__':
	contar()
	print(tabla)
	plot_hist()