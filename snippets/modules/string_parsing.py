

def find_parens(s, start='(', stop=')'):
    """find parens
    
    based on: https://stackoverflow.com/questions/29991917/indices-of-matching-parentheses-in-python
    keywords: parens, parentheses, brackets, nested
    """
    toret = []
    pstack = []
    for i, c in enumerate(s):
        if c == start:
            pstack.append(i)
        elif c == stop:
            if len(pstack) == 0:
                raise IndexError("No matching closing parens at: " + str(i))
            toret.append((pstack.pop(), i))
    if len(pstack) > 0:
        raise IndexError("No matching opening parens at: " + str(pstack.pop()))
    return toret
    
    
if __name__ == "__main__":
    text = '((a, b), (c, d), (e, f))'
    parens = find_parens(text)
    for (start, stop) in parens:
        print('{} -> {}'.format((start, stop), text[start:stop+1]))
        
        