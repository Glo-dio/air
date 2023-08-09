import sys

# fonctions utilisées

def args_to_array():
  i = 1
  args_table = []
  while i < len(sys.argv) - 1:
    args_table.append(sys.argv[i])
    i += 1
  return args_table

def converted_to_compare(array):
  new_array = []
  for word in array:
    new_array.append(word.casefold())
  return new_array

def ma_fonction(array_de_strings, string):
  i = 0
  nouvel_array_de_strings = []
  tmp_string = string.casefold()
  tmp_array_de_strings = converted_to_compare(array_de_strings)
  while i < len(array_de_strings):
    if tmp_string not in tmp_array_de_strings[i]:
      nouvel_array_de_strings.append(array_de_strings[i])
    i += 1
  nouvel_array_de_strings = ', '.join(nouvel_array_de_strings)
  return nouvel_array_de_strings

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
target = sys.argv[-1]

# Partie 3 : Résolution
answer = ma_fonction(args, target)

# Partie 4 : Affichage
print(answer)
