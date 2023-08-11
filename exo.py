import subprocess

success_test = 0
total_test = 0

def air00():
  examples = [["Bonjour les gars"],
              ["Bonjour les filles"]]
  file = "air00"
  test = 1
  global success_test
  global total_test
  for i in examples:
    nb_test = len(examples)
    arg = str(i)[1:-1]
    result = subprocess.run(f"python3 {file}.py {arg}", shell=True, capture_output=True, text=True)
    # print(f"arg : {arg}")
    # print(f"stdout : {result.stdout}")
    # print(f"stderr : {result.stderr}")
    if "can't open file" in result.stderr:
      print("==> File not found")
      print(f"\033[31;1m{file} ({test}/{nb_test}) : failure\033[00m")
    elif "error" in result.stderr:
      print(f"\033[31;1m{file} ({test}/{nb_test}) : failure\033[00m")
    elif ("error" not in result.stderr):
      print(f"\033[32;1m{file} ({test}/{nb_test}) : success\033[00m")
      success_test += 1
    test += 1
    total_test += 1

def air01():
  examples = [[["Bonjour les gars"], ["les"]],
              [["Bonjour les le lesa filles"] , ["lesa"]]]
  file = "air01"
  test = 1
  global success_test
  global total_test
  for i in examples:
    nb_test = len(examples)
    arg = str(i[0])[1:-1]
    arg2 = str(i[1])[1:-1]
    result = subprocess.run(f"python3 {file}.py {arg} {arg2}", shell=True, capture_output=True, text=True)
    # print(f"arg : {arg} + {arg2}")
    # print(f"stdout : {result.stdout}")
    # print(f"stderr : {result.stderr}")
    if "can't open file" in result.stderr:
      print("==> File not found")
      print(f"\033[31;1m{file} ({test}/{nb_test}) : failure\033[00m")
    elif "error" in result.stderr:
      print(f"\033[31;1m{file} ({test}/{nb_test}) : failure\033[00m")
    elif ("error" not in result.stderr):
      print(f"\033[32;1m{file} ({test}/{nb_test}) : success\033[00m")
      success_test += 1
    test += 1
    total_test += 1

def air02():
  examples = [[["Je tests des trucs"], ["  "]],
              [["Je tests des trucs"] , ["-"]]]
  file = "air02"
  test = 1
  global success_test
  global total_test
  for i in examples:
    nb_test = len(examples)
    arg = str(i[0])[2:-2]
    arg2 = str(i[1])[1:-1]
    result = subprocess.run(f"python3 {file}.py {arg} {arg2}", shell=True, capture_output=True, text=True)
    # print(f"arg : {arg} + {arg2}")
    # print(f"stdout : {result.stdout}")
    # print(f"stderr : {result.stderr}")
    if "can't open file" in result.stderr:
      print("==> File not found")
      print(f"\033[31;1m{file} ({test}/{nb_test}) : failure\033[00m")
    elif "error" in result.stderr:
      print(f"\033[31;1m{file} ({test}/{nb_test}) : failure\033[00m")
    elif ("error" not in result.stderr):
      print(f"\033[32;1m{file} ({test}/{nb_test}) : success\033[00m")
      success_test += 1
    test += 1
    total_test += 1

def air03():
  examples = [["1 2 3 4 5 4 3 2 1"],
              ["1 2 3 4 5 4 3 2 11"],
              ["bonjour monsieur bonjour"]]
  file = "air03"
  test = 1
  global success_test
  global total_test
  for i in examples:
    nb_test = len(examples)
    arg = str(i)[2:-2]
    result = subprocess.run(f"python3 {file}.py {arg}", shell=True, capture_output=True, text=True)
    # print(f"arg : {arg}")
    # print(f"stdout : {result.stdout}")
    # print(f"stderr : {result.stderr}")
    if "can't open file" in result.stderr:
      print("==> File not found")
      print(f"\033[31;1m{file} ({test}/{nb_test}) : failure\033[00m")
    elif "error" in result.stderr:
      print(f"\033[31;1m{file} ({test}/{nb_test}) : failure\033[00m")
    elif ("error" not in result.stderr):
      print(f"\033[32;1m{file} ({test}/{nb_test}) : success\033[00m")
      success_test += 1
    test += 1
    total_test += 1

def air04():
  examples = [["Hello milady,   bien ou quoi ??"],
              ["Hellooo milady,   biiiien ou quoiiii ??"]]
  file = "air04"
  test = 1
  global success_test
  global total_test
  for i in examples:
    nb_test = len(examples)
    arg = str(i)[1:-1]
    result = subprocess.run(f"python3 {file}.py {arg}", shell=True, capture_output=True, text=True)
    # print(f"arg : {arg}")
    # print(f"stdout : {result.stdout}")
    # print(f"stderr : {result.stderr}")
    if ("error" not in result.stdout) and result.stderr == "":
      print(f"\033[32;1m{file} ({test}/{nb_test}) : success\033[00m")
      success_test += 1
    elif result.stderr != "":
      print("==> File not found")
      print(f"\033[31;1m{file} ({test}/{nb_test}) : failure\033[00m")
    else:
      print(f"\033[31;1m{file} ({test}/{nb_test}) : failure\033[00m")
    test += 1
    total_test += 1

def air05():
  examples = [[["1 2 3 4 5"], ["+2"]],
              [["10 11 12 20"] , ["-5"]]]
  file = "air05"
  test = 1
  global success_test
  global total_test
  for i in examples:
    nb_test = len(examples)
    arg = str(i[0])[2:-2]
    arg2 = str(i[1])[1:-1]
    result = subprocess.run(f"python3 {file}.py {arg} {arg2}", shell=True, capture_output=True, text=True)
    # print(f"arg : {arg} + {arg2}")
    # print(f"stdout : {result.stdout}")
    # print(f"stderr : {result.stderr}")
    if "can't open file" in result.stderr:
      print("==> File not found")
      print(f"\033[31;1m{file} ({test}/{nb_test}) : failure\033[00m")
    elif "error" in result.stderr:
      print(f"\033[31;1m{file} ({test}/{nb_test}) : failure\033[00m")
    elif ("error" not in result.stderr):
      print(f"\033[32;1m{file} ({test}/{nb_test}) : success\033[00m")
      success_test += 1
    test += 1
    total_test += 1

def air06():
  examples = [["Michel Albert Thérèse Benoit t"],
              ["Michel Albert Thérèse Benoit a"]]
  file = "air06"
  test = 1
  global success_test
  global total_test
  for i in examples:
    nb_test = len(examples)
    arg = str(i)[2:-2]
    result = subprocess.run(f"python3 {file}.py {arg}", shell=True, capture_output=True, text=True)
    # print(f"arg : {arg}")
    # print(f"stdout : {result.stdout}")
    # print(f"stderr : {result.stderr}")
    if "can't open file" in result.stderr:
      print("==> File not found")
      print(f"\033[31;1m{file} ({test}/{nb_test}) : failure\033[00m")
    elif "error" in result.stderr:
      print(f"\033[31;1m{file} ({test}/{nb_test}) : failure\033[00m")
    elif ("error" not in result.stderr):
      print(f"\033[32;1m{file} ({test}/{nb_test}) : success\033[00m")
      success_test += 1
    test += 1
    total_test += 1

def air07():
  examples = [["1 3 4 0 2"],
              ["10 20 30 40 50 60 70 90 33"]]
  file = "air07"
  test = 1
  global success_test
  global total_test
  for i in examples:
    nb_test = len(examples)
    arg = str(i)[2:-2]
    result = subprocess.run(f"python3 {file}.py {arg}", shell=True, capture_output=True, text=True)
    # print(f"arg : {arg}")
    # print(f"stdout : {result.stdout}")
    # print(f"stderr : {result.stderr}")
    if "can't open file" in result.stderr:
      print("==> File not found")
      print(f"\033[31;1m{file} ({test}/{nb_test}) : failure\033[00m")
    elif "error" in result.stderr:
      print(f"\033[31;1m{file} ({test}/{nb_test}) : failure\033[00m")
    elif ("error" not in result.stderr):
      print(f"\033[32;1m{file} ({test}/{nb_test}) : success\033[00m")
      success_test += 1
    test += 1
    total_test += 1

def air08():
  examples = [["100 150 125"],
            ["1000 1500 1250"]]
  
  examples = [["11 15 12 14 fusion 5 8 7 9"],
            ["110 150 120 140 fusione 50 80 70 90"]]
  file = "air08"

  test = 1
  global success_test
  global total_test
  for i in examples:
    nb_test = len(examples)
    arg = str(i)[2:-2]
    # result = subprocess.run(f"python3 air08.py 11 15 12 14 fusion {arg}", shell=True, capture_output=True, text=True)
    result = subprocess.run(f"python3 {file}.py {arg}", shell=True, capture_output=True, text=True)
    # print(f"arg : {arg}")
    # print(f"stdout : {result.stdout}")
    # print(f"stderr : {result.stderr}")
    if "can't open file" in result.stderr:
      print("==> File not found")
      print(f"\033[31;1m{file} ({test}/{nb_test}) : failure\033[00m")
    elif "error" in result.stderr:
      print(f"\033[31;1m{file} ({test}/{nb_test}) : failure\033[00m")
    elif ("error" not in result.stderr):
      print(f"\033[32;1m{file} ({test}/{nb_test}) : success\033[00m")
      success_test += 1
    test += 1
    total_test += 1

def air09():
  examples = [["Michel Albert Thérèse Benoit"],
              ["Albert Thérèse Benoit Michel"]]
  file = "air09"
  test = 1
  global success_test
  global total_test
  for i in examples:
    nb_test = len(examples)
    arg = str(i)[2:-2]
    result = subprocess.run(f"python3 {file}.py {arg}", shell=True, capture_output=True, text=True)
    # print(f"arg : {arg}")
    # print(f"stdout : {result.stdout}")
    # print(f"stderr : {result.stderr}")
    if "can't open file" in result.stderr:
      print("==> File not found")
      print(f"\033[31;1m{file} ({test}/{nb_test}) : failure\033[00m")
    elif "error" in result.stderr:
      print(f"\033[31;1m{file} ({test}/{nb_test}) : failure\033[00m")
    elif ("error" not in result.stderr):
      print(f"\033[32;1m{file} ({test}/{nb_test}) : success\033[00m")
      success_test += 1
    test += 1
    total_test += 1

def air10():
  examples = [["air02.py"],
              ["air01.py"]]
  file = "air10"
  test = 1
  global success_test
  global total_test
  for i in examples:
    nb_test = len(examples)
    arg = str(i)[1:-1]
    result = subprocess.run(f"python3 {file}.py {arg}", shell=True, capture_output=True, text=True)
    # print(f"arg : {arg}")
    # print(f"stdout : {result.stdout}")
    # print(f"stderr : {result.stderr}")
    if "can't open file" in result.stderr:
      print("==> File not found")
      print(f"\033[31;1m{file} ({test}/{nb_test}) : failure\033[00m")
    elif "error" in result.stderr:
      print(f"\033[31;1m{file} ({test}/{nb_test}) : failure\033[00m")
    elif ("error" not in result.stderr):
      print(f"\033[32;1m{file} ({test}/{nb_test}) : success\033[00m")
      success_test += 1
    test += 1
    total_test += 1

def air11():
  examples = [["0 5r"],
              ["1 10"]]
  file = "air11"
  test = 1
  global success_test
  global total_test
  for i in examples:
    nb_test = len(examples)
    arg = str(i)[2:-2]
    result = subprocess.run(f"python3 {file}.py {arg}", shell=True, capture_output=True, text=True)
    # print(f"arg : {arg}")
    # print(f"stdout : {result.stdout}")
    # print(f"stderr : {result.stderr}")
    if "can't open file" in result.stderr:
      print("==> File not found")
      print(f"\033[31;1m{file} ({test}/{nb_test}) : failure\033[00m")
    elif "error" in result.stderr:
      print(f"\033[31;1m{file} ({test}/{nb_test}) : failure\033[00m")
    elif ("error" not in result.stderr):
      print(f"\033[32;1m{file} ({test}/{nb_test}) : success\033[00m")
      success_test += 1
    test += 1
    total_test += 1

def air12():
  examples = [["6 5 4 3 2 1"],
              ["6 5 4 3 2 1q"]]
  file = "air12"
  test = 1
  global success_test
  global total_test
  for i in examples:
    nb_test = len(examples)
    arg = str(i)[2:-2]
    result = subprocess.run(f"python3 {file}.py {arg}", shell=True, capture_output=True, text=True)
    # print(f"arg : {arg}")
    # print(f"stdout : {result.stdout}")
    # print(f"stderr : {result.stderr}")
    if "can't open file" in result.stderr:
      print("==> File not found")
      print(f"\033[31;1m{file} ({test}/{nb_test}) : failure\033[00m")
    elif "error" in result.stderr:
      print(f"\033[31;1m{file} ({test}/{nb_test}) : failure\033[00m")
    elif ("error" not in result.stderr):
      print(f"\033[32;1m{file} ({test}/{nb_test}) : success\033[00m")
      success_test += 1
    test += 1
    total_test += 1

success_test = 0
total_test = 0

def exo():
  air00()
  air01()
  air02()
  air03()
  air04()
  air05()
  air06()
  air07()
  air08()
  air09()
  air10()
  air11()
  air12()
  print(f"Total success: \033[33;7m{success_test}/{total_test}\033[00m")

exo()
print("J’ai terminé l’Épreuve de l’Air et c’était stylé")
