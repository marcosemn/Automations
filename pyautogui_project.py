import pyautogui
import time
import pyperclip
import pandas as pd

pyautogui.PAUSE = 1
pyautogui.alert("Vai começar, aperte OK e não mexa em nada")

# opção 1 - abrir navegador novo e entrar no chrome
pyautogui.press("winleft")
pyautogui.write("chrome")
pyautogui.press("enter")

# opção 2 - abrir uma nova aba
#pyautogui.hotkey('ctrl', 't')

# abrir drive
# ensinar aqui o write
link = "https://drive.google.com/drive/folders/1mhXZ3JPAnekXP_4vX7Z_sJj35VWqayaR?usp=sharing"
pyperclip.copy(link)
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")
time.sleep(5)

# baixar base de dados atualizada
pyautogui.click(426, 383, clicks=2)
time.sleep(1)
pyautogui.click(1017, 482)
time.sleep(1)
pyautogui.click(1669, 243)
time.sleep(1)
pyautogui.click(1482, 706)
time.sleep(10)

df = pd.read_excel(r"C:\Users\Dell\Downloads/Vendas - Dez.xlsx")
faturamento = df['Valor Final'].sum()
qtde_produtos = df['Quantidade'].sum()

# abrir aba hotmail
pyautogui.hotkey('ctrl', 't')
pyautogui.write("http://hotmail.com")
pyautogui.press('enter')
time.sleep(5)

# clicar em escrever email
pyautogui.click(161, 213)
time.sleep(5)

# preencher informações do e-mail
pyautogui.write('marcosemn+diretoria@hotmail.com')
i=1
while i<5:
    pyautogui.press('tab')
    i = i+1
assunto = "Relatório de Vendas de Ontem"
pyperclip.copy(assunto)
pyautogui.hotkey("ctrl", 'v')
time.sleep(1)
pyautogui.press("tab")
texto = f"""
Prezados, bom dia

O faturamento de ontem foi de: R${faturamento:,.2f}
A quantidade de produtos foi de: {qtde_produtos:,}

Abs
Marcos"""
pyperclip.copy(texto)
pyautogui.hotkey("ctrl", 'v')

# enviar e-mail
pyautogui.hotkey('ctrl', 'enter')

# avisar que acabou
pyautogui.alert("Fim da Automação. Seu computador já voltou a ser seu")