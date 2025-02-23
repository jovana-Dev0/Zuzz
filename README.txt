

                 Sistema de Monitoramento e Segurança



   Descrição

  Este projeto tem como objetivo monitorar pastas e arquivos no sistema em tempo real, identificando e reagindo a arquivos suspeitos. O sistema foi desenvolvido para detectar arquivos com palavras-chave associadas a vírus, trojans e outras ameaças cibernéticas. Ao identificar um arquivo suspeito, o sistema gera um alerta e move o arquivo para uma "quarentena" para evitar a execução de código malicioso.

   O sistema foi desenvolvido utilizando Python, com bibliotecas de monitoramento de arquivos e hash para verificação da integridade dos mesmos.



== Funcionalidades

- Monitoramento de Diretórios: Monitora pastas específicas no sistema em busca de novas criações de arquivos e alterações.

- Verificação de Arquivos: Realiza uma verificação em arquivos recém-criados, buscando por palavras-chave suspeitas (ex: "trojan", "malware")você pode mudar e adicionar mais.

- Geração de Hashes: Calcula o hash dos arquivos para garantir que a verificação seja única e confiável.

- Movimento para Quarentena: Arquivos identificados como suspeitos são movidos para uma pasta de quarentena.

- Notificação de Segurança: Envia notificações de alerta via e-mail ou outro método de notificação sobre os arquivos suspeitos.

---

== Tecnologias Utilizadas

- Python: Linguagem principal utilizada no desenvolvimento do sistema.
- watchdog: Biblioteca Python para monitoramento de mudanças nos sistemas de arquivos.

- hashlib: Biblioteca para a criação de hashes (SHA256) para verificação da integridade dos arquivos.
- smtplib: Biblioteca para envio de e-mails de notificação.

---

== Instalação

== Requisitos

1. Python 3.x instalado no seu sistema.

2. Bibliotecas Python necessárias:
   - `watchdog`
   - `hashlib`
   - `smtplib`

== Passo a Passo para Instalação

1. Clone o repositório (se estiver no GitHub) ou faça o download do código fonte:

   
   git clone https://github.com/seuusuario/sistema-seguranca.git
   cd sistema-seguranca
   

2. Instale as dependências:

   Você pode usar o `pip` para instalar as dependências necessárias. Crie e ative um ambiente virtual (opcional, mas recomendado) e instale as dependências:

   python -m venv venv
   source venv/bin/activate   * No Windows use 'venv\Scripts\activate'
   pip install -r requirements.txt


   Caso ainda não tenha um arquivo `requirements.txt`, basta instalar manualmente as bibliotecas necessárias:

   use

   pip install watchdog
  



== Como Rodar o Projeto


=== 1. Configuração do Sistema de Monitoramento

Antes de rodar o sistema, edite o arquivo `config.py` (ou qualquer outro arquivo de configuração, se existir) para adicionar os diretórios que você deseja monitorar.

Exemplo:

```python
MONITORAR = [
    r'C:\Users\name\Desktop',
    r'C:\Users\name\Downloads',
    r'C:\Users\name\Documents'
]
```

== 2. Rodando o Sistema

Para rodar o sistema de monitoramento, basta executar o script `monitor.py`:

```bash
python monitor.py
```

O sistema irá começar a monitorar as pastas configuradas e ficará aguardando eventos de criação ou alteração de arquivos. Quando um arquivo suspeito for encontrado, ele será movido para a quarentena.

== 3. Verificando Arquivos Suspeitos

Os arquivos serão analisados em tempo real e, ao serem identificados como suspeitos, o sistema irá calcular o **hash** do arquivo, gerar um alerta e mover o arquivo para a quarentena.

---

== Notificações de Segurança

O sistema envia notificações via e-mail quando um arquivo suspeito é detectado e movido para a quarentena. Para configurar isso, edite a função de envio de e-mail em `notificar.py` com suas credenciais.

Exemplo de código de notificação:


               python

import smtplib
from email.mime.text import MIMEText

def enviar_email(subject, body):
    # Configurar SMTP
    servidor = 'smtp.gmail.com'
    porta = 587
    usuario = 'seuemail@gmail.com'
    senha = 'suasenha'

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = usuario
    msg['To'] = usuario

    try:
        with smtplib.SMTP(servidor, porta) as server:
            server.starttls()
            server.login(usuario, senha)
            server.sendmail(usuario, usuario, msg.as_string())
        print('Notificação enviada com sucesso!')
 except Exception as e:
        print(f'Erro ao enviar e-mail: {e}')



== Contribuições

Se você quiser contribuir para este projeto, fique à vontade para **abrir issues** ou **enviar pull requests**. Para contribuir, basta fazer um fork do repositório, fazer as modificações e depois enviar uma pull request.

---

== Licença

Este projeto é licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

== Agradecimentos

- Agradeço aos desenvolvedores das bibliotecas `watchdog`, `hashlib` e `smtplib` por tornarem este projeto possível.




