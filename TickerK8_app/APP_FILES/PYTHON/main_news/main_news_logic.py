""" Import """
import mysql
import json
import requests
from io import BytesIO
#______________________________________________________________________________________________________________________
""" Import PyQt5 Widgets """
from PyQt5.QtWidgets import (
    QWidget, # Simple widget, window
    QPushButton, # Simple button
    QLabel, 
    QGridLayout, # Grid layout
    QSizePolicy, # Size policy
    QVBoxLayout 
)
#______________________________________________________________________________________________________________________
""" Import PyQt5 Core """
from PyQt5.QtCore import (
    Qt # Qt settings
)
#______________________________________________________________________________________________________________________
""" Import PyQt5 Gui """
from PyQt5.QtGui import (
    QIcon, # Icon
    QPixmap
)
#######################################################################################################################
""" News widget """
def news_widget(self, id):
    """ Get data """
    connect = mysql.connector.connect(
        host = "localhost",
        user = "client",
        password = "Qwerty123456#",
        database = "TickerK8"
    )
    cursor = connect.cursor()
    cursor.execute(f'SELECT json_file FROM news WHERE id={id};')
    json_file = json.loads(cursor.fetchall()[0][0])
#______________________________________________________________________________________________________________________
    """ Create objects """
    self.news_widget = QWidget(self.news_scroll)
    self.news_layout = QVBoxLayout(self.news_widget)
    self.news_photo_label = QLabel(self.news_widget)
    self.news_title_label = QLabel(self.news_widget)
    self.news_date_label = QLabel(self.news_widget)
    self.news_content_widget = QWidget(self.news_widget)
    self.news_content_layout = QGridLayout(self.news_content_widget)
    self.news_source_widget = QWidget(self.news_widget)
    self.news_source_layout = QGridLayout(self.news_source_widget)
    self.news_hash_widget = QWidget(self.news_widget)
    self.news_hash_layout = QGridLayout(self.news_hash_widget)
    # trzeba dorobic ładowanie danych etc. 
#______________________________________________________________________________________________________________________
    """ Set layout """
    self.news_layout.addWidget(self.news_photo_label)
    self.news_layout.addWidget(self.news_title_label)
    self.news_layout.addWidget(self.news_date_label)
    self.news_layout.addWidget(self.news_content_widget)
    self.news_layout.addWidget(self.news_source_widget)
    self.news_layout.addWidget(self.news_hash_widget)
    self.news_layout.setSpacing(0)
    self.news_layout.setContentsMargins(0,0,0,0)
    self.news_widget.setLayout(self.news_layout)
    self.news_content_layout.setSpacing(0)
    self.news_content_layout.setContentsMargins(0,0,0,0)
    for enc in range(100):
        self.news_content_layout.setColumnStretch(enc, 1)
    self.news_content_widget.setLayout(self.news_content_layout)
    self.news_source_layout.setSpacing(0)
    self.news_source_layout.setContentsMargins(0,0,0,0)
    for enc in range(100):
        self.news_source_layout.setColumnStretch(enc, 1)
    self.news_source_widget.setLayout(self.news_source_layout)
    self.news_hash_layout.setSpacing(0)
    self.news_hash_layout.setContentsMargins(0,0,0,0)
    for enc in range(100):
        self.news_hash_layout.setColumnStretch(enc, 1)
    self.news_hash_widget.setLayout(self.news_hash_layout)
#______________________________________________________________________________________________________________________
    """ Set widget """
    self.news_scroll.setWidget(self.news_widget)
#______________________________________________________________________________________________________________________
    """ Set label """
    self.news_title_label.setAlignment(Qt.AlignCenter)
    self.news_date_label.setAlignment(Qt.AlignLeft)
#______________________________________________________________________________________________________________________
    """ Set size """
    self.news_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.news_photo_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.news_title_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.news_date_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.news_content_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.news_source_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.news_hash_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
#______________________________________________________________________________________________________________________
    """ Set text """
    self.news_title_label.setText(json_file['title'])
    self.news_date_label.setText(json_file['date'])
#______________________________________________________________________________________________________________________
    """ Set photo """
    photo = requests.get(json_file['photo']['original'])
    photo.raise_for_status()
    pix = QPixmap()
    pix.loadFromData(BytesIO(photo.content).read())
    zoomed_pix = pix.scaled(self.news_photo_label.width(), self.news_photo_label.height(), Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)
    cropped_pix = zoomed_pix.copy(
        (zoomed_pix.width() - self.news_photo_label.width()) // 2,
        (zoomed_pix.height() - self.news_photo_label.height()) // 2,
        self.news_photo_label.width(),
        self.news_photo_label.height()
    )
    self.news_photo_label.setPixmap(cropped_pix)
#______________________________________________________________________________________________________________________
    """ Make content """
    for index, rows in enumerate(json_file['content'], start=0):
        label = QLabel(self.news_content_widget)
        label.setObjectName(f'news_content_label_{index}')
        label.setText(rows[3])
        label.setWordWrap(True)
        label.setStyleSheet(rows[1])
        if rows[0] == 'Plain_Text':
            label.setObjectName(f"Plain_Text_{index}")
            label.setAlignment(Qt.AlignLeft)
        elif rows[0] == 'Title_Text':
            label.setObjectName(f"Title_Text_{index}")
            label.setAlignment(Qt.AlignCenter)
        elif rows[0] == 'Heading_1_Text':
            label.setObjectName(f"Heading_1_Text_{index}")
            label.setAlignment(Qt.AlignLeft)
        elif rows[0] == 'Heading_2_Text':
            label.setObjectName(f"Heading_2_Text_{index}")
            label.setAlignment(Qt.AlignLeft)
        elif rows[0] == 'Heading_3_Text':
            label.setObjectName(f"Heading_3_Text_{index}")
            label.setAlignment(Qt.AlignLeft)
        elif rows[0] == 'Heading_4_Text':
            label.setObjectName(f"Heading_4_Text_{index}")
            label.setAlignment(Qt.AlignLeft)
        self.news_content_layout.addWidget(label, index, 0, 1, 100)
#______________________________________________________________________________________________________________________
    """ Make source """
    for index, rows in enumerate(json_file['source'], start=0):
        button = QPushButton(self.news_source_widget)
        button.setObjectName(f'news_source_button_{index}')
        button.setText(str(rows))
        self.news_source_layout.addWidget(button, index, 0, 1, 100)
#______________________________________________________________________________________________________________________
    """ Make hash """
    for index, rows in enumerate(json_file['hash'], start=0):
        button = QPushButton(self.news_hash_widget)
        button.setObjectName(f'news_hash_button_{index}')
        button.setText(str(rows))
        self.news_hash_layout.addWidget(button, index, 0, 1, 100)
#######################################################################################################################