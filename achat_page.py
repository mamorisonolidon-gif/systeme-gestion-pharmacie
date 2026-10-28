import sys
import time
import datetime
import sqlite3

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from commande import App_commande

class Achat(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("fournisseur")
        self.conn = sqlite3.connect("MonProjet.db")
        self.creer_table_achat()
        self.App_commande = App_commande()
        self.select = None
        #  row one    #
        
        self.lbl_gestion_vente = QLabel("Bon de commande")
        self.lbl_gestion_vente.setObjectName("lbl_gestion_vente")

        self.lbl_ticket_vente = QLabel("NO")
        self.lbl_ticket_vente.setObjectName("lbl_ticket_vente")

        self.edit_ticket_vente = QLineEdit()
        self.edit_ticket_vente.setObjectName("edit_ticket_vente")
        self.edit_ticket_vente.setFixedWidth(200)
        self.edit_ticket_vente.setPlaceholderText("....")

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
        
        #-------- row two
        
        
        lbl_nom_fournisseur = QLabel("Nom fournisseur")
        lbl_nom_fournisseur.setStyleSheet("background: qlineargradient(x1:0,y1:0,x2:0,y2:1, stop:0 #43A047, stop:1 #2E7D32);padding-left: 20px; padding-right:20px ;color: white;font-family: 'Nunito Sans Light', sans-serif;font-size: 15px")
        self.edit_combo_nom_fournisseur = QComboBox() 
        self.nom_fourni = []
        self.mise_a_jour_nom_fourni()
        self.edit_combo_nom_fournisseur.currentTextChanged.connect(self.formulaire_fourni)
        
        lbl_Adresse = QLabel("Adresse")
        lbl_Adresse.setStyleSheet("background: qlineargradient(x1:0,y1:0,x2:0,y2:1, stop:0 #43A047, stop:1 #2E7D32);padding-left: 20px; padding-right:20px ;color: white;font-family: 'Nunito Sans Light', sans-serif;font-size: 15px")
        self.adresse_fourni = QLineEdit() 
        lbl_tel = QLabel("Téléphone")
        lbl_tel.setStyleSheet("background: qlineargradient(x1:0,y1:0,x2:0,y2:1, stop:0 #43A047, stop:1 #2E7D32);padding-left: 20px; padding-right:20px ;color: white;font-family: 'Nunito Sans Light', sans-serif;font-size: 15px")
        self.edit_tel = QLineEdit()
        self.edit_tel.textChanged.connect(self.envoyer_vers_commande) 
        
        grid_formulaire_achat = QGridLayout()
        grid_formulaire_achat.addWidget(lbl_nom_fournisseur, 0, 0)
        grid_formulaire_achat.addWidget(self.edit_combo_nom_fournisseur, 0, 1)
        grid_formulaire_achat.addWidget(lbl_Adresse, 1, 0)
        grid_formulaire_achat.addWidget(self.adresse_fourni, 1, 1)
        grid_formulaire_achat.addWidget(lbl_tel, 2, 0)
        grid_formulaire_achat.addWidget(self.edit_tel, 2, 1)
        # form
        form_set_grid_fournisseur_commande = QVBoxLayout()
        form_set_grid_fournisseur_commande.addLayout(grid_formulaire_achat)
        frame_form_set_grid_fournisseur_commande = QFrame()
        frame_form_set_grid_fournisseur_commande.setObjectName("frame_row_one")
        frame_form_set_grid_fournisseur_commande.setLayout(form_set_grid_fournisseur_commande)
        # form fin
        
        
        lbl_designation = QLabel("Désignation")
        lbl_designation.setStyleSheet("background: qlineargradient(x1:0,y1:0,x2:0,y2:1, stop:0 #43A047, stop:1 #2E7D32);padding-left: 20px; padding-right:20px ;color: white;font-family: 'Nunito Sans Light', sans-serif;font-size: 15px")
        self.combo_designation = QComboBox()
        self.nom_medic = []
        self.mise_a_jour_nom_medic()
        
        Date_du_jour = QLabel("Date :")
        Date_du_jour.setStyleSheet("background: qlineargradient(x1:0,y1:0,x2:0,y2:1, stop:0 #43A047, stop:1 #2E7D32);padding-left: 20px; padding-right:20px ;color: white;font-family: 'Nunito Sans Light', sans-serif;font-size: 15px")
        self.Edit_date = QLineEdit()
        self.Edit_date.setText(time.strftime("%d - %m - %y"))
        
        lbl_unite = QLabel("Unité")
        lbl_unite.setStyleSheet("background: qlineargradient(x1:0,y1:0,x2:0,y2:1, stop:0 #43A047, stop:1 #2E7D32);padding-left: 20px; padding-right:20px ;color: white;font-family: 'Nunito Sans Light', sans-serif;font-size: 15px")
        self.edit_unite = QLineEdit()
        
        lbl_quantite = QLabel("Quantité")
        lbl_quantite.setStyleSheet("background: qlineargradient(x1:0,y1:0,x2:0,y2:1, stop:0 #43A047, stop:1 #2E7D32);padding-left: 20px; padding-right:20px ;color: white;font-family: 'Nunito Sans Light', sans-serif;font-size: 15px")
        self.edit_quantite  = QLineEdit()
        self.edit_quantite.textChanged.connect(self.calcul_montant)
        lbl_prix_unitaire = QLabel("Prix_unitaire")
        lbl_prix_unitaire.setStyleSheet("background: qlineargradient(x1:0,y1:0,x2:0,y2:1, stop:0 #43A047, stop:1 #2E7D32);padding-left: 20px; padding-right:20px ;color: white;font-family: 'Nunito Sans Light', sans-serif;font-size: 15px")
        self.edit_prix_unitaire = QLineEdit()
        self.edit_prix_unitaire.textChanged.connect(self.calcul_montant)
        lbl_montant= QLabel("Montant")
        lbl_montant.setStyleSheet("background: qlineargradient(x1:0,y1:0,x2:0,y2:1, stop:0 #43A047, stop:1 #2E7D32);padding-left: 20px; padding-right:20px ;color: white;font-family: 'Nunito Sans Light', sans-serif;font-size: 15px")
        self.edit_montant = QLineEdit()
        
        formulaire_achat = QGridLayout()
        formulaire_achat.addWidget(lbl_designation, 0, 0)
        formulaire_achat.addWidget(self.combo_designation, 0, 1)
        formulaire_achat.addWidget(Date_du_jour, 0, 2)
        formulaire_achat.addWidget(self.Edit_date, 0, 3)
        formulaire_achat.addWidget(lbl_unite, 1, 0)
        formulaire_achat.addWidget(self.edit_unite, 1, 1)
        formulaire_achat.addWidget(lbl_quantite, 1, 2)
        formulaire_achat.addWidget(self.edit_quantite, 1, 3)
        formulaire_achat.addWidget(lbl_prix_unitaire, 2, 0)
        formulaire_achat.addWidget(self.edit_prix_unitaire, 2, 1)
        formulaire_achat.addWidget(lbl_montant, 2, 2)
        formulaire_achat.addWidget(self.edit_montant, 2, 3)
        frame_formulaire_achat  = QFrame()
        frame_formulaire_achat.setObjectName("frame_row_one")
        frame_formulaire_achat.setLayout(formulaire_achat)

        
        row_two_commande = QHBoxLayout()
        row_two_commande.addWidget(frame_form_set_grid_fournisseur_commande, 40)
        row_two_commande.addWidget(frame_formulaire_achat, 60)
        
        frame_row_two_commande  = QFrame()
        frame_row_two_commande.setLayout(row_two_commande)
        
        #  row three#
    
        self.Table_commande = QTableWidget()
        self.Table_commande.setColumnCount(5)
        self.Table_commande.verticalHeader().setVisible(False)
        self.Table_commande.setHorizontalHeaderLabels(["Désignation", "Unité", "Prix-unitaire", "Quantité"," Montant"])
        self.Table_commande.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.Table_commande.cellClicked.connect(self.selectionner_une_ligne) 
        
        lbl_montant_total_achat = QLabel("MONTANT TOTAL")
        lbl_montant_total_achat.setStyleSheet("margin-left : 500px;")
        self.edit_montant_total_achat = QLineEdit()
        self.edit_montant_total_achat.textChanged.connect(self.envoyer_vers_commande)
        
        grid_montant = QGridLayout()
        grid_montant.addWidget(lbl_montant_total_achat, 0, 1)
        grid_montant.addWidget(self.edit_montant_total_achat, 0, 2)
        qv__montant = QVBoxLayout()
        qv__montant.addLayout(grid_montant) 
        
        box_table_commande = QVBoxLayout()
        box_table_commande.addWidget(self.Table_commande)
        box_table_commande.addLayout(qv__montant)
        frame_table_commande = QFrame()
        frame_table_commande.setObjectName("frame_row_one")
        frame_table_commande.setLayout(box_table_commande)
        
        
        btn_actualiser__commande = QPushButton("Actualiser")
        icon_act= QIcon("icon/actualiser.png")
        btn_actualiser__commande.setObjectName("btn_nouveau_vente")
        btn_actualiser__commande.setIcon(icon_act)
        btn_actualiser__commande.clicked.connect(self.afficher_commande)
        btn_valider__commande = QPushButton("Valider")
        btn_valider__commande.setObjectName("btn_nouveau_vente")
        icon_val= QIcon("icon/valide.png")
        btn_valider__commande.setIcon(icon_val)
        btn_valider__commande.clicked.connect(self.validation)
        btn_modifier__commande = QPushButton("Modifier")
        btn_modifier__commande.setObjectName("btn_nouveau_vente")
        icon_mod= QIcon("icon/modifier.jpg")
        btn_modifier__commande.setIcon(icon_mod)
        btn_modifier__commande.clicked.connect(self.modifier_achat)       
        btn_supprimer__commande = QPushButton("Supprimer")
        btn_supprimer__commande.setObjectName("btn_nouveau_vente")
        icon_sup= QIcon("icon/supprimer.png")
        btn_supprimer__commande.setIcon(icon_sup)
        btn_supprimer__commande.clicked.connect(self.effacer_achat)
        
        btn_actualiser__commande.setStyleSheet("margin : 0 auto")
        btn_valider__commande.setStyleSheet("margin : 0 auto")
        btn_modifier__commande.setStyleSheet("margin : 0 auto")
        btn_supprimer__commande.setStyleSheet("margin : 0 auto")
        
        
        btns_commande = QVBoxLayout()
        btns_commande.addWidget(btn_actualiser__commande)
        btns_commande.addWidget(btn_valider__commande)
        btns_commande.addWidget(btn_modifier__commande)
        btns_commande.addWidget(btn_supprimer__commande)
        frame_btns_commande = QFrame()
        frame_btns_commande.setObjectName("frame_row_one")
        frame_btns_commande.setLayout(btns_commande)
        
        row_three_commande = QHBoxLayout()
        row_three_commande.addWidget(frame_table_commande, 70)
        row_three_commande.addWidget(frame_btns_commande, 18)
        frame_row_three_commande = QFrame()
        frame_row_three_commande.setLayout(row_three_commande)
        #___________________layout__________________________
        
        mainLayout_achats = QVBoxLayout()
        mainLayout_achats.addWidget(self.frame_row_one)
        mainLayout_achats.addWidget(frame_row_two_commande)
        mainLayout_achats.addWidget(frame_row_three_commande)
        
        self.edit_unite.installEventFilter(self)
        self.edit_prix_unitaire.installEventFilter(self)
        self.edit_montant.installEventFilter(self)
        self.edit_prix_unitaire.installEventFilter(self)
        self.edit_quantite.installEventFilter(self)
        self.calcul_montant()
        self.afficher_commande()
        self.envoyer_vers_commande()
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
            QLineEdit { background-color: #FFFFFF; border: 1px solid #BFE6C3; border-radius: 8px; padding: 8px; font: 16px "Segoe UI"; color: #08321f; }
            QLineEdit:read-only { background-color: #F0FFF3; color: #2e7d32; }
            QComboBox { background-color: #FFFFFF; border: 1px solid #BFE6C3; border-radius: 8px; padding: 6px; font: 16px "Segoe UI"; color: #08321f; }
            QComboBox::drop-down { border: none; }
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
            QHeaderView::section { background: qlineargradient(x1:0,y1:0,x2:0,y2:1, stop:0 #43A047, stop:1 #2E7D32) ;color: white; font: bold 16px "Segoe UI"; padding: 8px; border: none; }
            QTableWidget::item { padding: 8px; }
            QTableWidget::item:selected { background-color: #BEE6C5; color: #0b3d2e; }
            QTableCornerButton::section { background-color: #1B5E20; border: none; }
        """)
        self.setLayout(mainLayout_achats)
        
    def formulaire_fourni(self):
        cur = self.conn.cursor()
        cur = self.conn.cursor()
        nom = self.edit_combo_nom_fournisseur.currentText()
        cur.execute("SELECT adresseF, tel FROM fournisseur WHERE nomF = ?", (nom, ))
        result = cur.fetchone()
        if result:
            print(result)
            a , t = result 
            self.adresse_fourni.setText(a)
            self.edit_tel.setText(t)  
            
        
    def next(self):
        cur = self.conn.cursor()
        cur.execute("SELECT No FROM achat ORDER BY No")
        codes = [row[0] for row in cur.fetchall()]
        print(codes)
        if codes : 
            for i in codes:
                print(i)
                next = i + 1           
                
            return next
        else:
            return 1
    def calcul_montant(self):
        try:
            a = self.edit_prix_unitaire.text()
            b = self.edit_quantite.text()
            if a != "" and b !="":
                if a.isdigit() and b.isdigit():
                    c = float(a)*float(b)  
                    self.edit_montant.setText(str(c)) 
                    if self.edit_unite.text().strip() =="":
                        QMessageBox.information(self, "Erreur","champ invalide, veuillez vérifier")
                    else:
                        self.edit_ticket_vente.setText(str(self.next()))
                        
                        print(self.next())                      
        except ValueError:
            QMessageBox.information(self, "Erreur","champ invalide, veuillez vérifier")
              
    def get_nom_fourni(self):
        cur = self.conn.cursor()
        cur.execute("SELECT nomF FROM fournisseur")
        return [row[0] for row in cur.fetchall()] 
    def mise_a_jour_nom_fourni(self):
        self.edit_combo_nom_fournisseur.clear()
        cursor = self.conn.cursor()
        cursor.execute("SELECT nomF FROM fournisseur")
        noms =[row[0] for row in cursor.fetchall()]
        self.edit_combo_nom_fournisseur.addItems(noms)
    def verifier_modification_fourni(self):
        nouveau_nom =  self.get_nom_fourni()
        if(nouveau_nom != self.nom_fourni):
            self.mise_a_jour_nom_fourni()
    
    def get_nom_medic(self):
        cur = self.conn.cursor()
        cur.execute("SELECT nomM FROM medicament")
        return [row[0] for row in cur.fetchall()] 
    def mise_a_jour_nom_medic(self):
        self.combo_designation.clear()
        cursor = self.conn.cursor()
        cursor.execute("SELECT nomM FROM medicament")
        noms =[row[0] for row in cursor.fetchall()]
        self.combo_designation.addItems(noms)
        
    def verifier_modification_designation(self):
        nouveau_medic =  self.get_nom_medic()
        if(nouveau_medic != self.nom_medic):
            self.mise_a_jour_nom_medic()
     
           
    def creer_table_achat(self):
        cursor = self.conn.cursor()
        cursor.execute("""
                       CREATE TABLE IF NOT EXISTS achat(
                            No INTEGER PRIMARY KEY AUTOINCREMENT, 
                            design VARCHAR(100),
                            unite VARCHAR(100),
                            prix_unit VARCHAR(100),
                            quantite VARCHAR(100),
                            montant VARCHAR(100)
                       )
                       """)
        
        self.conn.commit() 
    def insertion_Val(self):
        self.select = None
        design = self.combo_designation.currentText().upper()
        unite = self.edit_unite.text().strip().upper()
        prix_unit = self.edit_prix_unitaire.text().strip()
        quantite = self.edit_quantite.text().strip()
        montant = self.edit_montant.text().strip()
        cur = self.conn.cursor() 
        if unite and prix_unit and quantite and montant :
            
            cur.execute("INSERT INTO achat (design, unite, prix_unit, quantite, montant) VALUES (?, ?, ?, ?, ?)", (design, unite, prix_unit, quantite, montant))
            self.conn.commit()
            self.calcul_total()
            self.afficher_commande()
        else:
            QMessageBox.information(self, "Information", "champ invalide, veuillez vérifier")
            return
    def eventFilter(self, source,  event):
        if event.type() == event.KeyPress and event.key()==Qt.Key_Return:
            if source in (self.edit_unite, self.edit_prix_unitaire, self.edit_quantite, self.edit_montant):
                self.insertion_Val()
                self.afficher_commande()
                return True
        return super().eventFilter(source, event)
                
    def afficher_commande(self):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM achat") 
        row = cur.fetchall() 
        self.Table_commande.setRowCount(len(row))
        for i , (No, design, unite, prix_unit, quantite, montant) in enumerate(row):
            self.Table_commande.setItem(i, 0, QTableWidgetItem(design))
            self.Table_commande.setItem(i, 1, QTableWidgetItem(unite))
            self.Table_commande.setItem(i, 2, QTableWidgetItem(prix_unit))
            self.Table_commande.setItem(i, 3, QTableWidgetItem(quantite))
            self.Table_commande.setItem(i, 4, QTableWidgetItem(montant))
        self.edit_unite.clear()
        self.edit_prix_unitaire.clear()
        self.edit_quantite.clear()
        self.edit_montant.clear()
    
    def selectionner_une_ligne(self, row, column):
        select_lig = self.Table_commande.currentRow()
        d = self.Table_commande.item(row, 0).text()
        u = self.Table_commande.item(row, 1).text()
        p = self.Table_commande.item(row, 2).text()
        q = self.Table_commande.item(row, 3).text()
        m = self.Table_commande.item(row, 4).text()
        cur = self.conn.cursor()
        No =  cur.execute("SELECT No FROM achat LIMIT 1 OFFSET ?", (select_lig, )).fetchone()
        No = No[0]
        self.select = No
        
        self.combo_designation.setCurrentText(d)
        self.edit_unite.setText(u)
        self.edit_prix_unitaire.setText(p)
        self.edit_quantite.setText(q)
        self.edit_montant.setText(m)
    def modifier_achat(self):
        if not self.select:
            QMessageBox.information(self, "Information", "Veuillez sélectionner une ligne à modifier")
            return
        design = self.combo_designation.currentText()
        unite = self.edit_unite.text().strip()
        prix_unit = self.edit_prix_unitaire.text().strip()
        quantite = self.edit_quantite.text().strip()
        montant = self.edit_montant.text().strip()
        
        if unite and prix_unit and quantite and montant:
            cur = self.conn.cursor()
            cur.execute("UPDATE achat SET design = ?, unite = ?, prix_unit = ?, quantite = ?, montant = ? WHERE No = ? ", (design, unite, prix_unit, quantite, montant, self.select))
            self.conn.commit()
        else: 
            QMessageBox.information(self, "Information", "Veuillez sélectionner une ligne à modifier")
            return
        self.calcul_total()
        self.afficher_commande()
        self.edit_unite.clear()
        self.edit_prix_unitaire.clear()
        self.edit_quantite.clear()
        self.edit_montant.clear()
        self.select = None
        
    def effacer_achat(self):
        if not self.select:
            QMessageBox.information(self, "Information", "Veuillez sélectionner une ligne à supprimer")
            return
        reponse  = QMessageBox.question(self, "confirmation", f"Supprimer la code {self.select}?", QMessageBox.Yes | QMessageBox.No)
        if reponse ==QMessageBox.Yes:
            cur = self.conn.cursor()
            cur.execute("DELETE FROM achat WHERE No = ?", (self.select,))
            self.conn.commit()
        self.calcul_total()    
        self.afficher_commande()
        self.edit_unite.clear()
        self.edit_prix_unitaire.clear()
        self.edit_quantite.clear()
        self.edit_montant.clear()
        self.select = None
    def calcul_total(self):
        cur = self.conn.cursor()
        cur.execute("SELECT SUM(montant) FROM achat")
        resultat = cur.fetchone()
        total = resultat[0] if resultat[0] is not None else 0
        print(total)
        self.edit_montant_total_achat.setText(str("%.2f" %total))
    def envoyer_vers_commande(self):
        total = self.edit_montant_total_achat.text()
        nomF = self.edit_combo_nom_fournisseur.currentText()
        adresseF = self.adresse_fourni.text()
        tel = self.edit_tel.text()
        self.App_commande.recevoir_donnees(total, nomF, adresseF, tel)
    
    def validation(self):
        self.App_commande.show() 
        
    def compter_achat():
        import sqlite3
        conn = sqlite3.connect("MonProjet.db")
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM achat")
        resultat = cursor.fetchone()[0]
        conn.close()
        return str(resultat)