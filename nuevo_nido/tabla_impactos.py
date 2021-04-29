from qgis.PyQt.QtWidgets import *
from .tabla_impactos_dialog import Ui_dlg_impactos 

class DlgTabla(QDialog, Ui_dlg_impactos): 
    def __init__(self): 
        super(DlgTabla, self).__init__()
        self.setupUi(self)

        self.tbl_impactos.setColumnWidth(1, 200) 
        
        
    
