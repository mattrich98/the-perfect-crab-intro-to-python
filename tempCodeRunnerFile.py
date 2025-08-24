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
