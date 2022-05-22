import hashlib


def sha256_sum(content):
    """calc sha256 sum of content
    
    content is type of bytes
    """
    sha256_hash = hashlib.sha256(content).hexdigest()
    return sha256_hash
    
    
if __name__ == "__main__":
    pass
    # TODO: md5_sum, sha251_sum
    