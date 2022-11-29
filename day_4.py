# Only Floats

def only_floats(a, b):
    """returns 2 if both float,
    1 if one float, 0 if none float."""
    
    float_count = 0
    if type(a)==float:
        float_count += 1
    if type(b)==float:
        float_count += 1
    
    return 2 if float_count==2\
        else 1 if float_count==1\
            else 0

print(only_floats(12.1, 23))


# Extra Challenge: Index of the Longest Word

def word_index(l):
    """returns the index of the longest word in the list."""
    
    dup_count = 0
    max = 0
    
    for ind, ele in enumerate(l):
      
          if len(ele) == max:
            dup_count += 1
            
          if len(ele) > max:
            max = len(ele)
            max_ind = ind            
  
    return 0 if dup_count+1 == len(l)\
        else max_ind

words1 = ["Hate", "remorse", "vengeance"]
words2 = ["Love", "Hate"]

print(word_index(words1))
print(word_index(words2))
