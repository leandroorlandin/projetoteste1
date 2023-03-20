import time
from datetime import datetime, timedelta



# IMPRIME O HORÁRIO PARA CONTROLE
def imprime_time():
    localtime = time.localtime()
    time_stamp = time.time_ns()
    current_time = (datetime.now())
    result = time.strftime("%I:%M:%S %p", localtime)
    print(time_stamp)
    print(current_time)
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

imprime_time()
imprime_time()