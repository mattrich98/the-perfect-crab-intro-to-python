# Video alternative: https://vimeo.com/954334424/6e40d11ef1#t=501

from lib.helpers import check_that_these_are_equal

# Summarising is processing down a list to a single value. It is sometimes also
# called 'reduce' — like reducing a broth to a thick soup.

# Here are some examples:

# * Summing a list of numbers
# * Counting the number of 'q's in a string
# * Concatenating a list of strings

# I'm going to implement the last one, so you can see it at
# work:

lines = [
  "My King,",
  "I need another five years.",
  "Then your crab will be ready.",
  "Sincerely,",
  "Chuang-tzu"
]

#print(lines)

text = "" # This is called the accumulator variable
          # It's where we put our summary value
          # It starts off blank.

for line in lines: # We go through lines item by item -> line is just a variable name for selecting each individual item in the lines list 
  # Inside this loop, `line` is the individual line
  text = text + line # We append the line to our text -> adding each item from lines list to text string variable using line[i]
  text = text + "\n" # We add an `\n`, which means 'new line' -> each time it loops the first item, it makes a new line to split the text, as it cycles until the last item

print(text)


#tests = [1,2,3,4]

#result = 0

#for test in tests:
  #result += test #the reason result = test + test doesn't work is because 4 + 4 = 8, it doesn't add up the list numbers

#print(result)

# We have taken the list of strings and joined them all together into one text
# (the accumulator) with some new lines in it.

# There's actually a Python function that does this too:

another_text = "\n".join(lines)
# Uncomment this next line if you want to see it:
#print(another_text)

# `join` is actually little smarter — it only adds the `\n` character between
# lines, not at the end also.

# @TASK: Complete this exercise

print("")
print("Function: add_up_numbers")

# Add up all the numbers in the list
def add_up_numbers(numbers):
  #pass
  combo = 0 # need variable here for it to work in the loop, this is where your results go
  for number in numbers: #selected parameter numbers, [i] = number, the index
    #print(number) #this is to know that the for loop is cycling through the list numbers
    combo += number #adding the numbers to combo variable each number (index), 1 + 2 + 3 + 4 = 10. A bit confusing but I kind of understand by doing a lsit test above, so it would be looping 1 added to combo, 2 added to combo, 3 added to combo, 4 added to combo and returned to the combo variable
  return combo # this returns the result, it doesn't matter about the name, combo returns the parameter result


check_that_these_are_equal(
  add_up_numbers([1, 2, 3, 4]), 10)
check_that_these_are_equal(
  add_up_numbers([2, 3, 4, 5]), 14)

# When you're done, move on to 035_mapping.py
