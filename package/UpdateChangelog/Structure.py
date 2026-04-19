#   --- Import PySide6 ---
from PySide6.QtWidgets import (
    QWidget,
    QScrollArea,
    QLabel,
    QPushButton,
    QGridLayout,
    QVBoxLayout
)
#   --- Import UpdateChangelog modules ---
from .Ui import *
from .Logic import *


#   --- UpdateChangelogW ---

class UpdateChangelogW(QWidget):
    def __init__(self, parent, data=None):
        super().__init__(parent)
#           --- Set ---
        self.setAttribute(Qt.WA_StyledBackground, True)
#           --- Get data from parent [ core ] ---
        self.Path = parent.Path
        self.Theme = parent.Config['theme']
        self.Language = parent.Config['language']
        if not data:
            data = json.load(open(self.Path+'/assets/JSON/Changelog.json', 'r', encoding='utf-8'))
        self.ChangelogData = data
#           --- Create objects ---
        self.Layout = QGridLayout(self)
        self.TitleL = QLabel(self)
        self.ChangelogS = QScrollArea(self)
        self.ChangelogW = QWidget(self.scroll)
        self.ChangelogL = QVBoxLayout(self.update_widget)
        self.ChangelogTitleL = QLabel(self.update_widget)
        self.ChangelogDateL = QLabel(self.update_widget)
        self.ChangelogTextL = QLabel(self.update_widget)
        self.ExitB = QPushButton(self)
#           --- Call functions ---
        UpdateChangelogUi(self)
        UpdateChangelogReloadStyle(self)
        UpdateChangelogRetranslate(self)
#           --- Connect functions  ---
        self.ExitB.clicked.connect(parent.UpdateOpen)
