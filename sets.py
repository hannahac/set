def count_vowels(mystring):
    my_set = set()
    vowels_in_string = set()

    vowels = ['a', 'e', 'i', 'o', 'u']
    for element in mystring:
        if mystring.count(element) >= 2:
            my_set.add(element)
        if element in vowels:
            vowels_in_string.add(element)

    string_of_vowels = "".join(vowels_in_string)
    number_of_duplicates = len(my_set)
    return (string_of_vowels, number_of_duplicates)

mystring = input('enter your string here: ')
result = count_vowels(mystring)
print (result)
