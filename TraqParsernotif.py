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

    # ----------------------------------------------------------------
    # Retour de la valeur du paramètre
    nomfichiernotif = os.path.join(os.getcwd(),'Python/Traqueur_fdr/',fichiernotif_cible)
    nomsectionnotif = sectionnotif_cible
    nomcriterenotif = criterenotif_cible
    Parsernotif = configparser.ConfigParser()
    Parsernotif.read(nomfichiernotif)
    try:
        Parsernotif.get(nomsectionnotif, nomcriterenotif)
        valeurnotif_cible = Parsernotif.get(nomsectionnotif, nomcriterenotif)
        print(f"{nomcriterenotif}:", valeurnotif_cible)
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
