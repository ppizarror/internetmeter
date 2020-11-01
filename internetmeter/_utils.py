# coding=utf-8
"""
internetmeter
https://github.com/ppizarror/internetmeter
UTILS

License:
-------------------------------------------------------------------------------
The MIT License (MIT)
Copyright 2020 Pablo Pizarro R. @ppizarror
Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the Software
is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
-------------------------------------------------------------------------------
"""

from datetime import datetime
from internetmeter._cfgloader import ConfigLoader
from typing import Tuple

# Load the date configs
_cfg = ConfigLoader('settings.cfg')


def get_date() -> Tuple[str, str]:
    """
    Return date in day/hour strings.
    """
    return datetime.today().strftime(_cfg.get('time_day')), datetime.today().strftime(_cfg.get('time_hour'))


def info(verbose: bool, msg: str) -> None:
    """
    Print info message.

    :param verbose: Only print if True
    :param msg: Message
    """
    if verbose:
        _, hour = get_date()
        print('{0} [LOG] {1}'.format(hour, msg))
