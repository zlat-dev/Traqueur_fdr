import os
from os import path

log_file_path = path.join(path.dirname(path.abspath(__file__)), 'Logging.conf')    
    
print (os.path.dirname(log_file_path))
print (os.getcwd())