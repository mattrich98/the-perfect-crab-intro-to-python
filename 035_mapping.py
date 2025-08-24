# Video alternative: https://vimeo.com/954334322/c5a36d4407#t=0

from lib.helpers import check_that_these_are_equal

# Mapping is going through a list and converting ('mapping') each item to
# another item. This is useful when you want to perform the same operation
# across a list of items.

# For example:

# * Getting the price of each in a list of products
# * Making each in a list of words uppercase
# * Finding the first letter of each in a list of words

# Here's an example:

words = ['I', 'need', 'another', 'five', 'years']

first_letters = [] # This is our accumulator again -> this is where the results will be stored

for word in words: # We go through each word , word is the iterator of the words array
  first_letter = word[0] # Get the first letter -> think this is the index
  # And append it to our accumulator list:
  first_letters.append(first_letter) #it cycles through the words array 5 times

print(words)
print(first_letters)


#testing code

numberList = [1,2,3,4]

editList = []

for number in numberList:
  edit = number + 100
  editList.append(edit)

print(editList) #[101,102,103,104]

#testing code

# @TASK: run this program to see what it does.

# @TASK: Complete this exercise.

print("")
print("Function: add_one_hundred_to_numbers")

# Return a new list of each number with 100 added
def add_one_hundred_to_numbers(numbers):
  #pass
  hundredList = []

  for number in numbers:
    #print(number)
    edit = number + 100
    #print(edit) #test that i have the results, 101,102,103,104, just need to add to array/list
    hundredList.append(edit) 
    #by doing hundredlist print, i could test the results are appended
  return hundredList #returns hundredList is the result of using the function

  #overall conclusion is to make use of print more to test what I am doing


check_that_these_are_equal(
  add_one_hundred_to_numbers([1, 2, 3, 4]), [101, 102, 103, 104])
check_that_these_are_equal(
  add_one_hundred_to_numbers([2, 3, 4, 5]), [102, 103, 104, 105])

# When you're done, move on to 036_filtering.py
