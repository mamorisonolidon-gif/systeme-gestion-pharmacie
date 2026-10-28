import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from fournisseur_page import fournisseur
from famille_medic_page import Famille_medic
from vente_page import Vente
from medicament_page import Medicament
from achat_page import Achat
from stock_page import Stock
from table_borde import TableauBord
 
class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("GSP - Pharmacie")
        self.setGeometry(100, 100, 1200, 900)

        # Menu Bar
        bar = self.menuBar()
        bar.setStyleSheet("""
        QMenuBar {
            background-color: #3f493d;
            color: white;
            min-height: 25px;
            font-family: "Times New Roman", Times, serif;
            font-size: 16px;
            font-weight: bold;
        }
        QMenuBar::item:selected { background-color: #4fa047; }
        """)
        self.reglage = bar.addMenu("Réglage")
        self.prise_en_charge = bar.addMenu("Prise en charge")
        self.rapport = bar.addMenu("Rapport")
        self.facture = bar.addMenu("Facture")
        self.medic_perime = bar.addMenu("Médicament périmés")
        self.deconnect_menu = bar.addMenu("Déconnexion")

        # Stack pages
        self.stack_widget = QStackedWidget()
        self.fournisseur = fournisseur()
        self.Famille_medic = Famille_medic()
        self.Vente = Vente()
        self.Medicament = Medicament()
        self.Achat = Achat()
        self.Stock = Stock()
        self.table = TableauBord()
        for page in [self.Famille_medic, self.fournisseur, self.Vente, self.Medicament,
                     self.Achat, self.Stock, self.table]:
            self.stack_widget.addWidget(page)

        # Sidebar
        self.create_sidebar()

        # Right frame
        self.right_frame = self.create_right_frame()

        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setWidget(self.right_frame)

        # Main layout
        main_layout = QHBoxLayout()
        main_layout.addWidget(self.sidebar_frame, 20)
        main_layout.addWidget(scroll, 80)
        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

        # Timer date/heure
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_datetime)
        self.timer.start(1000)
        self.update_datetime()

        # Active bouton
        self.setup_active_buttons()

        # Stack animation
        self.opacity_effect = QGraphicsOpacityEffect()
        self.stack_widget.setGraphicsEffect(self.opacity_effect)
        self.opacity_effect.setOpacity(1.0)

        # Page initiale
        self.stack_widget.setCurrentWidget(self.table)

        # Style général
        self.setStyleSheet(self.get_stylesheet())

    # Sidebar
    def create_sidebar(self):
        self.sidebar_frame = QFrame()
        self.sidebar_frame.setObjectName("sidebar")
        sidebar_layout = QVBoxLayout()
        sidebar_layout.setContentsMargins(15,50,15,15)   
        sidebar_layout.setSpacing(10)

        self.label_logo = QLabel()
        pixmap = QPixmap("image/ISPM Logo2.png")  # Logo GSP tsy ovaina
        self.label_logo.setPixmap(pixmap)
        self.label_logo.setFixedSize(135,140)
        self.label_logo.setScaledContents(True)
        sidebar_layout.addWidget(self.label_logo, alignment=Qt.AlignCenter)

        self.btn_tab = self.create_btn("Tableau de bord","icon/tab.png",self.table)
        self.btn_vente = self.create_btn("Ventes","icon/vente.png",self.Vente)
        self.btn_famille = self.create_btn("Famille","icon/famille.png",self.Famille_medic)
        self.btn_medic = self.create_btn("Médicaments","icon/medicament.png",self.Medicament)
        self.btn_fourni = self.create_btn("Fournisseurs","icon/fournisseur.png",self.fournisseur)
        self.btn_achat = self.create_btn("Achats","icon/achat.png",self.Achat)
        self.btn_stock = self.create_btn("Stocks","icon/stock.png",self.Stock)
        self.btn_deconnexion = self.create_btn("Déconnexion","icon/deconnect.png",None)

        for btn in [self.btn_tab, self.btn_vente, self.btn_famille, self.btn_medic,
                    self.btn_fourni, self.btn_achat, self.btn_stock, self.btn_deconnexion]:
            sidebar_layout.addWidget(btn)
        sidebar_layout.addStretch()
        self.sidebar_frame.setLayout(sidebar_layout)

    def create_btn(self,text,icon_path,page_widget):
        btn = QPushButton(text)
        btn.setObjectName("btn_direction")
        btn.setIcon(QIcon(icon_path))
        btn.setIconSize(QSize(24,24))
        btn.setCursor(Qt.PointingHandCursor)
        btn.page_widget = page_widget
        if page_widget: btn.clicked.connect(lambda: self.switch_page(page_widget))
        else: btn.clicked.connect(self.deconnect)
        return btn

    # Switch Page Animation
    def switch_page(self,page_widget):
        self.opacity_anim = QPropertyAnimation(self.opacity_effect,b"opacity")
        self.opacity_anim.setDuration(250)
        self.opacity_anim.setStartValue(0.0)
        self.opacity_anim.setEndValue(1.0)
        self.opacity_anim.setEasingCurve(QEasingCurve.InOutQuad)
        self.stack_widget.setCurrentWidget(page_widget)
        self.opacity_anim.start()

    # Right frame
    def create_right_frame(self):
        frame = QFrame()
        frame.setObjectName("Frame_col2")
        layout = QVBoxLayout()
        layout.setContentsMargins(10,10,10,10)
        layout.setSpacing(10)

        # --- Top Frame nohavaozina ---
        top_frame = QFrame()
        top_frame.setObjectName("topContentFrame")
        top_layout = QHBoxLayout()
        top_layout.setContentsMargins(15,0,15,0)
        top_layout.setSpacing(15)

        logo_proj = QLabel()
        logo_proj.setPixmap(QPixmap("image/sary.png"))
        logo_proj.setFixedSize(100,90)  # Haavo sy largeur nohavaozina
        logo_proj.setScaledContents(True)
        logo_proj.setAlignment(Qt.AlignTop)

        label_title = QLabel("Gestion de Stock pour une Pharmacie")
        label_title.setObjectName("titre_projet")

        spacer = QSpacerItem(40,20,QSizePolicy.Expanding,QSizePolicy.Minimum)

        datetime_layout = QHBoxLayout()
        date_label = QLabel("Date :")
        heure_label = QLabel("Heure :")
        self.date_edit = QLineEdit()
        self.date_edit.setObjectName("date_edit")
        self.date_edit.setReadOnly(True)
        self.date_edit.setFixedWidth(140)
        self.date_edit.setFixedHeight(32)
        self.heure_edit = QLineEdit()
        self.heure_edit.setObjectName("heure_edit")
        self.heure_edit.setReadOnly(True)
        self.heure_edit.setFixedWidth(140)
        self.heure_edit.setFixedHeight(32)

        datetime_layout.addWidget(date_label)
        datetime_layout.addWidget(self.date_edit)
        datetime_layout.addSpacing(10)
        datetime_layout.addWidget(heure_label)
        datetime_layout.addWidget(self.heure_edit)

        top_layout.addWidget(logo_proj)
        top_layout.addWidget(label_title)
        top_layout.addItem(spacer)
        top_layout.addLayout(datetime_layout)
        top_layout.setAlignment(Qt.AlignVCenter)

        top_frame.setLayout(top_layout)
        top_frame.setFixedHeight(130)  # Haavo nohavaozina, mifanaraka tsara amin'ny fenetre

        # --- Stack Widget ---
        layout.addWidget(top_frame)
        layout.addWidget(self.stack_widget, 1)

        frame.setLayout(layout)
        return frame

    # Date & Heure
    def update_datetime(self):
        self.date_edit.setText(QDate.currentDate().toString("dd-MM-yyyy"))
        self.heure_edit.setText(QTime.currentTime().toString("hh : mm : ss"))

    # Active boutons
    def setup_active_buttons(self):
        self.stack_widget.currentChanged.connect(self.update_active_btn)

    def update_active_btn(self):
        current_widget = self.stack_widget.currentWidget()
        for b in [self.btn_tab,self.btn_vente,self.btn_famille,self.btn_medic,
                  self.btn_fourni,self.btn_achat,self.btn_stock,self.btn_deconnexion]:
            if getattr(b,"page_widget",None)==current_widget: b.setProperty("active",True)
            else: b.setProperty("active",False)
            b.style().unpolish(b)
            b.style().polish(b)

        # Fonctions pages spécifiques
        if current_widget==self.table:
            self.table.rafraichir()
            self.fournisseur.afficher_fournisseur()
        elif current_widget==self.Medicament:
            self.Medicament.verifier_modification()
        elif current_widget==self.Achat:
            self.Achat.verifier_modification_fourni()
            self.Achat.verifier_modification_designation()
            self.Achat.calcul_total()
        elif current_widget==self.fournisseur:
            self.fournisseur.afficher_fournisseur()

    # Sidebar responsive
    def resizeEvent(self,event):
        if self.width()<200: self.sidebar_frame.hide()
        else: self.sidebar_frame.show()
        super().resizeEvent(event)

    # Déconnexion
    def deconnect(self):
        self.close()

    # Styles
    def get_stylesheet(self):
        return """
QWidget { font-family: "Nunito Sans", "Arial", sans-serif; font-size:20px; color:#2f4f2f; }
QFrame#sidebar {
    background: qlineargradient(x1:0,y1:0,x2:0,y2:1, stop:0 #43A047, stop:1 #2E7D32);
    border-radius: 15px;
    border: 2px solid #a0d6a0;
    padding: 15px;
    min-width:200px;
    max-width:250px;
}
QPushButton#btn_direction {
    background-color:#6abf69;
    color:white;
    font-weight:bold;
    text-align:left;
    padding:5px 17px;
    border-radius:12px;
    margin:6px 12px;
    min-height:38px;
    border:2px solid #4fa047;
    font-size:16px;
}
QPushButton#btn_direction:hover { background-color:#4fa047; }
QPushButton#btn_direction[active="true"] { background-color:#3a7d3a; }

QFrame#Frame_col2 { background-color:#f9fff9; border-radius:15px; padding:12px; }
QFrame#topContentFrame { background-color:#d9ffd9;  border-radius:15px; padding:10px;
    margin-bottom:10px; border:2px solid #4fa047; }
QLabel#titre_projet { font-weight:bold; font-size:28px; color:#3a5c3a; }
QLineEdit#date_edit, QLineEdit#heure_edit {
    background-color: #e6ffe6; border: 2px solid #4fa047; border-radius: 10px; padding: 6px 12px;
    font-size: 18px; font-weight: bold; color: #1f3f1f; selection-background-color: #a0d6a0;
}
QLineEdit#date_edit:hover, QLineEdit#heure_edit:hover { border: 2px solid #2e7d2e; }
QLabel { font-size:18px; font-weight:bold; color:#2f4f2f; }
"""

if __name__=="__main__":
    app = QApplication(sys.argv)
    form = App()
    form.show()
    sys.exit(app.exec_())