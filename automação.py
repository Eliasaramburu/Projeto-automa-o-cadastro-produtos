import pyautogui
import time
import pandas

pyautogui.PAUSE= 1.5

pyautogui.hotkey('win', '3')

pyautogui.hotkey('Ctrl', 't')

#pyautogui.write('Chr')
#pyautogui.press('enter')

time.sleep(1)

#pyautogui.press('tab')

#pyautogui.press('enter')

time.sleep(1)

#
#   pyautogui.hotkey('Ctrl', 'l')


pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')

time.sleep(1)

pyautogui.press('enter')

time.sleep(1)

pyautogui.click(x=691, y=547)

pyautogui.write('eliasaramburu@gmail.com')

pyautogui.press('tab')


pyautogui.write('12345')

pyautogui.press('tab')

pyautogui.press('enter')


pyautogui.click(x=653, y=437)

tabela = pandas.read_csv('produtos (2).csv')
print(tabela)

#linha = 0  6.5

for linha in tabela.index:


    #cód produto
    cod = tabela.loc[linha, 'codigo']

    pyautogui.write(str(cod))
    pyautogui.press('tab')

    #marca produto
    marca = tabela.loc[linha, 'marca']

    pyautogui.write(str(marca))
    pyautogui.press('tab')

    #tipo produto
    tipo = tabela.loc[linha, 'tipo']

    pyautogui.write(str(tipo))
    pyautogui.press('tab')

    #categoria produto
    categoria = tabela.loc[linha, 'categoria']

    pyautogui.write(str(categoria))
    pyautogui.press('tab')

    #preço produto
    preco = tabela.loc[linha, 'preco_unitario']

    pyautogui.write(str(preco))
    pyautogui.press('tab')


    #custo produto
    custo = tabela.loc[linha, 'custo']

    pyautogui.write(str(custo))
    pyautogui.press('tab')

    #obs produto
    obs = tabela.loc[linha, 'obs']

    if not pandas.isna(obs):
        pyautogui.write(str(obs))
    pyautogui.press('tab')

    pyautogui.press('enter')

    time.sleep(1)

    pyautogui.scroll(5000)

    pyautogui.click(x=653, y=437)


