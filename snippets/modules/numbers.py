
def sizeof_fmt(num, suffix="B"):
    """human-readable file size
    https://stackoverflow.com/questions/1094841/get-a-human-readable-version-of-a-file-size
    """
    for unit in ("", "Ki", "Mi", "Gi", "Ti", "Pi", "Ei", "Zi"):
        if abs(num) < 1024.0:
            return f"{num:3.1f}{unit}{suffix}"
        num /= 1024.0
    return f"{num:.1f}Yi{suffix}"


if __name__ == "__main__":
    size = 12345678
    human_size = sizeof_fmt(size)
    print(f'{size}[B] -> {human_size}')
