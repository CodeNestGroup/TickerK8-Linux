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
    def __init__(self):
        super().__init__()
        self.backup_path = str(pathlib.Path(__file__).resolve().parents[4])
        self.main_path = str(pathlib.Path(__file__).resolve().parents[3])
        self.update_folder = None
        self.update_json_file_list = None
        self.zip_buffer = io.BytesIO()

    def run(self):
        self.backup()
        time.sleep(0.2)
        self.download()
        time.sleep(0.2)
        #self.un_zip()
        #time.sleep(0.2)
        #self.update_compatibility()
        #time.sleep(0.2)
        #self.install()
        #time.sleep(0.2)
        #self.delete_backup()
        #time.sleep(0.2)
        #self.restart()

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
            if os.path.exists(b):
                shutil.rmtree(b)


    def download(self):
        try:
            self.progress.emit(1)
            chunk_size = 8192
            downloaded = 0
            total_length = 533*1024*1024
            headers = {}
            while True:
                try:
                    if downloaded > 0:
                        headers['Range'] = f'bytes={downloaded}-'
                    response = requests.get(self.url, stream=True, timeout=10, headers=headers)
                    response.raise_for_status()
                    self.progress_index.emit(1)
                    chunk_generator = response.iter_content(chunk_size=chunk_size)
                    for chunk in chunk_generator: 
                        if not chunk:
                            continue
                        self.zip_buffer.write(chunk)
                        downloaded += len(chunk)
                        self.progress_index.emit(1)
                        self.progress_bar_value.emit(int((downloaded / total_length) * 100))
                        time.sleep(len(chunk) / (self.set_speed(self.main_self.settings_config_file['__capacity__']) * 1024))
                    break
                except (requests.RequestException, ConnectionError, TimeoutError):
                    self.progress_index.emit(11)
                    time.sleep(3)
        except Exception:
            print(f"{Exception} \n {traceback.format_exc()}", headers)
            self.progress_index.emit(10)
            if os.path.exists(self.backup_folder):
                shutil.rmtree(self.backup_folder)
            if self.zip_buffer:
                self.zip_buffer.seek(0)
                self.zip_buffer.truncate(0)
            raise

    def un_zip(self):
        try:
            self.progress_index.emit(2)
            with zipfile.ZipFile(self.zip_buffer, 'r') as zip_ref:
                self.update_folder = f'/{zip_ref.namelist()[0]}'
                list_files = zip_ref.namelist()
                total_files = len(list_files)
                extracted_files = 0 
                for file in list_files:
                    zip_ref.extract(file, self.main_self.main_path)
                    extracted_files += 1 
                    self.progress_bar_value.emit(int((extracted_files/total_files)*100))
                self.progress_bar_value.emit(100)
                self.zip_buffer.seek(0)
                self.zip_buffer.truncate(0)
        except:
            self.progress_index.emit(10)
            if os.path.exists(self.backup_folder):
                shutil.rmtree(self.backup_folder)
            if self.zip_buffer:
                self.zip_buffer.seek(0)
                self.zip_buffer.truncate(0)
            if os.path.exists(self.main_self.main_path+self.update_folder):
                shutil.rmtree(self.main_self.main_path+self.update_folder)
            raise

    def update_compatibility(self):
        try:
            self.progress_index.emit(3)
            self.update_json_file_list = json.load(open(self.main_self.main_path+self.update_folder+'TickerK8_updater/APP_FILES/CONFIG/_04_settings_app_file_list.json', 'r'))
            total_files = len(self.update_json_file_list)
            checked_file = 0 
            for file, check_sum in self.update_json_file_list.items():
                if os.path.exists(self.main_self.main_path+self.update_folder[:-1]+file):
                    if check_sum != 'config':
                        if check_sum != self.main_self.controller_update.calculate_sha256(self.main_self.main_path+self.update_folder[:-1]+file):
                            raise
                        checked_file += 1
                        self.progress_bar_value.emit(int((checked_file/total_files)*100))
            self.progress_bar_value.emit(100) 
        except:
            self.progress_index.emit(10)
            if os.path.exists(self.backup_folder):
                shutil.rmtree(self.backup_folder)
            if os.path.exists(self.main_self.main_path+self.update_folder): 
                shutil.rmtree(self.main_self.main_path+self.update_folder)
            raise

    def install(self):
        try:
            self.progress_index.emit(4) 
            total_files = len(self.update_json_file_list) 
            installed_files = 0
            for path, check_sum in self.update_json_file_list.items():
                installed_files += 1
                self.progress_bar_value.emit(int((installed_files / total_files) * 100))
                if os.path.exists(self.main_self.main_path+path):
                    if self.main_self.settings_app_file_list_file[path] == check_sum: 
                        continue
                shutil.copy(self.main_self.main_path+self.update_folder[:-1]+path, self.main_self.main_path+path) 
            for path in self.main_self.settings_app_file_list_file.keys():
                if path not in self.update_json_file_list.keys():
                    os.remove(self.main_self.main_path+path) 
            shutil.copy(self.main_self.main_path+self.update_folder[:-1]+'/TickerK8_updater/APP_FILES/CONFIG/_04_settings_app_file_list.json', self.main_self.main_path+'/TickerK8_updater/APP_FILES/CONFIG/_04_settings_app_file_list.json')
            self.progress_bar_value.emit(100)
            self.main_self.settings_app_file_list_file = json.load(open(self.main_self.main_path + '/TickerK8_updater/APP_FILES/CONFIG/_04_settings_app_file_list.json','r'))
            shutil.rmtree(self.main_self.main_path + self.update_folder[:-1])
            self.main_self.controller_update.check_compatibility()
        except:
            self.progress_index.emit(10)
            if os.path.exists(self.backup_folder):
                self.restore_backup()
            if os.path.exists(self.main_self.main_path+self.update_folder): 
                shutil.rmtree(self.main_self.main_path+self.update_folder)
            raise

    def delete_backup(self):
        self.progress_index.emit(5)
        if os.path.exists(self.backup_folder):
            shutil.rmtree(self.backup_folder)

    def restart(self):
        self.progress_index.emit(6)


    def restore_backup(self):
        for item in os.listdir(self.backup_folder):
            source_item = os.path.join(self.main_self.main_path, item)
            backup_item = os.path.join(self.backup_folder, item)
            if os.path.exists(source_item):
                if os.path.isdir(source_item):
                    shutil.rmtree(source_item)
                else:
                    os.remove(source_item) 
            if os.path.isdir(backup_item): 
                shutil.copytree(backup_item, source_item) 
            else:
                shutil.copy2(backup_item, source_item)
        if os.path.exists(self.backup_folder):
            shutil.rmtree(self.backup_folder)

    def set_speed(self, index):
        try: 
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
        except Exception:
            self.main_self.controller_report.write_log(f"{Exception} \n {traceback.format_exc()}")
            self.main_self.alert_text_label.setText(self.main_self.settings_translate_file['alert_text_label'][self.main_self.settings_config_file['__language__']][0])
            self.main_self.controller_alert.open()