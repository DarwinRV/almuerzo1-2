import random 


def read_breakFast(filepath="./archivos/breakfast.txt"):
    readBreak = []
    with open(filepath,"r", encoding="utf-8") as f:
        for line in f :
            readBreak.append(line.strip())
    return readBreak

#list
def breakf():
    data = read_breakFast(filepath="./archivos/breakfast.txt")
    chosen_readDesa = random.choice(data)
    print(chosen_readDesa)


def read_Lunch(filepath="./archivos/lunch.txt"):
    readLunch = []
    with open(filepath,"r", encoding="utf-8") as f:
        for line in f :
            readLunch.append(line.strip())
    return readLunch


def lunch():
    data = read_Lunch(filepath="./archivos/lunch.txt")
    chosen_readLunch = random.choice(data)
    print(chosen_readLunch)




def read_Dinner(filepath="./archivos/dinner.txt"):
    readDinner = []
    with open(filepath,"r", encoding="utf-8") as f:
        for line in f :
            readDinner.append(line.strip())
    return readDinner


def dinner():
    data = read_Dinner(filepath="./archivos/dinner.txt")
    chosen_readDinner = random.choice(data)
    print(chosen_readDinner)



def run():
    try:
        respuesta = str(input("""
    
 ________      # __          # ___ __ __     # __  __      # ______      # ______       # ______     # ______      #       # ______    # __  __    #
/_______/\     #/_/\         #/__//_//_/\    #/_/\/_/\     #/_____/\     #/_____/\      #/_____/\    #/_____/\     #       #/_____/\   #/_/\/_/\   #
\::: _  \ \    #\:\ \        #\::\| \| \ \   #\:\ \:\ \    #\::::_\/_    #\:::_ \ \     #\:::__\/    #\:::_ \ \    #       #\:::_ \ \  #\ \ \ \ \  #
 \::(_)  \ \   # \:\ \       # \:.      \ \  # \:\ \:\ \   # \:\/___/\   # \:(_) ) )_   #   /: /     # \:\ \ \ \   # ___   # \:(_) \ \ # \:\_\ \ \ #
  \:: __  \ \  #  \:\ \____  #  \:.\-/\  \ \ #  \:\ \:\ \  #  \::___\/_  #  \: __ `\ \  #  /::/___   #  \:\ \ \ \  #/__/\  #  \: ___\/ #  \::::_\/ #
   \:.\ \  \ \ #   \:\/___/\ #   \. \  \  \ \#   \:\_\:\ \ #   \:\____/\ #   \ \ `\ \ \ # /_:/____/\ #   \:\_\ \ \ #\::\ \ #   \ \ \   #    \::\ \ #
    \__\/\__\/ #    \_____\/ #    \__\/ \__\/#    \_____\/ #    \_____\/ #    \_\/ \_\/ # \_______\/ #    \_____\/ # \:_\/ #    \_\/   #     \__\/ #
               ##             ##               ##             ##             ##              ##            ##             ##       ##           ##  
    
    Hola Bienvenido 

    Ingresa lo que quieres comer hoy: 
	[1] desayuno
	[2] almuerzo
	[3] comida 
    [4] No gracias ya se que comer 

___________________________________________________________________________________________________________________________________________________

	seleciona :) >> """))


        if respuesta== "1":
            breakf()
            

        elif respuesta== "2":
            lunch()


        elif respuesta== "3":
            dinner()
        

        elif respuesta== "4":
            print("a sos re troll")


        else :
            print("Ingresa una opcion ")


    except ValueError:
        print("Ingrsa una opcion ")




if __name__ == "__main__":
    run()