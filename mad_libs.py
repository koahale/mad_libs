"""
A simple mad libs program!

The user enters in a series of nouns, adjectives, and verbs.
The input values are then inserted into a story.
"""

food =raw_input('Enter a food: ') + ','
adj1 = raw_input('Enter a adjective:') + " "
adj2 = raw_input('Enter another adjective: ') + " "
noun = raw_input('Enter a noun: ') + ','
verb = raw_input('Enter a verb present ending in ing: ') + ','
noun2 = raw_input('Enter a noun plural: ') + ','
noun3 = raw_input('Enter another noun plural: ') + ','

print("\n")

print('With a new beginning and a fresh piece of ' + food)
print('Full of inspiration and '+ adj1 + 'thoughts, ')
print("lets begin this year with a " + adj2 + noun)
print('Gone are the days of regret and ' + verb)
print('These rooms full of '+ noun2)
print("It's time to move with courage, ")
print("Full of confidence and " + noun3)
print("Let's begin this year with a "+ adj2 + noun)
