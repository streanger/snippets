import re
from string import ascii_letters, digits

from unidecode import unidecode


def sanitize_ascii_name(name):
    """sanitize name by keeping ascii characters (with digits) and joining them with dashes
    import re
    from string import ascii_letters, digits
    """
    allowed_chars = ascii_letters + digits
    new_name_chars = [c if c in allowed_chars else "-" for c in name]
    new_name = "".join(new_name_chars).strip("-")
    new_name = re.sub("\-\-+", "-", new_name)
    return new_name


def sanitize_unidecode_name(name):
    """sanitize name by keeping unidecoded ascii characters (with digits) and joining them with dashes
    pip install Unidecode
    import re
    from string import ascii_letters, digits
    from unidecode import unidecode
    """
    name = unidecode(name)
    allowed_chars = ascii_letters + digits
    new_name_chars = [c if c in allowed_chars else "-" for c in name]
    new_name = "".join(new_name_chars).strip("-")
    new_name = re.sub("\-\-+", "-", new_name)
    return new_name


if __name__ == "__main__":
    # test sanitize_ascii_name
    name = "this is [text](to)(be)<sanitized%%$%#$#>"
    sanitized = sanitize_ascii_name(name)
    print(f'     name: {name}')
    print(f'sanitized: {sanitized}')
    print()

    # test sanitize_unidecode_name
    name = "Zażółć   gęślą jaźń"
    sanitized = sanitize_unidecode_name(name)
    print(f'     name: {name}')
    print(f'sanitized: {sanitized}')
    print()
