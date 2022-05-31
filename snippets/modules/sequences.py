
def flatten_list(S):
    """flatten list of lists recursively
    
    based on: https://stackoverflow.com/questions/12472338/flattening-a-list-recursively
    keywords: flatten, list, nested, recursive
    """
    if S == []:
        return S
    if isinstance(S[0], list):
        return flatten_list(S[0]) + flatten_list(S[1:])
    return S[:1] + flatten_list(S[1:])
    
    
if __name__ == "__main__":
    nested_list = [[1,2], [[3], [4,5]], [[[6,7], [8]]]]
    flattened_list = flatten_list(nested_list)
    print(flattened_list)
    
    