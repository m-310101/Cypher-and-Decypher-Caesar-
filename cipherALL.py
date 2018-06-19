ciphered = []

def letterEncrypt(number):
    letter = ""
    if number == 1:
        letter = "a"
        ciphered.append(letter)
    if number == 2:
        letter = "b"
        ciphered.append(letter)
    if number == 3:
        letter = "c"
        ciphered.append(letter)
    if number == 4:
        letter = "d"
        ciphered.append(letter)
    if number == 5:
        letter = "e"
        ciphered.append(letter)
    if number == 6:
        letter = "f"
        ciphered.append(letter)
    if number == 7:
        letter = "g"
        ciphered.append(letter)
    if number == 8:
        letter = "h"
        ciphered.append(letter)
    if number == 9:
        letter = "i"
        ciphered.append(letter)
    if number == 10:
        letter = "j"
        ciphered.append(letter)
    if number == 11:
        letter = "k"
        ciphered.append(letter)
    if number == 12:
        letter = "l"
        ciphered.append(letter)
    if number == 13:
        letter = "m"
        ciphered.append(letter)
    if number == 14:
        letter = "n"
        ciphered.append(letter)
    if number == 15:
        letter = "o"
        ciphered.append(letter)
    if number == 16:
        letter = "p"
        ciphered.append(letter)
    if number == 17:
        letter = "q"
        ciphered.append(letter)
    if number == 18:
        letter = "r"
        ciphered.append(letter)
    if number == 19:
        letter = "s"
        ciphered.append(letter)
    if number == 20:
        letter = "t"
        ciphered.append(letter)
    if number == 21:
        letter = "u"
        ciphered.append(letter)
    if number == 22:
        letter = "v"
        ciphered.append(letter)
    if number == 23:
        letter = "w"
        ciphered.append(letter)
    if number == 24:
        letter = "x"
        ciphered.append(letter)
    if number == 25:
        letter = "y"
        ciphered.append(letter)
    if number == 26:
        letter = "z"
        ciphered.append(letter)

def add(number,key):
    while True:
        if number+key > 26:
            key-=26
        elif number+key < -26:
            key+=26
        else:
            break
    number+=key
    letterEncrypt(number)

def main():
    while True:
        ret = input("Please give me a sentence: ").lower()
        if not ret.isalpha() and not " ":
            print("Letters only please")
        else:
            for key in range(0,26):

                for i in ret:
                    number = 0 
                    if i == "a":
                        number = 1
                        add(number,key)
                    elif i == "b":
                        number = 2
                        add(number,key)
                    elif i == "c":
                        number = 3
                        add(number,key)
                    elif i == "d":
                        number = 4
                        add(number,key)
                    elif i == "e":
                        number = 5
                        add(number,key)
                    elif i == "f":
                        number = 6
                        add(number,key)
                    elif i == "g":
                        number = 7
                        add(number,key)
                    elif i == "h":
                        number = 8
                        add(number,key)
                    elif i == "i":
                        number = 9
                        add(number,key)
                    elif i == "j":
                        number = 10
                        add(number,key)
                    elif i == "k":
                        number = 11
                        add(number,key)
                    elif i == "l":
                        number = 12
                        add(number,key)
                    elif i == "m":
                        number = 13
                        add(number,key)
                    elif i == "n":
                        number = 14
                        add(number,key)
                    elif i == "o":
                        number = 15
                        add(number,key)
                    elif i == "p":
                        number = 16
                        add(number,key)
                    elif i == "q":
                        number = 17
                        add(number,key)
                    elif i == "r":
                        number = 18
                        add(number,key)
                    elif i == "s":
                        number = 19
                        add(number,key)
                    elif i == "t":
                        number = 20
                        add(number,key)
                    elif i == "u":
                        number = 21
                        add(number,key)
                    elif i == "v":
                        number = 22
                        add(number,key)
                    elif i == "w":
                        number = 23
                        add(number,key)
                    elif i == "x":
                        number = 24
                        add(number,key)
                    elif i == "y":
                        number = 25
                        add(number,key)
                    elif i == "z":
                        number = 26
                        add(number,key)
                    elif i == " ":
                        ciphered.append(i)

                cipher = "".join(ciphered)
                print(cipher)
                global ciphered
                ciphered = []

main()
