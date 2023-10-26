def print_upper_words(word_list, must_start_with):
    '''For a list of words, this will print out each word on a seperate line in all uppercase'''

    for letter in must_start_with:
        for word in word_list:
            if word[0].lower() == letter:
                print(word.upper())
    

# this should print "HELLO", "HEY", "YO", and "YES"

print_upper_words(["hello", "hey", "goodbye", "yo", "yes"],
                   must_start_with={"h", "y"})
