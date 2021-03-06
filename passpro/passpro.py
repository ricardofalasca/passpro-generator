import operator
from functools import reduce

from .utils import rand, DIGRAPHS_FREQUENCY 


class PasswordPronounceable:
    '''
        Generate pronounceable passwords

        This module generates pronuceable passwords, based the the English
        digraphs by D Edwards.

        History
        --

        This code derived from Perl module: Text::Password::Pronounceable,
        written by Ricardo Falasca <ricardo at falasca.com.br> published
        under MIT License.

        Python library by `Ricardo Falasca (MyCanadaPayday.com)`, 2018-04-03.

        That was derived from mpw.pl, a bit of code with a sordid history.

        CPAN module by Chia-liang Kao, 2006-09-11.
        Perl cleaned up a bit by Jesse Vincent, 2001-01-14.
        Converted to perl from C by Marc Horowitz, 2000-01-20.
        Converted to C from Multics PL/I by Bill Sommerfeld, 1986-04-21.
        Original PL/I version provided by Jerry Saltzer.
    '''

    # Default min and max length
    min_length = 6
    max_length = 10

    # We need to know the totals for each row 
    row_sums = [reduce(operator.add, f) for f in DIGRAPHS_FREQUENCY]

    # Frequency with which a given letter starts a word.
    start_freq = [
        1299, 425, 725, 271, 375, 470, 93, 223, 1009, 24, 20, 355, 379, 319,
        823, 618, 21, 317, 962, 1991, 271, 104, 516, 6, 16, 14
    ]

    total_sum = reduce(operator.add, start_freq)

    def _check_lengths(self, min_length, max_length):
        if not min_length:
            return 'Min length should be defined'
        elif min_length <= 0:
            return 'Min length should be > 0'
        
        if not max_length:
            return 'Max length should be defined'
        elif max_length <= 0:
            return 'Max length should be > 0'

        if min_length > max_length:
            return 'Max length must be >= min length'

    def generate(self, min_length, max_length):
        min_length = min_length or self.min_length
        max_length = max_length or self.max_length

        if not min_length and not max_length:
            return

        # When munging characters, we need to know where to start counting
        # letters from
        length = min_length + rand(max_length - min_length)
        char = self._generate_nextchar(self.total_sum, self.start_freq)
        a = ord('a')
        word = chr(char + a)

        for i in range(1, length):
            char = self._generate_nextchar(self.row_sums[char],
                                           DIGRAPHS_FREQUENCY[char])
            word += chr(char + a)
        return word


    # A private helper function for RandomPassword
    # Takes a row summary and a frequency chart for the next character to be
    # searched
    def _generate_nextchar(self, all, freq):
        i, pos = 0, rand(all)

        while i < (len(freq) - 1) and pos >= freq[i]:
            pos -= freq[i]
            i += 1
    
        return i
