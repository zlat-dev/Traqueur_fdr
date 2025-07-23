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
    """Récupère un paramètre de Config.conf. Le fichier Config.conf est structuré comme un ini.

    Args:
        fichierparam_cible (file): Le fichier Config.conf
        sectionparam_cible (txt): La section concernée
        critereparam_cible (txt): Le paramètre recherché

    Returns:
        txt: Le paramètre
    """

    # ----------------------------------------------------------------
    # Retour de la valeur du paramètre
    nomfichierparam = os.path.join(os.getcwd(),'',fichierparam_cible)
    nomsectionparam = sectionparam_cible
    nomcritereparam = critereparam_cible
    Parserparam = configparser.ConfigParser()
    Parserparam.read(nomfichierparam)
    try:
        Parserparam.get(nomsectionparam, nomcritereparam)
        valeurparam_cible = Parserparam.get(nomsectionparam, nomcritereparam)
        #print(f"{nomcritereparam}:", valeurparam_cible)
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
