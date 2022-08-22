import random
secret_data = []
def get_word_from_file(filename):
    global secret_data
    f = open(filename)
    secret_data = f.readlines() 
    #print(secret_data)
    f.close()

def get_random_from_file():
    length_of_list = (len(secret_data))
    n = random.randint(0,length_of_list)
    
    word  = secret_data[n]
    word = word.strip("\n")
    #print(f'{word} ')
    return (word)
    
    #print(n)
    

def get_random_sentence(length):
    i = 1
    sentence = " "
    while i <= length:
        i+= 1
        sentence += f'{get_random_from_file()} '
    print(sentence.lower())
    return(sentence)   
def main():
    try:
      number = int(input("Enter a number between 2 to 20\n"))
      if (number >=2 and number <=20):
        get_random_sentence(number)
      else:
        print("Number must be between 2 to 20")
    except:
        print("Rien ne marche!!")
     


get_word_from_file("sowpods.txt")

get_random_from_file()

get_random_sentence(5)

main()

