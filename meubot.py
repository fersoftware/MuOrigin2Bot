from PIL import ImageGrab, ImageOps, Image
import pyautogui
import time
from numpy import *

class Coordinates():
    iconeMu = (294, 331, 351, 387)
    btnStartServer = (646, 418, 708, 439)
    closeHome = (1151, 144, 1158, 152)
    btnStartChar = (1035, 598, 1089, 617)
    btnClaim = (931, 782, 995, 795)
    btnClaim2 = (925, 750, 991, 762)
    btnAtacar = (930, 624, 940, 631)
    xp = (362, 703, 432, 721)
    btnDungeon = (961, 183, 968, 188)
    btnAnuncio = (952, 162, 970, 177)
    msgItemClaim2 = (662, 288, 671, 292)
    btnEspera = (543, 345, 553, 354)
    Dungeon = (1244, 290)
    DungeonCadeado = (887, 115)
    CloseDungeon = (869, 602)

class Images():
    iconeMu = 28507
    btnStartServer = 22487
    closeHome = 4156
    btnStartChar = 21170
    btnClaim = 20981
    btnClaim2 = 15638
    btnAtacarOFF = 1367
    btnAtacarON = 5535
    btnDungeon = 898
    btnAnuncio = 16956
    msgItemClaim2 = 6984
    btnEspera = 3964

def info(txt):
    box = txt
    image = ImageGrab.grab(box)
    grayImage = ImageOps.grayscale(image)
    a = array(grayImage.getcolors())
    return a.sum()

if __name__ == "__main__":
    box = Coordinates.btnClaim
    print(info(box))

def main():
    print('BOT PROTOTIPO MU 1.1')
    time.sleep(5)
    tentativa = 0
    tentativaChar = 4
    while True:
        if (info(Coordinates.iconeMu) == Images.iconeMu):
            x = Coordinates.iconeMu
            print('Entrando no Mu Origin 2')
            pyautogui.click(x[0] + 5, x[1] + 5)
            time.sleep(3);
        if (info(Coordinates.closeHome) == Images.closeHome):
            x = Coordinates.closeHome
            print('Fecha Home')
            pyautogui.click(x[0] + 5, x[1] + 5)
            time.sleep(3);
        if (info(Coordinates.btnStartServer) == Images.btnStartServer):
            x = Coordinates.btnStartServer
            print('Entrando no Server')
            pyautogui.click(x[0] + 5, x[1] + 5)
            time.sleep(3);
        if (info(Coordinates.btnStartChar) == Images.btnStartChar):
            x = Coordinates.btnStartChar
            time.sleep(3)
            print('Entrando com o Char ', tentativaChar)
            pyautogui.click(x[0] + 5, x[1] + 5)
            time.sleep(10)
            if tentativaChar == 0:
                pyautogui.click(801, 74)
                tentativaChar = 4
            tentativaChar -= 1
        if (info(Coordinates.btnAnuncio) == Images.btnAnuncio):
            x = Coordinates.btnAnuncio
            print('Fechando Anuncio')
            pyautogui.click(x[0] + 5, x[1] + 5)
            time.sleep(1);
        if (info(Coordinates.btnClaim) == Images.btnClaim):
            x = Coordinates.btnClaim
            print('Tela Claim aceita')
            pyautogui.click(x[0] + 5, x[1] + 5)
            time.sleep(1);
        if (info(Coordinates.btnClaim2) == Images.btnClaim2):
            x = Coordinates.btnClaim2
            print('Tela Itens Claim aceita')
            pyautogui.click(x[0] + 5, x[1] + 5)
            time.sleep(1);
        if (info(Coordinates.msgItemClaim2) == Images.msgItemClaim2):
            x = Coordinates.msgItemClaim2
            print('Fechando Tela Claim Item')
            pyautogui.click(x[0] + 5, x[1] + 5)
            time.sleep(1);
        if (info(Coordinates.btnAtacar) == Images.btnAtacarOFF):
            x = Coordinates.btnAtacar
            print('Entrando em Modo Atacar')
            pyautogui.click(x[0] + 5, x[1] + 5)
            time.sleep(1);
        if (info(Coordinates.btnEspera) == Images.btnEspera):
            x = Coordinates.btnEspera
            print('Saindo da Tela Hibernação')
            pyautogui.click(x[0] + 5, x[1] + 5)
            pyautogui.dragTo(x[0] + 5, x[1] + 5, button='left')
            pyautogui.dragTo(x[0] + 400, x[1] + 5, 3, button='left')
            time.sleep(1);
        if (info(Coordinates.btnAtacar) == (
                Images.btnAtacarON or info(Coordinates.btnAtacar) == Images.btnAtacarOFF) and info(
            Coordinates.btnDungeon) == Images.btnDungeon):
            tentativa = 0;
            # print('Fora da Cidade')
        elif (info(Coordinates.btnAtacar) != (
                Images.btnAtacarON or info(Coordinates.btnAtacar) == Images.btnAtacarOFF) and info(
            Coordinates.btnDungeon) == Images.btnDungeon):
            if (tentativa == 2):
                print('Dentro da Cidade')
                time.sleep(8);
                print('Abrindo Mapa')
                time.sleep(3);
                pyautogui.click(1125, 155)
                time.sleep(3);
                print('Escolhendo...')
                pyautogui.click(220, 213)
                time.sleep(3);
                print('Indo até o MOB')
                pyautogui.click(545, 305)
                print('Aguardando...')
                time.sleep(15); # tempo de um ponto dacidade até o outro ponto onde voce vai upar
                pyautogui.click(212, 108)
                print('Upando...')
                tentativa = 0;
            tentativa += 1
main()
