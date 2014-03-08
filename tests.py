import scraper
import unittest

class TestApartmentScraper(unittest.TestCase):

    def setUp(self):
        testfile = open("testresults.html", "r")
        self.contents = eval(testfile.read())
        testfile.close()

    def testFetch(self):
        contents = scraper.fetch_search_results(minAsk=500, maxAsk=1000, bedrooms=2)
        self.assertEqual(contents[1], "utf-8")

    def testRead(self):
        testfile = scraper.read_search_results("testresults.html")
        self.assertEqual(testfile, self.contents)

    def testParse(self):
        results = scraper.parse_source(*self.contents)
        self.assertEqual(type(results), scraper.BeautifulSoup)

    def testExtract(self):
        self.assertEqual(type(scraper.extract_listings(scraper.parse_source(*self.contents))), list)

if __name__ == "__main__":
    unittest.main()