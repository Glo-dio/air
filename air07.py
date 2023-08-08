import sys

# fonctions utilisées
def args_to_array():
  i = 1
  args_table = []
  while i < len(sys.argv) - 1:
    args_table.append(int(sys.argv[i]))
    i += 1
  return args_table

def for_unique_element(array, new_element):
  new_array = []
  if array[0] > int(new_element):
    new_array.append(new_element)
    new_array.append(array[0])
  else:
    new_array.append(array[0])
    new_array.append(new_element)
  return new_array

def sorted_insert(array, new_element):
  i = 0
  new_array = []
  element_inserted = False
  if len(array) == 1:
    new_array = for_unique_element(array, new_element)
    new_array = str(new_array)[1:-1]
    return new_array
  while i < len(array) and element_inserted == False:
    if array[i] > int(new_element):
      new_array.append(new_element)
      element_inserted = True
    new_array.append(array[i])
    i+=1

  if element_inserted == True:
    while i < len(array):
      new_array.append(array[i])
      i+=1
  new_array = str(new_array)[1:-1]
  return (new_array)

def args_is_digit(args):
  for i in args:
    if i.isdigit() == False:
      return False

def is_arg_valid():
  list_of_args = sys.argv[1:]
  if is_nb_arg_correct == False:
    return False
  if args_is_digit(list_of_args) == False:
    return False

# Partie 1 : Gestion d'erreur
is_nb_arg_correct = len(sys.argv) > 2

if is_arg_valid() == False:
  print("error")
  sys.exit()

# Partie 2 : Parsing
args = args_to_array()
arg_to_insert = int(sys.argv[-1])

# Partie 3 : Résolution
answer = sorted_insert(args, arg_to_insert)

# Partie 4 : Affichage
print(answer)
