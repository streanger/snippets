import sys
from itertools import cycle
import numpy as np


def xor(var, key):
    """xor two byte strings
    
    cuts to shorter one
    https://stackoverflow.com/questions/29408173/byte-operations-xor-in-python
    """
    return bytes(a ^ b for a,b in zip(var, key))
    
    
def xor_int(var, key):
    """xor two byte strings
    
    cuts to shorter one
    uses int.from_bytes
    requires:
        import sys
    https://stackoverflow.com/questions/29408173/byte-operations-xor-in-python
    """
    byteorder=sys.byteorder
    key, var = key[:len(var)], var[:len(key)]
    int_var = int.from_bytes(var, byteorder)
    int_key = int.from_bytes(key, byteorder)
    int_enc = int_var ^ int_key
    return int_enc.to_bytes(len(var), byteorder)
    
    
def xor_cycle(var, key):
    """xor two byte strings
    
    uses cycle for key
    requires:
        from itertools import cycle
    https://stackoverflow.com/questions/29408173/byte-operations-xor-in-python
    """
    return [chr(ord(a)^ord(b)) for a,b in zip(var, cycle(key))]
    
    

def xor_numpy(var, key):
    """xor two byte strings
    
    requires:
        pip install numpy
        import numpy as np
    https://stackoverflow.com/questions/29408173/byte-operations-xor-in-python
    """
    a = np.frombuffer(var, dtype = np.uint8)
    b = np.frombuffer(key, dtype = np.uint8)
    return (a^b).tobytes()
    
    
if __name__ == "__main__":
    var = b'something'
    key = b'spam'
    xor_out = xor(var, key)
    xor_int_out = xor(var, key)
    xor_cycle_out = xor(var, key)
    xor_numpy_out = xor(var, key)
    print(xor_out)
    print(xor_int_out)
    print(xor_cycle_out)
    print(xor_numpy_out)
    