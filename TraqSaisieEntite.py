# ----------------------------------------------------------------
# TraqSaisieEntite.py
# ouvre une fenetre formulaire de saisie d'une entité
# alimente json entité
# 20260422
# @Zlatko
# ----------------------------------------------------------------

import sys
import json
import os
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QTabWidget, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QTextEdit, QMessageBox, QTableWidget, QTableWidgetItem
)

class Application(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gestion des données")

        # Chemin du fichier JSON
        self.fichier_json = "donnees.json"

        # Initialisation des données
        self.donnees = []
        self.charger_donnees()

        # Création des onglets
        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)

        # Onglet 1 : Saisie des informations
        self.onglet_saisie = QWidget()
        self.tabs.addTab(self.onglet_saisie, "Saisie")

        # Onglet 2 : Affichage des données
        self.onglet_affichage = QWidget()
        self.tabs.addTab(self.onglet_affichage, "Affichage")

        # Interface de saisie
        self.creer_interface_saisie()

        # Interface d'affichage
        self.creer_interface_affichage()

    def creer_interface_saisie(self):
        layout = QVBoxLayout()

        # Exemple de champs de saisie
        self.nom_input = QLineEdit()
        self.age_input = QLineEdit()

        layout.addWidget(QLabel("Nom:"))
        layout.addWidget(self.nom_input)
        layout.addWidget(QLabel("Âge:"))
        layout.addWidget(self.age_input)

        # Bouton pour ajouter des données
        self.bouton_ajouter = QPushButton("Ajouter")
        self.bouton_ajouter.clicked.connect(self.ajouter_donnees)
        layout.addWidget(self.bouton_ajouter)

        self.onglet_saisie.setLayout(layout)

    def creer_interface_affichage(self):
        layout = QVBoxLayout()

        # Tableau pour afficher les données
        self.tableau_donnees = QTableWidget()
        self.actualiser_tableau()
        layout.addWidget(self.tableau_donnees)

        self.onglet_affichage.setLayout(layout)

    def ajouter_donnees(self):
        nom = self.nom_input.text()
        age = self.age_input.text()

        if nom and age:
            self.donnees.append({"nom": nom, "age": age})
            self.sauvegarder_donnees()
            self.actualiser_tableau()
            self.nom_input.clear()
            self.age_input.clear()
        else:
            QMessageBox.warning(self, "Erreur", "Veuillez remplir tous les champs.")

    def actualiser_tableau(self):
        self.tableau_donnees.setRowCount(len(self.donnees))
        self.tableau_donnees.setColumnCount(2)
        self.tableau_donnees.setHorizontalHeaderLabels(["Nom", "Âge"])

        for i, donnee in enumerate(self.donnees):
            self.tableau_donnees.setItem(i, 0, QTableWidgetItem(donnee["nom"]))
            self.tableau_donnees.setItem(i, 1, QTableWidgetItem(donnee["age"]))

    def charger_donnees(self):
        if os.path.exists(self.fichier_json):
            with open(self.fichier_json, 'r') as file:
                self.donnees = json.load(file)

    def sauvegarder_donnees(self):
        with open(self.fichier_json, 'w') as file:
            json.dump(self.donnees, file, indent=4)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Application()
    window.show()
    sys.exit(app.exec())
