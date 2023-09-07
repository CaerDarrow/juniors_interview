from solution import beasts_parser,csv_writer, headers
from unittest import TestCase, main

headers_to_check = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/116.0'
}

class ParserAndWriterTest(TestCase):
    def testHeaders(self):
        self.assertEqual(headers_to_check, headers)
    def testWriterErrorRise(self):
        self.assertRaises(FileNotFoundError, csv_writer('not_beasts.csv',[[1,2],[3,4],[5,6]]))
    def testParserNone(self):
        self.assertIsNone(beasts_parser)

    

if __name__=='__main__':
    main()