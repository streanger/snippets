import time
import datetime


def unix_time():
    """generate unix time"""
    return time.time()
    
    
def timestamp():
    """generate timestamp in string format"""
    out = str(datetime.datetime.now())
    return out
    
    
def timestamp_to_datetime(str_timestamp):
    """convert string timestamp to datetime type"""
    out = datetime.datetime.strptime(str_timestamp, '%Y-%m-%d %H:%M:%S.%f')
    return out
    
    
def unix_to_datetime(unix_time):
    """convert unix to datetime"""
    out = datetime.datetime.fromtimestamp(unix_time)
    return out
    
    
if __name__ == "__main__":
    print(unix_time())
    