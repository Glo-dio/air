import sys

# fonctions utilisées

def args_to_array():
  i = 1
  args_table = []
  while i < len(sys.argv) - 1:
    args_table.append(sys.argv[i])
    i += 1
  return args_table

def ma_fonction(array_de_strings, separateur):
  string = []
  for i in range(len(array_de_strings)):
    string.append(array_de_strings[i])
    if i < len(array_de_strings) - 1:
      string.append(separateur)
  string = "".join(string)
  return (string)

def is_arg_valid():
  if is_nb_arg_correct == False:
    return False

# Partie 1 : Gestion d'erreur
is_nb_arg_correct = len(sys.argv) > 2

if is_arg_valid() == False:
  sys.exit("error")

# Partie 2 : Parsing
args = args_to_array()
separator = sys.argv[-1]

# Partie 3 : Résolution
answer = ma_fonction(args, separator)

# Partie 4 : Affichage
print(answer)
