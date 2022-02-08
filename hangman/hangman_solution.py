'''
Make sure you complete all the TODOs in this file.
The prints have to contain the same text as indicated, don't add any more prints,
or you will get 0 for this assignment.
'''

import random
import string # adding code for checking input

# Download a package with english words
# Natural Language Toolkit (nltk)
import nltk

# ATTENTION :
# !!!!!! first UNCOMMENT the line below and then recomment it !!!!!

# nltk.download('all')

from nltk.corpus import words
 

class Hangman:
    '''
    A Hangman Game that asks the user for a letter and checks if it is in the word.
    It starts with a default number of lives and a random word from the word_list.

    
    Parameters:
    ----------
    word_list: list
        List of words to be used in the game
    num_lives: int
        Number of lives the player has
    
    Attributes:
    ----------
    word: str
        The word to be guessed picked randomly from the word_list
    word_guessed: list
        A list of the letters of the word, with '_' for each letter not yet guessed
        For example, if the word is 'apple', the word_guessed list would be ['_', '_', '_', '_', '_']
        If the player guesses 'a', the list would be ['a', '_', '_', '_', '_']
    num_letters: int
        The number of UNIQUE letters in the word that have not been guessed yet
    num_lives: int
        The number of lives the player has
    list_letters: list
        A list of the letters that have already been tried

    Methods:
    -------
    check_letter(letter)
        Checks if the letter is in the word.
    ask_letter()
        Asks the user for a letter.
    '''
    
    def __init__(self, word_list):
        
        # initialize attributes
        
        self.word_list = word_list
        
        self.num_lives = 5 # lives remaining
        
        self.list_letters = [] # all the letters input from the user
                        
        self.word = random.choice(word_list) # the word chosen by the computer        
                
        self.letters  = [i for i in self.word]  # list with the letters of the word chosen            
        
        self.word_guessed = [i.replace(i, '_') for i in self.letters] # list with the letters of the list letters replaced with '_'
        
        self.num_letters = len(set(self.letters)) # the number of unique letters in the word chosen
                        
                
        print(f"\nThe mistery word has {self.num_letters} (unique) characters")
                                               

    def check_letter(self):
        '''
        Checks if the letter is in the word.
        If it is, it replaces the '_' in the word_guessed list with the letter.
        If it is not, it reduces the number of lives by 1.

        Parameters:
        ----------
        letter: str
            The letter to be checked

        ''' 
                           
        for i in range(len(self.letters)):
            
            # replace '_' with the the letter given (in the list word_guessed) if the letter is in the list letters
            if self.letter == self.letters[i]:
                self.word_guessed[i] = self.letter                                                                              
            else:            
                continue
            
                        
        if self.letter in self.word:
        # if the letter given is in the word, reduce the unique letters by one    
                self.num_letters -= 1                                            
                print(f"\nNice! Letter {self.letter} is in the word !")
                print(f"\nWords guessed : {self.word_guessed}")
                print(f"\nUnique letters remaining : {self.num_letters} !")
        else:
        # else reduce the lives remaining by one    
                self.num_lives -= 1                                          
                print(f"\nYou have {self.num_lives} lives left :\ ")                    
                
                                
        # as long as you still have lives AND you haven't guessed the word continue                        
        while self.num_lives != 0 and self.num_letters != 0:            
            break
        
        else:
            # else check if user wins and exit the game
            if self.num_lives != 0 :                
                print("\nYeah !!!! You won the game !!!!!")                                        
            else:
                print(f"\nAh you lost! the word was {self.word}")  
                
            self.replay() # wanna play again??

    def replay(self):
        
        while True:            
            play_me_again = input("\nWanna play again? (y/n): ")
            if play_me_again.lower() != "y" and play_me_again.lower() != "yes":           
                exit()
            else:
                play_game(word_list)                    
                                
                                                                                                                                                                                              
    def ask_letter(self):
        '''
        Asks the user for a letter and checks two things:
        1. If the letter has already been tried
        2. If the character is a single character
        If it passes both checks, it calls the check_letter method.
        '''                                       

        while True:
        
            self.letter = input("\nIf you please enter a letter (ctrl + c to escape) : ").lower() # make the input lowercase    
    
            if len(self.letter) == 1: # accept only one character
        
                if self.letter not in string.ascii_letters: # check if the letter given by the user is valid (and not a number i.e)            
                    print("\nPlease enter only letters..")            
                elif self.letter in self.list_letters: # check if the letter input was already tried           
                    print(f"\n'{self.letter}' was already tried ! ")                                    
                else:
                    self.list_letters.append(self.letter) # if letter is valid add it to the list                                             
                    self.check_letter() # and call check_letter method
                
            else:    
                print("\nPlease enter just one character..")                        
             
     
def play_game(word_list):
                
    game = Hangman(word_list)                    
    user_input = game.ask_letter()        
            
if __name__ == '__main__':     
    word_list = words.words()
    play_game(word_list)