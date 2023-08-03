import sys

ascii_space = 32
ascii_horizontal_tab = 10
ascii_line = 9

# fonctions utilisées

def is_white_space(char):
  if ord(char) == ascii_space or ord(char) == ascii_line or ord(char) == ascii_horizontal_tab:
    return True

""" def count_word(str):
  i = 0
  word = 1
  while is_white_space(str[i]):
    i += 1

  i += 1
  while i < len(str) - 1:
    if (is_white_space(str[i]) and str[i + 1].isalpha()):
      word += 1
      i += 1
    i += 1
  return word

  nb_word = count_word(sys.argv[1])
    
# print(nb_word(sys.argv[1])) """

def ma_fonction(str, string_séparateur):
  word = []
  tableau = []
  tmp = []
  i = 0
  while is_white_space(str[i]):
    i += 1
  while i < len(str) - 1:
    if is_white_space(str[i]) and str[i + 1].isalpha():
      tmp.append(''.join(word))
      tableau.append(tmp)
      tmp = []
      word = []
    else:
      word.append(str[i])
    i += 1
  word.append(str[i])
  tmp.append(''.join(word))
  tableau.append(tmp)
  return tableau

def is_arg_valid():
  if is_nb_arg_correct == False:
    return False

# Partie 1 : Gestion d'erreur
is_nb_arg_correct = len(sys.argv) == 2

if is_arg_valid() == False:
  print("error")
  sys.exit()

# Partie 2 : Parsing
arg = sys.argv[1]

# Partie 3 : Résolution
split = ma_fonction(arg, '')

# Partie 4 : Affichage
for word in split:
   print(word)
