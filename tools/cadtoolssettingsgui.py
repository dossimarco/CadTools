# -*- coding: utf-8 -*-
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from ui_cadtoolssettings import Ui_CadToolsSettings
import os, sys

class CadToolsSettingsGui(QDialog, Ui_CadToolsSettings):

    # btnSelectVertex_clicked = pyqtSignal()

    def __init__(self, parent):
        QDialog.__init__(self, parent)
        self.setupUi(self)
    
        self.settings = QSettings("CatAIS","cadtools")
        self.featurePitch = self.settings.value("arcs/featurepitch",  2)
        self.featureAngle = self.settings.value("arcs/featureangle",  1)
        self.rubberAngle = self.settings.value("arcs/rubberangle",  5)
        self.featureMethod = self.settings.value("arcs/featuremethod",  "pitch")

        self.spinBoxFeaturePitch.setMinimum(0.1)
        self.spinBoxFeaturePitch.setMaximum(1000)
        self.spinBoxFeaturePitch.setDecimals(1)
        self.spinBoxFeaturePitch.setValue(float(self.featurePitch))
        
        self.spinBoxFeatureAngle.setMinimum(1)
        self.spinBoxFeatureAngle.setMaximum(90)
        self.spinBoxFeatureAngle.setDecimals(1)    
        self.spinBoxFeatureAngle.setValue(float(self.featureAngle))    
        
        self.spinBoxRubberAngle.setMinimum(1)
        self.spinBoxRubberAngle.setMaximum(90)
        self.spinBoxRubberAngle.setDecimals(1)    
        self.spinBoxRubberAngle.setValue(float(self.rubberAngle))          
      
        if self.featureMethod == "pitch":
            self.radioFeaturePitch.setChecked(True)
            self.radioFeatureAngle.setChecked(False)
        else:
            self.radioFeaturePitch.setChecked(False)
            self.radioFeatureAngle.setChecked(True)  
        
        self.tabWidget.setTabEnabled(self.tabWidget.indexOf(self.tab2),  False)                
        
        self.okButton = self.buttonBox.button(QDialogButtonBox.Ok)
        self.okButton.clicked.connect(self.accept)

        self.cancelButton = self.buttonBox.button(QDialogButtonBox.Cancel)
        self.cancelButton.clicked.connect(self.close)

        pass



#    @pyqtSignature("on_btnSelectVertex_clicked()") 
#    def on_btnSelectVertex_clicked(self):
#        self.method = "vertex"
#        self.buttonBox.button(QDialogButtonBox.Ok).setEnabled(True)   
#        self.btnSelectVertex_clicked.emit()
#
#
    def accept(self):
        self.settings.setValue("arcs/featurepitch", self.spinBoxFeaturePitch.value())
        self.settings.setValue("arcs/featureangle", self.spinBoxFeatureAngle.value())
        self.settings.setValue("arcs/rubberangle", self.spinBoxRubberAngle.value())
        
        if self.radioFeaturePitch.isChecked():
            self.settings.setValue("arcs/featuremethod", "pitch")
        else:
            self.settings.setValue("arcs/featuremethod", "angle")

        self.close()
        
