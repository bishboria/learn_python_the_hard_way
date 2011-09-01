def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Sorts the words."""
    return sorted(words)

def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(0)
    print word

def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1)
    print word

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sorted(words)

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)

# Extra Credit
# >>> ex25.print_first_word(sorted_words)                           # printing out the first word in the sorted_words list
# All                                                               # which pops the word off the list
# >>> ex25.print_last_word(sorted_words)                            # same again but with the last word
# who
# >>> sorted_words                                                  # shows the state of sorted_words after all the popping
# ['come', 'good', 'things', 'those', 'to', 'wait.']
# >>> sorted_words = ex25.sort_sentence(sentence)                   # sorts the sentence
# >>> sorted_words                                                  # and shows the list
# ['All', 'come', 'good', 'things', 'those', 'to', 'wait.', 'who']
# >>> ex25.print_first_and_last(sentence)                           # print the first and last word in the sentence
# All
# wait.
# >>> ex25.print_first_and_last_sorted(sentence)                    # sorts the sentence before printing the first and last sentence
# All
# who
# >>> ^D                                                            # exit the repl
