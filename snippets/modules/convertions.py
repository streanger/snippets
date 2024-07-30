
def sizeof_fmt(num, suffix="B"):
    """human-readable file size
    https://stackoverflow.com/questions/1094841/get-a-human-readable-version-of-a-file-size
    """
    for unit in ("", "Ki", "Mi", "Gi", "Ti", "Pi", "Ei", "Zi"):
        if abs(num) < 1024.0:
            return f"{num:3.1f}{unit}{suffix}"
        num /= 1024.0
    return f"{num:.1f}Yi{suffix}"


def time_fmt(seconds):
    """Human-readable time format conversion
    Converts a given time in seconds to a format like '1h 20min 30s'.
    """
    # Define the units and the number of seconds each unit represents
    intervals = [
        ('y', 31536000),  # 365 days
        ('mth', 2592000), # 30 days
        ('w', 604800),    # 7 days
        ('d', 86400),     # 1 day
        ('h', 3600),      # 1 hour
        ('min', 60),      # 1 minute
        ('s', 1)          # 1 second
    ]

    # This will store the formatted output parts
    result = []

    # Iterate over the intervals
    for unit, count_in_seconds in intervals:
        if seconds >= count_in_seconds:
            value = seconds // count_in_seconds  # Get the whole number of this unit
            seconds %= count_in_seconds          # Get the remaining seconds
            result.append(f"{int(value)}{unit}") # Append the formatted part
    return ' '.join(result)


if __name__ == "__main__":
    # size convertions test
    size = 12345678
    human_size = sizeof_fmt(size)
    print(f'{size}[B] -> {human_size}')

    # time convertions test
    print(f'{1466.245}[s] -> {time_fmt(1466.245)}')    # Output: "24min 26s"
    print(f'{45000}[s] -> {time_fmt(45000)}')    # Output: "12h 30min"
    print(f'{100000}[s] -> {time_fmt(100000)}')  # Output: "1d 3h 46min 40s"
