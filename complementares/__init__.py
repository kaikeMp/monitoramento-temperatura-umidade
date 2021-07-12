def salvar(humid, temp, tempo):
    """
    Umidade = humid,
    Temperatura = temp
    Tempo = tempo
    """
    import pandas as pd
    dados = pd.DataFrame()
    dados['Umidade'] = humid
    dados['Temperatura'] = temp
    dados['Tempo'] = tempo
    return dados

def usb():
    while True:
        print('''Portas USB:
                    /dev/ttyUSB\033[1;31m0\033[0;0m = 0
                    /dev/ttyUSB\033[1;31m1\033[0;0m = 1''')
        cho = int(input('Digite o número da porta USB conectada /dev/ttyUSB\033[1;31mx\033[0;0m: '))
        if cho == 0 or cho == 1:
            if cho == 0:
                porta = '/dev/ttyUSB0'
                return porta
                break
            if cho == 1:
                porta = '/dev/ttyUSB1'
                return porta
                break
        else:
            print('Digite apenas 1 ou 2.')


def nome_():
    nome = str(input('Digite o nome do arquivo: '))
    nome = nome + '.csv'
    return nome

def intervalo():
    """
    Pergunta o intervalo que será usado na medida

    """
    while True:
        inter = str(input('Intervalo de tempo em segundos, minutos ou horas? [s, m ou h] ')).lower()
        if inter in 'smh':
            if inter == 's':
                n = 1
                break
            elif inter == 'm':
                n = 60
                break
            elif inter == 'h':
                n = 3600
                break
        else:
            print('Por favor, digite um intervalo válido, [s, m ou h]')
    return n

def subplot(x, y, t, xlabel ='x', ylabel1='y2', ylabel2='y2'):
    """
    Ordenada 1 = x,Ordenada 2 = y, Abscissa = t, xlabel1 = 'x1', ylabel1='y2', title1='Título 1', xlabel2 = 'x1', ylabel2='y2', title2='Título 2'
    """
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(12, 5))

    ax[0].plot(t, x, color='blue', lw=2)
    ax[0].set_xlabel(xlabel)
    ax[0].set_ylabel(ylabel1)

    ax[1].plot(t, y, color='red', lw=2)
    ax[1].set_xlabel(xlabel)
    ax[1].set_ylabel(ylabel2)

    return fig

def falha_():
    import time
    h = time.strftime('%H:%M:%S')
    print(f'''Falha no sistema às {h}:
            -Verifique a conexão USB;
            -Verifique se a porta USB {usb()} é a correta;
            
        Se nada der certo, contate o desenvolvedor:
        Kaike Pacheco -  kaikesoad.km@gmail.com''')
