import sys, json
import sqlite3
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtPrintSupport import QPrinter, QPrintDialog

class App_fact(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.num_fact = 1
        self.parent = parent
        self.conn = sqlite3.connect("MonProjet.db")
        self.setWindowTitle("Bon de commande")
        self.setFixedSize(700, 800)

        # Logo et titre
        logo = QLabel()
        logo.setPixmap(QPixmap("image/sary.png").scaled(110, 100, Qt.KeepAspectRatio))
        titre = QLabel("______FACTURE______")
        titre.setStyleSheet("font: bold 26px; qproperty-alignment: AlignCenter;")
        header = QHBoxLayout()
        header.addWidget(logo)
        header.addWidget(titre)
        row1_frame = QFrame()
        row1_frame.setLayout(header)

        # Infos facture
        self.ticket = QLabel(f"FACT-{self.num_fact}")
        self.caissier = QLabel("....")
        self.tel_val = QLabel("034...")
        form_left = QFormLayout()
        form_left.addRow("Ticket N°:", self.ticket)
        form_left.addRow("Caissier:", self.caissier)
        form_left.addRow("Téléphone:", self.tel_val)
        frame_left = QFrame()
        frame_left.setLayout(form_left)

        self.date = QLabel(QDate.currentDate().toString("dd-MM-yyyy"))
        self.heure = QLabel(QTime.currentTime().toString("hh : mm : ss"))
        self.tel_val_f = QLabel("033...")
        form_right = QFormLayout()
        form_right.addRow("Date:", self.date)
        form_right.addRow("Heure:", self.heure)
        form_right.addRow("Téléphone:", self.tel_val_f)
        frame_right = QFrame()
        frame_right.setLayout(form_right)

        info_layout = QHBoxLayout()
        info_layout.addWidget(frame_left)
        info_layout.addWidget(frame_right)

        # Tableau facture
        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["Désignation", "Prix-unitaire", "Quantité", "Total"])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table.verticalHeader().setVisible(False)

        # Montant total
        self.edit_total = QLineEdit()
        lbl_total = QLabel("MONTANT TOTAL")
        form_total = QFormLayout()
        form_total.addRow(lbl_total, self.edit_total)

        # Montant détaillé
        self.montant_total = QLabel(" ")
        self.remise = QLabel(" ")
        self.net_a_payer = QLabel(" ")
        vola = QFormLayout()
        vola.addRow("Montant Total:", self.montant_total)
        vola.addRow("Total Remise:", self.remise)
        vola.addRow("Net à Payer:", self.net_a_payer)
        frame_vola = QFrame()
        frame_vola.setLayout(vola)

        self.montant_verse = QLabel("")
        self.monnaie_R = QLabel("")
        self.mode = QLabel("")
        vola2 = QFormLayout()
        vola2.addRow("Montant Versé:", self.montant_verse)
        vola2.addRow("Montant Rendue:", self.monnaie_R)
        vola2.addRow("Mode de Paiement:", self.mode)
        frame_vola2 = QFrame()
        frame_vola2.setLayout(vola2)

        # Bouton imprimer (blue, droite ambany)
        btn_imprimer = QPushButton("Imprimer")
        btn_imprimer.setStyleSheet("background-color: blue; color: white; font-weight: bold; padding:5px 15px;")
        btn_imprimer.clicked.connect(self.imprimer_facture)
        btn_layout = QHBoxLayout()
        btn_layout.addStretch()
        btn_layout.addWidget(btn_imprimer)

        # Layout principal
        layout = QVBoxLayout()
        layout.addWidget(row1_frame)
        layout.addLayout(info_layout)
        layout.addWidget(self.table)
        layout.addLayout(form_total)
        qh = QHBoxLayout()
        qh.addWidget(frame_vola)
        qh.addWidget(frame_vola2)
        layout.addLayout(qh)
        layout.addLayout(btn_layout)

        self.setLayout(layout)
        self.setStyleSheet("""
            QLabel{font:14px;}
            QFrame{border:1px solid gray;}
            QHeaderView::section{border:1px solid black; background:lightgray; font:bold 16px;}
            QTableWidget::item:selected{background: rgba(174,247,174,0.9);}
        """)

    def afficher_facture(self):
        cur = self.conn.cursor()
        cur.execute("SELECT design, prix_unit, quantite, montant FROM vente") 
        rows = cur.fetchall()
        self.table.setRowCount(len(rows))

        for i, (design, prix_unit, quantite, montant) in enumerate(rows):
            self.table.setItem(i, 0, QTableWidgetItem(str(design)))
            self.table.setItem(i, 1, QTableWidgetItem(str(prix_unit)))
            self.table.setItem(i, 2, QTableWidgetItem(str(quantite)))
            self.table.setItem(i, 3, QTableWidgetItem(str(montant)))
            with open("c:/Users/ME-PC/Desktop/JHONY/projet_gsp/f.json", "r") as f:
                data = json.load(f)
            if design not in data:  
                data[design] =   int(quantite)
            else:
                data[design] +=  int(quantite)
            data = dict(sorted(data.items(), key=lambda item : item[1], reverse=True))
            with open("c:/Users/ME-PC/Desktop/JHONY/projet_gsp/f.json", "w") as f:
                json.dump(data, f, indent = 4) 
            


    def recevoir_donnees(self, montant, remise, payer, verse, mode):
        self.montant_total.setText(str(montant))
        self.edit_total.setText(str(montant))
        self.remise.setText(str(remise))
        self.net_a_payer.setText(str(payer))
        self.montant_verse.setText(str(verse))
        try:
            R = float(verse) - float(payer)
        except ValueError:
            QMessageBox.information(self, "Info", "Montant versé manquant")
            return
        self.monnaie_R.setText(str(max(R, 0)))
        self.mode.setText(mode)
        self.afficher_facture()

    def imprimer_facture(self):
        printer = QPrinter(QPrinter.HighResolution)
        dialog = QPrintDialog(printer, self)
        if dialog.exec_() == QDialog.Accepted:
            self.render(printer)

        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = App_fact()
    form.show()
    sys.exit(app.exec_())
