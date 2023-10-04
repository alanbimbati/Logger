## Logger

Classe per la registrazione delle attività.

### Funzioni disponibili

* `clear_log()`: metodo per pulire il contenuto del file di log.
* `log_function()`: funzione decorator per la registrazione delle attività.

### Esempio di utilizzo

```python
### While coding, adding @logger.log_function into a definition of a function, makes it wrap and log it automatically

logger = Logger('log.txt')

@logger.log_function
def my_function(arg1, arg2):
   #something to do

my_function('valore 1', 'valore 2')
```
#### OUTPUT
2021-07-12 15:27:57 INFO: Starting execution of function my_function with arguments ('valore 1', 'valore 2')
La mia funzione è stata chiamata con gli argomenti valore 1 e valore 2
La mia funzione ha terminato l'elaborazione
2021-07-12 15:27:59 INFO: Execution of function my_function took 2.002 seconds

'''