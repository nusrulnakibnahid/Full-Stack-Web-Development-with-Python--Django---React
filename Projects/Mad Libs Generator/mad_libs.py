print("🎉 Welcome to the Mad Libs Generator 🎉\n")

# Taking user input
name = input("Enter a name: ")
adjective1 = input("Enter an adjective: ")
adjective2 = input("Enter another adjective: ")
noun1 = input("Enter a noun: ")
noun2 = input("Enter another noun: ")
verb1 = input("Enter a verb (past tense): ")
verb2 = input("Enter a verb: ")
place = input("Enter a place: ")

# Story template
story = f"""
One day, {name} went to {place}.
It was a very {adjective1} day.
Suddenly, a {adjective2} {noun1} appeared!

{name} {verb1} and grabbed a {noun2}.
Without thinking, {name} decided to {verb2}.

Everyone in {place} was shocked.
It was the most unforgettable day ever!
"""

# Display the story
print("\n📖 Here is your Mad Libs story:")
print(story)
