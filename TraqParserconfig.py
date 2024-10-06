# ----------------------------------------------------------------
# Parserconfig.py
# paramètre fichier, section et critère cherché
# renvoi valeur texte trouvée
# 20240828
# @Zlatko
# ----------------------------------------------------------------
import os
import configparser

def param_cible_function(fichierparam_cible, sectionparam_cible, critereparam_cible):

    # ----------------------------------------------------------------
    # Retour de la valeur du paramètre
    nomfichierparam = os.path.join(os.getcwd(),'Traqueur_fdr/',fichierparam_cible)
    nomsectionparam = sectionparam_cible
    nomcritereparam = critereparam_cible
    Parserparam = configparser.ConfigParser()
    Parserparam.read(nomfichierparam)
    try:
        Parserparam.get(nomsectionparam, nomcritereparam)
        valeurparam_cible = Parserparam.get(nomsectionparam, nomcritereparam)
        print(f"{nomcritereparam}:", valeurparam_cible)
        # 
        # a journaliser INFO
        # 
    except configparser.NoOptionError:        
        print(f"No option '{nomcritereparam}'")
        # 
        # a journaliser ERROR
        # 
        
    # ----------------------------------------------------------------
    # journalisation
    
    return valeurparam_cible
