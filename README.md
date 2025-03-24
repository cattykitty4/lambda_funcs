# lambda_funcs

> lambda_funcs is сonsist of five modules which perform various actions with the lambda fuctions and how to convert lambda fuctions into custom functions.

#  1. How the anagram works?       

> This code compares the list elements passed to the function with the element passed to the function for comparison.
> The element passed to the function from the list is sorted in lexicographic order and compared with the element being compared wrapped in the sorted() function.

# 2. How is if_greater_than_string_length?        

> This code is split into two functions. The checkIsDigit(j, y) function and the findNumber(x) function. First, the findNumber(x) function takes a list of string elements, then it is split into elements. 
> Then the length of the list is found out, and then the elements are passed through a list comprehension to the checkIsDigit(j, y) function, which checks whether the element is a number and whether it is greater than the length of the list. If the result of the function is True, then the element is added to the numbers_collection variable, otherwise not.
   
# 3. How is len_stirngs_with_title works?     

> This code checks the elements to see if the element starts with a capital letter and then adds it to the list. The code then returns the length of all the elements in the list.
> The code also shows a variant using a lambda function, which does the same job, only more compactly.
> The lambda function iterates over the names variable and checks whether the element starts with a capital letter, the lambda function is wrapped in the filter() function, which returns an iterator, after which it is objectified by the list() function

# 4. How is list_with_min_and_max_len works? 
> This code finds nested lists with minimum and maximum length in a given list of lists. It returns tuples containing the length and the list itself for the minimum and maximum cases.
> The code also shows a variant using a lambda function, which does the same job, only more compactly.

# 5. How is positives_and_negatives works? 
> This simple function adds positive numbers to positive numbers and negative numbers to negative numbers. The function is passed a list containing positive and negative numbers.
> The code also shows a variant using a lambda function, which does the same job, only more compactly.
