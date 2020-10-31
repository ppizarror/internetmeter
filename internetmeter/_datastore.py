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


def check_create_file(filename: str) -> None:
    """
    Check file, if not exists then create.

    :param filename: Name of the file
    """
    if not os.path.isfile(filename):
        f = open(filename, 'w')
        f.close()
    assert os.path.isfile(filename), 'file {0} does not exist'.format(filename)


class DataStore(object):
    """
    Store the data from a query.
    """
    _data_file: str
    _dataview_file: str
    _error_file: str
    _fast: 'PyFastCom'

    def __init__(self, data_file: str, dataview_file: str, error_file: str, fast: 'PyFastCom'):
        """
        Constructor.

        :param data_file: Data file
        :param fast: Fast.com object
        """
        check_create_file(data_file)
        check_create_file(dataview_file)
        check_create_file(error_file)
        self._data_file = data_file
        self._dataview_file = dataview_file
        self._error_file = error_file
        self._fast = fast

    def store(self) -> None:
        """
        Store the query results to file.
        """
        assert self._fast.ready(), 'Fast results not ready'
        with open(self._data_file, 'a') as myfile:
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

    def log_error(self, error_name: str) -> None:
        """
        Write error info to file.

        :param error_name: Name of the error
        """
        with open(self._error_file, 'a') as myfile:
            myfile.write('{0}\t{1}\n'.format(datetime.today().strftime('%Y-%m-%d %H:%M:%S'), error_name))
