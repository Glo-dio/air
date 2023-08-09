import sys
import os

# fonctions utilisées
def read_file(name):
  file = open(name, "r")
  lines = file.readlines()
  for line in lines:
    print(line)
  file.close()

def is_arg_valid():
  if is_nb_arg_correct == False:
    return False
  if os.path.exists(sys.argv[1]) == False:
    return False

# Partie 1 : Gestion d'erreur
is_nb_arg_correct = len(sys.argv) == 2

if is_arg_valid() == False:
  print("error")
  sys.exit()

# Partie 2 : Parsing
arg = sys.argv[1]

# Partie 3 : Résolution

# Partie 4 : Affichage
read_file(arg)