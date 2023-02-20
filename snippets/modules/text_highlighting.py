"""this is for further usage"""
import os
import re
import itertools
from termcolor import colored


def highlight(text, word, color=None, case=True):
    """highlight single word in text, while full text is colored with color"""
    if color is None:
        color = 'white'
        
    if case:
        pattern = re.compile(word)
        text_to_process = text
    else:
        pattern = re.compile(word, re.IGNORECASE)
        text_to_process = text.lower()
        
    indexes = [index for item in re.finditer(word, text_to_process) for index in item.span()]
    indexes = list(itertools.chain([0], indexes, [len(text)]))
    indexes = [indexes[n:n+2] for n in range(0, len(indexes)-1, 1)]
    text_chunks = [
        colored(text[slice(*start_stop)], color) if not val%2
        else colored(text[slice(*start_stop)], color, None, ['reverse'])
        for val, start_stop in enumerate(indexes)
        ]
    highlighted_text = ''.join(text_chunks)
    return highlighted_text
    
    
if __name__ == "__main__":
    os.system('color')
    text, word = 'this is Word sentence with word to be colored', 'word'
    word = 'word'
    case = False
    color = 'green'
    highlighted_text = highlight(text, word, color, case)
    print(highlighted_text)
    