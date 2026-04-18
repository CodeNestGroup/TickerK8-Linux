#   --- Import ---
import json 
import sys
import os
import subprocess
import pathlib
import io
import shutil
import zipfile
import urllib.request
import requests
import hashlib
import time
from datetime import datetime
#   --- Import PySide6 ---
from PySide6.QtWidgets import (
    QLabel,
    QPushButton,
    QSizePolicy
)
from PySide6.QtCore import (
    QUrl,
    QThread,
    Signal
)
from PySide6.QtGui import (
    QDesktopServices
)

def OpenLink(u):
    try:
        QDesktopServices.openUrl(QUrl(u))
    except:
        pass

def DotsUpdate(self):
    t = self.ChaneglogDotsL.text()
    l = len(t)
    if l < 14:
        self.ChaneglogDotsL.setText(t+'.')
    else:
        self.ChaneglogDotsL.setText('.')

def ResetFuncInfo(self):
    if self.FuncB:
        self.FuncB.deleteLater()
        self.FuncB = None
    if self.InfoL:
        self.InfoL.deleteLater()
        self.InfoL = None

class GetReleasesT(QThread):
        Finished = Signal(list)
        def __init__(self):
            super().__init__()
            self.start()

        def run(self):
            r = urllib.request.urlopen('https://api.github.com/repos/CodeNestGroup/TickerK8-Linux/releases')
            self.Finished.emit(json.loads(r.read().decode()))

def ChangelogConnectionSetup(self, r):
    GithubVersion = r[0]['published_at']
    LocalVersion = json.load(open(self.main_path+'/assets/JSON/changelog.json', 'r', encoding='utf-8'))['published_at']
    GithubTime = datetime.fromisoformat(GithubVersion.replace("Z", "+00:00"))
    LocalTime = datetime.fromisoformat(LocalVersion.replace("Z", "+00:00"))
    ResetFuncInfo(self)
    self.FuncB = QPushButton(self)
    self.FuncB.setObjectName('FuncB')
    self.FuncB.setProperty('class', 'Button')
    self.Layout.addWidget(self.FuncB, 91, 51, 9, 48)
    self.FuncB.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    l = self.Language
    t = json.load(open(f'{self.Path}/assets/UpdateTranslate.json', 'r', encoding='utf-8'))
    if GithubTime <= LocalTime:
        self.FuncB.clicked.connect(self.LoginOpenF)
        self.FuncB.setText(t['FuncB'][0][l])
    elif GithubTime > LocalTime:
        self.FuncB.clicked.connect(lambda: StartUpdate(self))
        self.FuncB.setText(t['FuncB'][1][l])

    # Dorobić guziki XD

def StartUpdate(self):
    ResetFuncInfo(self)
    self.ControllerDownloadT = ControllerDownload(self)
    self.ControllerDownloadT.Progress.connect(self.InfoL.setText)
    self.ControllerDownloadT.start()

#   --- ControllerDownload ---

class ControllerDownload(QThread):
    Progress = Signal(str)
    """
    2 - Creating backup
    3 - Downloading
    4 - Un zip 
    5 - Check update compatibility
    6 - Install 
    7 - Delete backup 
    8 - Error
    0 - No connection  

    Init, creating items, set base variables like paths, screen size, etc. """
    def __init__(self, parent):
        super().__init__(parent)
        self.BackupPath = 'Dorobić ścieżke do bezpiecznej lokalizacji'
        self.Path = parent.Path
        self.UpdateFolder = None
        self.UpdateJsonFileList = None
        self.ZipBuffer = io.BytesIO()
        self.t = json.load(open(self.Path+'/assets/JSON/UpdateTranslate.json', 'r', encoding='utf-8'))
        self.l = parent.Language

    def run(self):
        self.Backup()
        time.sleep(0.2)
        self.Download()
        time.sleep(0.2)
        self.UnZip()
        time.sleep(0.2)
        self.UpdateCompatibility()
        time.sleep(0.2)
        self.Install()
        time.sleep(0.2)
        self.DeleteBackup()
        time.sleep(0.2)
        self.Restart()

    def Backup(self):
        try:
            self.Progress.emit(self.t['InfoL'][2][self.l])
            n = self.Path[-(len(self.Path)-len(self.BackupPath)):]
            b = self.BackupPath+f'/.backup{n}'
            m = self.BackupPath+n
            if os.path.exists(b):
                shutil.rmtree(b)
            shutil.copytree(m, b)
        except:
            self.Progress.emit(self.t['InfoL'][8][self.l])
            if os.path.exists(self.BackupP+'/.backup'):
                shutil.rmtree(self.BackupP+'/.backup')

    def Download(self):
        try:
            self.Progress.emit(self.t['InfoL'][3][self.l])
            r = urllib.request.urlopen('https://api.github.com/repos/CodeNestGroup/TickerK8-Linux/releases/latest')
            u = json.loads(r.read().decode())['zipball_url']
            c = 8192
            d = 0
            h = {}
            while True:
                try:
                    if d > 0:
                        h['Range'] = f'bytes={d}-'
                    r = requests.get(u, stream=True, timeout=10, headers=h)
                    r.raise_for_status()
                    ChunkGenerator = r.iter_content(chunk_size=c)
                    for chunk in ChunkGenerator: 
                        if not chunk:
                            continue
                        self.ZipBuffer.write(chunk)
                        d = len(chunk)
                    break
                except (requests.RequestException, ConnectionError, TimeoutError):
                    self.Progress.emit(self.t['InfoL'][0][self.l])
                    time.sleep(3)
        except Exception:
            self.Progress.emit(self.t['InfoL'][8][self.l])
            if os.path.exists(self.BackupP+'/.backup'):
                shutil.rmtree(self.BackupP+'/.backup')
            if self.ZipBuffer:
                self.ZipBuffer.seek(0)
                self.ZipBuffer.truncate(0)

    def UnZip(self):
        try:
            self.Progress.emit(self.t['InfoL'][4][self.l])
            with zipfile.ZipFile(self.ZipBuffer, 'r') as zip_ref:
                self.UpdateFolder = f'/{zip_ref.namelist()[0]}'
                l = zip_ref.namelist()
                t = len(l)
                for file in l:
                    zip_ref.extract(file, self.BackupPath)
                self.ZipBuffer.seek(0)
                self.ZipBuffer.truncate(0)
        except:
            self.Progress.emit(self.t['InfoL'][8][self.l])
            if os.path.exists(self.BackupPath+'/.backup'):
                shutil.rmtree(self.BackupPath+'/.backup')
            if self.ZipBuffer:
                self.ZipBuffer.seek(0)
                self.ZipBuffer.truncate(0)
            if os.path.exists(self.BackupPath+self.UpdateFolder):
                shutil.rmtree(self.BackupPath+self.UpdateFolder)

    def update_compatibility(self):
        try:
            self.Progress.emit(self.t['InfoL'][5][self.l])
            u = json.load(open(self.BackupPath+self.UpdateFolder+'/assets/JSON/AppFileList.json', 'r', encoding='utf-8'))
            t = len(u)
            for file, check_sum in u.items():
                if os.path.exists(self.BackupPath+self.UpdateFolder+file):
                    if check_sum != 'config':
                        if check_sum != self.calculate_sha256(self.BackupPath+self.UpdateFolder+file):
                            raise
        except:
            self.Progress.emit(self.t['InfoL'][8][self.l])
            if os.path.exists(self.BackupPath+'/.backup'):
                shutil.rmtree(self.BackupP+'/.backup')
            if os.path.exists(self.BackupPath+self.UpdateFolder): 
                shutil.rmtree(self.BackupPath+self.UpdateFolder)

    def install(self):
        try:
            self.Progress.emit(self.t['InfoL'][6][self.l]) 
            n = self.Path[-(len(self.Path)-len(self.BackupPath)):]
            m = self.Path
            b = self.BackupPath
            u = b+self.UpdateFolder
            s1 = b+f'/.backup{n}/assets/JSON/ConfigOffline.json'
            d1 = u+'/assets/JSON/ConfigOffline.json'
            shutil.copy2(s1, d1)
            for r, d, f in os.walk(u):
                rp = os.path.relpath(r, u)
                t = os.path.join(m, rp)
                os.makedirs(t, exist_ok=True)
                for file in f:
                    src_file = os.path.join(r, file)
                    dst_file = os.path.join(t, file)
                    shutil.copy2(src_file, dst_file)
        except:
            self.Progress.emit(self.t['InfoL'][8][self.l])
            if os.path.exists(self.BackupPath+'/.backup'):
                self.RestoreBackup()
            if os.path.exists(self.BackupPath+self.UpdateFolder): 
                shutil.rmtree(self.BackupPath+self.UpdateFolder)

    def DeleteBackup(self):
        self.Progress.emit(self.t['InfoL'][7][self.l])
        if os.path.exists(self.BackupPath+self.UpdateFolder):
            shutil.rmtree(self.BackupPath+self.UpdateFolder)
        if os.path.exists(self.BackupPath+'/.backup'):
            shutil.rmtree(self.BackupPath+'/.backup')

    def Restart(self):
        subprocess.Popen(['/bin/bash', self.Path+'/Launcher.sh'])
        sys.exit(0)

    def RestoreBackup(self):
        n = self.Path[-(len(self.Path)-len(self.BackupPath)):]
        b = self.BackupPath+f'/.backup{n}'
        m = self.BackupPath+n
        if os.path.exists(m):
            shutil.rmtree(m)
        shutil.copytree(b, m)

    def calculate_sha256(self, file):
        sha256 = hashlib.sha256()
        f = open(file, "rb")
        while chunk := f.read(4096):
            sha256.update(chunk)
        return sha256.hexdigest()
        