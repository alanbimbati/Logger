import logging
import time
from functools import wraps

class Logger:

    def __init__(self, log_filename):
        self.log_filename = log_filename
        # Configurazione del logger
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)

        # Aggiungi un gestore di file
        handler = logging.FileHandler(log_filename, encoding='utf-8')
        handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s',  datefmt='%Y-%m-%d %H:%M:%S'))
        logger.addHandler(handler)
        
        self.logger = logger
      
     
    def clear_log(self):
        """
        Metodo per pulire il contenuto del file di log.
        """
        try:
            open(self.log_filename, 'w').close()            
            self.logger.info("Il file di log '{}' è stato pulito con successo.".format(self.log_filename))            
        except Exception as e:
            self.logger.warning("Impossibile pulire il file di log '{}': {}".format(self.log_filename, e))
          
    # Funzione decorator per la registrazione delle attività
    def log_function(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            log_message = 'Inizio esecuzione della funzione {}'.format(
                func.__name__)
            start_time = time.time()
            self.logger.info(log_message)
            print(log_message)

            result = func(*args, **kwargs)

            end_time = time.time()
            elapsed_time = end_time - start_time
            
            minutes = elapsed_time // 60
            seconds = elapsed_time - minutes * 60
            log_message = 'Fine esecuzione della funzione {}. Tempo impiegato: {} minuti e {:.2f} secondi'.format(
            func.__name__, minutes, seconds)
            self.logger.info(log_message)
            print(log_message)

            return result

        return wrapper
       
'''
### While coding, adding @logger.log_function into a definition of a function, makes it wrap and log it automatically

logger = Logger('log.txt')

@logger.log_function
def my_function(arg1, arg2):
   #something to do

my_function('valore 1', 'valore 2')

#### OUTPUT
2021-07-12 15:27:57 INFO: Starting execution of function my_function with arguments ('valore 1', 'valore 2')
La mia funzione è stata chiamata con gli argomenti valore 1 e valore 2
La mia funzione ha terminato l'elaborazione
2021-07-12 15:27:59 INFO: Execution of function my_function took 2.002 seconds

'''