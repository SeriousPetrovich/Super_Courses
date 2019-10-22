f = open('text.txt')
text = f.read()

text = text + ' '

num_of_words = 0
num_of_mistakes = 0
probels = 50


for char in text:
    if char == ' ': num_of_words += 1
    elif char == '(': num_of_mistakes += 1
print('\n' * 5 + ' ' * probels  + 'num_of_words = ', num_of_words, '\n')
print(' ' * probels  + 'num_of_mistakes = ', num_of_mistakes, '\n')
print(' ' * probels  + 'accuracy = ', int((num_of_words-num_of_mistakes)/num_of_words*100),'%'+'\n' * 5)
                                                
f.close()