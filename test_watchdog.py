from watchdog.observers import Observer # type: ignore
from watchdog.events import FileSystemEventHandler # type: ignore
import time

class TestHandler(FileSystemEventHandler):
    def on_created(self, event):
        print(f"Arquivo criado: {event.src_path}")

monitor_folder = r"C:\Users\jovana\Documents"

event_handler = TestHandler()
observer = Observer()
observer.schedule(event_handler, monitor_folder, recursive=True)
observer.start()

print(f"Monitorando a pasta: {monitor_folder}...")

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()
