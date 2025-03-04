import requests
from bs4 import BeautifulSoup

#---------------------------------------------------------------------
#Scrapeo

# URL de la página para scrapear
url = 'https://www.pcgamer.com/epic-games-store-free-games-list/'

aux = ''

# Realiza la solicitud HTTP
response = requests.get(url)

# Comprueba si la solicitud fue exitosa (código de estado 200)
if response.status_code == 200:
    # Parsea el contenido HTML de la página usando BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Encuentra y extrae el texto de los elementos que te interesan
    paragraphs = soup.find_all('p')

    # Itera sobre los párrafos y guarda el texto
    for paragraph in paragraphs:
        aux = aux + paragraph.text + '\n'
else:
    # Si la solicitud no fue exitosa, muestra un mensaje de error
    print('Error al cargar la página:', response.status_code)

import re
texto = aux

patron_inicial = r"For games that are free all the time, check out our lists of best free PC games, best free games on Steam, and best browser games."

# Buscar el patrón inicial en el texto
resultado_inicial = re.search(patron_inicial, texto)

# Verificar si se encontró la línea inicial
if resultado_inicial:
    # Obtener la posición de inicio de la coincidencia encontrada
    inicio_coincidencia = resultado_inicial.end()

    # Obtener la línea que sigue al patrón inicial
    linea_siguiente = re.search(r".+", texto[inicio_coincidencia:])

    # Verificar si se encontró la línea siguiente y extraerla
    if linea_siguiente:
        linea_deseada = linea_siguiente.group()
        print(linea_deseada)
    else:
        print("Línea siguiente no encontrada en el texto.")
else:
    print("Patrón inicial no encontrado en el texto.")

#-------------------------------------------------------------
#Mandar correo

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Configuración del servidor SMTP de Gmail
smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_username = 'DIEGOPASTORBONET@gmail.com'
smtp_password = 'xwao howa lwiw zeyl'

# Configurar el mensaje
mensaje = MIMEMultipart()
mensaje['From'] = smtp_username
mensaje['To'] = 'diegopastorbonet@gmail.com'
mensaje['Subject'] = 'Juegos gratis Eppic'

cuerpo = linea_deseada
mensaje.attach(MIMEText(cuerpo, 'plain'))

# Iniciar la conexión SMTP y enviar el mensaje
try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()  # Habilitar el cifrado TLS
    server.login(smtp_username, smtp_password)
    server.sendmail(smtp_username, 'diegopastorbonet@gmail.com', mensaje.as_string())
    server.quit()  # Cerrar la conexión
    print('Correo electrónico enviado correctamente.')
except Exception as e:
    print('Error al enviar el correo electrónico:', str(e))
