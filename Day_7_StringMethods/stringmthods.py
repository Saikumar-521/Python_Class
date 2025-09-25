'''
string is a sequences of charaters and which is enclosed with the single or double qutus
stringmethods:
1.string repation(*)
2.string contation(+)
3.string comparsion:
>,<,>=,<=,==, != ---------->which returns true or false based on condtion


in Python, you can get the ASCII (Unicode code point) value of any character using ord(), 
and convert ASCII values back to characters using chr().

print(ord('A'))  # 65
print(ord('a'))  # 97
print(chr(90))   # 'Z'
print(chr(122))  # 'z'

'''

# string is immutable

s = "Hello"
print(id(s))   # memory location of "Hello"
s = s + "!"
print(id(s))   # different memory location (new object)

# The variable s is updated to point to the new string, while "Hello" may be garbage-collected if no reference exists.



print("sai"*3)
print("sai"+"kumar")
a='sai'
b='kumar'
print(a>b)
print(a<b)
print(a>=b)
print(dir(str))




# string slicing:in Python, string slicing is used to extract a portion (substring) 
# from a string. It works using the slicing operator [:].
# string[start:end:step]----------->by default the start value is index-zero and end-value is (string-length)-1,and step value is 1
# start → index where slice begins (inclusive).
# end → index where slice stops (exclusive).
# step → interval (default = 1).
# default starting value is zero and and it is index values
# | Slice Example       | Output                            |
# | ------------------- | --------------------------------- |
# | `s[start:end]`      | Substring from `start` to `end-1` |
# | `s[:end]`           | From start to `end-1`             |
# | `s[start:]`         | From `start` to end               |
# | `s[start:end:step]` | From `start` to `end-1` with step |
# | `s[::-1]`           | Reverse string                    |

txt = "Hello, world! world"
print(txt[0:5])   # 'Hello'   (from index 0 to 4)
print(txt[7:])    # 'World!'  (from index 7 to end)
print(txt[:5])    # 'Hello'   (from start to index 4)


# search methods
# 1.find()
# Returns the lowest index where the substring is found.
# Returns -1 if not found.
print(txt.find('world'))
print(txt.find('World!'))

# 2.rfind()
# Returns the highest index where the substring is found.
# Returns -1 if not found.
print(txt.rfind('world'))


# 3.index()
# Same as find(), but raises ValueError if substring is not found.

print(txt.index('world'))
# print(txt.index('python'))  ValueError: substring not found

# 4.rindex()
# Same as rfind(), but raises ValueError if substring is not found.
print(txt.rindex('world'))
# print(txt.rindex('python')) ValueError: substring not found

# 5.startwith()
# Checks if a string starts with the given substring. Returns True/False
print(txt.startswith('hello')) #false
print(txt.startswith('Hello')) #true

# 6.endswith()
# Checks if a string ends with the given substring. Returns True/False.
print(txt.endswith("world!")) #flase
print(txt.endswith("world")) #true

# 7.count()
# Returns the number of occurrences of a substring.
print(txt.count('h')) #0
print(txt.count('world')) #2


# aligning and padding methods

# 1.ljust(width,fillchar)
# Returns a left-aligned string of given width.
# Pads with spaces (default) or given fillchar.
name="sai"
print(name.ljust(10,"&"))
print(name.ljust(10,','))

# rjust(width,fillchar)
# Returns a right-aligned string of given width.
print(name.rjust(10,"*"))
print(name.rjust(20,"%"))

# center(width,fillchar)
print(name.center(10,'x'))
print(name.center(15,'*'))

# zfill(width)
# Pads the string on the left with 0s until it reaches given width.
# Useful for formatting numbers.
print(name.zfill(20))


# split() method in python
# purspose: split a string into list, based on a separator
# syntax: 
# string.split(separator,maxsplit)
text="apple,banana,cherry"
print(text)
print(text.split(","))
print(text.split(" ",2))
line="Hello world from python"
print(line.split(" ",2)) #it will be print first two space occerence of words then remainng words willprint

# join() 
# purpose: joins elements of alist (or anyiterable) into a single string, with a separator
# separator.join(iterable) 
word=['sai','kumar','yadavs']
print(",".join(word))
print(" ".join(word))
print("-".join(word))

# replace()
# purpose replace a substring with another substring
# string.replace(old,new,count)->count is optinal

text='''red is rose
rose is flower
flower is your
your is my lover'''
print(text.replace('your','sam'))
print(text.replace('is',"❣️",2)) #here first two occerence of (is ) is replaced with the heart symbol
print(text)


# rsplit(separator,maxsplit)
# string.rsplit(separator,maxsplit)

number="one two three four"
print(number.split(" ",2))
print(number.rsplit(" ",2))

# splitlines()
# splits a string into list at line breaks(\n,\r,\r\n)
print(text.splitlines())

# prefix ad suffix
# startswith()
# purpose: checks if a string starts with the given prefix
# syntax: string.strartswith(prefix,strat,end)

# prefix → string (or tuple of strings) to check.
# start → optional, index to start searching.
# end → optional, index to end searching.
# Returns: True or False

text="python programming is easy"
print(text.startswith("python")) #true
print(text.startswith("python",4)) #false
print(text.startswith(("Python","python","java"))) #-------> it is the tuple of string

# endswith()
# purpose: checks if a srting ends with the given suffix
# syntax: string.endswith(suffix,start,end)
print(text.endswith('easy'))
print(text.endswith('is',0,19))

# removesuffix
# removepreffix
# Purpose: Removes a prefix from a string if it exists.
# string.removeprefix()

text="remove from preffix method"
print(text.removeprefix('re'))
print(text.removeprefix('remove'))
print(text.removeprefix('from')) #no chnage from string

# removeSuffix()
# Purpose: Removes a suffix from a string if it exists.
# syntax: string.removesuffix(suffix)
filname="report.pdf"
print(filname.removesuffix(".pdf"))
print(filname.removesuffix(".txt"))


# partition()
# Purpose: Splits a string into 3 parts based on the first occurrence of a separator.
# syntax: string.partition(saparator)

# Returns: a tuple → (before, separator, after)
# If the separator is not found → returns (string, '', '').
text = "apple,banana,cherry"

# Split at first comma
print(text.partition(","))  
# ('apple', ',', 'banana,cherry')

# Separator not found
print(text.partition(";"))  
# ('apple,banana,cherry', '', '')

# rpartition()
# Purpose: Same as partition(), but splits at the last occurrence of the separator.
# Returns: a tuple → (before, separator, after)
# If separator is not found → returns ('', '', string).

text = "apple,banana,cherry"

# Split at last comma
print(text.rpartition(","))  
# ('apple,banana', ',', 'cherry')

# Separator not found
print(text.rpartition(";"))  
# ('', '', 'apple,banana,cherry')




'''
| **Category**                           | **Method**                 | **Definition / Use**                                                            |
| -------------------------------------- | -------------------------- | ------------------------------------------------------------------------------- |
| **Case Conversion**                    | `upper()`                  | Converts all characters to **uppercase**                                        |
|                                        | `lower()`                  | Converts all characters to **lowercase**                                        |
|                                        | `capitalize()`             | Capitalizes **first character** of string                                       |
|                                        | `title()`                  | Capitalizes **first letter of each word**                                       |
|                                        | `swapcase()`               | Swaps case → lowercase → uppercase and vice versa                               |
|                                        | `casefold()`               | Converts to lowercase (stronger than `lower()`, handles special chars like `ß`) |
| **Search & Check (Boolean / Enquiry)** | `startswith(prefix)`       | Checks if string starts with given prefix                                       |
|                                        | `endswith(suffix)`         | Checks if string ends with given suffix                                         |
|                                        | `isalnum()`                | True if all characters are letters or digits                                    |
|                                        | `isalpha()`                | True if all characters are alphabets                                            |
|                                        | `isdigit()`                | True if all characters are digits (0–9)                                         |
|                                        | `isdecimal()`              | True if all are decimal numbers only                                            |
|                                        | `isnumeric()`              | True if numeric (digits, fractions, unicode numbers)                            |
|                                        | `isspace()`                | True if only whitespace characters                                              |
|                                        | `islower()`                | True if all alphabets are lowercase                                             |
|                                        | `isupper()`                | True if all alphabets are uppercase                                             |
|                                        | `istitle()`                | True if string follows Title Case                                               |
|                                        | `isascii()`                | True if all characters are ASCII (0–127)                                        |
| **Modification (Replace & Remove)**    | `replace(old, new, count)` | Replaces substring with another, `count` = how many replacements                |
|                                        | `removeprefix(x)`          | Removes given prefix if present (Python 3.9+)                                   |
|                                        | `removesuffix(x)`          | Removes given suffix if present (Python 3.9+)                                   |
| **Splitting & Joining**                | `split(sep, maxsplit)`     | Splits string into list at separator (from left)                                |
|                                        | `rsplit(sep, maxsplit)`    | Splits string into list at separator (from right)                               |
|                                        | `splitlines(keepends)`     | Splits string into lines (`\n`, `\r\n`)                                         |
|                                        | `partition(sep)`           | Splits into 3 parts → (before, sep, after) at first occurrence                  |
|                                        | `rpartition(sep)`          | Splits into 3 parts → (before, sep, after) at last occurrence                   |
|                                        | `join(iterable)`           | Joins elements of iterable into a string with a separator                       |
| **Trimming / Removing Spaces**         | `strip(chars)`             | Removes leading & trailing whitespace (or given chars)                          |
|                                        | `lstrip(chars)`            | Removes leading whitespace (or given chars)                                     |
|                                        | `rstrip(chars)`            | Removes trailing whitespace (or given chars)                                    |
| **Alignment & Formatting**             | `center(width, fillchar)`  | Centers string within given width                                               |
|                                        | `ljust(width, fillchar)`   | Left aligns string in given width                                               |
|                                        | `rjust(width, fillchar)`   | Right aligns string in given width                                              |
|                                        | `zfill(width)`             | Pads string with zeros on the left                                              |
|                                        | `format()`                 | String formatting using `{}` placeholders                                       |
|                                        | `format_map(dict)`         | Similar to `format()` but works with dictionary                                 |
| **Searching & Finding**                | `find(sub, start, end)`    | Returns first index of substring (or -1 if not found)                           |
|                                        | `rfind(sub, start, end)`   | Returns last index of substring (or -1 if not found)                            |
|                                        | `index(sub, start, end)`   | Like `find()` but raises error if not found                                     |
|                                        | `rindex(sub, start, end)`  | Like `rfind()` but raises error if not found                                    |
|                                        | `count(sub, start, end)`   | Counts occurrences of substring                                                 |
| **Encoding & Bytes**                   | `encode(encoding, errors)` | Encodes string into bytes                                                       |
| **Other Utility**                      | `expandtabs(tabsize)`      | Replaces `\t` with spaces (default tabsize=8)                                   |

'''