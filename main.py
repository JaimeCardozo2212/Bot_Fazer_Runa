import pyautogui as pg
pg.useImageNotFoundException()
import schedule
import sys
import tkinter as tk 
from tkinter import ttk
import ctypes
import pygetwindow as gw
import keyboard
import win32gui

hotkey = "f1","f2","f3","f4","f5","f6","f7","f8","f9","f10","f11","f12"

def get_window_opacity(hwnd):
    ex_style = win32gui.GetWindowLong(hwnd, GWL_EXSTYLE)
    if ex_style & WS_EX_LAYERED:
        style = ctypes.c_ulong()
        opacity = ctypes.c_byte()
        ctypes.windll.user32.GetLayeredWindowAttributes(hwnd, None, ctypes.byref(opacity), ctypes.byref(style))
        return opacity.value
    else:
        return None

def hidden_client():
    windows = pg.getAllWindows()
    for window in windows:
        try:
            window_name = window.title.split('Tibia -')[1]
            if window_name:
                WINDOW_TITLE = window.title
        except:
            continue

    try:
        target_window = [item for item in gw.getWindowsWithTitle(WINDOW_TITLE) if item.title == WINDOW_TITLE][0]
    except:
        pg.alert(title="Hidden Client Tibia", text='Janela do Tibia não localizada')
        raise ValueError('Janela do Tibia não localizada')

    target_hwnd = target_window._hWnd

    OPACITY = 255
    current_opacity = get_window_opacity(target_hwnd)
    if current_opacity == -1:
        OPACITY = 1
    print('OPACITY', OPACITY)
    ex_style = ctypes.windll.user32.GetWindowLongA(target_hwnd, GWL_EXSTYLE)
    ctypes.windll.user32.SetWindowLongA(target_hwnd, GWL_EXSTYLE, ex_style | WS_EX_LAYERED)
    ctypes.windll.user32.SetLayeredWindowAttributes(target_hwnd, 0, OPACITY, LWA_ALPHA)
    print("Opacidade da janela modificada.")
    
    if current_opacity is not None:
        print(f"Opacidade atual da janela: {current_opacity}")
    else:
        print("A janela não é uma janela de camada (layered window).")
    return OPACITY

def imprimir_texto():
    global texto
    # texto = "00:00"
    texto = entrada.get()
    print(texto)
    # root.iconify()
def Hotkey_Runa():
    global hot_key
    global boots_hotkey
    global ring_hotkey
    boots_hotkey = hotkey_boots.get()
    ring_hotkey = hotkey_ring.get()
    hot_key = hotkey_runa.get()
def runa_fazer():
    global runa
    runa = entrada_runa.get()
    print(runa)
def minimizar_janela():
    root.iconify()

def mostar_janela():
    if keyboard.is_pressed('esc'):
        root.deiconify()
        print('Programa encerrado!')

def start():
    runa_fazer()
    imprimir_texto()
    Hotkey_Runa()
    root.withdraw()
    qual_runa_fazer()

def encerrar_programa():
    print("Encerrar Programa...")
    sys.exit()  

def change_color_enter(event):
    event.widget.config(bg='#62d329',fg="black") 

def change_color_leave(event):
    event.widget.config(bg="#6eed2e",fg="white")

def opacity_change_color_enter(event):
    event.widget.config(bg='#3da3ba',fg="black") 

def opacity_change_color_leave(event):
    event.widget.config(bg="#48c1dc",fg="white")

def encerrar_change_color_enter(event):
    event.widget.config(bg='#ed4343',fg="black") 

def encerrar_change_color_leave(event):
    event.widget.config(bg="#ff4d4d",fg="white")

def fazer_avalanche():
    while True:
        try:
            schedule.every().day.at(texto).do(encerrar_programa)
        except:
            pass
        try:
            if keyboard.is_pressed('esc'):
                root.deiconify()
                break
            pg.locateOnScreen("Bot_Fazer_Runa/avalanche.png",confidence=0.8)
            pg.press(hot_key)
            pg.sleep(1)
            aumentar_capacidade()
        except pg.ImageNotFoundException:
            food()
            soft_boots()
            ring()
            tibia_logar()
            aumentar_capacidade()

def fazer_sd():
    while True:
        try:
            schedule.every().day.at(texto).do(encerrar_programa)
        except:
            pass
        try:
            if keyboard.is_pressed('esc'):
                root.deiconify()
                break
            pg.locateOnScreen("imgs/runa_sd.png",confidence=0.8)
            pg.press(hot_key)
            pg.sleep(1)
            aumentar_capacidade()
        except pg.ImageNotFoundException:
            food()
            soft_boots()
            ring()
            tibia_logar()
            aumentar_capacidade()
def fazer_arrow():
    while True:
        try:
            schedule.every().day.at(texto).do(encerrar_programa)
        except:
            pass
        try:
            if keyboard.is_pressed('esc'):
                root.deiconify()
                break
            pg.locateOnScreen("imgs/arrow.png",confidence=0.8)
            pg.press(hot_key)
            pg.sleep(2)
            aumentar_capacidade()
        except pg.ImageNotFoundException:
            food()
            soft_boots()
            ring()
            tibia_logar()
            aumentar_capacidade()
def fazer_holy():
    while True:
        try:
            schedule.every().day.at(texto).do(encerrar_programa)
        except:
            pass
        try:
            if keyboard.is_pressed('esc'):
                root.deiconify()
                break
            pg.locateOnScreen("imgs/holy.png",confidence=0.8)
            pg.press(hot_key)
            pg.sleep(1)
            aumentar_capacidade()
        except pg.ImageNotFoundException:
            food()
            soft_boots()
            ring()
            tibia_logar()
            aumentar_capacidade()

horario = ["01:00","02:00","03:00","04:00","05:00","06:00","07:00","08:00",
           "09:00","10:00","11:00","12:00","13:00","14:00","15:00","16:00",
           "17:00","18:00","19:00","20:00","21:00","22:00","23:00","23:59"]

arrow ="imgs/arrow.png"
holy = "imgs/holy.png"
Sd = "imgs/sd.png"
runas = "Avalanche","Sudden Death" , "Holy", "Arrow"

def ring():
    if usar_ring.get() == 1:
        try:
            pg.locateOnScreen("Bot_Fazer_Runa/imgs/sem anel.png",confidence=0.8)
            pg.press(ring_hotkey)
        except pg.ImageNotFoundException:
            pass
    else:
        pass

def soft_boots():
    if usar_boots.get() == 1:
        try:
            pg.locateOnScreen("Bot_Fazer_Runa/imgs/botas_gastas.png",confidence=0.8)
            pg.press(boots_hotkey)
        except pg.ImageNotFoundException:
            pass
    else:
        pass
def food():
    try:
        pg.locateOnScreen("Bot_Fazer_Runa/imgs/food02.png",confidence=0.9)
        pg.press("f9")
    except pg.ImageNotFoundException:
        pass



def qual_runa_fazer():
    if runa == "Avalanche":
        fazer_avalanche()
    if runa == "Sudden Death":
        fazer_sd()
    if runa == "Arrow":
        fazer_arrow()
    if runa == "Holy":
        fazer_holy()
    else:
        pass

def tibia_logar():
    try:
        pg.locateOnScreen("Bot_Fazer_Runa/tibia_fora.png",confidence=0.8)
        print("primeira imagem")
        ok = pg.locateCenterOnScreen("Bot_Fazer_Runa/ok.png",confidence=0.8)
        print("segunda imagem")
        pg.moveTo(ok, duration=0.5)
        pg.click()
        pg.sleep(3)
        pg.press('enter')
    except pg.ImageNotFoundException:
        pass

def aumentar_capacidade():
    if usar_capacidade.get() == 1:
        try:
            sd = pg.locateCenterOnScreen("Bot_Fazer_Runa/imgs/ava_mochila.png",confidence=0.7,region= region_mochila)
            pg.moveTo(sd,duration=0.5)
            try:
                pg.dragTo(centro_tela, button='left',duration=0.5)
            except pg.ImageNotFoundException:
                pass
        except pg.ImageNotFoundException:
                pass
        try:
            sd = pg.locateCenterOnScreen("Bot_Fazer_Runa/imgs/sd.png",confidence=0.7,region= region_mochila)
            pg.moveTo(sd,duration=0.5)
            try:
                pg.dragTo(centro_tela, button='left',duration=0.5)
            except pg.ImageNotFoundException:
                pass
        except pg.ImageNotFoundException:
                pass
        
        try:
            pg.locateCenterOnScreen("Bot_Fazer_Runa/blank1.png",confidence=0.8,region= region_mochila)
            pass
        except pg.ImageNotFoundException:
            try:
                blank = pg.locateCenterOnScreen("Bot_Fazer_Runa/blank.png", region= area_dp, confidence=0.8)
                pg.moveTo(blank,duration=0.5)
                pg.dragTo(region_mochila, button='left',duration=0.5)
            except pg.ImageNotFoundException:
                pass
    else:
        pass

root = tk.Tk()
root.title("Bot Runa")

OPACITY1 = tk.Button(root, text="Aplicar Opacidade",command=hidden_client,fg="white",bd=2,bg="#48c1dc")
OPACITY1.grid(row=3, column=0,columnspan=5,padx=10,pady=5,sticky="nsew")
OPACITY1.bind("<Enter>", opacity_change_color_enter)
OPACITY1.bind("<Leave>",opacity_change_color_leave)

laabel_ring = tk.Label(text="Usar Ring")
laabel_ring.grid(row=0,column=2)

usar_ring = tk.IntVar()
comando_ring = tk.Checkbutton(root,variable=usar_ring)
comando_ring.grid(row=0, column=3)

hotkey_ring = ttk.Combobox(values=hotkey,width=5)
hotkey_ring.grid(row=0, column=4)

laabel_boots = tk.Label(text="Usar Boots")
laabel_boots.grid(row=1,column=2)

usar_boots = tk.IntVar()
comando_boots = tk.Checkbutton(root,variable=usar_boots)
comando_boots.grid(row=1, column=3,padx=10,pady=10)

hotkey_boots = ttk.Combobox(values=hotkey,width=5)
hotkey_boots.grid(row=1, column=4,padx=10,pady=10)

laabel_capacidade = tk.Label(text="Mover Runa")
laabel_capacidade.grid(row=2,column=2)

usar_capacidade = tk.IntVar()
comando_capacidade = tk.Checkbutton(root,variable=usar_capacidade)
comando_capacidade.grid(row=2, column=3,padx=10,pady=10)

laabel_horario = tk.Label(text="Escolha Horário para termino do programa")
laabel_horario.grid(row=0,column=0)

entrada = ttk.Combobox(values=horario,text="00:00",width=10)
entrada.grid(row=0, column=1,padx=10,pady=10)

laabel_qual_runa = tk.Label(text="Selecione qual Runa fazer")
laabel_qual_runa.grid(row=1,column=0)

entrada_runa = ttk.Combobox(values=runas,width=10)
entrada_runa.grid(row=1, column=1,padx=10,pady=10)

laabel_hotkey = tk.Label(text="Selecione qual HotKey")
laabel_hotkey.grid(row=2,column=0)

hotkey_runa = ttk.Combobox(values=hotkey,width=10)
hotkey_runa.grid(row=2, column=1,padx=10,pady=10)

botao = tk.Button(root,text='Start', command=start,bg="#6eed2e" ,fg="white",bd=2)
botao.grid(row=4,column=0,columnspan=5, padx=10,pady=5,sticky="nsew")
botao.bind("<Enter>", change_color_enter)
botao.bind("<Leave>",change_color_leave)

botao_encerrar = tk.Button(root,text='Encerrar', command=encerrar_programa,bg="#ff4d4d",fg="white",bd=2)
botao_encerrar.grid(row=5,column=0,columnspan=5, padx=10,pady=5,sticky="nsew")
botao_encerrar.bind("<Enter>", encerrar_change_color_enter)
botao_encerrar.bind("<Leave>",encerrar_change_color_leave)
GWL_EXSTYLE = -20
WS_EX_LAYERED = 0x00080000
LWA_ALPHA = 0x00000002

def localizar_img(text,button,delay):
    try:
        pg.locateOnScreen(text,confidence=0.9)
        pg.press(button)
    except pg.ImageNotFoundException:
        pg.sleep(delay)
        pass
boots_hotkey = hotkey_boots.get()
ring_hotkey = hotkey_ring.get()
region_mochila = (1023, 40, 146, 185)
area_dp = (531,251,33,27)
centro_tela = (499,304)

schedule.run_pending()
    
root.mainloop()





        


# pg.displayMousePosition()


    





