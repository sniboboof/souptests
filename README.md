souptests
=========

some simple functions to use BeautifulSoup 4 to ready craig's list search results

fetch_search_results takes parameters and sends a craigslist search, then returns the resulting page data and its character encoding

then the content has to be put through parse_source, which returns a BeautifulSoup object, with the html elements converted to python objects

finally, put that into extract_listings, which extracts only the listings and turns them into an easy-to-manage python list