"""
Implement a bunch of functions which receive a changeable number of strings and return next
parameters:
1) characters that appear in all strings
2) characters that appear in at least one string
3) characters that appear at least in two strings
  Note: raise ValueError if there are less than two strings
4) characters of alphabet, that were not used in any string
  Note: use `string.ascii_lowercase` for list of alphabet letters

Note: raise TypeError in case of wrong data type

Examples,
```python
test_strings = ["hello", "world", "python", ]
print(chars_in_all(*test_strings))
#{'o'}
print(chars_in_one(*test_strings))
#{'d', 'e', 'h', 'l', 'n', 'o', 'p', 'r', 't', 'w', 'y'}
print(chars_in_two(*test_strings))
#{'h', 'l', 'o'}
print(not_used_chars(*test_strings))
#{'q', 'k', 'g', 'f', 'j', 'u', 'a', 'c', 'x', 'm', 'v', 's', 'b', 'z', 'i'}
"""
import string


def chars_in_all(*strings):
    ret = list(strings[0])
    for element in strings:
        for _ in element:
            for j in ret:
                if j not in element:
                    ret.remove(j)
    return set(ret)


def chars_in_one(*strings):
    list_of_chars = []
    for element in strings:
        for el in element:
            if el not in list_of_chars:
                list_of_chars.append(el)
    return set(list_of_chars)


def chars_in_two(*strings):
    if len(strings) < 2:
        raise ValueError
    big_clear_str = []
    list_of_chr = []
    for word in strings:
        clear_str = []
        for letter in word:
            if letter not in clear_str:
                clear_str += letter
        big_clear_str += clear_str

    for letter in big_clear_str:
        if big_clear_str.count(letter) >= 2:
            list_of_chr.append(letter)
            big_clear_str.remove(letter)
    return set(list_of_chr)


def not_used_chars(*strings):
    list_of_abs = string.ascii_lowercase
    ret_list = []
    for element in strings:
        for el in list_of_abs:
            if el in element and el not in ret_list:
                ret_list.append(el)
    return set(list_of_abs) - set(ret_list)


print(chars_in_all('hello', 'world', 'python'))
