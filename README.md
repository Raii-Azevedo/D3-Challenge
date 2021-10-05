# D3-Challenge
Desafio cálculo do Covid

## O Ponto escolhido
- Partindo da premissa que antes de atingir o platô o contágio de Covid chegou a níveis exponenciais, o cálculo foi baseado nesse momento.
- Então, foi realizada uma função exponencial partindo de 0 que aumenta de acordo com os dias determinados de contágio definidos no input de N.

## O Código
[D3-Chalenge](https://github.com/Raii-Azevedo/D3-Challenge/blob/master/d3-challenge.py)

## O Raciocínio
As bibliotecas utilizadas foram:
- Matplotlib: Para fazer gŕaficos.
- Numpy: Para manipulação de listas e vetores.
- Math

## Codando
- Foi definida uma função de ativação principal que recebe o input de N...
- def main():
    print(' --COVID 19-- ')
    n = int(input('Nº de dias de contágio: '))

    n = np.linspace(0, 3, n)
    covid(n)
    
- E a função principal denominada "covid", que recebe a função exponencial:
-   lam = [0.5, 1.0, 1.5, 2.0, 2.5]
    colors = ['red', 'blue', 'green', 'orange', 'cyan']
    fs = []
    for i in range(len(lam)):
        f = lam[i]*np.exp(1.0*lam[i]*n)
        fs.append(f)
        
 - E a função de montagem de gráfico:
 -  for i in range(len(lam)):
        plt.plot(n, fs[i], color=colors[i], label=r'$\lambda$='+str(lam[i]))
    plt.ylabel('n')
    plt.xlabel(r'f(x,$\lambda$)')
    plt.legend()
    plt.tight_layout()
    matplotlib.pyplot.show()
    
 - Dessa forma, cada vez que o N (nº de dias é definido, o gráfico com aumento de função é gerado).
 - PS: Quanto maior o número de dias, maior a curva de contágio.


## Author
- Raíssa Azevedo

