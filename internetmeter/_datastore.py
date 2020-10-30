# coding=utf-8
"""
internetmeter
https://github.com/ppizarror/internetmeter
DATA STORE

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
from pyfastcom import PyFastCom
import os


class DataStore(object):
    """
    Store the data from a query.
    """
    _datafile: str
    _fast: 'PyFastCom'

    def __init__(self, datafile: str, fast: 'PyFastCom'):
        """
        Constructor.

        :param datafile: Data file
        :param fast: Fast.com object
        """
        if not os.path.isfile(datafile):
            f = open(datafile, 'w')
            f.close()
        assert os.path.isfile(datafile), 'Data file {0} does not exist'.format(datafile)
        self._datafile = datafile
        self._fast = fast

    def store(self) -> None:
        """
        Store the query results to file.
        """
        assert self._fast.ready(), 'Fast results not ready'
        with open(self._datafile, 'a') as myfile:
            myfile.write('{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}\t{7}\t{8}\n'.format(
                datetime.today().strftime('%Y-%m-%d\t%H:%M:%S'),
                self._fast.get_download_speed()[0],
                self._fast.get_download_speed()[1],
                self._fast.get_upload_speed()[0],
                self._fast.get_upload_speed()[1],
                self._fast.get_download_latency()[0],
                self._fast.get_download_latency()[1],
                self._fast.get_upload_latency()[0],
                self._fast.get_upload_latency()[1]
            ))
