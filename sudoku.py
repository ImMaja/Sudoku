# -*- coding: utf-8 -*-
# Le script utilise des caractères UTF-8.

#   PEIFFER Guillaume
#   contact at guill.peiffer@gmail.com
#   https://github.com/ImMaja/sudoku

from random import seed, randrange, choice
import os.path
import os


# // VARIABLES \\ #

# mg est la matrice 9x9 correspondant à la grille du Sudoku.
mg = [['_' for j in range(9)]for i in range(9)]

# player_choice est une liste contenant la ligne, la colonne et la valeur sélectionné par l'utilisateur
# dans la fonction player_move().
player_choice = [0, 0, 0]

# Fonction permettant de quitter "proprement" le programme avec CTRL + C.
def exitSudoku():
    os.system('clear')
    print('Exit.')
    exit()


# Cette fonction a uniquement pour but l'affichage de la grille du sudoku.
def print_patern(mg):
    os.system('clear')
    print(
    '\n', '          1  2  3     4  5  6     7  8  9',
    '\n', '          ╵  ╵  ╵     ╵  ╵  ╵     ╵  ╵  ╵'
    '\n', '       ┌───────────┬───────────┬───────────┐',
    '\n', f' 1╶    │  {mg[0][0]}  {mg[0][1]}  {mg[0][2]}  │  {mg[0][3]}  {mg[0][4]}  {mg[0][5]}  │  {mg[0][6]}  {mg[0][7]}  {mg[0][8]}  │',
    '\n', '       │           │           │           │',
    '\n', f' 2╶    │  {mg[1][0]}  {mg[1][1]}  {mg[1][2]}  │  {mg[1][3]}  {mg[1][4]}  {mg[1][5]}  │  {mg[1][6]}  {mg[1][7]}  {mg[1][8]}  │',
    '\n', '       │           │           │           │',
    '\n', f' 3╶    │  {mg[2][0]}  {mg[2][1]}  {mg[2][2]}  │  {mg[2][3]}  {mg[2][4]}  {mg[2][5]}  │  {mg[2][6]}  {mg[2][7]}  {mg[2][8]}  │',
    '\n', '       ├───────────┼───────────┼───────────┤',
    '\n', f' 4╶    │  {mg[3][0]}  {mg[3][1]}  {mg[3][2]}  │  {mg[3][3]}  {mg[3][4]}  {mg[3][5]}  │  {mg[3][6]}  {mg[3][7]}  {mg[3][8]}  │',
    '\n', '       │           │           │           │',
    '\n', f' 5╶    │  {mg[4][0]}  {mg[4][1]}  {mg[4][2]}  │  {mg[4][3]}  {mg[4][4]}  {mg[4][5]}  │  {mg[4][6]}  {mg[4][7]}  {mg[4][8]}  │',
    '\n', '       │           │           │           │',
    '\n', f' 6╶    │  {mg[5][0]}  {mg[5][1]}  {mg[5][2]}  │  {mg[5][3]}  {mg[5][4]}  {mg[5][5]}  │  {mg[5][6]}  {mg[5][7]}  {mg[5][8]}  │',
    '\n', '       ├───────────┼───────────┼───────────┤',
    '\n', f' 7╶    │  {mg[6][0]}  {mg[6][1]}  {mg[6][2]}  │  {mg[6][3]}  {mg[6][4]}  {mg[6][5]}  │  {mg[6][6]}  {mg[6][7]}  {mg[6][8]}  │',
    '\n', '       │           │           │           │',
    '\n', f' 8╶    │  {mg[7][0]}  {mg[7][1]}  {mg[7][2]}  │  {mg[7][3]}  {mg[7][4]}  {mg[7][5]}  │  {mg[7][6]}  {mg[7][7]}  {mg[7][8]}  │',
    '\n', '       │           │           │           │',
    '\n', f' 9╶    │  {mg[8][0]}  {mg[8][1]}  {mg[8][2]}  │  {mg[8][3]}  {mg[8][4]}  {mg[8][5]}  │  {mg[8][6]}  {mg[8][7]}  {mg[8][8]}  │',
    '\n', '       └───────────┴───────────┴───────────┘',
    '\n', sep = '')

    return None



#Fonction permettant l'affichage du menu, l'utilisateur choisi s'il souhaite jouer au sudoku ou cracker une grille.
def menu():
    def _sudoku():
        os.system('clear')
        print('\n\n',
            '\n', ' ███████ ██    ██ ██████   ██████  ██   ██ ██    ██ ',
            '\n', ' ██      ██    ██ ██   ██ ██    ██ ██  ██  ██    ██ ',
            '\n', ' ███████ ██    ██ ██   ██ ██    ██ █████   ██    ██ ',
            '\n', '      ██ ██    ██ ██   ██ ██    ██ ██  ██  ██    ██ ',
            '\n', ' ███████  ██████  ██████   ██████  ██   ██  ██████  ',
            '\n\n\n')
        return None

    menu_choice = int(-1)
    grid_choice = int(-1)

    def _first_menu(menu_choice):
        while(1):
            try:
                _sudoku()
                print('\n[1] - Jouer au Sudoku.',
                      '\n[2] - Cracker une grille de Sudoku.',
                      '\n[3] - Quitter.')

                menu_choice = int(input("\n--> "))
                if menu_choice == 3:
                    exitSudoku()
                elif menu_choice in range(1, 3):
                    return menu_choice
            except ValueError:
                pass
            except KeyboardInterrupt:
                exitSudoku()

    def _second_menu(grid_choice):
        while(1):
            try:
                _sudoku()
                print('\n[1] - Grille existante (format .txt).',
                      '\n[2] - Générer une grille.',
                      '\n[3] - Retour.')

                grid_choice = int(input("\n--> "))
                if grid_choice in range(1, 4):
                    return grid_choice
            except ValueError:
                pass
            except KeyboardInterrupt:
                exitSudoku()


    bool_first_menu = False
    bool_second_menu = False

    while bool_first_menu == False:
        menu_choice = _first_menu(menu_choice)

        while bool_second_menu == False:
            grid_choice = _second_menu(grid_choice)
            if grid_choice == 3:
                bool_first_menu = False
                bool_second_menu = True
            else:
                bool_second_menu = True
                bool_first_menu = True
        if grid_choice == 3:
            bool_second_menu = False

    if grid_choice == 1:
        grid_path = False

        while os.path.isfile(grid_path) != True:
            print('\n', 'Placez une grille de sudoku au format .txt dans le même dossier que ce programme.',
                  '\n', 'Quel est le nom de votre grille ?')

            grid_path = str(input("\n--> "))

        with open(grid_path, 'r') as file:
            line_number = 0
            for current_line in file:
                column_number = 0
                if '*' in current_line:
                    continue
                for char in str(current_line):
                    if char == '_' or char.isdigit():
                        update_matrice(mg, line = line_number, column = column_number, value = char)
                        column_number += 1
                line_number += 1

    if grid_choice == 2:
        generate_grid(mg)

    if menu_choice == 1:
        return 1
    return 0



# Cette fonction permet de vérifier si la grille est complète ou non.
# Lorsque les 9 matrices sont complété, le programme sort de la boucle.
def over(mg):
    for line in mg:
        for char in line:
            if char == '_' or char == 0:
                return False
    return True



# Cette fonction va demander au joueur d'inscrire une valeur sur la grille en vérifiant
# qu'il n'a pas fais d'erreur de saisie.
def player_move(player_choice):

    while(1):
        try:
            user_interaction = str(input('--> '))
        except KeyboardInterrupt:
            exitSudoku()

        if user_interaction == 'quit':
            exitSudoku()

        elif len(user_interaction) != 5:
            print("Vous avez fait une erreur de saisie.")
        elif user_interaction[0].isalpha() or user_interaction[2].isalpha() or user_interaction[4].isalpha() or user_interaction[4] == '_':
            print("Vous avez fait une erreur de saisie.")
        elif user_interaction[1].isdigit() or user_interaction[3].isdigit():
            print("Vous avez fait une erreur de saisie.")
        elif user_interaction[0] == '0' or user_interaction[2] == '0':
            print("Vous avez fait une erreur de saisie.")
        else:

            player_choice[0] = int(user_interaction[0]) - 1
            player_choice[1] = int(user_interaction[2]) - 1
            player_choice[2] = int(user_interaction[4])

            return None

#  Cette fonction va vérifier si un placement est correct ( ligne, colonne et zone ).
#  La fonction peut retourner 0, 1, 2 ou 3.
def correct_move(mg, line, column, value):
    
    # Check de la ligne
    for i in range(9):
        if mg[line][i] == value:
            return 1
    
    # Check de la colonne
    for i in range(9):
        if mg[i][column] == value:
            return 2
    
    # Check de la zone
    if line in range(0,3) and column in range(0,3):
        start_line = int(0)
        start_column = int(0)
    elif line in range(0,3) and column in range(3,6):
        start_line = int(0)
        start_column = int(3)
    elif line in range(0,3) and column in range(6,9):
        start_line = int(0)
        start_column = int(6)
    elif line in range(3,6) and column in range(0,3):
        start_line = int(3)
        start_column = int(0)
    elif line in range(3,6) and column in range(3,6):
        start_line = int(3)
        start_column = int(3)
    elif line in range(3,6) and column in range(6,9):
        start_line = int(3)
        start_column = int(6)
    elif line in range(6,9) and column in range(0,3):
        start_line = int(6)
        start_column = int(0)
    elif line in range(6,9) and column in range(3,6):
        start_line = int(6)
        start_column = int(3)
    elif line in range(6,9) and column in range(6,9):
        start_line = int(6)
        start_column = int(6)
    
    for i in range(start_line, start_line+3):
        for j in range(start_column, start_column+3):
            if mg[i][j] == value:
                return 3
    
    return 0

# Cette fonction va mettre à jour la matrice lors d'un mouvement.
def update_matrice(mg, line, column, value):
    def _insert(value):
        if value == '_':
            return str(value)
        return int(value)

    mg[line][column] = _insert(value)

    return None

# Cette fonction permet de remplir totalement une grille de sudoku à partir d'une grille
# vide ou partiellement compléter.
def solve_grid(mg):
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    seed(randrange(1, 1000000))

    for a in range(9):
        random_choice = choice(lst)
        lst.remove(random_choice)
        mg[0][a] = random_choice

        update_matrice(mg, line = 0, column = a, value = random_choice)
    
    print_patern(mg)

    all_line_solutions = []

    for i in range(1, 9):
        for j in range(9):
            temp = []
            for val in range(1, 10):
                if correct_move(mg, line = i, column = j, value = val) == 0:
                    temp += [val]
                    
            all_line_solutions += [temp]

        # for x in range(9):
        #     mg[i][x] = 
        
        break
    
    for line in all_line_solutions:
        print(line)

    temp = str(input())
    return None


# Cette fonction va permettre, à partir d'une grille entièrement compléter, de créer
# une grille à solution unique.
def generate_grid(mg):
    # Rien pour le moment.
    return None




# Execution du programme
while(1):
    menu_var = int(menu())

    if menu_var == 1:
        while over(mg) == False:
            print_patern(mg)
            player_move(player_choice)
            if player_choice[2] != 0:
                is_correct_move = correct_move(mg, line = player_choice[0], column = player_choice[1], value = player_choice[2])
                match is_correct_move:
                    case 0:
                        update_matrice(mg, line = player_choice[0], column = player_choice[1], value = player_choice[2])
                    case 1:
                        print(f"Impossible de placer {player_choice[2]} à cet endroit.",
                              f"{player_choice[2]} est déjà sur cette ligne.")
                        temp = str(input('Appyez sur ENTRER pour continuer.'))
                    case 2:
                        print(f"Impossible de placer {player_choice[2]} à cet endroit.",
                              f"{player_choice[2]} est déjà dans cette colonne.")
                        temp = str(input('Appyez sur ENTRER pour continuer.'))
                    case 3:
                        print(f"Impossible de placer {player_choice[2]} à cet endroit.",
                              f"{player_choice[2]} est déjà dans cette zone.")
                        temp = str(input('Appyez sur ENTRER pour continuer.'))

        print_patern(mg)
        print('\n\nFélicitation, vous avez résolue la grille.')
        try:
            temp = input('Appyez sur ENTRER pour retourner au menu principal.')
        except KeyboardInterrupt:
            exitSudoku()

    elif menu_var == 0:
        solve_grid(mg)
        print_patern(mg)
        try:
            temp = input('Appyez sur ENTRER pour retourner au menu principal.')
        except KeyboardInterrupt:
            exitSudoku()
