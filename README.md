Traqueur_fdr
@zlat
2024

Application destinée à gérer la répartition des tâches entre agents et les représenter dans une feuille de route globale d'un organisme.
But pédagogique personnel pour apprendre python via pyside6.

ORGANISATION
- ok [ une fenètre principale
- ok [ une feuille de style en qss
- ok [ layout conteneur et sous blocs (hors menu, tool, status) / 
- ok [ une barre de status en bas avec :
- ok --- un message timé
- ok --- une barre de progression
- ok --- un label status notification
- ok --- un label status user
- ok --- un label status timestamp du fichier de données
- ok --- un label status du dernier item log
- ok [ fichier conf pour les messages préenregistré (configparser)
- ok [ fichier ini pour le programme (configparser)
- ok [ une boite à outils (icones 32)
- ok [ un menu (icones 32)
- ok --- fichier / édition / A propos
- ok --- les actions associées au menu et toolbar
- ok [ une icone application (icones 512)
- ok [ dans le layout mid-W
- ok --- un Treeview pour les données json
- ok --- un TreeView pour les dir
- ok --- splitter pour séparer et ajuster
- ok [ un journal d'évènement appli (file et stdout)
- ok --- log file par jour
- ok --- créer un journal de log et archiver les actions
- ok --- nettoyer le msg info
- ok [ fenetre modale création entité
- ok [ fenetre modale création cible pour une entité
- ok [ fenetre modale boite à propos
- ok --- affiche le README file dans A propos

ACTION
- ok [ message bienvenue
- ok [ parser conf
- ok [ logger
- ok [ affiche dir
- ok [ boite dialogue fermeture
- ok [ fenetre modale création entité (via designer6)
- ok [ fenetre modale création cible (via designer6)
- ok [ fenetre modale A propos (via designer6)

TODO
- todo revoir box cible pour ajouter une cible à choisir parmi
- todo enregistrer entité dans json

RESTE
- des fichiers json pour les données
- une fenètre noms des agents en arborescence et objectifs et ssobjectifs
- une fenètre avec leurs données (taches, parent, fils)
- une fenètre graphique avec des stats
- une fenètre graphique avec la feuille de route
- une fenetre de log pour profil appli et profil log
- nettoyer les notifications
- associer les user avec profil et logger
- associer les tips avec messages.conf et msglogger
- affiche json data
- Créer une entité
- Créer des cibles pour cette entité
- Créer des agents rattachés à l'entité et connecter à une cible
- Créer des objectifs pour une cible et connecter à un agent
- créer un organisme avec agents et objectif final visé
- affecter des taches aux agents et les positionner dans la feuille de route
- segmenter les taches par groupe en ligne
- cadencer les taches sur une ligne de temps
- générer des stats de réalisation de l'objectif final
- générer les stats de réalisation des agents
- exporter les graphes en png
- exporter la feuille de route en png
- extraire la fiche d'un agent et ses stats
- extraire la fiche de l'objectif principal et les réalisations
- remplacer les layout de la page principale par des splitters

STRUCTURE DES DONNÉES
- json entité : id, nom, code
- json cible de la feuille de route : id, id entité, nom, code
- json agent : id, nom, poste, code nom
- json tache : id, id cible rattachée, id agent arttaché, nom, description, actions constituantes, critère de réussite
