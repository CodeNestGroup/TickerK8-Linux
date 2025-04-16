""" Import PyQt5 Widgets """
from PyQt5.QtWidgets import (
    QWidget, # Simple widget, window
    QPushButton, # Simple button
    QGridLayout, # Grid layout
    QSizePolicy # Size policy 
)
#______________________________________________________________________________________________________________________
""" Import PyQt5 Core """
from PyQt5.QtCore import (
    Qt # Qt settings
)
#______________________________________________________________________________________________________________________
""" Import PyQt5 Gui """
from PyQt5.QtGui import (
    QIcon # Icon
)
#######################################################################################################################
""" News widget """
def news_widget(self, content):
    """ Create objects """
    self.news_widget = QWidget(self.news_scroll)
    self.news_layout = QVboxLayout(self.news_widget)
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
        self.news_content_layout.setRowStretch(enc, 1)
        self.news_content_layout.setColumnStretch(enc, 1)
    self.news_content.setLayout(self.news_content_layout)
    self.news_source_layout.setSpacing(0)
    self.news_source_layout.setContentsMargins(0,0,0,0)
    for enc in range(100):
        self.news_source_layout.setRowStretch(enc, 1)
        self.news_source_layout.setColumnStretch(enc, 1)
    self.news_source_widget.setLayout(self.news_source_layout)
    self.news_hash_layout.setSpacing(0)
    self.news_hash_layout.setContentsMargins(0,0,0,0)
    for enc in range(100):
        self.news_hash_layout.setRowStretch(enc, 1)
        self.news_hash_layout.setColumnStretch(enc, 1)
    self.news_hash_widget.setLayout(self.news_hash_layout)
#______________________________________________________________________________________________________________________
    """ Set widget """
    self.news_scroll.setWidget(self.news_widget)
#______________________________________________________________________________________________________________________
    """ Set label """
    self.news_title_label.setAlignment(Qt.AlignCenter)
    self.news_date_label.setAlignment(Qt.AlignCenter)
#______________________________________________________________________________________________________________________
    """ Set size """
    self.news_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.news_photo_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.news_title_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.news_date_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.news_content_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.news_source_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.news_hash_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
#######################################################################################################################