'''Crea una clase Account() que represente una cuenta bancaria con los siguientes atributos:

bank para el nombre del banco;
acc_id para la ID de la cuenta;
holder_id para la ID del titular;
balance para el saldo inicial de la cuenta;
start_date para la fecha y hora en que se abrió la cuenta.
Asegúrate de que balance sea del tipo float y tenga un valor predeterminado de 0.0.. Para establecer un valor y tipo de 'balance' predeterminados, 
pasa la información dentro de __init__(). Este es un ejemplo donde establecemos un valor inicial de 32 y el tipo int en strength:

def __init__(self, strength:int=32):
Cuando se inicia una instancia de la clase Account(), esta debe registrar automáticamente la fecha y hora en que se abre la cuenta y almacenar estos datos como start_date. 
Para hacerlo, deberás importar el módulo datetime del paquete datetime:

from datetime import datetime
Una vez que lo hayas importado, puedes utilizar su método de clase now() para crear una marca temporal a partir de la fecha y la hora reales como esta:

from datetime import datetime

datetime.now()'''
#Código

from datetime import datetime

class Account:
  def _init_ (self, bank, acc_id, holder_id, balance:float=0.0):
    self.bank = bank
    self.acc_id = acc_id
    self.holder_id = holder_id
    self.balance = balance
    self.start_date = datetime.now()
    
