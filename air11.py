import sys

# fonctions utilisées
def pyramid(character, stage):
  stage += 1
  for rows in range(1, stage):
    for column in range(1, stage - rows):
      print(" ", end="")
    for column in range(1, (2 * rows - 1) +1):
      print(character, end="")
    print("")

def is_arg_valid():
  if is_nb_arg_correct == False:
    return False
  if sys.argv[1].isdigit() == False or sys.argv[2].isdigit() == False:
    return False

# Partie 1 : Gestion d'erreur
is_nb_arg_correct = len(sys.argv) == 3

if is_arg_valid() == False:
  print("error")
  sys.exit()

# Partie 2 : Parsing
print_character = sys.argv[1]
height_pyramid = int(sys.argv[2])

# Partie 3 : Résolution
answer = pyramid(print_character, height_pyramid)

# Partie 4 : Affichage
