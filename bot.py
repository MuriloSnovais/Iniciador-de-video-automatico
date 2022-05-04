import pyautogui
pyautogui.position()
()

video = str(input('Digite o Nome do video: '))

# Inicio do programa
pyautogui.FailSafeException
pyautogui.alert('Então iniciaremos o Video {}'.format(video))
pyautogui.PAUSE = 1.5

# Abrir o Navegador
pyautogui.press('winleft')
pyautogui.write('Navegador Opera')
pyautogui.press('enter')
pyautogui.write('youtube.com')
pyautogui.press('enter')


# Movendo o mouse e clicando
pyautogui.moveTo(1000,130)
pyautogui.click(1000, 130)

# Pesquisando o Video
pyautogui.write('{}'.format(video))
pyautogui.press('enter')
pyautogui.moveTo(800, 350)
pyautogui.click(800, 350)
pyautogui.press('f')

pyautogui.alert('Obrigado por usar o Bot de teste')





