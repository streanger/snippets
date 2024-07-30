from io import StringIO
from pprint import pprint

import lxml
import pandas as pd
import requests
from bs4 import BeautifulSoup as bs


def save_img_from_url(url, path):
    """save image from specified url, to specified local path"""
    response = requests.get(url)
    if response.status_code != 200:
        return False
    with open(path, 'wb') as f:
        f.write(response.content)
    return True
    
    
def url_image_to_bytes(url):
    """read url image as bytes"""
    response = requests.get(url)
    if response.status_code != 200:
        return False
    return response.content
    

def make_soup(response):
    """create soup object from requests response
    
    requires:
        pip install lxml
        pip install beautifulsoup4
        import lxml
        from bs4 import BeautifulSoup as bs
    """
    soup = bs(response.text, "lxml")
    return soup


def parse_html_table(table):
    """convert html table to list of lists

    :param table: html table soup object
    :type table: bs4.Tag

    pip install pandas
    import pandas as pd
    """
    df = pd.read_html(StringIO(str(table)), header=0)[0]
    return [df.columns.values.tolist()] + df.values.tolist()


if __name__ == "__main__":
    # TODO: other tests
    # url = 'https://unsplash.com/photos/4DW0D3CK9B4/download?force=true'

    # INFO: parse_html_table test
    url = 'https://www.w3schools.com/html/html_tables.asp'
    response = requests.get(url)
    soup = bs(response.text, "lxml")
    for index, table in enumerate(soup.find_all('table'), start=1):
        print(f'{index})')
        parsed_table = parse_html_table(table)
        pprint(parsed_table, indent=4, width=100)
        print()
