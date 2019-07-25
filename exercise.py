def word_counter(str):
    count = 0
    words = str.split()
    for word in words:
        count += 1
    print(count)


word_counter("Hello world") # returns 2

word_counter("This is a sentence") # returns 4

word_counter("") # returns 0