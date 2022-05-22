import ctypes


def check_if_user_is_admin():
    """check if current Windows user is admin"""
    return ctypes.windll.shell32.IsUserAnAdmin()
    
    
def hide_windows_console():
    """hide windows console"""
    ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)
    return None
    
    
def ctypes_hello_popup(text, title):
    """message window topmost
    
    https://stackoverflow.com/questions/50086178/python-how-to-keep-messageboxw-on-top-of-all-other-windows
    """
    ctypes.windll.user32.MessageBoxW(0, text, title, 0x1002)  # 0x2
    return None
    
    
if __name__ == "__main__":
    pass
    print(check_if_user_is_admin())
    ctypes_hello_popup('hello', 'title')
    