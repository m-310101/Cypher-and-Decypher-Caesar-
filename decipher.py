# The reason for why I have not changed the values of numbers in the decipher
# is because it is unlikely that the will be ciphered, as if it was then the
# key would be very easy to find when comparing numbers to things like dates.

mostCommon = open("mostCommon.txt")
mostCommon = mostCommon.read().split(" , ")
others = ["1","2","3","4","5","6","7","8","9","0",\
          ",",".","<",">",";","'","#",":","@","~",\
          "[","]","{","}","!",'"',"£","$","%","^",\
          "&","*","(",")","_","+","-","="," ","?"]
letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
holding = []
word = []
current_word = []
def capitalize (str1: str):
    sentences = str1.split(". ")
    sentences2 = [i[0].capitalize() + i[1:] for i in sentences]
    string2 = '. '.join(sentences2)
    return string2


def main():
    found = False
    global holding,word,current_word
    ret = input("Enter the ciphered message").lower() # Takes user's input
    for i in range(0,26): # Loops through the number of different letters in alphabet
        for count in ret: # Loops through every character

            # If the character is not a letter, it will append the character.
            if count in others:
                holding = "".join(holding)
                current_word.append(holding)
                current_word.append(count)
                holding = []

            if count in letters: # For if the letter is lowercase
                let = letters.index(count) # Sets variable let to the value of the
                                           # index number of the letter in the array
                if let + i < 26: # If adding i to it is within the
                    let += i                      # range of the alphabet, then it
                    holding.append(letters[let])    # will do so and append that letter
                elif let + i > 25: # If the addition returns a value over 25, it takes
                    let -= 26      # away 26 so it goes back to the beginning
                    let += i
                    holding.append(letters[let])

        # After the word has been altered by 1 key, the array is joined and then
        # appended to a different array called current_word, which is the appended to the
        # array word and both current_word and holdingare reset and the next key is tried.
        holding = "".join(holding)
        current_word.append(holding)
        word.append(current_word)
        current_word=[]
        holding = []


    # Loops through the length of the array word (all the possible keys for the cipher)
    for j in mostCommon: # Loops through each element of the most common words
        for i in range(len(word)):
            while found != True: # If the word has not been found it loops
                if j not in word[i]:
                    found = False # Found = false if it hasn't been found
                elif j in word[i]: # If the element is found in one element of the key versions
                    word[i] = "".join(word[i])
                    out = capitalize(word[i])
                    print("The sentence reads:\n"+out)# That key value will be printed
                    found = True # Found = True and the loop breaks
                    holding = []
                    word = []
                    current_word = []
                    break
                break
    # After looping through all keys, if the correct sentence hasn't been found,
    # code prints error message.
    if found != True:
        print("Either this sentence is not a Caesar cipher, or this sentence does not make sense.")
        holding = []
        word = []
        current_word = []   
main()
