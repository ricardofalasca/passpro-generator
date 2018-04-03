# passpro-generator
Generates pronounceable passwords

## About
This module generates pronuceable passwords, based the the English digraphs by D Edwards.

Derived from Perl module: `Text::Password::Pronounceable`, written by Ricardo Falasca (MyCanadaPayday.com) - 2018-04-03 - published under MIT License.

## History
Python library by `Ricardo Falasca (MyCanadaPayday.com)`, 2018-04-03.

That was derived from mpw.pl, a bit of code with a sordid history.

CPAN module by Chia-liang Kao, 2006-09-11.
Perl cleaned up a bit by Jesse Vincent, 2001-01-14.
Converted to perl from C by Marc Horowitz, 2000-01-20.
Converted to C from Multics PL/I by Bill Sommerfeld, 1986-04-21.
Original PL/I version provided by Jerry Saltzer.

## Install

```
pip install passpro-generator
```

## How to use
```
from passpro import PasswordPronounceable

# instantiate
pp = PasswordPronounceable()

# generate a new password as length between 5 and 10 chars
pwd = pp.generate(5, 10)
```

Enjoy.
