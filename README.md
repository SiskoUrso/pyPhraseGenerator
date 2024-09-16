# pyPhraseGenerator
Python Passphrase Generator as a project I choose for a first self python project outside of a class objective.

As I have been learning python for the last 3 months I had been thinking about what kind of project that I could work on outside of the ones learning in the classes I have been taking on udemy and other sites. 

I came across ideas of a password generator would be a good project to start with at a level like mind, and it probably would have been if it had stayed at that but when I started putting together my plan I realized how more often than not passphrases were starting to become more secure than just randomness and they can "sometimes" be easier to remember. 

So the project turned into much more than I expected it to be at first which the ideas I was coming across when searching for projects intended this to be which probably was simple random number and letter generation. I was also doing this at night after I had already done some learning for the day and found that as I started it , it would change rapidly over the next day with new knowledge and ideas. Finally I ended up to a point that I felt was ready to go on a repo. Does it need work of course, do I still have changes in mind, yes indeed. But as a starting point for this repo its great. 

Now to some of the details, it uses a word list that I used from [dwyl/english-words](https://github.com/dwyl/english-words) which contains a list of 466K english words that this uses to compile the passphrase. 

It creates it passphrase by determining the amount of max characters used,spaces or not (which can be determined by the user as whitespace, symbol, letter, number), capital letters or not (which would capitalize the first letter of each phrase used), a personal phrase the user provides and its length, and the phrase count limit.

It will determine which words to pull based on the max characters,spaces or not, the length of the personal phrase, and the max phrase amount. 

Whenever random choice was involved I used secrets over random module to maintain security with the passing of the phrases.

Welcome any suggestions, improvements, ideas, etc. 


To Run: 

Close this repo than change your directory to pyPhraseGenerator, than run the main.py file with ```python3 main.py```
