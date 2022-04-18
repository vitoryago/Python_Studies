#AULA 1 - GRAFICOS PYTHON

vendas_meses = [1500, 1727, 1350, 999, 1050, 1027, 1022, 1500, 2000, 2362, 2100, 2762]
meses = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez']

import matplotlib.pyplot as plt

plt.plot(meses, vendas_meses)
plt.ylabel('Vendas')
plt.xlabel('Meses')
plt.axis([0, 12, 0, max(vendas_meses)+100])
plt.show()

#AULA 2 - NUMPY

import matplotlib.pyplot as plt
import numpy as np

vendas = np.random.randint(1000, 3000, 50)
meses = np.arange(1, 51)
print(meses)

plt.axis([0, 50, 0, max(vendas) + 200])
plt.xlabel('Meses')
plt.ylabel('Vendas')
plt.plot(meses, vendas)
plt.show()

plt.scatter(meses, vendas)
plt.show()

plt.bar(meses, vendas)
plt.show()

plt.figure(1)
plt.subplot(1, 3, 1)
plt.plot(meses, vendas, color = 'red')

plt.subplot(1, 3, 2)
plt.scatter(meses, vendas)

plt.subplot(1, 3, 3)
plt.bar(meses, vendas)

plt.show()