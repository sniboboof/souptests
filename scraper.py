import requests
import pdb
import sys
from bs4 import BeautifulSoup

def fetch_search_results(
    query="", minAsk=None, maxAsk=None, bedrooms=None
):
    search_params = {
        key: val for key, val in locals().items() if val is not None
    }
    if not search_params:
        raise ValueError("No valid keywords")

    base = 'http://seattle.craigslist.org/search/apa'
    resp = requests.get(base, params=search_params, timeout=3)
    resp.raise_for_status()  # <- no-op if status==200
    return resp.content, resp.encoding

def read_search_results(filepath="localresults.html"):
    myfile = open(filepath, "r")
    return eval(myfile.read())

def parse_source(html, encoding='utf-8'):
    parsed = BeautifulSoup(html, from_encoding=encoding)
    return parsed

def extract_listings(parsed):
    location_attrs = {'data-latitude': True, 'data-longitude': True}
    listings = parsed.find_all('p', class_='row', attrs=location_attrs)
    extracted = []
    for listing in listings:
        location = {key: listing.attrs.get(key, '') for key in location_attrs}
        link = listing.find('span', class_='pl').find('a')
        price_span = listing.find('span', class_='price')   # add me
        this_listing = {
            'location': location,
            'link': link.attrs['href'],
            'description': link.string.strip(),
            'price': price_span.string.strip(),             # and me
            'size': price_span.next_sibling.strip(' \n-/')  # me too
        }
        extracted.append(this_listing)
    return extracted

if __name__ == '__main__':
    import pprint                                  # add this import
    if len(sys.argv) > 1 and sys.argv[1] == 'test':
        html, encoding = read_search_results()
    else:
        html, encoding = fetch_search_results(
            minAsk=500, maxAsk=1000, bedrooms=2
        )
    doc = parse_source(html, encoding)
    listings = extract_listings(doc)
    for indListing in listings:
        pprint.pprint(indListing)
        print("")