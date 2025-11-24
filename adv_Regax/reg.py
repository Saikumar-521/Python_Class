import re

'''
1. re.match(pattern, string, flags=0)

Definition:
Searches for a pattern only at the beginning of the string.
If the pattern matches, it returns a Match object; otherwise, it returns None.

2. re.search(pattern, string, flags=0)

Definition:
Searches the entire string for the first location where the pattern matches.
Returns a Match object if found, else None.

3. re.findall(pattern, string, flags=0)

Definition:
Finds all non-overlapping matches of the pattern in the string and returns them as a list of strings.

4. re.finditer(pattern, string, flags=0)

Definition:
Returns an iterator yielding Match objects for all matches found in the string.

5. re.split(pattern, string, maxsplit=0, flags=0)

Definition:
Splits the string by the occurrences of the pattern.
Returns a list of substrings.

6. re.sub(pattern, repl, string, count=0, flags=0)

Definition:
Replaces all occurrences of the pattern with the replacement string (repl).
Returns the modified string.


7. re.subn(pattern, repl, string, count=0, flags=0)

Definition:
Similar to re.sub(), but returns a tuple (new_string, number_of_subs_made).


8. re.fullmatch(pattern, string, flags=0)

Definition:
Checks if the entire string matches the pattern.
If yes, returns a Match object, else None.

9. re.compile(pattern, flags=0)

Definition:
Compiles a regular expression pattern into a Regex object, which can be reused for multiple matches.

Example:


10. re.escape(string)

Definition:
Escapes all special characters in the string, so they can be used as literal characters in a pattern.

Example:

'''