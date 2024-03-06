import pyautogui as pg
pg.useImageNotFoundException()

while True:
    try:
        add=pg.locateOnScreen("ok.png",confidence=0.9)
        print(add)
        break
    except pg.ImageNotFoundException:
        print("nao encontrada")