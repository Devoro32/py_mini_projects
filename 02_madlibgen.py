#https://youtu.be/21FnnGKSRZo?t=1429
#'r' is reading the file, 'w' is write, where it will write over existing file
with open('02_story.txt','r') as f:
    #reading the entire file into story
    story =f.read()
    #print(story)

words=set()
start_of_word= -1

target_start = "<"
target_end = ">"

for i, char in enumerate(story):
    if char == target_start:
        start_of_word = i

    if char == target_end and start_of_word !=-1:
        word =story[start_of_word: i + 1]
        words.add(word)
        start_of_word=-1


print(words)

#create a dictionary to have key and value
answers ={}      

for word in words:
    answer = input ('Enter a word for '+ word + ": ")
    answer[word] = answer

print(answers)

for word in words:
   story= story.replace(word,answer[word])