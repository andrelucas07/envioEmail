from string import Template
from datetime import datetime

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib

meu_email = 'login_email'
senha = 'senha_email'

# Abre o arquivo "template.html" para manupular.
with open('template.html', 'r') as html:
    # Instacio a classe Template e passo como parametro o html.read; html -> é o arquivo; .read() -> vai ler o
    # template.html.
    template = Template(html.read())

    data_atual = datetime.now().strftime('%d/%m/%Y')

    # 1 - corpo_msg vai receber o template com os atributos definidos. 1.1 - template.substitute vai fazer a
    # atribuição dos valores passados em parametro nas variaveis criadas no template ($nome, $data)
    corpo_msg = template.substitute(nome='Seu Nome', data=data_atual)

# msg instacia a classe MIMEMultipart() que foi importada de email.mime.multipart
# essa classe é responsável por definir a estrutura do email: remetente, destinatário, titulo, e o corpo do email.
msg = MIMEMultipart()

# define o remetente
msg['from'] = 'Nome_remetente'

# define o email do cliente/destinatário
msg['to'] = meu_email

# define o assunto do email.
msg['subject'] = 'Atenção: email de teste.'

# De fine o corpo da mensagem .html ou sem formatação.
corpo = MIMEText(corpo_msg, 'html')

# Anexa o corpo da mensagem.
msg.attach(corpo)

# Abro arquivo de imagem para manipulação.
with open('test-img.jpg', 'rb') as img:
    # Instancio a clace MIMEImage e passo a imagem.read() para leitura.
    img = MIMEImage(img.read())

    # anexo a imagem a mensagem.
    msg.attach(img)

# Abro o SMTP para o envio automático do email, defino o host correspondente ao email e porta.
with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    # inicializa o smtp
    smtp.ehlo()
    # Coloca a conexão SMTP em modo TSL (Segurança da camada de transporte)
    smtp.starttls()
    # Inserir o login e senha
    smtp.login(meu_email, senha)
    # Responsável por fazer o envio da mensagem passando ela como parambetro.
    smtp.send_message(msg)
    print('Enviado com sucesso.')
