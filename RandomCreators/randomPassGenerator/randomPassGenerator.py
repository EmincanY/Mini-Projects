import random

def passGenerator():
    while True : 
        password = ""
        letters = "abdefghjklmnoöprstyvziqı"
        specialChars = "-,.#+*!"
        difficulty = int(input("Please choose your password difficulty : \n1.Hard\n2.Medium\n3.Easy\nYour Choice : \n"))
        if difficulty == 1 :
            for i in range(1,3):
                password += random.choice(letters) + random.choice(specialChars)
            for i in range(1,4):
                password += str(random.randint(1, 9))
            for i in range(1,3):
                password += random.choice(specialChars)
            print(f"\n\nYour random password : {password}\n\n")
            another = int(input("Do you want another password ? ?\n1 : Yes\n2 : No\nYour Choice : \n"))
            if another == 1:
                pass
            if another == 2:
                return password
        elif difficulty == 2 :
            for i in range(1,4):
                password += random.choice(letters)
            for i in range(1,3):
                password += str(random.randint(1,9))
            print(f"\n\nYour random password : {password}\n\n")
            another = int(input("Do you want another password ? ?\n1 : Yes\n2 : No\nYour Choice : \n"))
            if another == 1:
                pass
            if another == 2:
                return password
        elif difficulty == 3 :
            for i in range(1,5):
                password += str(random.randint(1, 9))
            print(f"\n\nYour random password : {password}\n\n")
            another = int(input("Yeni bir rastgele şifre oluşturmak istiyor musunuz ?\n1 : Evet\n2 : Hayır\nYour Choice : \n"))
            if another == 1:
                pass
            if another == 2:
                return password
        else : 
            print("Please choose right decision, program quit")


print(passGenerator())