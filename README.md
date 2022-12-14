# Hangman Game

Hangman Game is a Python terminal game, which runs in the Code Institute mock terminal on Heroku. You can read more about it on wikipedia https://en.wikipedia.org/wiki/Hangman_(game)

The computer generates a random word from a given list in the code and the game is for the user to guess what is the word. 


Here is my Hangman project https://hangman-ga.herokuapp.com/ 


<img src="README images/Screenshot (109).png" alt="">

## How to play
<hr>

My Hangman Game is based on the classic pen and paper game that's usually played by two players. One player comes up with a word and puts dashes on a piece of paper for the empty spaces for the letters to be guessed. The second player then has to guess letters from the word and has limited guesses or until the player is "hanged". The first player has to put the correctly guessed letter in the correct position.

In my version the computer generates a random word from a given list with possible choices. The user than gets 7 'lives' to try and guess either a letter or the whole word. For every wrong entry or invalid input (such as blank space, symbol or a number) the player looses a live and can continue guessing until they loose all their lives which is when they get a message "You are HUNG" and the correct word displayed.
If the player guesses a correct letter said letter is put in the right position and the player doesn't loose a life. The user can also try and guess the whole word and if it's correct the word gets displayed in the terminal with the message "You win! Well done!"

## Features
<hr>
Random word generation
<ul>
    <br>
    <li> The computer generates random word from a list provided in the code
    <li> The user sees the word displayed as dashes ('-') with the correct amount of letters but no letters visible
</ul>  <img src="README images/Start.png" alt="">
<ul>
    <li> Accepts user input and displays the user's guess
    <li> Prints the user's guess and if its correct it replaces one of the dashes with the correct letter in the correct position
</ul>  <img src="README images/Correct.png" alt="">
    <li> Prints a different message depending on if the player's input is correct
</ul>  <img src="README images/You win + correct guess.png" alt="">
</ul>  <img src="README images/Invalid input + Hung.png" alt="">
    <li> If the guess is incorrect one live out of seven is taken from the user
    <li> Displays a message with number of lives left
    <hr>
    Input validation and error
    <ul>
    <br>
    <li> If the user enters an incorrect value such as symbol, number or a space a message displays "Invalid input! Please enter a letter or a whole word."
    <li> If an invalid input has been entered the player looses a live
</ul>  <img src="README images/Invalid input.png" alt="">

## Testing
<hr>
<li> I have manually tested the code in PEP8 and there were few minor indentation problems that did not affect the functionallity of the code but have been fixed
<li> Given invalid inputs: empty spaces, symbols and numbers both in GitPod and the Heroku mock terminal

## Data Model
<hr>
For my data model I have attached a link to a flowchart of my game

[https://lucid.app/lucidspark/49bb29b7-fa45-4b02-b526-e96e61ca21eb/edit?viewport_loc=244%2C2147%2C3530%2C1630%2C0_0&invitationId=inv_cbfe13d4-a556-4448-b490-b43e9048acaa]


## Bugs
<hr>
Solved bugs
<li> At first I was using a while loop for the invalid input. I wrote down the function on paper and then is when I actually realized I was using a loop so I changed it to an exception error handling following a simple structure of exception/error handling and just replacing it with the values and messages for my own game. Also at first my game was taking lives for invalid input but after showing the game to friends they said in a real life game I wouldn't be taking lives for invalid input Ill just remind the other player that they have to give me a letter or a word so I removed what I had at first lives_remaining = lives_remaining - 1 and I added the 'raise ValueError ('invalid input') to actually raise that error as thought by the course material in Code Institute.

## Remaining bugs
<li> After checking my code in PEP8 Syntax Checker there are few bugs that remain but do not affect the functionality of the code such as white space around operators. I feel like it looks better without the space around the dash:
<img src="README images/White spaces around operators.png" alt="">
and:
<img src="README images/Indentation white spaces.png" alt="">
Which does not affect the functionallity of the code

## Validator testing
<li>PEP8
No significant errors found only the ones stated above in unfixed bugs

## Deployment
 <li> Steps for deployment
 <li> Create a new Heroku app
 <li> Set the buildbacks to Python and NodeJS in that order
 <li> Link the Heroku app to the repository
 <li> Click on Deploy
 
 <li> Clone the repository 
 <li> Open the code tab in my repository
 <li> Copy the link from HTTPS tab
 <li>Open git Bash and type git clone and add the link

 ## Credits
 <li> For main structure used this tutorial: [https://biteresources.com/attachments/article/20/Hangman%20Guide.pdf]
 <li> Code institute lessons
 <li> WW3 Schools for checking syntax