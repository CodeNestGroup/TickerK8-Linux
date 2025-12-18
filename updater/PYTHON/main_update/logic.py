""" Import packages """
import os
import sys
import shutil
import subprocess
import traceback
import socket
import json 
import io 
import zipfile
import urllib.request
import requests
import hashlib
import pathlib
import time
""" Import PyQT5 packages """
from PyQt5.QtCore import (
    QTimer,
    QThread,
    pyqtSignal
)
#______________________________________________________________________________________________________________________
    
def loading_thread(self):
    self.timer = QTimer(self)
    self.timer.timeout.connect(lambda: update_label(self))
    self.timer.start(500)
#______________________________________________________________________________________________________________________

def update_label(self):
    t = self.dots_label.text()
    l = len(t)
    if l < 5:
        self.dots_label.setText(t+'.')
    else:
        self.dots_label.setText('.')
#______________________________________________________________________________________________________________________

def load_text(self):
    self.text = json.load(open(self.main_path+'/CONFIG/main_update/updating_translate.json', 'r'))
    self.language = json.load(open(self.main_path+'/CONFIG/GLOBAL/global_config.json', 'r'))['language']
#______________________________________________________________________________________________________________________
# Zamiania całego folderu, pobraniu configu z backupu

class controller_download(QThread):
    progress = pyqtSignal(int)
    """
    0 - Creating backup
    1 - Downloading
    10 - Error 
    """
    progress_bar_value = pyqtSignal(int)
    """ Init, creating items, set base variables like paths, screen size, etc. """
    def __init__(self, url):
        super().__init__()
        self.backup_path = str(pathlib.Path(__file__).resolve().parents[4])
        self.main_path = str(pathlib.Path(__file__).resolve().parents[3])
        self.capacity = self.set_speed(json.load(open(self.main_path+'/updater/CONFIG/GLOBAL/global_config.json', 'r'))['capacity'])
        self.url = url
        self.update_folder = None
        self.update_json_file_list = None
        self.zip_buffer = io.BytesIO()

    def run(self):
        self.backup()
        time.sleep(0.2)
        self.download()
        time.sleep(0.2)
        self.un_zip()
        time.sleep(0.2)
        self.update_compatibility()
        time.sleep(0.2)
        self.install()
        time.sleep(0.2)
        self.delete_backup()
        time.sleep(0.2)
        self.restart()

    def backup(self):
        try:
            self.progress.emit(0)
            self.progress_bar_value.emit(0)
            b = os.path.join(self.backup_path, '.backup')
            m = self.main_path
            i = len(os.listdir(m))
            j = 0
            if not os.path.exists(b):
                os.mkdir(b)
                for item in os.listdir(m):
                    if item == '.backup':
                        continue
                    source_item = os.path.join(m, item)
                    backup_item = os.path.join(b, item)
                    if os.path.isdir(source_item):
                        shutil.copytree(source_item, backup_item)
                    else:
                        shutil.copy2(source_item, backup_item)
                    j += 1
                    self.progress_bar_value.emit(int((j/i)*100))
            self.progress_bar_value.emit(100)
        except:
            self.progress.emit(6)
            if os.path.exists(self.backup_path+'/.backup'):
                shutil.rmtree(self.backup_path+'/.backup')


    def download(self):
        try:
            self.progress.emit(1)
            self.progress_bar_value.emit(0)
            c = 8192
            d = 0
            h = {}
            while True:
                try:
                    if d > 0:
                        h['Range'] = f'bytes={d}-'
                    r = requests.get(self.url, stream=True, timeout=10, headers=h)
                    r.raise_for_status()
                    chunk_generator = r.iter_content(chunk_size=c)
                    for chunk in chunk_generator: 
                        if not chunk:
                            continue
                        self.zip_buffer.write(chunk)
                        d += len(chunk)
                        time.sleep(len(chunk) / self.capacity*1024)
                    break
                    self.progress_bar_value.emit(100)
                except (requests.RequestException, ConnectionError, TimeoutError):
                    self.progress.emit(7)
                    time.sleep(3)
        except Exception:
            self.progress.emit(6)
            if os.path.exists(self.backup_path+'/.backup'):
                shutil.rmtree(self.backup_path+'/.backup')
            if self.zip_buffer:
                self.zip_buffer.seek(0)
                self.zip_buffer.truncate(0)

    def un_zip(self):
        try:
            self.progress.emit(2)
            self.progress_bar_value.emit(0)
            with zipfile.ZipFile(self.zip_buffer, 'r') as zip_ref:
                self.update_folder = f'/{zip_ref.namelist()[0]}'
                l = zip_ref.namelist()
                t = len(l)
                e = 0 
                for file in l:
                    zip_ref.extract(file, self.backup_path)
                    e += 1 
                    self.progress_bar_value.emit(int((e/t)*100))
                self.progress_bar_value.emit(100)
                self.zip_buffer.seek(0)
                self.zip_buffer.truncate(0)
        except:
            self.progress.emit(6)
            if os.path.exists(self.backup_path+'/.backup'):
                shutil.rmtree(self.backup_path+'/.backup')
            if self.zip_buffer:
                self.zip_buffer.seek(0)
                self.zip_buffer.truncate(0)
            if os.path.exists(self.backup_path+self.update_folder):
                shutil.rmtree(self.backup_path+self.update_folder)

    def update_compatibility(self):
        try:
            self.progress.emit(3)
            self.progress_bar_value.emit(0)
            u = json.load(open(self.backup_path+self.update_folder+'/TickerK8_updater/APP_FILES/CONFIG/_04_settings_app_file_list.json', 'r'))
            t = len(u)
            c = 0 
            for file, check_sum in u.items():
                if os.path.exists(self.backup_path+self.update_folder+file):
                    if check_sum != 'config':
                        if check_sum != self.calculate_sha256(self.backup_path+self.update_folder+file):
                            raise
                        c += 1
                        self.progress_bar_value.emit(int((c/t)*100))
            self.progress_bar_value.emit(100) 
        except:
            self.progress.emit(6)
            if os.path.exists(self.backup_path+'/.backup'):
                shutil.rmtree(self.backup_path+'/.backup')
            if os.path.exists(self.backup_path+self.update_folder): 
                shutil.rmtree(self.backup_path+self.update_folder)
            raise

    def install(self):
        try:
            self.progress.emit(4) 
            self.progress_bar_value.emit(0)

            
            



            self.progress_bar_value.emit(100)
        except:
            self.progress.emit(6)
            if os.path.exists(self.backup_path+'/.backup'):
                self.restore_backup()
            if os.path.exists(self.backup_path+self.update_folder): 
                shutil.rmtree(self.backup_path+self.update_folder)
            raise

    def delete_backup(self):
        self.progress.emit(5)
        self.progress_bar_value.emit(0)
        if os.path.exists(self.backup_path+'.backup'):
            shutil.rmtree(self.backup_path+'.backup')
            self.progress_bar_value.emit(100)

    def restart(self):
        pass
#______________________________________________________________________________________________________________________

    def restore_backup(self):
        pass
        # Dodać przywracanie backupu 

    def calculate_sha256(self, file):
        sha256 = hashlib.sha256()
        f = open(file, "rb")
        while chunk := f.read(4096):
            sha256.update(chunk)
        return sha256.hexdigest()

    def set_speed(self, index):
        capacity = 0 
        if index == 0:
            capacity = 500
        elif index == 1:
            capacity = 1000
        elif index == 2:
            capacity = 2000
        elif index== 3:
            capacity = 5000
        elif index == 4:
            capacity = float('inf')
        return capacity
#______________________________________________________________________________________________________________________
