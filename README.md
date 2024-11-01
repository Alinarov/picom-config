configuracion de picom en manjaro i3. 

para poner los bordes redondeados con picom.
-  corner-radius = 3

Este es para que solucionar el error del pip install:
- sudo rm /usr/lib/python3.11/EXTERNALLY-MANAGED

Estos comandos es para instalar los emojis en manjaro en brave
- sudo pacman -S noto-fonts-emoji
- fc-cache -f -v

Esto es para la cofiguracion de las teclas de mi nuevo tecladoV
- setxkbmap -layout es
- xmodmap -e "keycode 78 = Delete" 
- xmodmap -e "keycode 118 = Home" 
- xmodmap -e "keycode 119 = End" 
  

