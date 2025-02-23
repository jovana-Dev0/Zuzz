import logging
import time
import win32serviceutil # type: ignore
import win32service # type: ignore
import win32event # type: ignore
import os
from watchdog.observers import Observer # type: ignore
from watchdog.events import FileSystemEventHandler # type: ignore
from win10toast import ToastNotifier # type: ignore

# Configuração do logger
logging.basicConfig(
    filename="C:\\Zuzz\\zuzz.log",  # Caminho onde o arquivo de log será armazenado
    level=logging.DEBUG,  # Nível de log
    format="%(asctime)s - %(levelname)s - %(message)s"  # Formato da mensagem de log
)

class ZuzzService(win32serviceutil.ServiceFramework):
    _svc_name_ = 'Zuzz'
    _svc_display_name_ = 'Zuzz Security Service'
    
    def __init__(self, args):
        win32serviceutil.ServiceFramework.__init__(self, args)
        self.stop_event = win32event.CreateEvent(None, 0, 0, None)
        logging.info("Zuzz Service Inicializado")

    def SvcStop(self):
        self.reportServiceStatus(win32service.SERVICE_STOP_PENDING)
        logging.info("Zuzz Service Parando")
        win32event.SetEvent(self.stop_event)

    def SvcDoRun(self):
        logging.info("Zuzz Service Iniciado")
        
        # Monitoramento de arquivos
        self.monitor_files()
        
    def monitor_files(self):
        # Diretório que será monitorado
        path_to_watch = "C:\\Zuzz\\"
        
        event_handler = FileSystemEventHandler()
        
        # Função para tratar eventos de modificação de arquivo
        def on_modified(event):
            logging.info(f"Arquivo modificado: {event.src_path}")
            toaster = ToastNotifier()
            toaster.show_toast("Zuzz Alert", f"Arquivo modificado: {event.src_path}", duration=10)
        
        event_handler.on_modified = on_modified

        observer = Observer()
        observer.schedule(event_handler, path=path_to_watch, recursive=False)
        observer.start()

        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            observer.stop()

        observer.join()


if __name__ == '__main__':
    win32serviceutil.HandleCommandLine(ZuzzService)
