import sys
import time
import datetime
import sqlite3

from PyQt5.QtGui import*
from PyQt5.QtWidgets import*
from PyQt5.QtCore import*
from achat_page import*
# from Medicament_page import *

class fournisseur(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("fournisseur")
        self.select = None
        self.conn = sqlite3.connect("MonProjet.db")
        self.creer_table_fournisseur()
        self.achat = Achat()
        #------------row1------------------#fin
        self.lbl_gestion_vente = QLabel("Fournisseurs")
        self.lbl_gestion_vente.setObjectName("lbl_gestion_vente")

        self.lbl_ticket_vente = QLabel("Recherche")
        self.lbl_ticket_vente.setObjectName("lbl_ticket_vente")

        self.edit_ticket_vente = QLineEdit()
        self.edit_ticket_vente.setObjectName("edit_ticket_vente")
        self.edit_ticket_vente.setFixedWidth(200)
        self.edit_ticket_vente.setPlaceholderText("...")
        self.edit_ticket_vente.textChanged.connect(self.recherche)
        self.frame_ticket = QFrame()
        self.frame_ticket.setObjectName("frame_ticket")
        hbox_ticket = QHBoxLayout()
        hbox_ticket.setContentsMargins(0, 0, 0, 0)
        hbox_ticket.setSpacing(8)
        hbox_ticket.addWidget(self.lbl_ticket_vente)
        hbox_ticket.addWidget(self.edit_ticket_vente)
        self.frame_ticket.setLayout(hbox_ticket)

        hbox_row_one = QHBoxLayout()
        hbox_row_one.setContentsMargins(0, 0, 0, 0)
        hbox_row_one.setSpacing(12)
        hbox_row_one.addWidget(self.lbl_gestion_vente)
        hbox_row_one.addWidget(self.frame_ticket, 0, Qt.AlignRight)

        self.frame_row_one = QFrame()
        self.frame_row_one.setObjectName("frame_row_one")
        self.frame_row_one.setLayout(hbox_row_one)
        #------------row2------------------
        
        
        self.code_fournisseur = QLabel("Code fournisseur")
        self.code_fournisseur.setStyleSheet("background: qlineargradient(x1:0,y1:0,x2:0,y2:1, stop:0 #43A047, stop:1 #2E7D32);padding-left: 20px; padding-right:20px ;color: white;font-family: 'Nunito Sans Light', sans-serif;font-size: 15px")
        self.code_fournisseur_edit = QLineEdit()
        self.code_fournisseur_edit.setFixedSize(270, 30)
        self.nom_fournisseur = QLabel("nom")
        self.nom_fournisseur.setStyleSheet("background: qlineargradient(x1:0,y1:0,x2:0,y2:1, stop:0 #43A047, stop:1 #2E7D32);padding-left: 20px; padding-right:100px ;color: white;font-family: 'Nunito Sans Light', sans-serif;font-size: 15px")
        self.nom_fournisseur_edit = QLineEdit()
        self.nom_fournisseur_edit.setFixedSize(270, 30)
        self.adresse_fournisseur = QLabel("Adresse")
        self.adresse_fournisseur.setStyleSheet("background: qlineargradient(x1:0,y1:0,x2:0,y2:1, stop:0 #43A047, stop:1 #2E7D32);padding-left: 20px; padding-right:77px ;color: white;font-family: 'Nunito Sans Light', sans-serif;font-size: 15px")
        self.adresse_fournisseur_edit = QLineEdit()
        self.adresse_fournisseur_edit.setFixedSize(270, 30)
        self.tel_fournisseur = QLabel("Télephone")
        self.tel_fournisseur.setStyleSheet("background: qlineargradient(x1:0,y1:0,x2:0,y2:1, stop:0 #43A047, stop:1 #2E7D32);padding-left: 20px; padding-right:62px ;color: white;font-family: 'Nunito Sans Light', sans-serif;font-size: 15px")
        self.tel_fournisseur_edit = QLineEdit()
        self.tel_fournisseur_edit.setFixedSize(270, 30)
        
        ################################# grid_formulaire
        form_fournisseur = QFormLayout()
        form_fournisseur.addRow(self.code_fournisseur, self.code_fournisseur_edit)
        form_fournisseur.addRow(self.nom_fournisseur, self.nom_fournisseur_edit)
        form_fournisseur.addRow(self.adresse_fournisseur, self.adresse_fournisseur_edit)
        form_fournisseur.addRow(self.tel_fournisseur, self.tel_fournisseur_edit)
        
        
        qv_form_fournisseur = QVBoxLayout()
        qv_form_fournisseur.addLayout(form_fournisseur)
        fram_qv_form_fournisseur = QFrame()
        fram_qv_form_fournisseur.setObjectName("frame_row_one")
        fram_qv_form_fournisseur.setLayout(qv_form_fournisseur)
        
        #################################grid_btn
        btn_nouveau_fournisseur = QPushButton('Nouveau')
        btn_nouveau_fournisseur.setObjectName("btn_nouveau_vente")
        icon_nouv= QIcon("icon/nouveau (2).png")
        btn_nouveau_fournisseur.setIcon(icon_nouv)
        btn_nouveau_fournisseur.clicked.connect(self.preparer_ajout_fournisseur)
        btn_enregistrer_fournisseur= QPushButton('Enregistrer')
        btn_enregistrer_fournisseur.setObjectName("btn_nouveau_vente")
        icon_enr= QIcon("icon/enregistre.png")
        btn_enregistrer_fournisseur.setIcon(icon_enr)
        btn_enregistrer_fournisseur.clicked.connect(self.enregistrer_fournisseur)
        btn_supprimer_fournisseur = QPushButton('Supprimer')
        btn_supprimer_fournisseur.setObjectName("btn_nouveau_vente")
        icon_sup= QIcon("icon/supprimer.png")
        btn_supprimer_fournisseur.setIcon(icon_sup)
        btn_supprimer_fournisseur.clicked.connect(self.effacer_fournisseur)
        btn_modifier_fournisseur = QPushButton('Modifier')
        btn_modifier_fournisseur.setObjectName("btn_nouveau_vente")
        icon_modif= QIcon("icon/modifier.jpg")
        btn_modifier_fournisseur.setIcon(icon_modif)
        btn_modifier_fournisseur.clicked.connect(self.modifier_fournisseur)
        btn_actualiser_fournisseur = QPushButton('Actualiser')
        btn_actualiser_fournisseur.setObjectName("btn_nouveau_vente")
        icon_act= QIcon("icon/actualiser.png")
        
        btn_actualiser_fournisseur.setIcon(icon_act)
        btn_actualiser_fournisseur.clicked.connect(self.afficher_fournisseur)
        
        grid_btn_fournisseur = QGridLayout()
        grid_btn_fournisseur.addWidget(btn_nouveau_fournisseur, 0, 0)
        grid_btn_fournisseur.addWidget(btn_enregistrer_fournisseur, 0, 1)
        grid_btn_fournisseur.addWidget(btn_supprimer_fournisseur, 1, 0)
        grid_btn_fournisseur.addWidget(btn_modifier_fournisseur, 1, 1)
        grid_btn_fournisseur.addWidget(btn_actualiser_fournisseur, 2, 0)

        fram_qv_grid_btn_fournisseur = QFrame()
        fram_qv_grid_btn_fournisseur.setObjectName("frame_row_one")
        fram_qv_grid_btn_fournisseur.setLayout(grid_btn_fournisseur)
        
        ################################# grid_btn_fournisseur + grid_formulaire
        hv_furmulaire = QHBoxLayout() 
        hv_furmulaire.addWidget(fram_qv_form_fournisseur, 60)
        hv_furmulaire.setSpacing(70)
        hv_furmulaire.addWidget(fram_qv_grid_btn_fournisseur, 40)
        
        #################################Table
        self.list_fournisseur = QTableWidget()
        self.list_fournisseur.setColumnCount(4)
        self.list_fournisseur.setObjectName("frame_row_one")
        list_header = ["Code fournisseur", "Nom", "Adresse", "Télephone"]
        self.list_fournisseur.verticalHeader().setVisible(False)
        self.list_fournisseur.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.list_fournisseur.setHorizontalHeaderLabels(list_header)
        self.list_fournisseur.cellClicked.connect(self.selectionner_une_ligne)
        self.list_fournisseur.cellClicked.connect(self.achat.verifier_modification_fourni)
        
        hvTable =QVBoxLayout()
        hvTable.addWidget(self.list_fournisseur)
        
        frameTable = QFrame()
        frameTable.setLayout(hvTable)
        frameTable.setObjectName("frame_row_one")
        #------------row3------------------#
        box_row_two_fournisseur = QVBoxLayout() 
        box_row_two_fournisseur.addLayout(hv_furmulaire)
        box_row_two_fournisseur.addWidget(frameTable)
        
        frame_box_row_two_fournisseur = QFrame()
        frame_box_row_two_fournisseur.setLayout(box_row_two_fournisseur)
        
        
        # ajouter au main layout
        mainLayout_fournisseur = QVBoxLayout()
        mainLayout_fournisseur.setContentsMargins(0, 0, 0, 0)
        mainLayout_fournisseur.addWidget(self.frame_row_one)
        mainLayout_fournisseur.addWidget(frame_box_row_two_fournisseur)
        self.setStyleSheet("""
            QWidget { background-color: #F6FBF6; }
            QFrame#frame_row_one, QFrame#frame_row_two, QFrame#frame_row_three,
            QFrame#frame_formulaire, QFrame#frame_prod, QFrame#frame_date_validation,
            QFrame#frame_validation {
                background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #EAF6EA, stop:1 #DFF2DF);
                border: 1px solid #C7E8C7;
                border-radius: 10px;
                padding: 10px;
            }
            QLabel#lbl_gestion_vente {
                font: 24px "Segoe UI";
                font-weight: 700;
                color: #0b3d2e;
                background: white;
                padding: 10px 14px;
                border-radius: 8px;
            }
            QLabel { font: 16px "Segoe UI"; color: #0b3d2e; padding: 4px 6px; }
            QLineEdit, QDateEdit, QSpinBox, QDoubleSpinBox, QComboBox { background-color: #FFFFFF; border: 1px solid #BFE6C3; border-radius: 8px; padding: 8px; font: 16px "Segoe UI"; color: #08321f; min-width: 200px; min-height: 25px; }
            QLineEdit:read-only { background-color: #F0FFF3; color: #2e7d32; }
            QPushButton#btn_validation_vente, QPushButton#btn_nouveau_vente {
                background: qlineargradient(x1:0,y1:0,x2:0,y2:1, stop:0 #43A047, stop:1 #2E7D32);
                color: white; border-radius: 8px; padding: 10px 14px; font: bold 16px "Segoe UI";
            }
            QPushButton#btn_validation_vente:hover, QPushButton#btn_nouveau_vente:hover {
                background: qlineargradient(x1:0,y1:0,x2:0,y2:1, stop:0 #66BB6A, stop:1 #43A047);
            }
            QPushButton#btn_validation_vente:pressed, QPushButton#btn_nouveau_vente:pressed { background: #1F6B26; }
            QPushButton#btn_recherche { background-color: #66BB6A; color: white; border: none; border-radius: 8px; padding: 8px; min-width: 36px; min-height: 36px; }
            QPushButton#btn_recherche:hover { background-color: #5ABA62; }
            QPushButton#btn_recherche:pressed { background-color: #4F9F55; }
            QTableWidget#table_vente { background-color: #FFFFFF; alternate-background-color: #F3FBF4; gridline-color: #E6F2EA; color: #08321f; font: 14px "Segoe UI"; border: 1px solid #E6F2EA; border-radius: 8px; padding: 6px; }
            QHeaderView::section { background: qlineargradient(x1:0,y1:0,x2:0,y2:1, stop:0 #43A047, stop:1 #2E7D32); color: white; font: bold 16px "Segoe UI"; padding: 8px; border: none; }
            QTableWidget::item { padding: 8px; }
            QTableWidget::item:selected { background-color: #BEE6C5; color: #0b3d2e; }
            QTableCornerButton::section { background-color: #1B5E20; border: none; }
        """)
        self.setLayout(mainLayout_fournisseur)
    def creer_table_fournisseur(self):
        cursor = self.conn.cursor()
        cursor.execute("""
                       CREATE TABLE IF NOT EXISTS fournisseur(
                            codeF INTEGER PRIMARY KEY AUTOINCREMENT, 
                            nomF VARCHAR(100),
                            adresseF VARCHAR(100),
                            tel TEXT
                       )
                       """)
        
        self.conn.commit() 
    def next(self):
        cur = self.conn.cursor()
        cur.execute("SELECT codeF FROM fournisseur ORDER BY codeF")
        codes = [row[0] for row in cur.fetchall()]
        print(codes)
        if codes : 
            for i in codes:
                print(i)
                next = i + 1           
                
            return next
        else:
            return 1
    def preparer_ajout_fournisseur(self):
        count = self.next()
        self.code_fournisseur_edit.setText(str(count))
        self.nom_fournisseur_edit.clear()
        self.adresse_fournisseur_edit.clear()
        self.tel_fournisseur_edit.clear()
        self.select = None 
        
    def  enregistrer_fournisseur(self):
        n = self.nom_fournisseur_edit.text().strip().capitalize()
        a = self.adresse_fournisseur_edit.text().strip().upper()
        t = self.tel_fournisseur_edit.text().strip().upper()
        if len(n)==0 or len(a)==0 or len(t)==0:
            QMessageBox.information(self, "Information", "Verifier tous les champs")
            return
        cur = self.conn.cursor()
        cur.execute("INSERT INTO fournisseur(nomF, adresseF, tel) VALUES (?, ?, ?)", (n, a, t))
        self.conn.commit()
        self.afficher_fournisseur()
        
    def afficher_fournisseur(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT *  FROM fournisseur")
        row = cursor.fetchall()
        self.list_fournisseur.setRowCount(len(row))
        for i, (c, n, a, t) in enumerate (row):
            self.list_fournisseur.setItem(i, 0, QTableWidgetItem(str(c)))
            self.list_fournisseur.setItem(i, 1, QTableWidgetItem(str(n)))
            self.list_fournisseur.setItem(i, 2, QTableWidgetItem(str(a)))
            self.list_fournisseur.setItem(i, 3, QTableWidgetItem(str(t)))
        
    def selectionner_une_ligne(self, row, column):
        c = self.list_fournisseur.item(row, 0).text()
        n = self.list_fournisseur.item(row, 1).text()
        a = self.list_fournisseur.item(row, 2).text()
        t = self.list_fournisseur.item(row, 3).text()
        self.select = c
        self.code_fournisseur_edit.setText(c)
        self.nom_fournisseur_edit.setText(n)
        self.adresse_fournisseur_edit.setText(a)
        self.tel_fournisseur_edit.setText(t)
        
        
        
        
    def modifier_fournisseur(self):
        if not self.select:
            QMessageBox.information(self, "Information", "Veuillez sélectionner une ligne à modifier")
            return
        n = self.nom_fournisseur_edit.text().strip()
        a = self.adresse_fournisseur_edit.text().strip()
        t = self.tel_fournisseur_edit.text().strip() 
        if len(n)==0 or len(a)==0 or len(t)==0:
            QMessageBox.information(self, "Information", "Verifier tous les champs")
            return
        cursor = self.conn.cursor()
        cursor.execute("UPDATE fournisseur  SET nomF = ?, adresseF = ?, tel = ? WHERE codeF = ?", (n, a, t, self.select)) 
        self.conn.commit()
        self.afficher_fournisseur()
        self.select = None
    def effacer_fournisseur(self):
        if not self.select:
            QMessageBox.information(self, "Information", "Veuillez sélectionner une ligne à supprimer")
            return
        reponse  = QMessageBox.question(self, "confirmation", f"Supprimer la code {self.select}?", QMessageBox.Yes | QMessageBox.No)
        if reponse ==QMessageBox.Yes:
            self.cursor = self.conn.cursor()
            self.cursor.execute("DELETE FROM fournisseur WHERE codeF = ?", (self.select, ))
            self.conn.commit()
            self.nom_fournisseur_edit.clear()
            self.adresse_fournisseur_edit.clear()
            self.tel_fournisseur_edit.clear()
            self.select = None 
            self.afficher_fournisseur()
    def recherche(self):
        r = self.edit_ticket_vente.text()
        cursor = self.conn.cursor()
        cursor.execute("SELECT *  FROM fournisseur WHERE nomF LIKE ?", (r + '%', ))
        row = cursor.fetchall()
        self.list_fournisseur.setRowCount(len(row))
        for i, (c, n, a, t) in enumerate (row):
            self.list_fournisseur.setItem(i, 0, QTableWidgetItem(str(c)))
            self.list_fournisseur.setItem(i, 1, QTableWidgetItem(str(n)))
            self.list_fournisseur.setItem(i, 2, QTableWidgetItem(str(a)))
            self.list_fournisseur.setItem(i, 3, QTableWidgetItem(str(t)))
    def compter_fournisseur( ):
        import sqlite3
        
        conn = sqlite3.connect("MonProjet.db")
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM fournisseur")
        resultat = cursor.fetchone()[0]
        conn.close()
        return str(resultat) 



