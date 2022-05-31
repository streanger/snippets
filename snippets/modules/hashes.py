import hashlib


def sha256_sum(content):
    """calc sha256 sum of content
    
    content is type of bytes
    keywords: sha256, hash
    """
    sha256_hash = hashlib.sha256(content).hexdigest()
    return sha256_hash
    
    
def sha1_sum(content):
    """calc sha1 sum of content
    
    content is type of bytes
    keywords: sha1, hash
    """
    sha1_hash = hashlib.sha1(content).hexdigest()
    return sha1_hash
    
    
def md5_sum(content):
    """calc md5 sum of content
    
    content is type of bytes
    keywords: md5, hash
    """
    md5_hash = hashlib.md5(content).hexdigest()
    return md5_hash
    
    
if __name__ == "__main__":
    data = b'something'
    md5_hash = md5_sum(data)
    print('md5_hash: {}'.format(md5_hash))
    sha1_hash = sha1_sum(data)
    print('sha1_hash: {}'.format(sha1_hash))
    sha256_hash = sha256_sum(data)
    print('sha256_hash: {}'.format(sha256_hash))
    