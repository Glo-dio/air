import sys

# fonctions utilisées
def args_to_array():
  i = 1
  args_table = []
  while i < len(sys.argv):
    args_table.append(sys.argv[i])
    i += 1
  return args_table

def ma_rotation(array):
  new_array = []
  first_element = array[0]
  for i in range(1, len(array)):
    new_array.append(array[i])
  new_array.append(first_element)
  new_array = str(', '.join(new_array)[0:])
  return new_array

def is_arg_valid():
  if is_nb_arg_correct == False:
    return False

# Partie 1 : Gestion d'erreur
is_nb_arg_correct = len(sys.argv) > 2

if is_arg_valid() == False:
  print("error")
  sys.exit()

# Partie 2 : Parsing
args = args_to_array()

# Partie 3 : Résolution
answer = ma_rotation(args)

# Partie 4 : Affichage
print(answer)
