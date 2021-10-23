from numpy.random import default_rng
import numpy as np
import pandas as pd

# Proyecto PIA a)
# Este archivo solo genera las muestras aleatorias.
# Se recomienda no ejecutar para mantener las muestras intactas
# en el archivo csv de esta carperta.

gen = default_rng() # Variable generadora de aleatorios

def lista_n(n):
	return [i for i in range(1, n + 1)]

# Construyedo el dataframe
def exp_completo(va_s = 1, obs = 1):
	muestra = gen.integers(1, 21, size=obs)
	i = 1
	d = {'x'+str(i): muestra}
	while(i < va_s):
		i = i + 1
		muestra = gen.integers(1, 21, size=obs)
		d.update({'x'+str(i): muestra})
		if va_s < 1:
			d = 0
			break
	return d

df = pd.DataFrame(exp_completo(50, 20), index=lista_n(20))

df.to_csv("muestras.csv")

print(df)
