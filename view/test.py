import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QRadioButton,
    QGroupBox,
    QPushButton,
    QGridLayout,
    QButtonGroup,
    QApplication,
    QTabWidget,
)


class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setStyleSheet("font: 15pt Tw Cen MT")

        self.data_tab = DataTab()
        self.analysis_tab = AnalysisTab()

        self.tabWidget = QTabWidget()
        self.tabWidget.addTab(self.data_tab, "Data Input")
        self.tabWidget.addTab(self.analysis_tab, "Analysis")

        layout = QVBoxLayout(self)
        layout.addWidget(self.tabWidget)

        self.data_tab.intervalRadioButton.toggled.connect(
            self.analysis_tab.analyzeIntervalButton.setEnabled
        )
        self.data_tab.ordinalRadioButton.toggled.connect(
            self.analysis_tab.analyzeOrdinalButton.setEnabled
        )
        self.data_tab.frequencyRadioButton.toggled.connect(
            self.analysis_tab.analyzeFrequencyButton.setEnabled
        )


class DataTab(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QGridLayout(self)
        self.intervalRadioButton = QRadioButton("Interval")
        self.ordinalRadioButton = QRadioButton("Ordinal")
        self.frequencyRadioButton = QRadioButton("Frequency")
        self.submitButton = QPushButton("Submit Data")
        layout.addWidget(self.intervalRadioButton, 7, 0, 1, 3)
        layout.addWidget(self.ordinalRadioButton, 8, 0, 1, 3)
        layout.addWidget(self.frequencyRadioButton, 9, 0, 1, 3)


class AnalysisTab(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.createChooseIntervalGroup()
        self.createChooseOrdinalGroup()
        self.createChooseFrequencyGroup()

        layout = QGridLayout(self)
        layout.addWidget(self.ChooseIntervalGroup, 0, 1)
        layout.addWidget(self.ChooseOrdinalGroup, 1, 1)
        layout.addWidget(self.ChooseFrequencyGroup, 2, 1)

    def createChooseIntervalGroup(self):
        self.ChooseIntervalGroup = QGroupBox("Tests for Interval Data")
        self.analyzeIntervalButton = QPushButton("Analyze")
        self.analyzeIntervalButton.setEnabled(False)
        layout = QGridLayout(self.ChooseIntervalGroup)
        layout.addWidget(self.analyzeIntervalButton, 1, 1)

    def createChooseOrdinalGroup(self):
        self.ChooseOrdinalGroup = QGroupBox("Tests for Ordinal Data")
        self.analyzeOrdinalButton = QPushButton("Analyze")
        self.analyzeOrdinalButton.setEnabled(False)
        layout = QGridLayout(self.ChooseOrdinalGroup)
        layout.addWidget(self.analyzeOrdinalButton, 1, 1)

    def createChooseFrequencyGroup(self):
        self.ChooseFrequencyGroup = QGroupBox("Tests for Frequency Data")
        self.analyzeFrequencyButton = QPushButton("Analyze")
        self.analyzeFrequencyButton.setEnabled(False)
        layout = QGridLayout(self.ChooseFrequencyGroup)
        layout.addWidget(self.analyzeFrequencyButton, 1, 1)


def run():
    app = QApplication(sys.argv)
    tabPage = Widget()
    tabPage.show()
    app.exec_()


run()