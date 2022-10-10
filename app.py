import pywhatkit as kit
import pyautogui
import time

# https://github.com/Ankit404butfound/PyWhatKit

# Send a WhatsApp Message to a Group instantly
# kit.sendwhatmsg_to_group_instantly("G7mDIKUlU25HsWC7iasnNT", "Turma, O poder que tem opções com muito gamma, é impressionante para muitos. Movimentações pequenas no ativo subjacente, trazem valorizações bruscas. Veja os exemplos abaixo das calls de ELET6 que tem muito gamma (devido a baixa volatilidade implícita) e das puts de CSNA3 que tem alta volatilidade implícita.")

# Send an Image to a Contact with the no Caption
# For MacOS users, only JPEG is supported currently.
kit.sendwhats_image("G7mDIKUlU25HsWC7iasnNT", '/1.jpeg1.jpeg', 19, 44)

# kit.sendwhatmsg_to_group_instantly("G7mDIKUlU25HsWC7iasnNT", "Quanto maior a volatilidade implícita, menor será a concentração de gamma em strikes próximos do dinheiro.")

# kit.sendwhatmsg_to_group_instantly("G7mDIKUlU25HsWC7iasnNT", "Sobre minhas posições nos dois ativos por opções, minha visão é: Mantive ELET6, porém é totalmente aconselhável se colocar pelo menos o valor alocado no bolso. Muitos já estão com mais de 200% de lucro. CSNA3, fechei a que estava e rolei para um delta mais distante, colocando o lucro no bolso. Abrir uma ponta travada com delta de -0,15 é muito sensato e é o que devo fazer.")

WIDTH, HEIGHT = pyautogui.size()
pyautogui.click(WIDTH / 2, HEIGHT / 2)
time.sleep(7)
# kit.press_and_release('enter')