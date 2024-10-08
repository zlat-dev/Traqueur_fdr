# ----------------------------------------------------------------
# TraqLogW.py
# 20240905
# @Zlatko
# ----------------------------------------------------------------

import logging
import logging.config
from os import path

def param_log_function(param_log_user, param_lvl, param_msg):
    
    log_file_path = path.join(path.dirname(path.abspath(__file__)), 'Logging.conf')
    logging.config.fileConfig(log_file_path)
    #logging.config.fileConfig('Traqueur_fdr/Logging.conf')
    
    msg_utilisateur = param_log_user
    msg_lvl = param_lvl
    msg_log_txt = param_msg
    
    # create logger
    logger = logging.getLogger(msg_utilisateur)

    # 'application' code
    match msg_lvl:
        case 'INFO':
            logger.info(msg_log_txt)
        case 'WARNING':
            logger.warning(msg_log_txt)
        case 'ERROR':
            logger.error(msg_log_txt)
        case 'CRITICAL':
            logger.critical(msg_log_txt)
        case 'DEBUG':
            logger.debug(msg_log_txt)
    
    # print = logger.debug(msg_log_txt)
    
    # return logger.debug(msg_log_txt)
    # Shut down the logger
    logging.shutdown()