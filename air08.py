import sys

# fonctions utilisées
def args_to_array():
	i = 1
	args_table = []
	while i < len(sys.argv):
		args_table.append(sys.argv[i])
		i += 1
	return args_table

def create_array_1(array):
  array_1 = []
  for i in array:
    if i == "fusion":
      return array_1
    array_1.append(i)

def create_array_2(array):
  array_2 = []
  if "fusion" not in array:
    print("error")
    sys.exit()
  start = array.index("fusion") + 1
  for i in array[start:]:
    array_2.append(i)
  return array_2

args = args_to_array()
array_arg_1 = create_array_1(args)
array_arg_2 = create_array_2(args)

def merge_table(array_1, array_2):
  merge_tab = []
  for i in array_1:
    merge_tab.append(int(i))
  for i in array_2:
    merge_tab.append(int(i))
  return merge_tab

def swap(array, index_1):
  tmp = array[index_1]
  array[index_1] = array[index_1 + 1]
  array[index_1 + 1] = tmp

def my_bubble_sort(array):
  new_array = array
  i = 0
  while i < len(array) - 1:
    if int(array[i]) > int(array[i + 1]):
      swap(new_array, i)
      i = -1
    i+=1
  return (new_array)

def sorted_fusion(array1, array2):
  new_array = merge_table(array1, array2)
  my_bubble_sort(new_array)
  new_array = str(new_array)[1:-1]
  return new_array

def args_is_digit(args):
  for i in args:
    if i.isdigit() == False:
      return False

def is_arg_valid():
  if is_nb_arg_correct == False:
    return False
  if args_is_digit(array_arg_1) == False or args_is_digit(array_arg_2) == False:
    return False

# Partie 1 : Gestion d'erreur
is_nb_arg_correct = len(sys.argv) > 3

if is_arg_valid() == False:
  print("error")
  sys.exit()

# Partie 2 : Parsing

# Partie 3 : Résolution
answer = sorted_fusion(array_arg_1, array_arg_2)

# Partie 4 : Affichage
print(answer)
