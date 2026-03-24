# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define robo = Character("Robô", color="#00ffb4")
default passounoteste = False

transform midleft:
    yalign 0.5
    xcenter 0.40

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg blurred

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.

    "ProjetoDirigido 1q2026"

    show robo happy at midleft
    robo "Essa vai ser a nossa divulgação científica"

    show robo nerd with dissolve
    robo "Aqui está o \"Olá, Mundo!\" por garantia"

    show robo sad with dissolve
    

    # This ends the game.
    #return

label choice:

    robo "Temos um longo caminho pela frente"
    menu:
        "Sim":
            jump choices1_a
        "Talvez":
            jump choices1_b
    
    label choices1_a:
        show robo happy with dissolve
        robo "Uhum"
        jump choices1_common
    
    label choices1_b:
        robo "..."
        show robo happy with dissolve
        jump choices1_common
    
    label choices1_common:
        robo "Vamos ao trabalho!"

    robo "Aqui vai uma sequência de várias falas para testar o posicionamento do texto, vai saber"
