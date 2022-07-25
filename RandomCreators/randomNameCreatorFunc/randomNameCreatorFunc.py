names = ["Emincan", "Alperen", "John", "İbrahim", "Michael", "Cenk" , "Daren" , "Bella" , "Bartu" , "Karen" , "Darius" , "Bilal"]
surnames = ["YILMAZ", "Kulaksız", "Smith" , "Çakıcı", "Monroe" ,"Dilsiz", "Brandon" , "Wallace" ,"Davulcu"]

def randomNameCreator():
    from random import choice as rd
    return rd(names) + " " + rd(surnames)

print(randomNameCreator())
