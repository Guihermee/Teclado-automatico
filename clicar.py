import tkinter as tk
import keyboard
import time
import json

CONFIG_FILE = "config.json"

def press_key(key):
    keyboard.press(key)
    keyboard.release(key)

def start_command():
    start_interval = int(start_entry.get())  # Obtém o valor do intervalo de início
    loop_interval = int(loop_entry.get())  # Obtém o valor do intervalo do loop
    qt_repetida = int(qt_repetida_entry.get())  # Obtém a quantidade de vezes que as teclas serão repetidas
    keys1 = keys1_entry.get()  # Obtém a primeira tecla a ser repetida
    keys2 = keys2_entry.get()  # Obtém a segunda tecla a ser repetida
    stop_button = stop_button_entry.get()  # Obtém a tecla para parar o programa

    print("Comando iniciado!")
    time.sleep(start_interval)  # Espera o intervalo de início

    while True:
        for _ in range(qt_repetida):
            for key in keys1:
                press_key(key)
                if keyboard.is_pressed(stop_button):
                    break

            for key in keys2:
                press_key(key)
                if keyboard.is_pressed(stop_button):
                    break

            if keyboard.is_pressed(stop_button):
                break

        if keyboard.is_pressed(stop_button):
            break

        for _ in range(loop_interval):
            if keyboard.is_pressed(stop_button):
                break
            time.sleep(1)  # Aguarda 1 segundo
    

def stop_command():
    print("Comando parado!")

def predefined_button_pressed(go_button):
    start_command()

def save_config():
    config = {
        "start_interval": start_entry.get(),
        "loop_interval": loop_entry.get(),
        "qt_repetida": qt_repetida_entry.get(),
        "keys1": keys1_entry.get(),
        "keys2": keys2_entry.get(),
        "stop_button": stop_button_entry.get()
    }

    with open(CONFIG_FILE, "w") as file:
        json.dump(config, file)

def load_config():
    try:
        with open(CONFIG_FILE, "r") as file:
            config = json.load(file)
            start_entry.insert(0, config["start_interval"])
            loop_entry.insert(0, config["loop_interval"])
            qt_repetida_entry.insert(0, config["qt_repetida"])
            keys1_entry.insert(0, config["keys1"])
            keys2_entry.insert(0, config["keys2"])
            stop_button_entry.insert(0, config["stop_button"])
    except FileNotFoundError:
        pass

window = tk.Tk()
window.geometry("400x450")  # Define o tamanho da janela
window.title("Auto Teclado") # Muda o título da janela

frame1 = tk.Frame(window)
frame1.pack(pady=10)  # Adiciona espaçamento vertical

start_label = tk.Label(frame1, text="Intervalo de Início (segundos):")
start_label.pack()
start_entry = tk.Entry(frame1)
start_entry.pack()

frame2 = tk.Frame(window)
frame2.pack(pady=10)  # Adiciona espaçamento vertical

loop_label = tk.Label(frame2, text="Intervalo do Loop (segundos):")
loop_label.pack()
loop_entry = tk.Entry(frame2)
loop_entry.pack()

frame3 = tk.Frame(window)
frame3.pack(pady=10)  # Adiciona espaçamento vertical

qt_repetida_label = tk.Label(frame3, text="Quantidade de vezes que as teclas serão repetidas (loop):")
qt_repetida_label.pack()
qt_repetida_entry = tk.Entry(frame3)
qt_repetida_entry.pack()

frame4 = tk.Frame(window)
frame4.pack(pady=10)  # Adiciona espaçamento vertical

keys1_label = tk.Label(frame4, text="Primeira tecla a ser repetida:")
keys1_label.pack()
keys1_entry = tk.Entry(frame4)
keys1_entry.pack()

keys2_label = tk.Label(frame4, text="Segunda tecla a ser repetida:")
keys2_label.pack()
keys2_entry = tk.Entry(frame4)
keys2_entry.pack()

frame5 = tk.Frame(window)
frame5.pack(pady=10)  # Adiciona espaçamento vertical

stop_button_label = tk.Label(frame5, text="Tecla para parar o programa:")
stop_button_label.pack()
stop_button_entry = tk.Entry(frame5)
stop_button_entry.pack()

frame6 = tk.Frame(window)
frame6.pack(pady=10)  # Adiciona espaçamento vertical

#stop_button_label = tk.Label(frame6, text="Tecla para iniciar o programa:")
#stop_button_label.pack()
#stop_button_entry = tk.Entry(frame6)
#stop_button_entry.pack()

load_config()  # Carrega as configurações salvas (se existirem)

frame7 = tk.Frame(window)
frame7.pack(pady=10)  # Adiciona espaçamento vertical

start_button = tk.Button(frame7, text="Iniciar", command=start_command)
#stop_button = tk.Button(frame6, text="Parar", command=stop_command)
save_button = tk.Button(frame7, text="Salvar Configuração", command=save_config)

start_button.pack(side="left", padx=5)
#stop_button.pack(side="left", padx=5)
save_button.pack(side="left", padx=5)

window.mainloop()
