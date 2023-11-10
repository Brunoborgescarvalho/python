Varia = 0
import random
primeira_coluna = [ ('Coelho' , 10) , ('aguia' , 20) , ('Bomba' , -1000)]
segunda_coluna = [('Coelho' , 10) , ('aguia' , 20) , ('Bomba' , -1000)]
terceira_coluna = [('Coelho' , 10) , ('aguia' , 20) , ('Bomba' , -1000)]
while Varia == 0: 
    random.shuffle(primeira_coluna)
    print(primeira_coluna[0])
    random.shuffle(segunda_coluna)
    print(segunda_coluna[0])
    random.shuffle(terceira_coluna)
    print(terceira_coluna[0])
    if primeira_coluna[0] == segunda_coluna[0]:
        print("ganhou")