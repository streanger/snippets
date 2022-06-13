import itertools


def toggle_cycle():
    """toggle value between list of elements
    
    use as oneliner function
    https://stackoverflow.com/questions/8381735/how-to-toggle-a-value/8381955#8381955
    """
    toggle = itertools.cycle(['red', 'green', 'blue']).__next__
    print(toggle())
    print(toggle())
    print(toggle())
    
    # or
    toggle = itertools.cycle(['red', 'green', 'blue'])
    print(next(toggle))
    print(next(toggle))
    print(next(toggle))
    return None
    
    
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
    # toggle
    toggle_cycle()
    
    # flatten
    nested_list = [[1,2], [[3], [4,5]], [[[6,7], [8]]]]
    flattened_list = flatten_list(nested_list)
    print(flattened_list)
    