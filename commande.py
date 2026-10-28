import sys, json
import sqlite3
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtPrintSupport import QPrinter, QPrintDialog
from PyQt5.QtGui import QTextDocument

class App_commande(QWidget):
    def __init__(self):
        super().__init__()
        self.conn = sqlite3.connect("MonProjet.db")
        self.setWindowTitle("Bon de commande")
        
        # Logo
        logo_projet = QPixmap("image/sary.png")
        image_projet = QLabel()
        image_projet.setPixmap(logo_projet)
        image_projet.setFixedSize(110, 100)
        image_projet.setScaledContents(True)
        
        # Titre
        LABEL = QLabel("BON DE COMMANDE (BC)")
        LABEL.setStyleSheet("qproperty-alignment: AlignCenter; font: bold 26px;")
        
        row1 = QHBoxLayout()
        row1.addWidget(image_projet)
        row1.addWidget(LABEL)
        row1.setContentsMargins(0, 0, 0, 5)
        
        row1_frame = QFrame()
        row1_frame.setLayout(row1) 
        row1_frame.setContentsMargins(0, 0, 0, 0)
        
        # BC No et Date
        self.label_bc_val = QLabel("1")
        form1 = QFormLayout()
        form1.addRow("BC No: ", self.label_bc_val)
        
        self.date_val = QLabel(QDate.currentDate().toString("dd-MM-yyyy"))
        form2 = QFormLayout()
        form2.addRow("Date: ", self.date_val)
        
        row2 = QHBoxLayout()
        row2.addLayout(form1)
        row2.addLayout(form2)
        
        # Infos pharmacie
        self.pharma = QLabel("PHARMACIE...")
        self.adresse_val = QLabel("ISPM Antsobolo")
        self.tel_val = QLabel("034...")
        form3 = QFormLayout()
        form3.addRow("Adresse: ", self.adresse_val)
        form3.addRow("Téléphone: ", self.tel_val)
        
        qv = QVBoxLayout()
        qv.addWidget(self.pharma)
        qv.addLayout(form3)
        qv.addStretch()
        
        form3_frame = QFrame()
        form3_frame.setLayout(qv)
        form3_frame.setObjectName("frame")
        form3_frame.setContentsMargins(0, 0, 100, 0)
        
        # Infos fournisseur
        self.nom_f = QLabel("ISPM Antsobolo")
        self.adresse_val_f = QLabel("ISPM Antsobolo")
        self.tel_val_f = QLabel("033...")
        form4 = QFormLayout()
        form4.addRow("Fournisseur: ", self.nom_f)
        form4.addRow("Adresse: ", self.adresse_val_f)
        form4.addRow("Téléphone: ", self.tel_val_f)
        form4_frame = QFrame()
        form4_frame.setLayout(form4)
        form4_frame.setObjectName("frame")
        
        form3_add_form4 = QHBoxLayout()
        form3_add_form4.addWidget(form3_frame)
        form3_add_form4.addWidget(form4_frame)
        form3_add_form4.setContentsMargins(0, 0, 0, 10)
        
        # Table commande
        self.Table_commande = QTableWidget()
        self.Table_commande.setColumnCount(6)
        self.Table_commande.verticalHeader().setVisible(False)
        self.Table_commande.setHorizontalHeaderLabels(
            ["Produit", "Désignation", "Unité", "Prix-unitaire", "Quantité","Montant"])
        self.Table_commande.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        
        # Montant total
        lbl_total_achat = QLabel("MONTANT TOTAL")
        lbl_total_achat.setStyleSheet("margin-left : 500px;")
        self.edit_total = QLineEdit()
        self.edit_total.setReadOnly(True)
        
        form5 = QFormLayout()
        form5.addRow(lbl_total_achat, self.edit_total)
        
        # Signatures
        
        
        # Bouton imprimer
        btn_imprimer = QPushButton("Imprimer")
        btn_imprimer.setStyleSheet("background-color: blue; color: white; font-weight: bold; padding:5px 15px;")
        btn_imprimer.clicked.connect(self.imprimer_facture)
        btn_layout = QHBoxLayout()
        btn_layout.addStretch()
        btn_layout.addWidget(btn_imprimer)
        

        
        # Layout principal
        layout = QVBoxLayout()
        layout.addWidget(row1_frame)
        layout.addLayout(row2)
        layout.addLayout(form3_add_form4)
        layout.addWidget(self.Table_commande)
        layout.addLayout(form5)
        
        layout.addLayout(btn_layout)
        
        self.setLayout(layout)
        self.afficher_commande()
        self.setStyleSheet(self.stylesheet())
    
    
    def afficher_commande(self):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM achat") 
        rows = cur.fetchall()
        self.Table_commande.setRowCount(len(rows))
        total = 0
        for i, (No, design, unite, prix_unit, quantite, montant) in enumerate(rows):
            self.Table_commande.setItem(i, 0, QTableWidgetItem(str(No)))
            self.Table_commande.setItem(i, 1, QTableWidgetItem(design))
            self.Table_commande.setItem(i, 2, QTableWidgetItem(unite))
            self.Table_commande.setItem(i, 3, QTableWidgetItem(str(prix_unit)))
            self.Table_commande.setItem(i, 4, QTableWidgetItem(str(quantite)))
            self.Table_commande.setItem(i, 5, QTableWidgetItem(str(montant)))
            total += float(montant)
            
            with open("c:/Users/ME-PC/Desktop/JHONY/projet_gsp/a.json", "r") as f:
                data = json.load(f)
            data["a"] += int(quantite)
            with open("c:/Users/ME-PC/Desktop/JHONY/projet_gsp/a.json", "w") as f:
                json.dump(data, f, indent = 4)    
        self.edit_total.setText(str(total))
    
    def recevoir_donnees(self, total, nomF, adresseF, tel):
        self.edit_total.setText(total)
        self.nom_f.setText(nomF)
        self.adresse_val_f.setText(adresseF)
        self.tel_val_f.setText(tel)
        self.afficher_commande()
        
    def closeEvent(self, event):
        r = QMessageBox.question(self, "Information", "Voulez-vous fermer la fenêtre ?", QMessageBox.Yes | QMessageBox.No)
        if r == QMessageBox.Yes:
            cur = self.conn.cursor()
            cur.execute("DELETE FROM achat")
            self.conn.commit()
            event.accept()
        else:
            event.ignore()
    
    def imprimer_facture(self):
        printer = QPrinter(QPrinter.HighResolution)
        dialog = QPrintDialog(printer, self)
        if dialog.exec_() == QDialog.Accepted:
            doc = QTextDocument()
            html = "<h2>BON DE COMMANDE</h2><table border='1' cellspacing='0' cellpadding='4'>"
            html += "<tr><th>Produit</th><th>Désignation</th><th>Unité</th><th>Prix-unitaire</th><th>Quantité</th><th>Montant</th></tr>"
            for i in range(self.Table_commande.rowCount()):
                html += "<tr>"
                for j in range(self.Table_commande.columnCount()):
                    html += f"<td>{self.Table_commande.item(i,j).text()}</td>"
                html += "</tr>"
            html += "</table>"
            html += f"<p><b>Total: {self.edit_total.text()}</b></p>"
            doc.setHtml(html)
            doc.print_(printer)
    
    def stylesheet(self):
        return """
            QLabel{
                border: none;
                font : 16px;
            }
            QFrame#frame{
                border: 1px solid gray;
                max-height: 110px;
            }
            QFrame#Frame{
                border: 1px solid gray;
                max-height: 150px;
            }
            QHeaderView::section{
                border : 1px solid black;
                font-size: 16px;
                background : lightgray;
                font: bold 16px;
            }
            QTableWidget::item:selected{
                background-color : rgba(174, 247, 174, 0.886);
                color : black;
                outline : none;
            }
            QTableWidget{
                border: 1px solid black;
                border-top: none;
                gridline-color: gray;
                background: transparent;
            }
        """

if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = App_commande()
    form.show()
    sys.exit(app.exec_())
