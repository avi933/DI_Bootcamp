import random
wordslist = ['correction', 'childish', 'beach', 'python', 'assertive', 'interference', 'complete', 'share', 'credit card', 'rush', 'south']

word = random.choice(wordslist)
print(word)
word_hidden = []
for x in word:
  if(x == " "):
    word_hidden.append(" ")
  else:
    word_hidden.append("*")
print(word_hidden)
trials = 0
while(True):
    replaced = False
    letter = input("Enter alphabets to guess the word: ")
    for pos in range(len(word)):
        if(word[pos] == letter):
            print(pos, letter)
            word_hidden[pos] = letter
            replaced = True
    print("".join(word_hidden))
    if(word_hidden.count("*") <= 0):
        print("Congratz, you won!")
        break
    if(not replaced):
        trials = trials + 1
    if(trials >= 3):
        print("you lost")
        break