import sys

# fonctions utilisées

def args_to_array():
  i = 1
  args_table = []
  while i < len(sys.argv) - 1:
    args_table.append(int(sys.argv[i]))
    i += 1
  return args_table

def operate_on(array, operator):
  i = 0
  new_array = []
  sign_operator = operator[0]
  if sign_operator == '+':
    for i in range(len(array)):
      new_array.append(array[i] + int(operator))
  elif sign_operator == '-':
    for i in range(len(array)):
      new_array.append(array[i] + int(operator)) # "+" et "-" = "-"
  new_array = str(new_array)[1:-1]
  return new_array

def args_is_digit(args):
  for i in args:
    if i.isdigit() == False:
      return False

def is_arg_valid():
  list_of_args = sys.argv[1:-1]
  sign = sys.argv[-1][0]
  operator_arg = sys.argv[-1][1:]
  if is_nb_arg_correct == False:
    return False
  if args_is_digit(list_of_args) == False or args_is_digit(operator_arg) == False:
    return False
  if sign != '+' and sign != '-':
    return False

# Partie 1 : Gestion d'erreur
is_nb_arg_correct = len(sys.argv) > 2

if is_arg_valid() == False:
  sys.exit("error")

# Partie 2 : Parsing
args = args_to_array()
operator = sys.argv[-1]

# Partie 3 : Résolution
answer = operate_on(args, operator)

# Partie 4 : Affichage
print(answer)