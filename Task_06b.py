#Task 6b New Words
'''
Task 6b New Words - Part2 (4marks)

Add to the code from part 1 to create another new word. 
The new word should replace 'o' in the word with a 'y'. 
Use a for loop to print out each letter of this new word on a new line. 
Then print this new word on 1 line at the end.

For example:
=========================
Say: typo
New word!
t
y
p
y
y
y
y
y
y
typyyyyyy!
========================= 

'''
def main():
    x="Task6b"
    #===============================
    # Write your code here
message = input("Say: ")
parts = message.rsplit(' ', 1)
if len(parts) > 1:
        last_word = parts[1]
else:
        last_word = parts[0]
    
if last_word:
        # Replace 'o' with 'y' in the original last word
        replaced_word = last_word.replace('o', 'y')
        # Emphasize: add last character 5 times
        last_char = replaced_word[-1]
        new_word = replaced_word + last_char * 5
else:
        new_word = ''
    
print("New word!")
    # Use for loop to print each letter on a new line
for char in new_word:
        print(char)
    # Print the full new word on one line with !
print(new_word + '!')
    

    # End of your code here
    #===============================

if __name__ == '__main__':
    main()
