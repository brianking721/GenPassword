import random
import sys,time

def banner():
    print('''  _____           ___                                 __
 / ___/__ ___    / _ \___ ____ ____    _____  _______/ /
/ (_ / -_) _ \  / ___/ _ `(_-<(_-< |/|/ / _ \/ __/ _  / 
\___/\__/_//_/ /_/   \_,_/___/___/__,__/\___/_/  \_,_/  
                                                      
Tu nueva contraseña es :                                                      ''')




def generador():
    letras = 'abcdefghijklmnopkrstyyz'
    numeros = '1234567890'
    unidos = f'{letras}{numeros}'
    contraseña = ''.join(random.sample(unidos,10))
    print(contraseña)

print('''   ______                                     _                         
  (_____ \                                   | |                        
   _____) )___  ___  ___ _ _ _  ___   ____ _ | |                        
  |  ____/ _  |/___)/___) | | |/ _ \ / ___) || |                        
  | |   ( ( | |___ |___ | | | | |_| | |  ( (_| |                        
  |_|    \_||_(___/(___/ \____|\___/|_|   \____|                        
                                                                        
                    ______                                              
                   / _____)                             _               
                  | /  ___  ____ ____   ____  ____ ____| |_  ___   ____ 
                  | | (___)/ _  )  _ \ / _  )/ ___) _  |  _)/ _ \ / ___)
                  | \____/( (/ /| | | ( (/ /| |  ( ( | | |_| |_| | |    
                   \_____/ \____)_| |_|\____)_|   \_||_|\___)___/|_|    
                                                                    By Blackjack    ''')
print('Tu contraseña es: ')
print('==========')
generador()
print('==========')
menu = print('''GENERAR NUEVA CONTRASEÑA DIGITE <1>
          CERRAR LA APLICACION   DIGITE <2>''')
numero = input(">>>>> elige una opcion: ")
if  numero == '1':
    banner()    
    generador()
else:
    print('gracias por usar el script <3')

    
    