#Task 8 Band Welcome !
'''
Task 8 Band Welcome ! (7 marks)

Your band has its very first gig! What songs are you going to play?

Write a program that asks for your band name, and then for a 
list of space-separated song titles.

Note: Your band only sings songs with one=word titles!

The output should look like this:
=========================
Band: The One Word Wonders
Songs: Song Lyric Ballad
Please welcome to the stage, The One Word Wonders!
They will be playing...
! Song
! Lyric
! Ballad
Give it up for The One Word Wonders!
========================= 

Here's another example:
=========================
Band: Lady Gaga
Songs: Paparazzi Applause Shallow
Please welcome to the stage, Lady Gaga!
They will be playing...
! Paparazzi
! Applause
! Shallow
Give it up for Lady Gaga!
=========================

HINT: Use "!" as the symbol in front of the songs!

'''

def main():
    x="Task8"
    #===============================
    # Write your code here
band_name = input("Band: ")
songs_input = input("Songs: ")
songs_list = songs_input.split()  # Split space-separated songs into a list
    
    # Print the initial lines
print(f"Band: {band_name}")
print(f"Songs: {songs_input}")
print(f"Please welcome to the stage, {band_name}!")
print("They will be playing...")
    
    # Loop over songs and print each with "!"
for song in songs_list:
        print(f"! {song}")
    
    # Final line
print(f"Give it up for {band_name}!")    

    
    # End of your code here
    #===============================

if __name__ == '__main__':
    main()
