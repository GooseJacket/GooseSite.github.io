from random import randint
from random import choices


def way(l):
  values = []
  ret = []
  for i in l:
    if i not in values:
      values.append(i)
      ret.append(1)
    else:
      ret[values.index(i)] += 1
  div = sum(ret)
  ret = [i / div for i in ret]
  return ret


def weightedChoice(n, l):
  if (n == 2): return choices([0, 1, 2], way(l))[0]
  if (n == 3): return choices([0, 1, 2, 3], way(l))[0]
  return 0


adjectives = [
    "bunt", "beliebt", "echt", "schoen", "toll", "blau", "besser", "gut",
    "deutlich", "international"
]
fem = ["Katze", "Frau", "Tante", "Freundin", "Familie", "Offenkeit"]
masc = ["Herr", "Hund", "Junge", "Freund", "Arbeiter"]
neut = ["Maedchen", "Handy", "Heim", "Kind", "Haus"]
pl = ["Herren", "Eltern", "Augen", "Geschwister", "Freunde"]

femEnds = [
    ["e", "e", "en", "en"],  #der
    ["e", "e", "en", "en"],  #ein
    ["e", "e", "er", "er"]  #unp
]
mascEnds = [
    ["e", "en", "en", "en"],  #der
    ["er", "en", "en", "en"],  #ein
    ["er", "en", "em", "en"]  #unp
]
neutEnds = [
    ["e", "e", "en", "en"],  #der
    ["es", "es", "en", "en"],  #ein
    ["es", "es", "em", "en"]  #unp
]
plEnds = [
    ["en", "en", "en", "en"],  #der
    ["en", "en", "en", "en"],  #ein
    ["e", "e", "en", "er"]  #unp
]

derW = [
    ["die", "die", "der", "der"],  #fem
    ["der", "den", "dem", "des"],  #masc
    ["das", "das", "dem", "des"],  #neut
    ["die", "die", "den", "der"]  #pl
]
einW = [
    ["eine", "eine", "einer", "einer"],  #fem
    ["ein", "einen", "einem", "eines"],  #masc
    ["ein", "ein", "einem", "eines"],  #neut
    ["keine", "keine", "keinen", "keiner"]  #pl
]
unpW = [
    [  #fem,masc,neut
        ["Toll ist", "Wo ist", "Welche Farbe ist"],
        ["Gern habe ich", "Ich kenne", "Es gibt"],
        ["Das Essen gefaellt", "Es ist kalt bei", "Die Karte von"],
        ["Waehrend", "Trotz", "Die Mutter"]
    ],
    [  #pl
        ["Toll sind", "Wo sind", "Welche Farbe ist"],
        ["Gern habe ich", "Ich kenne", "Es gibt"],
        ["Das Essen gefaellt", "Es ist kalt bei", "Die Karte von"],
        ["Waehrend", "Trotz", "Die Tante"]
    ]
]

stats = [
    [0, 1, 2, 3],  #gender - f m n p 
    [0, 1, 2, 3],  #case - n a d g
    [0, 1, 2]
]  #type - d e unp

wins = 0

for i in range(100):
  print("Round", i + 1)
  prompt = ""
  ans = ""
  hint = ["", "", ""]

  case = weightedChoice(3, stats[1])  #0=nom 1=acc 2=dat 3=gen
  gender = weightedChoice(3, stats[0])  #0=fem 1=masc 2=neut 3=pl
  type = weightedChoice(2, stats[2])  #0=der 1=ein 3=unp

  if (gender < 3):
    prompt += unpW[0][case][randint(0, len(unpW[0][case]) - 1)] + " "
  else:
    prompt += unpW[1][case][randint(0, len(unpW[1][case]) - 1)] + " "

  if (type == 0):
    hint[0] = "der"
    prompt += derW[gender][case] + " "
  elif (type == 1):
    hint[0] = "ein"
    prompt += einW[gender][case] + " "
  else:
    hint[0] = "unp"

  prompt += adjectives[randint(0, len(adjectives) - 1)] + "__ "

  if (gender == 0): prompt += fem[randint(0, len(fem) - 1)]
  elif (gender == 1): prompt += masc[randint(0, len(masc) - 1)]
  elif (gender == 2): prompt += neut[randint(0, len(neut) - 1)]
  elif (gender == 3): prompt += pl[randint(0, len(pl) - 1)]

  should = ""
  if (gender == 0):
    hint[1] = "fem"
    should = femEnds[type][case]
  elif (gender == 1):
    hint[1] = "masc"
    should = mascEnds[type][case]
  elif (gender == 2):
    hint[1] = "neut"
    should = neutEnds[type][case]
  elif (gender == 3):
    hint[1] = "pl"
    should = plEnds[type][case]

  print(prompt)
  ans = input()
  if (case == 0): hint[2] = "nom"
  elif (case == 1): hint[2] = "acc"
  elif (case == 2): hint[2] = "dat"
  elif (case == 3): hint[2] = "gen"

  if (ans == "hint"):
    print(hint)
    ans = input()

  affect = 0
  if (ans == should):
    print("good job!")
    wins += 1
    ans == ""
    stats[0].remove(gender)
    stats[1].remove(case)
    stats[2].remove(type)

    if (gender not in stats[0]): stats[0].append(gender)
    if (case not in stats[1]): stats[1].append(case)
    if (type not in stats[2]): stats[2].append(type)

  else:
    print("The answer was:", should, "because", hint)
    ans = ""

    stats[0].append(gender)
    stats[1].append(case)
    stats[2].append(type)

  print()

print(wins)
