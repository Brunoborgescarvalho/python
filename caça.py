Varia = 0
import random
primeira_coluna = {0: "Ford",
  "model": "Mustang",
  "year": 1964}
primeiro = primeira_coluna.values()
print(primeira_coluna[0])
primeira_coluna = [ ('Coelho' , 10) , ('aguia' , 20) , ('Bomba' , -1000)]
segunda_coluna = [('Coelho' , 10) , ('aguia' , 20) , ('Bomba' , -1000)]
terceira_coluna = [('Coelho' , 10) , ('aguia' , 20) , ('Bomba' , -1000)]

random.shuffle(primeira_coluna)

random.shuffle(segunda_coluna)

random.shuffle(terceira_coluna)

#segunda coluna
random.shuffle(primeira_coluna)

random.shuffle(segunda_coluna)

random.shuffle(terceira_coluna)

#terceira coluna
random.shuffle(primeira_coluna)

random.shuffle(segunda_coluna)

random.shuffle(terceira_coluna)

if primeira_coluna[0] == segunda_coluna[0] == terceira_coluna[0]:
    print("ganhou 10")
if primeira_coluna[1] == segunda_coluna[1] == terceira_coluna[1]:
    print("ganhou 20")
if primeira_coluna[2] == segunda_coluna[2] == terceira_coluna[2]:
    print("ganhou 30")