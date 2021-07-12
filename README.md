# monitoramento-temperatura-umidade
Sistema de monitoramento com comunicação arduino e python

Com o arquivo .ino instalado no arduíno, o programa "arduínodata.py" é capaz de realizar a leitura e importação das grandezas avaliadas pelo sensor DHT no arduíno.
As portas usb disponíveis no programa são recorrentes mas podem mudar de acordo com computador.

A porta USB correta pode ser encontrado no programa do arduíno em /Ferramentar(Tools)/Porta(Port)/ Com o arduíno conectado.
Para mudar a porta no programa em python, basta mudar o nome da porta no caminho em - Serial.

