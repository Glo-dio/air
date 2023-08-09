import sys

# fonctions utilisées

def args_to_array():
  i = 1
  args_table = []
  while i < len(sys.argv):
    args_table.append(sys.argv[i])
    i += 1
  return args_table

def is_count_intruder_valide(array):
  number_of_one = array.count(1)
  answer = True if number_of_one == 1 else False
  return answer

def find_intru(array):
  i = 0
  duplicates_values = []
  for i in range(len(array)):
    duplicates_values.append(array.count(array[i]))

  index = 0
  for i in duplicates_values:
    if i == 1:
      break
    index += 1
  
  if is_count_intruder_valide(duplicates_values) == True:
    intruder = array[index]
    return intruder
  else:
    print("error")
    sys.exit()

def is_arg_valid():
  if is_nb_arg_correct == False:
    return False

# Partie 1 : Gestion d'erreur
is_nb_arg_correct = len(sys.argv) > 3

if is_arg_valid() == False:
  print("error")
  sys.exit()

# Partie 2 : Parsing
args = args_to_array()

# Partie 3 : Résolution
answer = find_intru(args)

# Partie 4 : Affichage
print(answer)