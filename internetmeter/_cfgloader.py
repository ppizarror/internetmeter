# coding=utf-8
"""
internetmeter
https://github.com/ppizarror/internetmeter
CONFIG LOADER

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

import os
from typing import Dict, Union

CFG_SEP = ' = '


def isfloat(value: str) -> bool:
    """
    Check if the given string is a float.

    :param value: String to check
    :return: True if float
    """
    try:
        float(value)
        return True
    except ValueError:
        return False


class ConfigLoader(object):
    """
    Configuration loader class.
    """

    _cfg: Dict[str, Union[str, int, float, bool]]

    def __init__(self, cfg_file: str):
        """
        Constructor.

        :param cfg_file: Config file path
        """
        assert os.path.isfile(cfg_file), 'File {0} does not exist'.format(cfg_file)
        assert '.cfg' in cfg_file, 'Invalid configuration file extension'
        d = open(cfg_file, 'r')
        self._cfg = {}
        k = 1  # Line no.
        for i in d:
            assert CFG_SEP in i, 'Invalid config at line {0}'.format(k)
            i = i.strip()
            j = i.split(CFG_SEP)
            jkey = j.pop(0)
            j = CFG_SEP.join(j).strip()

            # Check type
            if j.isdigit():
                j = int(j)
            elif isfloat(j):
                j = float(j)
            elif j.lower() == 'false' or j.lower() == 'true':
                if j.lower() == 'false':
                    j = False
                else:
                    j = True

            self._cfg[jkey] = j
            k += 1

    def get_size(self) -> int:
        """
        Return the number of configs.

        :return: Total configs
        """
        return len(self._cfg.keys())

    def get(self, key: str) -> Union[str, int, float, bool]:
        """
        Get the value of the config.

        :param key: Value key
        :return: Value
        """
        return self._cfg[key]
