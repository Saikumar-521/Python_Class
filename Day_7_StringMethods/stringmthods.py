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
# string[start:end:step]
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