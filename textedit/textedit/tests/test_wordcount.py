import pytest
import sys
import os

sys.path.append(os.path.abspath("/Users/david/Documents/development/python/python_packaging_vickyboykis/textedit/textedit/review"))
from wordcount import WC


WC_test = WC(os.path.join(os.path.dirname(__file__), '../texts/alice.txt'))


class TestWordcount(object):
    wc = ('Words:', 274)
    sc = ('Sentences:', 7)
    cc = ('Letters:', 1120)

    def test_wc(self):
        assert WC_test.word_count() == self.wc

    def test_sentences(self):
        assert WC_test.sentence_count() == self.sc

    def test_characters(self):
        assert WC_test.letter_count() == self.cc


if __name__ == '__main__':
    pytest.main()
