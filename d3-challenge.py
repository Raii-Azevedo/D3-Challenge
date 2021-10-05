import math

import matplotlib.pyplot
import numpy as np
import matplotlib.pyplot as plt

x = 0


def covid(n):
    lam = [0.5, 1.0, 1.5, 2.0, 2.5]
    colors = ['red', 'blue', 'green', 'orange', 'cyan']
    fs = []
    for i in range(len(lam)):
        f = lam[i]*np.exp(1.0*lam[i]*n)
        fs.append(f)

    for i in range(len(lam)):
        plt.plot(n, fs[i], color=colors[i], label=r'$\lambda$='+str(lam[i]))
    plt.ylabel('n')
    plt.xlabel(r'f(x,$\lambda$)')
    plt.legend()
    plt.tight_layout()
    matplotlib.pyplot.show()


def main():
    print(' --COVID 19-- ')
    n = int(input('Nº de dias de contágio: '))

    n = np.linspace(0, 3, n)
    covid(n)


if __name__ == '__main__':
    main()
