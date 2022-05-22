import os
from termcolor import colored


def highlight_text_color(text, word, color):
    """highlight single word in text, while full text is colored with color
    
    if os.name == 'nt':
        os.system('color')
    """
    parts = text.split(word)
    selection = colored(word, color, None, ['reverse'])
    colored_parts = [colored(item, color) for item in parts]
    highlighted_text = selection.join(colored_parts)
    return highlighted_text
    
    
if __name__ == "__main__":
    if os.name == 'nt':
        os.system('color')
        
    some = 'something some here thesomeone'
    print(highlight_text_color(some, 'some', 'red'))
    