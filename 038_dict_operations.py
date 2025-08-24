# Video alternative: https://vimeo.com/954334322/c5a36d4407#t=726

from lib.helpers import check_that_these_are_equal

# Here's a great use for dictionaries: counting!

# For example, counting how many times each letter appears in a string. -> counting how many letters are in a string

# We can use a for loop to iterate over some items, and then use a dictionary to -> use a for loop to loop over all the items
# keep count of the items we've seen.

# In the process, you'll see a few dictionary functions at work, plus the sneaky
# addition of looping over characters in strings.

text = "the quick brush jumped over the lazy crab"

# We'll use a dictionary to keep count of the letters we've seen. We'll start
# with an empty dictionary:




#my information

# it includes the spaces between the letters in the string

#letter is linked with text string and letter_counts dictionary

#letter is like index

#we give the letter the numeric value 1, so when its incremented when it shows again, we add +1 to it

#tip -> also need to make sure using the write dictionary name, wrote letter_counts by mistake

#for letter in text:
#  if letter not in letter_count:
#    letter_counts[letter] = 1
#  else:
#    letter_counts[letter] = letter_counts[letter] + 1

#my information

# We'll use a for loop to iterate over each letter in the string:


letter_counts = {}
# The keys will be the letters, and the values will be the number of that letter
# we've seen.

for letter in text:
  # We'll check if the letter is already in our dictionary of counts. We can do
  # this using the `not in` operator. 
  if letter not in letter_counts:
    # If it isn't, we'll add it to the dictionary with a starting count of 1.
    letter_counts[letter] = 1
    # Note that the syntax for assigning a value to a key in a dict is similar
    # to assigning a variable.
  else:
    # If it is, we'll increment the count for that letter.
    letter_counts[letter] = letter_counts[letter] + 1

# Let's print out the dictionary to see what we've got:
print(letter_counts)







# If you're curious as to why we need to check if the letter is in the
# dictionary, try uncommenting this code and see what happens:

# letter_counts = {}
# for letter in text:
#   letter_counts[letter] = letter_counts[letter] + 1

# In the assignment above, our right hand expression tries to access the value
# for a key that has not been added yet. This causes an error.

# @TASK: Complete this exercise.

print("")
print("Function: count_words_by_length")

# Write this function that counts the number of words by how many letters they
# have. For example:



# words:  ["hat", "cat", "I", "bird"]
# result: {3: 2, 1: 1, 4: 1}
# Since there are two words of length 3, etc.


#to do

# what i need to do this: i need to save the thing in items as a number length

#to do


def count_words_by_length(words):
  #pass
  items = {}

  for word in words:

    #print(len(thing)) #check that works, + len syntax

    if len(word) not in items: #had to add len to first part oh, since it recognises the words individually
      items[len(word)] = 1
    else:
      items[len(word)] = items[len(word)] + 1
  return items

check_that_these_are_equal(
  count_words_by_length(["hat", "cat", "I", "bird"]),
  {3: 2, 1: 1, 4: 1}
)

check_that_these_are_equal(
  count_words_by_length(["four", "four", "four", "one"]),
  {4: 3, 3: 1}
)

# Once you're done, move on to 039_challenge_1_example.py
