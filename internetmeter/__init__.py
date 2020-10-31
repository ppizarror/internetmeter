# coding=utf-8
"""
internetmeter
https://github.com/ppizarror/internetmeter
INTERNETMETER
Sources folder.

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

from internetmeter._cfgloader import ConfigLoader
from internetmeter._datastore import DataStore
from internetmeter._utils import info

import internetmeter._version

__author__ = 'ppizarror'
__contributors__ = []
__copyright__ = 'Copyright 2020 Pablo Pizarro R. @ppizarror'
__description__ = "Internet velocity meter tool that let's graph the speed/latency of your internet connection at intervals"
__email__ = 'pablo@ppizarror.com'
__keywords__ = 'fast.com selenium internet velocity speed scrapper viewer meter'
__license__ = 'MIT'
__url__ = 'https://github.com/ppizarror/internetmeter'
__url_source_code__ = 'https://github.com/ppizarror/internetmeter'
__url_documentation__ = 'https://github.com/ppizarror/internetmeter'
__url_bug_tracker__ = 'https://github.com/ppizarror/internetmeter/issues'
__version__ = internetmeter._version.ver
