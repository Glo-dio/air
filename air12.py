import sys

# fonctions utilisées
def args_to_array():
  i = 1
  args_table = []
  while i < len(sys.argv):
    args_table.append(int(sys.argv[i]))
    i += 1
  return args_table

def my_quick_sort(array):
  if len(array) <= 1:
    return array
  pivot = array.pop()
  smaller = []
  bigger = []
  for i in array:
    if i < pivot:
      smaller.append(i)
    else:
      bigger.append(i)
  return my_quick_sort(smaller)+[pivot]+my_quick_sort(bigger)

def args_is_digit(args):
  for i in args:
    if i.isdigit() == False:
      return False

def is_arg_valid():
  if is_nb_arg_correct == False:
    return False
  if args_is_digit(sys.argv[1:]) == False:
    return False

# Partie 1 : Gestion d'erreur
is_nb_arg_correct = len(sys.argv) > 2

if is_arg_valid() == False:
  sys.exit("error")

# Partie 2 : Parsing
args = args_to_array()

# Partie 3 : Résolution
answer = str(my_quick_sort(args))[1:-1]

# Partie 4 : Affichage
print(answer)