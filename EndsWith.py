# Complete the solution so that it returns true if the first argument(string) passed in ends with the 2nd argument (also a string).

# Examples:

# solution('abc', 'bc') # returns true
# solution('abc', 'd') # returns false

def solution(text, ending):
    lenCompare = len(text) - len(text)
    string3 = text[lenCompare:]
    if string3 == ending:
        return True
    else:
        return False

        # or
        
def solution(string, ending):
	return string.endswith(ending);