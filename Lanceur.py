# ----------------------------------------------------------------
# Lanceur.py
# 20240820
# @Zlatko
# ----------------------------------------------------------------
import sys

# ----------------------------------------------------------------
# modules natifs
from pathlib import Path
from PySide6.QtCore import(
    QSize,
    Qt,
    QDir,
    QRect
)
from PySide6.QtGui import(
    QAction,
    QIcon,
    QPalette,
    QColor,
    QCloseEvent
)
from PySide6.QtWidgets import(
    QApplication,
    QCheckBox,
    QLabel,
    QMainWindow,
    QToolBar,
    QPushButton,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QGridLayout,
    QTextEdit,
    QTabWidget,
    QProgressBar,
    QTreeWidgetItem,
    QTreeWidget,
    QTreeView,
    QFileSystemModel,
    QSplitter,
    QMessageBox,
    QComboBox,
    QGroupBox,
    QRadioButton,
    QSpinBox,
    QSlider,
    QLineEdit,
    QLCDNumber,
    QDialog,
    QDialogButtonBox
)
# ----------------------------------------------------------------
# modules perso
import TraqParserconfig
import TraqParsernotif
import TraqLogW
# >>>''''''''''''''''''''''''''''''''''''''''''''''''''''''''''<<<
# journalisation
TraqLogW.param_log_function("user","INFO","Dépendances chargées")
# 
# ----------------------------------------------------------------
# Subclass QColor to customize your QColor
# juste pour travailler sur les layout
# ----------------------------------------------------------------
class Color(QWidget):
    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)
# ----------------------------------------------------------------
# Subclass QMainWindow to customize your application's main window
# Fenètre principale
# ----------------------------------------------------------------
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # ----------------------------------------------------------------
        # Préparer la fenètre principale
        self.setWindowTitle("Traqueur_Feuille de route")   
        icoAppli=(TraqParserconfig.param_cible_function("Config.conf","Chemins","Chemin_Icone_appli"))     
        self.setWindowIcon(QIcon(icoAppli))
        self.resize(1024, 600) 
        # ----------------------------------------------------------------
        # Déclarer les entités
        self.createAirecentrale()
        self.createActions()        
        self.createToolBar()
        self.createMenuBar()
        self.createStatusBar()
        # >>>''''''''''''''''''''''''''''''''''''''''''''''''''''''''''<<<
        # journalisation
        TraqLogW.param_log_function("user","INFO","Eléments fonctionnels du programme créés")
        #         
    # ----------------------------------------------------------------
    # Les widgets de l'appli          
    def createAirecentrale(self) :          
        splitterHorizMid = QSplitter(Qt.Horizontal)
        
        # ----------------------------------------------------------------
        # A GAUCHE
        # ----------------------------------------------------------------
        
        splitterV = QSplitter(Qt.Vertical,splitterHorizMid)        
        # ----------------------------------------------------------------
        # exemple bouton
        button1 = QPushButton("Press Me!")
        # self.setFixedSize(QSize(400, 300)) 
        
        # ----------------------------------------------------------------
        # Utilisation du widget QTreeView pour préparer json
        treeview1 = QTreeWidget()        
        treeview1.setColumnCount(1)
        treeview1.insertTopLevelItems(0, [QTreeWidgetItem(None, ["Tables"])])
        root = treeview1.topLevelItem(0)
        for i in range(10):
            node = QTreeWidgetItem(None, ["Item" + str(i)])
            root.addChild(node)
        # >>>''''''''''''''''''''''''''''''''''''''''''''''''''''''''''<<<
        # journalisation
        TraqLogW.param_log_function("user","INFO","Arborescence DATA créée")
        
        # ----------------------------------------------------------------
        # Utilisation du widget QTreeView pour dir 
        treeModel = QFileSystemModel()
        treeModel.setRootPath(QDir.currentPath())
        treeView2 = QTreeView()
        treeView2.setModel(treeModel)
        treeView2.expandToDepth(0)    
        # >>>''''''''''''''''''''''''''''''''''''''''''''''''''''''''''<<<
        # journalisation
        TraqLogW.param_log_function("user","INFO","Arborescence DIR créée")
        
        # ----------------------------------------------------------------
        # QSplitter permet de diviser l'espace en sous-zones.                
        splitterV.addWidget(button1)
        splitterV.addWidget(treeview1)
        splitterV.addWidget(treeView2)
        splitterHorizMid.addWidget(splitterV)   
        
        # ----------------------------------------------------------------
        # AU CENTRE
        # ----------------------------------------------------------------
        
        # ----------------------------------------------------------------
        # exemple Tab       
        tabs = QTabWidget(splitterHorizMid)
        tabs.setTabPosition(QTabWidget.West)
        tabs.setMovable(True)
        for n, color in enumerate(["red", "green", "blue", "yellow"]):
            tabs.addTab(Color(color), color)   
            
        # ----------------------------------------------------------------
        # A DROITE
        # ----------------------------------------------------------------
        
        # Un autre splitter pour séparer l'espace de droite du splitter principal 
        # en deux sous-zones affichées l'une sous l'autre (Qt.Vertical).
        verticalSplitter = QSplitter(Qt.Vertical, splitterHorizMid)
        editor = QTextEdit(verticalSplitter)
        self.fillEditor(editor)
        propertyPanel = QWidget(verticalSplitter)
        gridLayout = QGridLayout(propertyPanel)
        gridLayout.addWidget(self.createFirstGroupBox(), 0, 0)
        group2 = QGroupBox("Second group")
        gridLayout.addWidget(self.createSecondGroupBox(), 0, 1)
        group3 = QGroupBox("Third group")
        gridLayout.addWidget(self.createThirdGroupBox(), 0, 2)    

        # ----------------------------------------------------------------
        # sélection du widget central
        self.setCentralWidget(splitterHorizMid) 
        # >>>''''''''''''''''''''''''''''''''''''''''''''''''''''''''''<<<
        # journalisation
        TraqLogW.param_log_function("user","INFO","Widgets organisés")
        #  
    def fillEditor(self, editor):
        # On charge le contenu du fichier dans l'éditeur
        with open("TraqLogW.py", "r") as file:
            content = "".join(file.readlines())
        editor.setText(content)
        # 
    def createFirstGroupBox(self):
        # On définit un premier groupe de cases à cocher (exclusives).
        group1 = QGroupBox("First group")
        vBox = QVBoxLayout()
        vBox.addWidget(QRadioButton("Exclusive choice 1", checked=True))
        vBox.addWidget(QRadioButton("Exclusive choice 2"))
        vBox.addWidget(QRadioButton("Exclusive choice 3"))
        vBox.addStretch(1)
        group1.setLayout(vBox)
        return group1
    def createSecondGroupBox(self):
        # On définit un second groupe de cases à cocher (non exclusives).
        group2 = QGroupBox("Second group")
        vBox = QVBoxLayout()
        vBox.addWidget(QCheckBox("Choice 1", checked=True))
        vBox.addWidget(QCheckBox("Choice 2", checked=True))
        vBox.addWidget(QCheckBox("Choice 3"))
        vBox.addStretch(1)
        group2.setLayout(vBox)
        return group2
    def createThirdGroupBox(self):
        # On définit un dernier groupe de widgets.
        group3 = QGroupBox("Third group")
        vBox = QVBoxLayout()
        vBox.addWidget(QSpinBox(value=50))
        vBox.addWidget(QSlider(Qt.Horizontal, value=50))
        vBox.addWidget(QPushButton("Click me"))
        vBox.addWidget(QLineEdit("Edit me"))
        vBox.addWidget(QLCDNumber(value=50))
        vBox.addStretch(1)
        group3.setLayout(vBox)
        return group3    
    # ----------------------------------------------------------------
    # toolbar (attention cohérence action et menu)
    def createToolBar(self):
        toolbar = QToolBar("Barre d'outils")
        # toolbar.setIconSize(QSize(16, 16))
        # toolbar.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.addToolBar(toolbar)
        toolbar.addAction(self.button_action1)
        toolbar.addSeparator()
        toolbar.addAction(self.button_action2)
        toolbar.addSeparator()
        toolbar.addWidget(QLabel("Exemple"))
        toolbar.addWidget(QCheckBox())
                
        toolbar1 = self.addToolBar("Standard ToolBar")
        toolbar1.addAction(self.actionNewE)
        toolbar1.addSeparator()
        toolbar1.addAction(self.actionOpen)
        toolbar1.addAction(self.actionSave)
        toolbar1.addSeparator()
        toolbar1.addAction(self.actionExit)

        toolbar2 = self.addToolBar("Edit ToolBar")
        toolbar2.addAction(self.actUndo)
        toolbar2.addAction(self.actRedo)
        toolbar2.addSeparator()
        toolbar2.addAction(self.actCopy)
        toolbar2.addAction(self.actCut)
        toolbar2.addAction(self.actPaste)

        toolbar3 = self.addToolBar("Test ToolBar")
        comboBox = QComboBox(self)
        comboBox.addItems(["First item", "Second item", "Third item"])
        toolbar3.addWidget(comboBox)
        toolbar3.addSeparator()
        toolbar3.addWidget(QCheckBox("Check me", self))
        
        # >>>''''''''''''''''''''''''''''''''''''''''''''''''''''''''''<<<
        # journalisation
        TraqLogW.param_log_function("user","INFO","Boites à outils créée")
        # 
    # ----------------------------------------------------------------
    # Menu 
    def createMenuBar(self): 
        menu = self.menuBar()
        
        file_menu = menu.addMenu("Administration")
        file_menu.addAction(self.actionNewE)
        file_menu.addAction(self.actionNewC)
        file_menu.addSeparator()
        file_menu.addAction(self.actionOpen)
        file_menu.addAction(self.actionSave)
        file_menu.addSeparator()        
        file_menu.addAction(self.button_action1)        
        file_menu.addSeparator()
        file_menu.addAction(self.button_action2)
        file_menu.addSeparator()
        file_menu.addAction(self.actionExit)
        
        file_menu = menu.addMenu("Edition")
        
        file_menu = menu.addMenu("Analyse")
        
        file_menu = menu.addMenu("A propos")
        # >>>''''''''''''''''''''''''''''''''''''''''''''''''''''''''''<<<
        # journalisation
        TraqLogW.param_log_function("user","INFO","Menu créé")
        # 
    # ----------------------------------------------------------------
    # barre de status
    def createStatusBar(self):
        barrestatus = self.statusBar()
        # un message timer si besoin
        barrestatus.showMessage("bonjour")
        # les labels contextuels  
        label1_barrestatus = QLabel(text=TraqParserconfig.param_cible_function('Config.conf','User','Profil'))
        label2_barrestatus = QLabel(text=TraqParserconfig.param_cible_function('Config.conf','User','Profil'))
        label3_barrestatus = QLabel(text=TraqParsernotif.notif_cible_function('Messages.conf','Menu','StatusTip01'))
        label4_barrestatus = QLabel(text=TraqParsernotif.notif_cible_function('Messages.conf','Menu','StatusTip02'))
        # Une barre de progression
        progress_barrestatus = QProgressBar()
        progress_barrestatus.setMaximumHeight(20)
        progress_barrestatus.setValue(50)
        # les widgets permanents à la droite de la barre de status.
        barrestatus.addPermanentWidget(progress_barrestatus)
        barrestatus.addPermanentWidget(label1_barrestatus)
        barrestatus.addPermanentWidget(label2_barrestatus)
        barrestatus.addPermanentWidget(label3_barrestatus)
        barrestatus.addPermanentWidget(label4_barrestatus)
        # >>>''''''''''''''''''''''''''''''''''''''''''''''''''''''''''<<<
        # journalisation
        TraqLogW.param_log_function("user","INFO","Barre de status créée")
        # 
    # ----------------------------------------------------------------
    # Gestion des évènements   
    def onMyToolBarButtonClick(self, s):
        print("click", s)
        # >>>''''''''''''''''''''''''''''''''''''''''''''''''''''''''''<<<
        # journalisation
        TraqLogW.param_log_function("user","INFO","Click sur le bouton xxx")
        # 
    def createActions(self):
        icoParser = TraqParserconfig.param_cible_function("Config.conf","Chemins_rel","Chemin_Icones_svg")
        
        icoFichier=icoParser+"applications-office.svg"  
        notifFichier=(TraqParsernotif.notif_cible_function("Messages.conf","Menu","StatusTip01"))     
        self.button_action1 = QAction(QIcon(icoFichier), "Fichier", self)
        self.button_action1.setStatusTip(notifFichier)
        self.button_action1.triggered.connect(self.onMyToolBarButtonClick)
        self.button_action1.setCheckable(True)
        
        icoEdition=icoParser+"preferences-desktop-locale.svg" 
        notifEdition=(TraqParsernotif.notif_cible_function("Messages.conf","Menu","StatusTip02")) 
        self.button_action2 = QAction(QIcon(icoEdition), "Edition", self)
        self.button_action2.setStatusTip(notifEdition)
        self.button_action2.triggered.connect(self.onMyToolBarButtonClick)
        self.button_action2.setCheckable(True)
        
        icoNewE=icoParser+"preferences-system-network.svg" 
        self.actionNewE = QAction(QIcon(icoNewE), "Créer une entité", self)
        self.actionNewE.setStatusTip("Nouvelle entité")
        self.actionNewE.triggered.connect(self.newEntite)
        
        icoNewC=icoParser+"preferences-plugin.svg" 
        self.actionNewC = QAction(QIcon(icoNewC), "Créer une cible", self)
        self.actionNewC.setStatusTip("Nouvelle cible")
        self.actionNewC.triggered.connect(self.newCible)
        
        icoOpen=icoParser+"actions/16/rating.svg" 
        self.actionOpen = QAction(QIcon(icoOpen), "&Open...", self)
        self.actionOpen.setStatusTip("Open file")
        
        icoSave=icoParser+"actions/16/rating.svg" 
        self.actionSave = QAction(QIcon(icoSave), "&Save", self)
        self.actionSave.setStatusTip("Save File")
        
        icoExit=icoParser+"system-shutdown.svg" 
        self.actionExit = QAction(QIcon(icoExit), "Exit", self)
        self.actionExit.setStatusTip("Exit")
        # La méthode close est directement fournie par la classe QMainWindow.
        self.actionExit.triggered.connect(self.close)
        
        icoUndo=icoParser+"actions/16/rating.svg"
        self.actUndo = QAction(QIcon(icoUndo), "&Undo", self)
        self.actUndo.setStatusTip("Undo")
        
        icoRedo=icoParser+"actions/16/rating.svg"
        self.actRedo = QAction(QIcon(icoRedo), "&Redo", self)
        self.actRedo.setStatusTip("Redo")

        icoCopy=icoParser+"actions/16/rating.svg"
        self.actCopy = QAction(QIcon(icoCopy), "&Copy", self)
        self.actCopy.setStatusTip("Copy")
        
        icoCut=icoParser+"actions/16/rating.svg"
        self.actCut = QAction(QIcon(icoCut), "Cu&t", self)
        self.actCut.setStatusTip("Cut")
        
        icoPaste=icoParser+"actions/16/rating.svg"
        self.actPaste = QAction(QIcon(icoPaste), "&Paste", self)
        self.actPaste.setStatusTip("Paste")
        
        icoAbout=icoParser+"help-about.svg"
        self.actAbout = QAction(QIcon(icoAbout), "About...", self)
        self.actAbout.setStatusTip("About...")
        # 
    def newEntite(self, Dialog):
        dlg = CustomDialog(self)
        if dlg.exec():
            # >>>''''''''''''''''''''''''''''''''''''''''''''''''''''''''''<<<
            # journalisation
            TraqLogW.param_log_function("user","INFO","Création d'une entité")
            #
        else:
            # >>>''''''''''''''''''''''''''''''''''''''''''''''''''''''''''<<<
            # journalisation
            TraqLogW.param_log_function("user","INFO","Annulation création d'une entité")
            #
    def newCible(self):
        print("Création d'une nouvelle cible")
        # >>>''''''''''''''''''''''''''''''''''''''''''''''''''''''''''<<<
        # journalisation
        TraqLogW.param_log_function("user","INFO","Création d'une cible")
        #
    # ----------------------------------------------------------------
    # Gestion de la fermeture
    def closeEvent(self, event: QCloseEvent) -> None:
        reply = QMessageBox.question(self, self.windowTitle(),
                                     "Are you sure to quit?",
                                     QMessageBox.Yes, QMessageBox.No)
        if reply == QMessageBox.Yes:
            # >>>''''''''''''''''''''''''''''''''''''''''''''''''''''''''''<<<
            # journalisation
            TraqLogW.param_log_function("user","INFO","Fermeture de Traqueur_fdr")
            event.accept()
        else:
            event.ignore()
            #             
# ----------------------------------------------------------------
# Crée les subclass
# et les affiche
# ----------------------------------------------------------------   
class CustomDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.resize(540, 130)
        self.setWindowTitle("Création d'une entité")
        label_1 = QLabel("Nom de l'entité pour laquelle une feuille de route doit être réalisée")
        label_1.setMinimumSize(QSize(255, 0))
        label_1.setWordWrap(True)
        lineEdit_1 = QLineEdit()
        lineEdit_1.setMinimumSize(QSize(255,0))
        # lineEdit_1.setPlaceholderText("Placeholder Text")
        lineEdit_1.setFocus()
        
        vertlayout = QVBoxLayout()
        
        horizLayout_1 = QHBoxLayout()
        horizLayout_1.addWidget(label_1)
        horizLayout_1.addWidget(lineEdit_1)
        
        vertlayout.addLayout(horizLayout_1)
        
        label_2 = QLabel("Intitulé de la cible à atteindre")
        label_2.setMinimumSize(QSize(255, 0))
        label_2.setWordWrap(True)
        lineEdit_2 = QLineEdit()
        lineEdit_2.setMinimumSize(QSize(255,0))
        # lineEdit_2.setPlaceholderText("Placeholder Text")
        
        horizLayout_2 = QHBoxLayout()
        horizLayout_2.addWidget(label_2)
        horizLayout_2.addWidget(lineEdit_2)
        
        vertlayout.addLayout(horizLayout_2)
        
        QBtn = (
            QDialogButtonBox.Ok | QDialogButtonBox.Cancel
            )
        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
        
        vertlayout.addWidget(self.buttonBox)
        
        self.setLayout(vertlayout)
        
# ----------------------------------------------------------------
# Crée l'application
# et l'affiche
# ----------------------------------------------------------------        
app = QApplication(sys.argv)
# >>>''''''''''''''''''''''''''''''''''''''''''''''''''''''''''<<<
# journalisation
TraqLogW.param_log_function("user","INFO","Démarrage Traqueur-fdr")
# 
window = MainWindow()
# 
# style de l'appli avant affichage
styleQss = TraqParserconfig.param_cible_function("Config.conf","Style","Style")
with open("Style/"+styleQss,"r") as file:
    app.setStyleSheet(file.read())
# 
# >>>''''''''''''''''''''''''''''''''''''''''''''''''''''''''''<<<
# journalisation
TraqLogW.param_log_function("user","INFO","Style appliqué")
# 
# affichage
window.show()
app.exec()

