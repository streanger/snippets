import ast
import hashlib
import json
import os
import random
import sys
from pathlib import Path

import pkg_resources
import pyperclip
from rich import print
from rich.columns import Columns
from rich.console import Console
from rich.panel import Panel
from rich.syntax import Syntax
from rich.table import Table


class SnippetsViewer():
    """code snippets viewer"""
    def __init__(self, definitions, prompt=None, prompt_color=None):
        if prompt is None:
            self.__prompt = '« snippets » '
        else:
            self.__prompt = prompt
            
        if prompt_color is None:
            self.__prompt_color = random.choice(['magenta1', 'red1', 'green_yellow', 'gold1'])
        else:
            self.__prompt_color = prompt_color
            
        self.__console = Console()
        self.__definitions = definitions
        self.__matched = {}  # 1-, 2-, 3-...
        self.__lines_numbers = False
        self.__codebox = True
        self.__clipboard = True
        self.__last_definition = ''
        
    def _console_help(self):
        """console help text"""
        table = Table(title="console help", border_style="blue")
        table.add_column("Command", style="green_yellow")
        table.add_column("Description", justify="right", style="royal_blue1")
        
        help_text = [
            ['cls\clear', 'clear console'],
            ['exit\quit', 'exit from console'],
            ['flags', 'show flags status'],
            ['all', 'show all snippets'],
            ['copy', 'copy last definition to clipboard'],
            ['codebox', 'turn on/off codebox'],
            ['clipboard', 'True -> always copy to clipboard'],
        ]
        for command, description in help_text:
            table.add_row(command, description)
            
        self.__console.print(table)
        return None
        
    def run(self):
        """run console"""
        while True:
            try:
                query = self.__console.input('[{}]{}'.format(self.__prompt_color, self.__prompt))
                
            except KeyboardInterrupt:
                print()
                continue
                
            try:
                # clear query from white characters
                query = query.strip()
                if not query:
                    continue
                    
                # ********* execute command *********
                if query in ('exit', 'quit'):
                    return None
                    
                elif query in ('cls', 'clear'):
                    if os.name == 'nt':
                        os.system('cls')
                    else:
                        os.system('clear')
                    continue
                    
                elif query == 'help':
                    self._console_help()
                    continue
                    
                elif query == 'all':
                    query = '""'
                    
                elif query == 'codebox':
                    # switch codebox flag
                    self.__codebox = not self.__codebox
                    print('codebox --> {}'.format(self.__codebox))
                    continue
                    
                elif query == 'clipboard':
                    # switch clipboard flag
                    self.__clipboard = not self.__clipboard
                    print('clipboard --> {}'.format(self.__clipboard))
                    continue
                    
                elif query == 'copy':
                    # copy last code definition
                    if not self.__last_definition:
                        print('[red]nothing to copy')
                        continue
                    pyperclip.copy(self.__last_definition)
                    print('[gold1]code copied to clipboard!')
                    continue
                    
                elif query == 'flags':
                    table = Table(title="flags", border_style="blue")
                    table.add_column("Flag", justify="right")
                    table.add_column("Status", justify="right")
                    
                    flags_status = [
                        ['codebox', self.__codebox],
                        ['clipboard', self.__clipboard],
                    ]
                    for flag, status in flags_status:
                        if status:
                            status_style = 'green'
                        else:
                            status_style = 'red'
                        table.add_row(flag, str(status), style=status_style)
                    self.__console.print(table)
                    continue
                    
                else:
                    pass
                    
                # ********* execute query *********
                try:
                    query_index = int(query)
                    single_match = self.__matched.get(query_index, False)
                    if not single_match:
                        continue
                    func_content = single_match.get('func_content', '')
                    self.__last_definition = func_content
                    
                    if self.__codebox:
                        highlighted = Syntax(func_content, "python", theme='monokai', line_numbers=True, indent_guides=True, word_wrap=True)
                        highlighted = Columns([Panel(highlighted)])
                        self.__console.print(highlighted)
                    else:
                        highlighted = Syntax(func_content, "python", theme='monokai', line_numbers=False, word_wrap=True)
                        print(highlighted)
                        
                    if self.__clipboard:
                        pyperclip.copy(self.__last_definition)
                        # print('[gold1]code copied to clipboard!')  # too much spam?
                    continue
                except ValueError:
                    pass
                    
                query = query.strip('"')
                self.match_query(query)
                self.print_matched_block(query)
                
            except KeyboardInterrupt:
                print()
                continue
                
            except Exception as err:
                print('[red][!] unexpected error catched: {}'.format(err))
                
            finally:
                if not query.strip():
                    continue
                print()
        return None

    def print_matched_block(self, query):
        """print functions that matches current query"""
        table = Table(title="query: [gold1]{}".format(query))
        table.add_column("No", justify="right", style="gold1", no_wrap=True)
        table.add_column("Function", style="green_yellow")
        table.add_column("Module", justify="right", style="royal_blue1")
        for key, value in self.__matched.items():
            table.add_row(str(key), value['func_name'], value['filename'])
        self.__console.print(table)
        
    def match_query(self, query):
        matched_list = [item for item in self.__definitions if query in item['func_name']]
        self.__matched = {index+1: item for index, item in enumerate(matched_list)}
        
        
def static_file_path(directory, filename):
    """get path of the specified filename from specified directory"""
    resource_path = '/'.join((directory, filename))   # Do not use os.path.join()
    try:
        template = pkg_resources.resource_filename(__name__, resource_path)
    except KeyError:
        return 'none'   # empty string cause AttributeError, and non empty FileNotFoundError
    return template
    
    
def script_path():
    """set current path, to script path"""
    current_path = os.path.realpath(os.path.dirname(sys.argv[0]))
    os.chdir(current_path)
    return current_path
    
    
def read_file(filename, mode='r'):
    """read from file"""
    content = ''
    try:
        with open(filename, mode, encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError as err:
        print('[x] FileNotFoundError: {}'.format(filename))
    return content
    
    
def write_json(filename, data):
    """write to json file"""
    with open(filename, 'w', encoding='utf-8') as fp:
        # ensure_ascii -> False/True -> characters/u'type'
        json.dump(data, fp, sort_keys=True, indent=4, ensure_ascii=False)
    return True
    
    
def read_json(filename, default_type='dict'):
    """read json file to dict"""
    if default_type == 'dict':
        data = {}
    else:
        data = []
    try:
        with open(filename, encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError:
        print('[x] FileNotFoundError: {}'.format(filename))
    return data
    
    
def parse_functions(body):
    """return functions from ast parsed body tree
    
    look for:
        ClassDef
        FunctionDef
    """
    functions = []
    for func in body:
        if isinstance(func, ast.FunctionDef):
            functions.append(func)
            continue
        if isinstance(func, ast.ClassDef):
            sublist = parse_functions(func.body)
            functions.extend(sublist)
    return functions
    
    
def sha256_sum(content):
    """calc sha256 sum of content"""
    sha256_hash = hashlib.sha256(content).hexdigest()
    return sha256_hash
    
    
def collect_definitions(directory='modules'):
    """collect code definitions from many files"""
    definitions = []
    modules_directory = static_file_path(directory, "")
    files = [static_file_path(directory, filename) for filename in os.listdir(modules_directory) if filename.endswith('.py')]
    for file_path in files:
        try:
            content = read_file(file_path)
            filename = Path(file_path).name
            tree = ast.parse(content, filename=filename)
            for key, func in enumerate(parse_functions(tree.body)):
                func_name = func.name
                func_content = ast.unparse(func)
                sha256 = sha256_sum(func_content.encode('utf-8'))
                
                # ****** func definition ******
                single_definition = {}
                single_definition['filename'] = filename
                single_definition['func_name'] = func_name
                single_definition['func_content'] = func_content
                single_definition['sha256'] = sha256
                definitions.append(single_definition)
                
                # DEBUG
                # highlighted = Syntax(func_content, "python", theme='monokai', word_wrap=True)
                # print(highlighted)
                
        except SyntaxError:
            print('[red][x] SyntaxError while parsing function: {}'.format(function_name))
            
        finally:
            pass
    return definitions
    
    
def remove_duplicates_definitions(list_of_dicts):
    """remove duplicate dicts from list"""
    reverse_dict = {(dictionary['func_name'], dictionary['sha256']): dictionary for dictionary in list_of_dicts}
    no_dupli_definitions = list(reverse_dict.values())
    return no_dupli_definitions
    
    
def viewer():
    """snippets viewer
    
    for commandline script
    """
    if os.name == 'nt':
        os.system('color')
        
    definitions = collect_definitions(directory='modules')
    definitions = remove_duplicates_definitions(definitions)
    snippets = SnippetsViewer(definitions, prompt='« snippets » ')
    snippets.run()
    return None
    
    
if __name__ == "__main__":
    script_path()
    viewer()
    
"""
useful:
    https://stackoverflow.com/questions/139180/how-to-list-all-functions-in-a-python-module
    https://www.educative.io/edpresso/what-is-the-astparse-method-in-python
    https://pygments.org/docs/styles/
    https://blog.jcharistech.com/2020/06/11/rich-text-and-beautiful-formatting-in-the-terminal-with-rich-python/
    https://rich.readthedocs.io/en/stable/appendix/colors.html
    
think of/todo:
    -list all functions and classes from many python files (+)
    -return it by user queries (+)
    -use ast parse instead of import & inspect (+)
    -use https://github.com/streanger/console-wrapper (+)
    -parse classes methods as functions (+)
    -copy to clipboard as flag in console (+)
    -name for pypi - snippets
    -python code chunks for everyone
    -many functions with the same name in one files is ok (+)
    -definitions in .json (for now removed)
    -download external codes
    -remove local db if someones don't need it
    -prompt color as option stored in .json config
    -json config file stored in setup directory
    -some banner at start and/or number of snippets
    -
"""
