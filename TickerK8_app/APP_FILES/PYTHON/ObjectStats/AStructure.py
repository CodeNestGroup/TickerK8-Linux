#   --- Import ---
import json
from PyQt5.QtWidgets import (
    QWidget,
    QPushButton,
    QLabel, 
    QScrollArea,
    QGridLayout
)
from PyQt5.QtCore import (
    Qt
)
from .AUi import *
from .ALogic import *

#   --- Class ---
class ObjectStatsS(QScrollArea): 
    def __init__(self, parent, s):
        super().__init__(parent)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.Path = s.Path
        self.Theme = s.Theme
        self.Language = s.Language

    def Country(self):
        pass

    def Market(self):
        pass

    def Stock(self):
#           --- Create objects ---
        self.Widget = QWidget(self)
        self.Layout = QGridLayout(self.Widget)
        self.TitleL = QLabel(self.Widget)

        self.FundamentalDataTitleL = QLabel(self)

        self.IndicatorsSubTitleL = QLabel(self)
        self.MarketCapNameL
        self.MarketCapValueL
        self.PENameL
        self.PEValueL
        self.ForwardPENameL
        self.ForwardPEValueL
        self.PEGNameL
        self.PEGValueL
        self.PBNameL
        self.PBValueL
        self.PSNameL
        self.PSValueL
        
        self.ProfitabilitySubTitleL = QLabel(self)
        self.ROENameL
        self.ROEValueL
        self.ROANameL
        self.ROAValueL
        self.ROINameL
        self.ROIValueL
        self.NetMarginNameL
        self.NetMarginValueL
        self.OperatingMarginNameL
        self.OperatingMarginValueL
        self.GrossMarginNameL
        self.GrossMarginValueL

        self.BalanceSubTitleL = QLabel(self)
        self.AssetsNameL
        self.AssetsValueL
        self.LiabilitiesNameL
        self.LiabilitiesValueL
        self.EquityNameL
        self.EquityValueL
        self.CashNameL
        self.CashValueL
        self.DebtNameL
        self.DebtValueL

        self.FinancialReportsTitleL = QLabel(self)

        self.IncomeStatementSubTitleL = QLabel(self)
        self.RevenueNameL
        self.RevenueValueL
        self.GrossProfitNameL
        self.GrossProfitValueL
        self.OperatingIncomeNameL
        self.OperatingIncomeValueL
        self.NetIncomeNameL
        self.NetIncomeValueL
        self.EPSIncomeNameL
        self.EPSIncomeValueL

        self.BalanceSheetSubTitleL = QLabel(self)
        self.TotalAssetsNameL
        self.TotalAssetsValueL
        self.TotalLiabilitiesNameL
        self.TotalLiabilitiesValueL
        self.ShareholderEqulityNameL
        self.ShareholderEqulityValueL

        self.CashFlowSubTitleL = QLabel(self)
        self.OperatingCashFlowNameL
        self.OperatingCashFlowValueL
        self.InvestingCashFlowNameL
        self.InvestingCashFlowValueL
        self.FinancingCashFlowNameL
        self.FinancingCashFlowValueL
        self.FreeCashFlowNameL
        self.FreeCashFlowValueL

        self.DividendDataSubTitleL = QLabel(self)
        self.DividendYieldNameL
        self.DividendYieldValueL
        self.DividendPerShareNameL
        self.DividendPerShareValueL
        self.PayoutRatioNameL
        self.PayoutRatioValueL

        
#           --- Call functions ---
        StockUi(self)
        StockReloadStyle(self)
        StockRetranslate(self)
#           --- Connect functions ---




