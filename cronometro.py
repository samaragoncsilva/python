import time #importa a biblioteca time para usar o cronômetro

inicio = time.time()  # marca o início do cronômetro

try: 
    while True:
        # calcula quantos segundos passaram desde que começou
        tempo_passando = int(time.time() - inicio)

        # transforma os segundos em horas
        horas, resto = divmod(tempo_passando, 3600)   #1 hora
        # transforma os segundos restantes em minutos e segundos
        minutos, segundos = divmod(resto, 60)  # 1 minuto

        # mostra o tempo no formato 00:00:00
        print("\r{:02d}:{:02d}:{:02d}".format(horas, minutos, segundos), end="") # \r para continuar na mesma linha, end para nao pular linha

        time.sleep(1)  # espera 1 segundo antes de atualizar

except KeyboardInterrupt:  # captura quando o usuário pressiona Ctrl+C
    print("\nCronômetro parado!")  # exibe mensagem ao parar
