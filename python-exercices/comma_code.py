#!/usr/bin/python3

iSay you have a list value like this:


"""spam = ['apples', 'bananas', 'tofu', 'cats']
Write a function that takes a list value as an argument and returns a string with all the items separated by a comma and a space, with and inserted before the last item. For example, passing the previous spam list to the function would return 'apples, bananas, tofu, and cats'. But your function should be able to work with any list value passed to it."""

"""def commacode(liste1):

    for i, mot in enumerate(liste1):
        if i < len(liste1) - 1):
            print('{}, '.format(mot), end='')
        else:
            print('and {}.'.format(mot))
liste1 = ['apples', 'bananas', 'cats', 'tofu']
commacode(liste1)"""


def commacode(spam):
    if len(spam) == 1:
        return spam[0]
    else:
        return ('{} and {}'.format(', '.join(spam[:-1]), spam[-1]))

spam = ['a', 'b', 'c', 'd']
x = commacode(spam)
print(x)
