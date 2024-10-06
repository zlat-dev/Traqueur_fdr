# ----------------------------------------------------------------
# TraqLogW.py
# 20240905
# @Zlatko
# ----------------------------------------------------------------

import logging
import logging.config

def param_log_function(param_log_user, param_msg):
    
    logging.config.fileConfig('Traqueur_fdr/Logging.conf')
    
    msg_utilisateur = param_log_user
    msg_log_txt = param_msg
    # msg_level = param_level
    
    # create logger
    logger = logging.getLogger(msg_utilisateur)

    # 'application' code
    logger.debug(msg_log_txt)
    logger.info(msg_log_txt)
    logger.warning(msg_log_txt)
    logger.error(msg_log_txt)
    logger.critical(msg_log_txt)
    
    # print = logger.debug(msg_log_txt)
    
    # return logger.debug(msg_log_txt)
    # Shut down the logger
    logging.shutdown()