import sys

# fonctions utilisées

def delete_siamese_character(array):
  i = 1
  string = []
  string.append(array[0])

  while i < len(array) - 1:
    while array[i - 1] == array[i]:
      i += 1
    string.append(array[i])
    i += 1	
  string = ''.join(string)
  return string

def is_arg_valid():
  if is_nb_arg_correct == False:
    return False

# Partie 1 : Gestion d'erreur
is_nb_arg_correct = len(sys.argv) == 2

if is_arg_valid() == False:
  print("error")
  sys.exit()

# Partie 2 : Parsing
args = sys.argv[1]

# Partie 3 : Résolution
answer = delete_siamese_character(args)

# Partie 4 : Affichage
print(answer)
