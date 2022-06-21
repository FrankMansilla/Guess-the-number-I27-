#%%
import random

def jugarFacil(vidas): 

    numero_pc = random.randint(1,100)  
    numero_usu = None 

    while numero_pc != numero_usu: 
        numero_usu = int(input("Ingrese un numero: ")) 

        if numero_usu > numero_pc: 
            print("El numero es menor") 
            vidas -= 1

        elif numero_usu < numero_pc: 
            print("El numero es mayor")
            vidas -= 1

        if vidas == 0: 
            print("Perdiste") 
            break 
        print(f"Vidas restantes: {vidas}")

        if numero_pc == numero_usu: 
            print("Ganaste")
jugarFacil(10)
# %%
