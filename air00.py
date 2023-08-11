import sys

ascii_space = 32
ascii_horizontal_tab = 10
ascii_line = 9

# fonctions utilisées

def is_white_space(char):
  if ord(char) == ascii_space or ord(char) == ascii_line or ord(char) == ascii_horizontal_tab:
    return True

def ma_fonction(string_à_couper, string_séparateur):
  word = []
  tableau = []
  tmp = []
  i = 0
  while is_white_space(string_à_couper[i]):
    i += 1
  while i < len(string_à_couper) - 1:
    if is_white_space(string_à_couper[i]) and string_à_couper[i + 1].isalpha():
      tmp.append(''.join(word))
      tableau.append(tmp)
      tmp = []
      word = []
    else:
      word.append(string_à_couper[i])
    i += 1
  word.append(string_à_couper[i])
  tmp.append(''.join(word))
  tableau.append(tmp)
  return tableau

def is_arg_valid():
  if is_nb_arg_correct == False:
    return False

# Partie 1 : Gestion d'erreur
is_nb_arg_correct = len(sys.argv) == 2

if is_arg_valid() == False:
  sys.exit("error")

# Partie 2 : Parsing
arg = sys.argv[1]

# Partie 3 : Résolution
split = ma_fonction(arg, '')

# Partie 4 : Affichage
for word in split:
   print(word)
