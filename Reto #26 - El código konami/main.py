# /*
#  * Crea un programa que detecte cuando el famoso "Código Konami" se ha introducido correctamente
#  * desde el teclado. Si sucede esto, debe notificarse mostrando un mensaje en la terminal.
#  */

import keyboard

in_seq = False
counter = 0
seq = ['up','up','down','down','left','right','left','right','b','a','enter']
def sequence(e):
    global in_seq,counter
    print(e.name)
    if e.name == seq[counter]:
        counter+=1
        in_seq = True
        if counter == 11:
            print('ganó!!!')
            counter=0
            in_seq= False
    else:
        counter = 0
        in_seq = False
    
    
    
print('Ingrese el código Konami(Escape para terminar)')
keyboard.on_press(sequence)
# Added hotkey so you can exit block and continue program execution
keyboard.wait("ESC") 
# Run this after you press escape so it stops running the hook when you exit
keyboard.unhook_all() 