import sys
import time
import logging
import os
from rokit import start_process
from watchdog.observers import Observer
from watchdog.events import DirModifiedEvent, LoggingEventHandler, FileModifiedEvent

class RobloxLuau(LoggingEventHandler):
    def on_modified(self, event: DirModifiedEvent | FileModifiedEvent) -> None:
        if isinstance(event, DirModifiedEvent):
            return
        # log_folder = os.path.join(python_folder, "logs")
        # os.makedirs(log_folder,exist_ok=True)

        src_path: str = event.src_path.decode() if isinstance(event.src_path, bytes) else event.src_path
        dest_path: str = event.dest_path.decode() if isinstance(event.dest_path, bytes) else event.dest_path
        
        _, err, out, __ = start_process(["selene", src_path])
        if len(err) > 0:
            logging.error(f"\n{err}")
        if len(out) > 0:
            logging.info(f"\n{out}")
        _, err, out, __ = start_process(["stylua", src_path])
        if len(err) > 0:
            logging.error(f"\n{err}")
        if len(out) > 0:
            logging.info(f"\n{out}")
        

if __name__ == "__main__":
    # Modified from watchdog sample code
    python_folder = os.getcwd()
    source_folder = os.path.join(os.pardir,os.pardir,"src")
    
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = sys.argv[1] if len(sys.argv) > 1 else source_folder
    os.chdir(path)
    
    event_handler = RobloxLuau()
    observer = Observer()
    observer.schedule(event_handler, os.curdir, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()