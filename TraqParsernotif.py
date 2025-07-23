# ----------------------------------------------------------------
# Parsernotif.py
# paramètre fichier, section et critère cherché
# renvoi valeur texte trouvée
# 20240828
# @Zlatko
# ----------------------------------------------------------------
import os
import configparser

def notif_cible_function(fichiernotif_cible, sectionnotif_cible, criterenotif_cible):
    """Récupère un message type de Messages.conf pour alimenter la barre d'information de l'application. Le fichier Messages.conf est structuré comme un ini.

    Args:
        fichiernotif_cible (file): Le fichier Messages.conf
        sectionnotif_cible (txt): La section contenant le message à afficher
        criterenotif_cible (txt): Pointe vers la notification souhaitée

    Returns:
        txt: La notification
    """

    # ----------------------------------------------------------------
    # Retour de la valeur du paramètre
    nomfichiernotif = os.path.join(os.getcwd(),'',fichiernotif_cible)
    nomsectionnotif = sectionnotif_cible
    nomcriterenotif = criterenotif_cible
    Parsernotif = configparser.ConfigParser()
    Parsernotif.read(nomfichiernotif)
    try:
        Parsernotif.get(nomsectionnotif, nomcriterenotif)
        valeurnotif_cible = Parsernotif.get(nomsectionnotif, nomcriterenotif)
        #print(f"{nomcriterenotif}:", valeurnotif_cible)
        # 
        # a journaliser INFO
        # 
    except configparser.NoOptionError:        
        print(f"No option '{nomcriterenotif}'")
        # 
        # a journaliser ERROR
        # 
        
    # ----------------------------------------------------------------
    # journalisation
    
    return valeurnotif_cible
