import matplotlib.pyplot as plt
import numpy as np

# konstanter
R = 200000
C = 100*10**(-6)

# teoretisk modell 

skritt = 1000
T = 120
h = skritt/T

t = np.linspace(0, T, skritt)
v = np.zeros(len(t))

def spenning(t):
    return 9*(1 - np.e**(-t/(R*C)))

v = spenning(t)

# praktiske målinger 

tP = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]
vP = [0, 3.1, 5.2, 6.44, 7.24, 7.70, 7.99, 8.19, 8.31, 8.38, 8.44, 8.47, 8.50]


# plotting

plt.plot(t, v)
plt.plot(tP, vP, "r--")

legendListe = ["Teoretisk modell", "Praktiske målinger"]
plt.legend(legendListe)

plt.grid()
plt.ylabel("Spenning [V]")
plt.xlabel("Tid [s]")
plt.title("Spenningen over kondensatoren over tid")
plt.show()
