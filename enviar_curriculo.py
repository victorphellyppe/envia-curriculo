import csv
import smtplib
from email.message import EmailMessage

# === CONFIGURAÇÕES ===
ARQUIVO_CSV = 'emails.csv'
EMAIL_REMETENTE = 'vitinifal@gmail.com'
SENHA = 'ymzjetjpozmtuyje'
CAMINHO_CURRICULO = 'Curriculo 2025  victoroliveiradev detalhado ATUALIZADO!.pdf'

# === LER DADOS DO CSV ===
def ler_empresas_do_csv(arquivo_csv):
    empresas = []
    with open(arquivo_csv, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            email = row.get('Email')
            empresa = row.get('Empresa')
            if email and empresa:
                empresas.append({
                    'empresa': empresa.strip(),
                    'email': email.strip()
                })
    return empresas

# === ENVIAR E-MAIL COM CURRÍCULO ===
def enviar_email(destinatario, nome_empresa):
    msg = EmailMessage()
    msg['Subject'] = f'Currículo - Victor Oliveira'
    msg['From'] = EMAIL_REMETENTE
    msg['To'] = destinatario
    msg.set_content(f'''
Prezados(as) da {nome_empresa},

Segue em anexo meu currículo atualizado para avaliação. 

Agradeço pela atenção e fico à disposição para quaisquer informações adicionais.

Atenciosamente,
Victor Oliveira
''')

    # Anexar currículo
    with open(CAMINHO_CURRICULO, 'rb') as f:
        file_data = f.read()
        file_name = f.name
    msg.add_attachment(file_data, maintype='application', subtype='pdf', filename=file_name)

    # Enviar via SMTP
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_REMETENTE, SENHA)
        smtp.send_message(msg)
        print(f'Email enviado com sucesso para {nome_empresa} - {destinatario}')

# === EXECUÇÃO PRINCIPAL ===
if __name__ == '__main__':
    empresas = ler_empresas_do_csv(ARQUIVO_CSV)
    if not empresas:
        print('Nenhum e-mail encontrado no CSV.')
    for item in empresas:
        enviar_email(item['email'], item['empresa'])
