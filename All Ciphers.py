import string

temp = string.ascii_lowercase
lowerBet = list(temp) #Array for lowercase alphabet
temp = string.ascii_uppercase
upperBet = list(temp) #Array for uppercase alphabet
alphaLen = 26
ciphered = []

def encrypt(n, case):
  letter = ""
  for i in range(0, alphaLen):
    if n == i+1:
      letter = case[i]
      ciphered.append(letter)

def add(n, key, case):
  inRange = False
  while not inRange:
    if (n + key) > alphaLen:
      key -= alphaLen
    elif (n + key) < -alphaLen:
      key += alphaLen
    else:
      inRange = True
  n += key
  encrypt(n, case)

def main():
  global ciphered
  running = True
  while running:
    toEncrypt = input("Enter a sentence: ")

    if toEncrypt == "1q2w3e4r5t6y7u8i9o0p": # Kill code (alternating going across top two rows on keyboard)
      running = False

    else:
      for key in range(0,alphaLen):
        for i in toEncrypt:
          n = 1
          if i in lowerBet:
            n += lowerBet.index(i)
            add(n, key, lowerBet)
          elif i in upperBet:
            n += upperBet.index(i)
            add(n, key, upperBet)
          else:
            ciphered.append(i)
        completedWord = "".join(ciphered)
        print(completedWord)
        ciphered = []

main()
