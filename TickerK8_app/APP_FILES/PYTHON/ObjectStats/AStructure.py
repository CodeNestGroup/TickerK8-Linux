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
    def __init__(self, parent, s, t, i):
        super().__init__(parent)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.Path = s.Path
        self.Theme = s.Theme
        self.Language = s.Language
        if t == 'country':
                self.Country()
        elif t == 'market':
                self.Market()
        elif t == 'stock':
                self.Stock()
        print(t, i)
    def Country(self):
        pass

    def Market(self):
#           --- Create objects ---
        self.WidgetW = QWidget(self)
        self.LayoutL = QGridLayout(self.WidgetW)
#           --- 

    def Stock(self):
#           --- Create objects ---
        self.WidgetW = QWidget(self)
        self.LayoutL = QGridLayout(self.WidgetW)
#           --- Fundamental Data ---
        self.FundamentalDataTitleL = QLabel(self)
        self.IndicatorsSubTitleL = QLabel(self)
        self.MarketCapNameL = QLabel(self)
        self.MarketCapValueL = QLabel(self)
        self.PENameL = QLabel(self)
        self.PEValueL = QLabel(self)
        self.ForwardPENameL = QLabel(self)
        self.ForwardPEValueL = QLabel(self)
        self.PEGNameL = QLabel(self)
        self.PEGValueL = QLabel(self)
        self.PBNameL = QLabel(self)
        self.PBValueL = QLabel(self)
        self.PSNameL = QLabel(self)
        self.PSValueL = QLabel(self)
#           --- Profitability --- 
        self.ProfitabilitySubTitleL = QLabel(self)
        self.ROENameL = QLabel(self)
        self.ROEValueL = QLabel(self)
        self.ROANameL = QLabel(self)
        self.ROAValueL = QLabel(self)
        self.ROINameL = QLabel(self)
        self.ROIValueL = QLabel(self)
        self.NetMarginNameL = QLabel(self)
        self.NetMarginValueL = QLabel(self)
        self.OperatingMarginNameL = QLabel(self)
        self.OperatingMarginValueL = QLabel(self)
        self.GrossMarginNameL = QLabel(self)
        self.GrossMarginValueL = QLabel(self)
#           --- Balance --- 
        self.BalanceSubTitleL = QLabel(self)
        self.AssetsNameL = QLabel(self)
        self.AssetsValueL = QLabel(self)
        self.LiabilitiesNameL = QLabel(self)
        self.LiabilitiesValueL = QLabel(self)
        self.EquityNameL = QLabel(self)
        self.EquityValueL = QLabel(self)
        self.CashNameL = QLabel(self)
        self.CashValueL = QLabel(self)
        self.DebtNameL = QLabel(self)
        self.DebtValueL = QLabel(self)
#           --- Financial Reports ---
        self.FinancialReportsTitleL = QLabel(self)
        self.IncomeStatementSubTitleL = QLabel(self)
        self.RevenueNameL = QLabel(self)
        self.RevenueValueL = QLabel(self)
        self.GrossProfitNameL = QLabel(self)
        self.GrossProfitValueL = QLabel(self)
        self.OperatingIncomeNameL = QLabel(self)
        self.OperatingIncomeValueL = QLabel(self)
        self.NetIncomeNameL = QLabel(self)
        self.NetIncomeValueL = QLabel(self)
        self.EPSIncomeNameL = QLabel(self)
        self.EPSIncomeValueL = QLabel(self)
#           --- Balance Sheet ---
        self.BalanceSheetSubTitleL = QLabel(self)
        self.TotalAssetsNameL = QLabel(self)
        self.TotalAssetsValueL = QLabel(self)
        self.TotalLiabilitiesNameL = QLabel(self)
        self.TotalLiabilitiesValueL = QLabel(self)
        self.ShareholderEqulityNameL = QLabel(self)
        self.ShareholderEqulityValueL = QLabel(self)
#           --- Cash Flow --- 
        self.CashFlowSubTitleL = QLabel(self)
        self.OperatingCashFlowNameL = QLabel(self)
        self.OperatingCashFlowValueL = QLabel(self)
        self.InvestingCashFlowNameL = QLabel(self)
        self.InvestingCashFlowValueL = QLabel(self)
        self.FinancingCashFlowNameL = QLabel(self)
        self.FinancingCashFlowValueL = QLabel(self)
        self.FreeCashFlowNameL = QLabel(self)
        self.FreeCashFlowValueL = QLabel(self)
#           --- Dividend Data ---
        self.DividendDataSubTitleL = QLabel(self)
        self.DividendYieldNameL = QLabel(self)
        self.DividendYieldValueL = QLabel(self)
        self.DividendPerShareNameL = QLabel(self)
        self.DividendPerShareValueL = QLabel(self)
        self.PayoutRatioNameL = QLabel(self)
        self.PayoutRatioValueL = QLabel(self)
        self.DividendHistoryNameL = QLabel(self)
        self.DividendHistoryValueL = QLabel(self)
        self.ExDividendNameL = QLabel(self)
        self.ExDividendValueL = QLabel(self)
        self.PaymentDateNameL = QLabel(self)
        self.PaymentDateValueL = QLabel(self)
#           --- Corporation Data ---
        self.CorporationDataTitleL = QLabel(self)
        self.CorporateActionsSubTitleL = QLabel(self)
        self.StockSplitNameL = QLabel(self)
        self.StockSplitValueL = QLabel(self)
        self.ReverseSplitNameL = QLabel(self)
        self.ReverseSplitValueL = QLabel(self)
        self.MergersNameL = QLabel(self)
        self.MergersValueL = QLabel(self)
        self.AcquisitionsNameL = QLabel(self)
        self.AcquisitionsValueL = QLabel(self)
        self.BuyBacksNameL = QLabel(self)
        self.BuyBacksValueL = QLabel(self)
#           --- Events ---
        self.EventsSubTitleL = QLabel(self)
        self.EarningsDateNameL = QLabel(self)
        self.EarningsDateValueL = QLabel(self)
        self.AGMNameL = QLabel(self)
        self.AGMValueL = QLabel(self)
        self.InvestorDayNameL = QLabel(self)
        self.InvestorDayValueL = QLabel(self)
#           --- Ownership Data ---
        self.OwnershipDataTitleL = QLabel(self)
        self.ShareholdingSubTitleL = QLabel(self)
        self.InstitutionalOwnershipNameL = QLabel(self)
        self.InstitutionalOwnershipValueL = QLabel(self)
        self.InsiderOwnershipNameL = QLabel(self)
        self.InsiderOwnershipValueL = QLabel(self)
        self.TopShareholdersNameL = QLabel(self)
        self.TopShareholdersValueL = QLabel(self)
#           --- Insider Trading ---
        self.InsiderTradingSubTitleL = QLabel(self)
        self.InsiderBuysNameL = QLabel(self)
        self.InsiderBuysValueL = QLabel(self)
        self.InsiderSellsNameL = QLabel(self)
        self.InsiderSellsValueL = QLabel(self)
#           --- Analitical Data ---
        self.AnaliticalDataTitleL = QLabel(self)
        self.MovingAveragesNameL = QLabel(self)
        self.MovingAveragesValueL = QLabel(self)
        self.RSINameL = QLabel(self)
        self.RSIValueL = QLabel(self)
        self.MACDNameL = QLabel(self)
        self.MACDValueL = QLabel(self)
        self.BollingerBandsNameL = QLabel(self)
        self.BollingerBandsValueL = QLabel(self)
        self.MomentumNameL = QLabel(self)
        self.MomentumValueL = QLabel(self)
        self.VolatillityNameL = QLabel(self)
        self.VolatillityValueL = QLabel(self)
#           --- ESG Data ---
        self.ESGDataTitleL = QLabel(self)
        self.ESGScoreNameL = QLabel(self)
        self.ESGScoreValueL = QLabel(self)
        self.EnvironmentalScoreNameL = QLabel(self)
        self.EnvironmentalScoreValueL = QLabel(self)
        self.GovernanceScoreNameL = QLabel(self)
        self.GovernanceScoreValueL = QLabel(self)
#           --- Call functions ---
        StockUi(self)
        StockReloadStyle(self)
        StockRetranslate(self)
#           --- Connect functions ---
