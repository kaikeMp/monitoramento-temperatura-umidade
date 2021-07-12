import matplotlib.pyplot as plt
import serial
from serial.tools import list_ports
import time
from complementares import *

#Entrada de leitura do arduíno
print('\033[1;107m\033[1;31mBem vindo ao Sistema de Monitoramento de Temperatura e Umidade \033[;1m(S.M.T.U) - Dine \033[0;0m ')
time.sleep(1)
try:
    porta = usb()
    ser = serial.Serial(porta, 9600, timeout=0)
    ports = list_ports.comports()
    nome = nome_()
    i = intervalo()
    hora = time.ctime()
    temp = []
    humid = []
    tempo = []
    try:
        while True:
            line = ser.readline()
            if line:
                string = line.decode()
                if len(string)==11:
                    H = float(string[:5])
                    T = float(string[6:])
                    temp.append(T)
                    humid.append(H)
                    h = time.strftime('%H:%M:%S')
                    tempo.append(h)
                    print(H, T, h)
                    time.sleep(i)

    except (KeyboardInterrupt):
        info = salvar(humid, temp, tempo)
        subplot(humid, temp, tempo, ylabel1='Umidade [%]', ylabel2='Temperatura [ºC]', xlabel=f'Tempo' )
        plt.gcf().autofmt_xdate()
        plt.show()
        info.to_csv(nome, index=False)
        print()
        print('Processo interrompido pelo usuário')
    except (ValueError):
        falha_()
        if hora[len(hora)] - hora[0] >10:
            info = salvar(humid, temp, tempo)
            info.to_csv(nome, index=False)
    ser.close()
except serial.serialutil.SerialException:
    falha_()

except (KeyboardInterrupt):
    print()
    print('Processo interrompido pelo usuário')
