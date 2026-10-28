import sys
import time
import sqlite3

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from liste_medic import*
from facture import App_fact 
class Vente(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("fournisseur")
        self.conn = sqlite3.connect("MonProjet.db")
        self.creerTableVente()
        self.fact = App_fact()
        
        #  row one    #
        self.lbl_gestion_vente = QLabel("Gestion des ventes")
        self.lbl_gestion_vente.setObjectName("lbl_gestion_vente")

        self.lbl_ticket_vente = QLabel("Ticket")
        self.lbl_ticket_vente.setObjectName("lbl_ticket_vente")

        self.edit_ticket_vente = QLineEdit()
        self.edit_ticket_vente.setObjectName("edit_ticket_vente")
        self.edit_ticket_vente.setFixedWidth(200)
        self.edit_ticket_vente.setPlaceholderText("Numéro du ticket")

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
        
        
        lbl_montant_total = QLabel("Montant total")
        lbl_montant_total.setStyleSheet("background: qlineargradient(x1:0,y1:0,x2:0,y2:1, stop:0 #43A047, stop:1 #2E7D32);padding-left: 20px; padding-right:60px ;color: white;font-family: 'Nunito Sans Light', sans-serif;font-size: 15px")
        self.edit_montant_total = QLineEdit() 
        lbl_montant_verse = QLabel("Montant versé")
        lbl_montant_verse.setStyleSheet("background: qlineargradient(x1:0,y1:0,x2:0,y2:1, stop:0 #43A047, stop:1 #2E7D32);padding-left: 20px; padding-right:30px ; margin-left: 80px;color: white;font-family: 'Nunito Sans Light', sans-serif;font-size: 15px")
        
        self.edit_montant_verse = QLineEdit() 
        self.edit_montant_verse.textChanged.connect(self.calcul_monnaie_rendue)
        lbl_total_remise = QLabel("Total remise")
        lbl_total_remise.setStyleSheet("background: qlineargradient(x1:0,y1:0,x2:0,y2:1, stop:0 #43A047, stop:1 #2E7D32);padding-left: 20px; padding-right:35px ;color: white;font-family: 'Nunito Sans Light', sans-serif;font-size: 15px")
        self.edit_total_remise = QLineEdit() 
        lbl_monnaie_rendue= QLabel("Monnaie rendue")
        lbl_monnaie_rendue.setStyleSheet("background: qlineargradient(x1:0,y1:0,x2:0,y2:1, stop:0 #43A047, stop:1 #2E7D32);padding-left: 20px; padding-right:335px ;margin-left: 80px;color: white;font-family: 'Nunito Sans Light', sans-serif;font-size: 15px")
        self.edit_monnaie_rendue = QLineEdit() 
        lbl_net_payer = QLabel("Net à payer ")
        lbl_net_payer.setStyleSheet("background: qlineargradient(x1:0,y1:0,x2:0,y2:1, stop:0 #43A047, stop:1 #2E7D32);padding-left: 20px; padding-right:35px ;color: white;font-family: 'Nunito Sans Light', sans-serif;font-size: 15px")
        self.edit_net_payer  = QLineEdit() 
        lbl_mode_paiement = QLabel("Mode paiement")
        lbl_mode_paiement.setStyleSheet("background: qlineargradient(x1:0,y1:0,x2:0,y2:1, stop:0 #43A047, stop:1 #2E7D32);padding-left: 20px; padding-right:35px ;margin-left: 80px ;color: white;font-family: 'Nunito Sans Light', sans-serif;font-size: 15px")
        self.edit_mode_paiement= QComboBox() 
        self.edit_mode_paiement.addItems(["Espèces", "Chèque", "Autres"])
        
        grid_formulaire_vente = QGridLayout()
        grid_formulaire_vente.addWidget(lbl_montant_total, 0, 0)
        grid_formulaire_vente.addWidget(self.edit_montant_total, 0, 1)
        grid_formulaire_vente.addWidget(lbl_montant_verse, 0, 2)
        grid_formulaire_vente.addWidget(self.edit_montant_verse, 0, 3)
        grid_formulaire_vente.addWidget(lbl_total_remise, 1, 0)
        grid_formulaire_vente.addWidget(self.edit_total_remise, 1, 1)
        grid_formulaire_vente.addWidget(lbl_monnaie_rendue, 1, 2)
        grid_formulaire_vente.addWidget(self.edit_monnaie_rendue, 1, 3)
        grid_formulaire_vente.addWidget(lbl_net_payer, 2, 0)
        grid_formulaire_vente.addWidget(self.edit_net_payer, 2, 1)
        grid_formulaire_vente.addWidget(lbl_mode_paiement, 2, 2)
        grid_formulaire_vente.addWidget(self.edit_mode_paiement, 2, 3)
        
        
            
        # form
        form_setGrid_formulaire = QVBoxLayout()
        form_setGrid_formulaire.addLayout(grid_formulaire_vente)
        frame_form_setGrid_formulaire = QFrame()
        frame_form_setGrid_formulaire.setLayout(form_setGrid_formulaire)
        frame_form_setGrid_formulaire.setObjectName("frame_row_one")
        
        # form fin
        
        date_label = QLabel("Date :") 
        date_edit = QLineEdit()
        date_edit.setObjectName("date_edit_vente")
        date_edit.setText(time.strftime("%d - %m - %y"))
        
        grid_date = QGridLayout()
        grid_date.addWidget(date_label, 0, 0)
        grid_date.addWidget(date_edit, 0, 1)
        frame_grid_date  = QFrame()
        
        frame_grid_date.setLayout(grid_date)
        frame_grid_date.setObjectName("frame_row_one")
        btn_validation = QPushButton("Valider")
        icon_validation = QIcon("icon/valide.png")
        btn_validation.setIcon(icon_validation)
        btn_validation.clicked.connect(self.ouvrir_fact)
        btn_validation.setObjectName("btn_validation_vente")
       #8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888 
        btn_nouveau = QPushButton("Nouveau")
        icon_nou= QIcon("icon/nouveau (2).png")
        btn_nouveau.setIcon(icon_nou)
        btn_nouveau.clicked.connect(self.vider_champ)
        btn_nouveau.setObjectName("btn_validation_vente")
        #8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
        qv_btn_validation = QVBoxLayout()
        qv_btn_validation.addWidget(btn_validation)
        qv_btn_validation.addWidget(btn_nouveau)
        frame_btn_validation  = QFrame()
        frame_btn_validation.setObjectName("frame_row_one")
        
        frame_btn_validation.setLayout(qv_btn_validation)
        
        date_et_validation = QVBoxLayout()
        date_et_validation.addWidget(frame_grid_date)
        date_et_validation.addWidget(frame_btn_validation)
        fram_date_et_validation = QFrame()
        fram_date_et_validation.setObjectName("Validation")
        fram_date_et_validation.setLayout(date_et_validation)
        
        row_two_vente = QHBoxLayout()
        row_two_vente.addWidget(frame_form_setGrid_formulaire, 75)
        row_two_vente.addWidget(fram_date_et_validation, 25)
        
        
        frame_row_two_vente  = QFrame()
        frame_row_two_vente.setLayout(row_two_vente)
        
        #  row three#
        
        lbl_code_produit = QLabel("Code produit")
        lbl_code_produit.setStyleSheet("background: qlineargradient(x1:0,y1:0,x2:0,y2:1, stop:0 #43A047, stop:1 #2E7D32);padding-left: 20px; padding-right:20px ;color: white;font-family: 'Nunito Sans Light', sans-serif;font-size: 15px")
        self.edit_code_produit = QLineEdit()
        self.edit_code_produit.setObjectName("line_edit_vente")
        self.edit_code_produit.setFixedSize(200, 40)
        lbl_designation = QLabel("Désignation")
        lbl_designation.setStyleSheet("background: qlineargradient(x1:0,y1:0,x2:0,y2:1, stop:0 #43A047, stop:1 #2E7D32);padding-left: 20px; padding-right:20px ;color: white;font-family: 'Nunito Sans Light', sans-serif;font-size: 15px")
        self.edit_designation = QLineEdit()
        self.edit_designation.setFixedSize(200, 40)
        lbl_Prix_unitaire = QLabel("Prix_unitaire")
        lbl_Prix_unitaire.setStyleSheet("background: qlineargradient(x1:0,y1:0,x2:0,y2:1, stop:0 #43A047, stop:1 #2E7D32);padding-left: 20px; padding-right:20px ;color: white;font-family: 'Nunito Sans Light', sans-serif;font-size: 15px")
        self.edit_Prix_unitaire = QLineEdit()
        self.edit_Prix_unitaire.setFixedSize(200, 40)
        lbl_quantite = QLabel("Quantité")
        lbl_quantite.setStyleSheet("background: qlineargradient(x1:0,y1:0,x2:0,y2:1, stop:0 #43A047, stop:1 #2E7D32);padding-left: 20px; padding-right:20px ;color: white;font-family: 'Nunito Sans Light', sans-serif;font-size: 15px")
        self.edit_quantite= QLineEdit()
        self.edit_quantite.setFixedSize(200, 40)
        self.edit_quantite.textChanged.connect(self.afficher_stock_restante)
        self.edit_quantite.textChanged.connect(self.calcul_montant_total)
        lbl_total = QLabel("Total")
        lbl_total.setStyleSheet("background: qlineargradient(x1:0,y1:0,x2:0,y2:1, stop:0 #43A047, stop:1 #2E7D32);padding-left: 20px; padding-right:20px ;color: white;font-family: 'Nunito Sans Light', sans-serif;font-size: 15px")
        self.edit_total = QLineEdit()
        self.edit_total.setFixedSize(200, 40)
        lbl_Remise = QLabel("Remise")
        lbl_Remise.setStyleSheet("background: qlineargradient(x1:0,y1:0,x2:0,y2:1, stop:0 #43A047, stop:1 #2E7D32);padding-left: 20px; padding-right:20px ;color: white;font-family: 'Nunito Sans Light', sans-serif;font-size: 15px")
        self.edit_pourcentage= QLineEdit()
        self.edit_pourcentage.textChanged.connect(self.calcul_montant_net)
        label_pourcent = QLabel("%")
        self.valeur_pourcent = QLineEdit()
        lbl_Montant_net = QLabel("Montant net")
        lbl_Montant_net.setStyleSheet("background: qlineargradient(x1:0,y1:0,x2:0,y2:1, stop:0 #43A047, stop:1 #2E7D32);padding-left: 20px; padding-right:20px ;color: white;font-family: 'Nunito Sans Light', sans-serif;font-size: 15px")
        self.edit_Montant_net = QLineEdit()
        self.edit_Montant_net.setFixedSize(200, 40)
        
        ##################################################################################################""""""""""
        btn_recherche = QPushButton()
        btn_recherche.setStyleSheet("")
        btn_recherche.setObjectName("btn_r")
        icon_r =QIcon("icon/recherche1.png")
        btn_recherche.setIcon(icon_r)
    
        btn_recherche.clicked.connect(self.ouvrir_liste_medic)
        ##################################################################################################################
        
        grid_prod_vente = QGridLayout()
        grid_prod_vente.addWidget(lbl_code_produit, 0, 0)
        grid_prod_vente.addWidget(btn_recherche, 0, 3)
        grid_prod_vente.addWidget(self.edit_code_produit , 0, 1)
        grid_prod_vente.addWidget(lbl_designation, 1, 0)
        grid_prod_vente.addWidget(self.edit_designation, 1, 1)
        grid_prod_vente.addWidget(lbl_Prix_unitaire, 2, 0)
        grid_prod_vente.addWidget(self.edit_Prix_unitaire, 2, 1)
        grid_prod_vente.addWidget(lbl_quantite, 3, 0)
        grid_prod_vente.addWidget(self.edit_quantite, 3, 1)
        grid_prod_vente.addWidget(lbl_total, 4, 0)
        grid_prod_vente.addWidget(self.edit_total, 4, 1)
        grid_prod_vente.addWidget(lbl_Remise, 5, 0)
        grid_prod_vente.addWidget(self.edit_pourcentage, 5, 1)
        grid_prod_vente.addWidget(label_pourcent, 5, 2)
        grid_prod_vente.addWidget(self.valeur_pourcent, 5, 3)
        grid_prod_vente.addWidget(lbl_Montant_net, 6, 0)
        grid_prod_vente.addWidget(self.edit_Montant_net, 6, 1)
        
        qv_grid_prod_vente = QVBoxLayout()
        qv_grid_prod_vente.addLayout(grid_prod_vente)
        
        frame_prod_vente = QFrame()
        frame_prod_vente.setObjectName("frame_row_one")
        frame_prod_vente.setLayout(qv_grid_prod_vente)
        
        
        self.Table_vente = QTableWidget()
        self.Table_vente.setColumnCount(7)
        self.Table_vente.verticalHeader().setVisible(False)
        self.Table_vente.setHorizontalHeaderLabels(["Code produit", "Désignation", "Prix unitare", "Quantité", "Montant", "Remise", "Montant net"])
        self.Table_vente.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.Table_vente.setObjectName("frame_row_one")
        
        
        row_three_vente = QHBoxLayout()
        row_three_vente.addWidget(frame_prod_vente, 30)
        row_three_vente.addWidget(self.Table_vente, 70) 
        
        frame_row_three_vente = QFrame()
        frame_row_three_vente.setLayout(row_three_vente)
        
        
        #___________________layout__________________________
        
        mainLayout_ventes = QVBoxLayout()
        mainLayout_ventes.addWidget(self.frame_row_one)
        mainLayout_ventes.addWidget(frame_row_two_vente)
        mainLayout_ventes.addWidget(frame_row_three_vente)
        mainLayout_ventes.setContentsMargins(0, 0, 0, 0)
        self.edit_pourcentage.installEventFilter(self)
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
                background-color:white;
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
            QHeaderView::section { background: qlineargradient(x1:0,y1:0,x2:0,y2:1, stop:0 #43A047, stop:1 #2E7D32); color: white; font: bold 16px "Segoe UI"; padding: 8px; border: none; }
            QTableWidget::item { padding: 8px; }
            QTableWidget::item:selected { background-color: #BEE6C5; color: #0b3d2e; }
            QTableCornerButton::section { background-color: #1B5E20; border: none; }
        """)
        self.setLayout(mainLayout_ventes)
    def recevoir_donnees(self, c, d, p, called = False):
        self.edit_code_produit.setText(c)
        self.edit_designation.setText(d)
        self.edit_Prix_unitaire.setText(p)   
        
    def ouvrir_liste_medic(self):
        self.fenetre = Liste_medic(self)
        self.fenetre.show()
    
    
#####################################################################################################################
    def creerTableVente(self):
        cursor = self.conn.cursor()
        cursor.execute("""
                       CREATE TABLE IF NOT EXISTS vente(
                            code VARCHAR(100), 
                            design VARCHAR(100),
                            prix_unit VARCHAR(100),
                            quantite VARCHAR(100),
                            montant VARCHAR(100),
                            prise_val VARCHAR(100),
                            montant_net VARCHAR(100)
                       )
                       """)
        self.conn.commit()
        
    def calcul_montant_total(self):    
        
        try:
            p = self.edit_Prix_unitaire.text()
            q = float(self.edit_quantite.text())
        except ValueError:
            self.edit_quantite.clear()
            return
        PB = float(p) * q
        self.edit_total.setText(str("%.2f" %PB)) 
    def calcul_montant_net(self):      
        PB = self.edit_total.text()
        try:
            pourc = float(self.edit_pourcentage.text())
        except ValueError:
            return
        val = (float(PB) * pourc)/100
        self.valeur_pourcent.setText(str(val))
        net = float(PB) - val 
        self.edit_Montant_net.setText(str("%.2f" %net))
        
    def inserer_table_vente(self):
        code = self.edit_code_produit.text()
        design = self.edit_designation.text()
        Prix = self.edit_Prix_unitaire.text()
        quantite = self.edit_quantite.text()
        Total = self.edit_total.text()
        prise = self.valeur_pourcent.text()
        net = self.edit_Montant_net.text().strip()
        if net:
            cur = self.conn.cursor()
            cur.execute("""INSERT INTO vente (code, design , prix_unit, quantite, montant, prise_val, montant_net) 
                        VALUES  (?, ?, ?, ?, ?, ?, ?)""", (code, design, Prix, quantite, Total, prise, net))
            self.conn.commit()
            
    def afficher_vente(self):
        cur = self.conn.cursor()
        cur.execute("""SELECT vente.code, vente.design , vente.prix_unit, vente.quantite, vente.montant, vente.prise_val, vente.montant_net,medicament.quantiteStock  
                    FROM medicament
                    INNER JOIN vente
                    ON medicament.codeM = vente.code
                    WHERE medicament.quantiteStock >= vente.quantite 
                    """)
        row = cur.fetchall()
        self.Table_vente.setRowCount(len(row))
        for i, (a, b, c, d, e, f, j,h) in enumerate(row) :
            self.Table_vente.setItem(i, 0, QTableWidgetItem(a))
            self.Table_vente.setItem(i, 1, QTableWidgetItem(b))
            self.Table_vente.setItem(i, 2, QTableWidgetItem(c))
            self.Table_vente.setItem(i, 3, QTableWidgetItem(d))
            self.Table_vente.setItem(i, 4, QTableWidgetItem(e))
            self.Table_vente.setItem(i, 5, QTableWidgetItem(f))
            self.Table_vente.setItem(i, 6, QTableWidgetItem(j))
            d = int(d)
            h = int(h)
            stock = h-d
            if stock > 0:
                stock = str(stock)
                
                cursor = self.conn.cursor()
                cursor.execute("UPDATE medicament SET quantiteStock = ?  WHERE codeM = ?", (stock, a)) 
                self.conn.commit()     
            if stock == 0:
                cursor = self.conn.cursor()
                cursor.execute("DELETE FROM medicament WHERE codeM = ?", (a, )) 
                self.conn.commit()
        self.calcul__net__payer()
        self.calcul__total__remise()
        montanTotal = float(self.edit_net_payer.text()) + float(self.edit_total_remise.text())
        self.edit_montant_total.setText(str(montanTotal))
        
    def eventFilter(self, source,  event):
        if event.type() == event.KeyPress and event.key()==Qt.Key_Return:
            if source in (self.edit_pourcentage, self.edit_Montant_net):
                self.inserer_table_vente()
                self.afficher_vente()
                self.vider_input()
                return True
        return super().eventFilter(source, event)   
    def vider_input(self):
        self.edit_code_produit.clear()
        self.edit_designation.clear()
        self.edit_Prix_unitaire.clear()
        self.edit_quantite.clear()
        self.edit_total.clear()
        self.edit_pourcentage.clear()
        self.valeur_pourcent.clear()
        self.edit_Montant_net.clear()
    def afficher_stock_restante(self):

        nom = self.edit_designation.text()
        cur = self.conn.cursor()
        cur.execute("SELECT quantiteStock   FROM medicament WHERE nomM = ?", (nom, ))
        q = [row[0] for row in cur.fetchall()]
        print(q)
        if q : 
            for i in q:
                quantite = int(i)          

        try:
            quantite_entree = int(self.edit_quantite.text())
        except ValueError:
            return
        print(type(quantite_entree))
        
        print(quantite, quantite_entree)
        if quantite < quantite_entree:
            QMessageBox.information(self, "Information", "Stock insuffisante \n stock = "+str(quantite)) 
        #   QMessageBox.information(self,"Information",  "Champ invalide, veuillez vérifier") 
        
        
    def calcul__net__payer(self):
        cur = self.conn.cursor()
        cur.execute("SELECT SUM(montant_net) FROM vente")
        resultat = cur.fetchone()
        total = resultat[0] if resultat[0] is not None else 0
        self.edit_net_payer.setText(str("%.2f" %total))
    def calcul__total__remise(self):
        cur = self.conn.cursor()
        cur.execute("SELECT SUM(prise_val) FROM vente")
        resultat = cur.fetchone()
        total = resultat[0] if resultat[0] is not None else 0
        self.edit_total_remise.setText(str("%.2f" %total))
    def calcul_monnaie_rendue(self):
        try:
            M = float(self.edit_montant_verse.text())
        except ValueError:
            self.edit_montant_verse.clear()
            return
        M_rendue = M - float(self.edit_net_payer.text()) 
        self.edit_monnaie_rendue.setText(str(M_rendue))
    def ouvrir_fact(self):
        montant_total = self.edit_montant_total.text()
        remise = self.edit_total_remise.text()
        payer = self.edit_net_payer.text()
        verse = self.edit_montant_verse.text()
        mode =self.edit_mode_paiement.currentText()
        self.fact.recevoir_donnees(montant_total, remise, payer, verse, mode)
        self.fact.show()
    def  vider_champ(self):
        conn = sqlite3.connect("MonProjet.db")
        self.edit_montant_total.clear()
        self.edit_total_remise.clear()
        self.edit_net_payer.clear()
        self.edit_montant_verse.clear()
        
        cur = conn.cursor()
        self.edit_monnaie_rendue.clear()
        cur.execute("DELETE FROM vente")
        conn.commit()
        self.afficher_vente()
        
    def compter_vente():
        import sqlite3
        conn = sqlite3.connect("MonProjet.db")
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM vente")
        resultat = cursor.fetchone()[0]
        conn.close()
        return str(resultat)