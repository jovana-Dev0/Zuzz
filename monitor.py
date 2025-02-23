import os
import hashlib
from watchdog.observers import Observer # type: ignore # type: ignore
from watchdog.events import FileSystemEventHandler # type: ignore
import subprocess
import time

# Diretórios a serem monitorados
DIRETORIOS = [
    os.path.expanduser("~/Desktop"),
    os.path.expanduser("~/Downloads"),
    os.path.expanduser("~/Documents"),
    "C:\\Zuzz"
]

# Lista de palavras-chave suspeitas
PALAVRAS_SUSPEITAS = ["virus", "trojan", "malware", "ransomware", "spyware", "worm", "backdoor", "keylogger"]

# Função para calcular o hash SHA-256 do arquivo
def calcular_hash_arquivo(caminho_arquivo):
    try:
        with open(caminho_arquivo, "rb") as f:
            hash_sha256 = hashlib.sha256()
            while chunk := f.read(8192):
                hash_sha256.update(chunk)
            return hash_sha256.hexdigest()
    except Exception as e:
        print(f"Erro ao calcular hash: {e}")
        return None

# Função para verificar se o arquivo é suspeito
def verificar_arquivo_suspeito(caminho_arquivo):
    nome_arquivo = os.path.basename(caminho_arquivo).lower()
    print(f"Verificando: {nome_arquivo}")
    for palavra in PALAVRAS_SUSPEITAS:
        if palavra in nome_arquivo:
            print(f"Palavra suspeita encontrada: {palavra} em {nome_arquivo}")
            return True
    return False

# Função para mover o arquivo para quarentena
def mover_para_quarentena(caminho_arquivo):
    try:
        destino = "C:\\Zuzz\\quarentena"
        if not os.path.exists(destino):
            os.makedirs(destino)
        nome_arquivo = os.path.basename(caminho_arquivo)
        destino_arquivo = os.path.join(destino, nome_arquivo)
        os.rename(caminho_arquivo, destino_arquivo)
        print(f"Arquivo movido para quarentena: {destino_arquivo}")
        return destino_arquivo
    except Exception as e:
        print(f"Erro ao mover arquivo para quarentena: {e}")
        return None

# Função para mostrar a notificação via notificar.py (chamado por subprocess)
def mostrar_alerta(titulo, mensagem):
    try:
        # Chama notificar.py, que deve estar em C:\Zuzz\notificar.py
        subprocess.Popen(["python", "C:\\Zuzz\\notificar.py", titulo, mensagem])
        print(f"Notificação enviada: {titulo} - {mensagem}")
    except Exception as e:
        print(f"Erro ao enviar notificação: {e}")

# Classe para lidar com os eventos do sistema de arquivos
class MeuHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            print(f"Pasta criada: {event.src_path}")
            # Aqui você pode também adicionar lógica de notificação para pastas, se desejar
        else:
            print(f"Arquivo criado: {event.src_path}")
            if verificar_arquivo_suspeito(event.src_path):
                print(f"Arquivo suspeito detectado: {event.src_path}")
                hash_arquivo = calcular_hash_arquivo(event.src_path)
                if hash_arquivo:
                    print(f"Hash do arquivo: {hash_arquivo}")
                    destino = mover_para_quarentena(event.src_path)
                    if destino:
                        mostrar_alerta(
                            "⚠️ Alerta de Segurança!",
                            f"Arquivo suspeito detectado e movido para quarentena:\n{event.src_path}\nHash: {hash_arquivo}"
                        )
                    else:
                        print(f"Não foi possível mover para quarentena: {event.src_path}")
                else:
                    print(f"Erro ao calcular hash para: {event.src_path}")
            else:
                print(f"Arquivo não é suspeito: {event.src_path}")

# Função principal para iniciar o monitoramento
def iniciar_monitoramento():
    observer = Observer()
    handler = MeuHandler()
    for diretorio in DIRETORIOS:
        if os.path.exists(diretorio):
            print(f"Monitorando o diretório: {diretorio}")
            observer.schedule(handler, diretorio, recursive=True)
        else:
            print(f"Diretório não encontrado: {diretorio}")
    observer.start()
    try:
        print("🚨 Monitoramento iniciado. Aguardando eventos...")
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        print("🛑 Monitoramento encerrado.")
    observer.join()

if __name__ == "__main__":
    iniciar_monitoramento()
