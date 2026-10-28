
import sqlite3
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class Stock(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("")
        self.select = None
        self.conn = sqlite3.connect("MonProjet.db")
        
        #  row one    #
        lbl_stock = QLabel("Stock")
        lbl_stock.setStyleSheet("max-width : 300px; font: 24px 'Segoe UI';font-weight: 700;color: #0b3d2e;background: white;padding: 10px 14px;border-radius: 8px;")
        row_one_stock = QVBoxLayout()
        row_one_stock.addWidget(lbl_stock)
        frame_row_one_stock = QFrame()
        frame_row_one_stock.setStyleSheet("background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #EAF6EA, stop:1 #DFF2DF);padding: 10px 14px;border-radius: 8px;")
        frame_row_one_stock.setLayout(row_one_stock)
        
        #-------- row two
        
        
        lbl_code_medicament = QLabel("Code medicament")
        lbl_code_medicament.setStyleSheet("background: qlineargradient(x1:0,y1:0,x2:0,y2:1, stop:0 #43A047, stop:1 #2E7D32);padding-left: 20px; padding-right:20px ;color: white;font-family: 'Nunito Sans Light', sans-serif;font-size: 15px")
        self.edit_code_medicament = QLineEdit()
        lbl_nom_medicament = QLabel("Nom_medicament")
        lbl_nom_medicament.setStyleSheet("background: qlineargradient(x1:0,y1:0,x2:0,y2:1, stop:0 #43A047, stop:1 #2E7D32);padding-left: 20px; padding-right:20px ;color: white;font-family: 'Nunito Sans Light', sans-serif;font-size: 15px")
        self.edit_nom_medicament = QLineEdit() 
        lbl_famille = QLabel("Famille")
        lbl_famille.setStyleSheet("background: qlineargradient(x1:0,y1:0,x2:0,y2:1, stop:0 #43A047, stop:1 #2E7D32);padding-left: 20px; padding-right:95px ;color: white;font-family: 'Nunito Sans Light', sans-serif;font-size: 15px")
        self.edit_famille = QLineEdit() 
        lbl_quantite_actuelle = QLabel("Quantité actuelle")
        lbl_quantite_actuelle.setStyleSheet("background: qlineargradient(x1:0,y1:0,x2:0,y2:1, stop:0 #43A047, stop:1 #2E7D32);padding-left: 20px; padding-right:30px ;color: white;font-family: 'Nunito Sans Light', sans-serif;font-size: 15px")
        self.edit_quantite_actuelle = QLineEdit() 
        lbl_quantite_a_ajouter = QLabel("Quantite_à_ajouter")
        lbl_quantite_a_ajouter.setStyleSheet("background: qlineargradient(x1:0,y1:0,x2:0,y2:1, stop:0 #43A047, stop:1 #2E7D32);padding-left: 20px; padding-right:15px ;color: white;font-family: 'Nunito Sans Light', sans-serif;font-size: 15px")
        self.edit_quantite_a_ajouter = QLineEdit() 
        self.edit_quantite_a_ajouter.textChanged.connect(self.calcul_q)
        lbl_stock_mis_a_jour = QLabel("Stock mis à jour")
        lbl_stock_mis_a_jour.setStyleSheet("background: qlineargradient(x1:0,y1:0,x2:0,y2:1, stop:0 #43A047, stop:1 #2E7D32);padding-left: 20px; padding-right:35px ;color: white;font-family: 'Nunito Sans Light', sans-serif;font-size: 15px")
        self.edit_stock_mis_a_jour= QLineEdit() 
        lbl_date_entree= QLabel("Date d'entrée")
        lbl_date_entree.setStyleSheet("background: qlineargradient(x1:0,y1:0,x2:0,y2:1, stop:0 #43A047, stop:1 #2E7D32);padding-left: 20px; padding-right:50px ;color: white;font-family: 'Nunito Sans Light', sans-serif;font-size: 15px")
        self.edit_date_entree= QDateEdit() 
        lbl_date_prod = QLabel("Date de production")
        lbl_date_prod.setStyleSheet("background: qlineargradient(x1:0,y1:0,x2:0,y2:1, stop:0 #43A047, stop:1 #2E7D32);padding-left: 20px; padding-right:15px ;color: white;font-family: 'Nunito Sans Light', sans-serif;font-size: 15px")
        self.edit_date_prod = QDateEdit() 
        lbl_date_peremption = QLabel("Date de péremption")
        lbl_date_peremption.setStyleSheet("background: qlineargradient(x1:0,y1:0,x2:0,y2:1, stop:0 #43A047, stop:1 #2E7D32);padding-left: 20px; padding-right:10px ;color: white;font-family: 'Nunito Sans Light', sans-serif;font-size: 15px")
        self.edit_date_peremption = QDateEdit()
        
        btn_valider = QPushButton('Valider la mise à jour du stock')
        btn_valider.setStyleSheet("background: qlineargradient(x1:0,y1:0,x2:0,y2:1, stop:0 #43A047, stop:1 #2E7D32);padding-left: 20px; padding-right:15px ;min-width: 300px; min-height: 30px; color: white;")
        icon_act= QIcon("icon/valide.png")
        btn_valider.setIcon(icon_act)
        btn_valider.clicked.connect(self.modifier_medic)
        formulaire_stock = QFormLayout()
        formulaire_stock.addRow(lbl_code_medicament, self.edit_code_medicament)
        formulaire_stock.addRow(lbl_nom_medicament, self.edit_nom_medicament)
        formulaire_stock.addRow(lbl_famille, self.edit_famille)
        formulaire_stock.addRow(lbl_quantite_actuelle, self.edit_quantite_actuelle)
        formulaire_stock.addRow(lbl_quantite_a_ajouter, self.edit_quantite_a_ajouter)
        formulaire_stock.addRow(lbl_stock_mis_a_jour, self.edit_stock_mis_a_jour)
        formulaire_stock.addRow(lbl_date_entree, self.edit_date_entree)
        formulaire_stock.addRow(lbl_date_prod, self.edit_date_prod)
        formulaire_stock.addRow(lbl_date_peremption, self.edit_date_peremption)

        form_stock = QVBoxLayout()
        form_stock.addLayout(formulaire_stock)
        
        
        frame_form_stock = QFrame()
        frame_form_stock.setObjectName("frame_row_one")
        frame_form_stock.setLayout(form_stock)
        frame_form_stock.setStyleSheet("margin-top:13px;")
        colonne_btn_et_form = QVBoxLayout()
        colonne_btn_et_form.addWidget(frame_form_stock)
        colonne_btn_et_form.addWidget(btn_valider)
        # form colonne form et btn
        

        lbl_recherche= QLabel("Recherche")
        lbl_recherche.setStyleSheet("background: qlineargradient(x1:0,y1:0,x2:0,y2:1, stop:0 #43A047, stop:1 #2E7D32);padding-left: 20px; padding-right:20px ;color: white;font-family: 'Nunito Sans Light', sans-serif;font-size: 15px")
        self.edit_recherche= QLineEdit()
        self.edit_recherche.textChanged.connect(self.recherche_medic)
        self.edit_recherche.setFixedSize(250, 50)
        btn_actualiser__stock = QPushButton("Actualiser")
        btn_actualiser__stock.setObjectName("btn_nouveau_vente")
        icon_act= QIcon("icon/actualiser.png")
        btn_actualiser__stock.setIcon(icon_act)
        btn_actualiser__stock.clicked.connect(self.afficher_table_medic)
        btn_imprimer__stock = QPushButton("Imprimer")
        btn_imprimer__stock.setObjectName("btn_nouveau_vente")
        icon_impr= QIcon("icon/imprimer.png")
        btn_imprimer__stock.setIcon(icon_impr)
        
        recherche_et_btns = QHBoxLayout()
        recherche_et_btns.addWidget(lbl_recherche)
        recherche_et_btns.addWidget(self.edit_recherche)
        recherche_et_btns.addWidget(btn_actualiser__stock)
        recherche_et_btns.addWidget(btn_imprimer__stock)
        
        frame_recherche_et_btns  = QFrame()
        frame_recherche_et_btns.setObjectName("frame_row_one")
        frame_recherche_et_btns.setLayout(recherche_et_btns)
        
    
        self.Table_stock = QTableWidget()
        self.Table_stock.setColumnCount(7)
        self.Table_stock.verticalHeader().setVisible(False)
        self.Table_stock.setHorizontalHeaderLabels(["Code_médic...", "Médicament", "Famille", "Quantité","Date_entrée", "Date_prod...", "Date_pérem..."])
        self.Table_stock.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.Table_stock.cellClicked.connect(self.selectionner_une_ligne)
        self.Table_stock.setObjectName("frame_row_one")
        
        
        
        
        search_and_table = QVBoxLayout()
        search_and_table.addWidget(frame_recherche_et_btns)
        search_and_table.addWidget(self.Table_stock)

        frame_search_and_table = QFrame()
        frame_search_and_table.setLayout(search_and_table)
        
        row_two_stock = QHBoxLayout()
        row_two_stock.addLayout(colonne_btn_et_form, 30)
        row_two_stock.addWidget(frame_search_and_table, 70)
        frame_row_two_stock = QFrame()
        frame_row_two_stock.setLayout(row_two_stock)
        #___________________layout__________________________
        
        mainLayout_stock = QVBoxLayout()
        mainLayout_stock.setContentsMargins(0, 0, 0, 0)
        mainLayout_stock.addWidget(frame_row_one_stock)
        mainLayout_stock.addWidget(frame_row_two_stock)
        self.afficher_table_medic()
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
                background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #2e7d32, stop:1 #1b5e20);
                padding: 10px 14px;
                border-radius: 8px;
            }
            QLabel { font: 16px "Segoe UI"; color: #0b3d2e; padding: 4px 6px; }
            QLineEdit , QDateEdit{ background-color: #FFFFFF; border: 1px solid #BFE6C3; border-radius: 8px; padding: 8px; font: 16px "Segoe UI"; color: #08321f; }
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
            QHeaderView::section {background: qlineargradient(x1:0,y1:0,x2:0,y2:1, stop:0 #43A047, stop:1 #2E7D32); color: white; font: bold 16px "Segoe UI"; padding: 8px; border: none; }
            QTableWidget::item { padding: 8px; }
            QTableWidget::item:selected { background-color: #BEE6C5; color: #0b3d2e; }
            QTableCornerButton::section { background-color: #1B5E20; border: none; }
        """)
        self.setLayout(mainLayout_stock)

    
    def afficher_table_medic(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM medicament")
        row = cursor.fetchall()
        self.Table_stock.setRowCount(len(row))
        for i, (codeM, nomM, familleM, quantiteStock, p_a, pv, dateE, dateProd, datePeremp) in enumerate(row):
            self.Table_stock.setItem(i, 0, QTableWidgetItem(str(codeM)))
            self.Table_stock.setItem(i, 1, QTableWidgetItem(nomM))
            self.Table_stock.setItem(i, 2, QTableWidgetItem(familleM))
            self.Table_stock.setItem(i, 3, QTableWidgetItem(str(quantiteStock)))
            self.Table_stock.setItem(i, 4, QTableWidgetItem(str(dateE)))
            self.Table_stock.setItem(i, 5, QTableWidgetItem(str(dateProd)))
            self.Table_stock.setItem(i, 6, QTableWidgetItem(str(datePeremp)))
            
    def selectionner_une_ligne(self, row, column):
        codeM = self.Table_stock.item(row, 0).text()
        nomM = self.Table_stock.item(row, 1).text()
        familleM = self.Table_stock.item(row, 2).text()
        quantiteStock = self.Table_stock.item(row, 3).text()
        dateE = self.Table_stock.item(row, 4).text()
        dateProd = self.Table_stock.item(row, 5).text()
        datePeremp = self.Table_stock.item(row, 6).text()
        print(codeM, nomM, familleM, quantiteStock, dateE, dateProd, datePeremp)
        
        self.select = codeM
        self.edit_code_medicament.setText(codeM)
        self.edit_nom_medicament.setText(nomM)
        self.edit_famille.setText(familleM)
        self.edit_quantite_actuelle.setText(quantiteStock)
        d_e = QDate.fromString(dateE, "dd-MM-yyyy")
        self.edit_date_entree.setDate(d_e)
        print(d_e)
        self.edit_date_prod.setDate(QDate.fromString(dateProd, "dd-MM-yyyy"))
        self.edit_date_peremption.setDate(QDate.fromString(datePeremp, "dd-MM-yyyy"))
        print(self.select)
        
    def modifier_medic(self):
        if not self.select:
            QMessageBox.information(self, "Information", "Veuillez sélectionner une ligne à modifier")
            return
        
        r = QMessageBox.question(self, "Information", "voulez-vous mettre à jour le stock", QMessageBox.Yes | QMessageBox.No)
        if r ==QMessageBox.Yes:
            n = self.edit_nom_medicament.text().strip()
            f = self.edit_famille.text().strip()
            q_actuelle = self.edit_quantite_actuelle.text().strip()
            q_ajouter = self.edit_quantite_a_ajouter.text().strip()
            q_mise = self.edit_stock_mis_a_jour.text().strip()
            d_p = self.edit_date_prod.date().toString("dd-MM-yyyy")
            d_e = self.edit_date_entree.date().toString("dd-MM-yyyy")
            d_peremp = self.edit_date_peremption.date().toString("dd-MM-yyyy")
            
            if len(n) ==0 or len(f)==0 or int(q_ajouter)<=0 or int(q_actuelle)<=0 :
                QMessageBox.information(self, "Information", "champ invalide, veuillez vérifier")
                return
            if d_p <= d_e < d_peremp:
                self.conn = sqlite3.connect("MonProjet.db")
                cursor = self.conn.cursor()
                cursor.execute("UPDATE medicament  SET nomM=?, familleM = ?, quantiteStock = ?,dateE = ?, dateProd = ?,datePeremp = ? WHERE codeM = ?", (n, f, q_mise, d_e, d_p, d_peremp, self.select)) 
                self.conn.commit()
                self.edit_nom_medicament.clear()
                self.edit_famille.clear()
                self.edit_quantite_actuelle.clear()
                self.edit_quantite_a_ajouter.clear()
                self.edit_stock_mis_a_jour.clear()
                self.edit_date_prod.date().toString("dd-MM-yyyy")
                self.edit_date_entree.date().toString("dd-MM-yyyy")
                self.edit_date_peremption.date().toString("dd-MM-yyyy")
                self.select = None
            else:
                QMessageBox.warning(self, "Erreur de date", "Les dates doivent respecter: \n Date production <= Date entrée < Date péremption.")
            self.afficher_table_medic()
            
    def calcul_q(self):
        q_actuelle = self.edit_quantite_actuelle.text()
        q_ajouter = self.edit_quantite_a_ajouter.text()
        if q_actuelle.strip() !='':
            q1 = int (q_actuelle)
        else:
            q1 = 0
         
        if q_ajouter.strip() !='':
            q2 = int (q_ajouter)
        else:
            q2 = 0   
        r = q1 + q2
        self.edit_stock_mis_a_jour.setText(str(r))
    def recherche_medic(self):
        r = self.edit_recherche.text()
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM medicament WHERE nomM LIKE ?", (r + "%", ))
        row = cursor.fetchall()
        self.Table_stock.setRowCount(len(row))
        for i, (codeM, nomM, familleM, quantiteStock, p_a, pv, dateE, dateProd, datePeremp) in enumerate(row):
            self.Table_stock.setItem(i, 0, QTableWidgetItem(str(codeM)))
            self.Table_stock.setItem(i, 1, QTableWidgetItem(nomM))
            self.Table_stock.setItem(i, 2, QTableWidgetItem(familleM))
            self.Table_stock.setItem(i, 3, QTableWidgetItem(str(quantiteStock)))
            self.Table_stock.setItem(i, 4, QTableWidgetItem(str(dateE)))
            self.Table_stock.setItem(i, 5, QTableWidgetItem(str(dateProd)))
            self.Table_stock.setItem(i, 6, QTableWidgetItem(str(datePeremp)))