import time
import time
import ast
import os
from pathlib import Path
import csv
import numpy as np
import fnmatch


# IMPRIME O HORÁRIO PARA CONTROLE
def imprime_time():
    localtime = time.localtime()
    result = time.strftime("%I:%M:%S %p", localtime)
    print(result)

print("*********************************")
print("***INICIO ***********************")
print("*********************************")

imprime_time()

print("*********************************")
print("***FIM **************************")
print("*********************************")

imprime_time()
imprime_time()

imprime_time()
imprime_time()

imprime_time()
imprime_time()
