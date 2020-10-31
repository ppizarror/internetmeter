# coding=utf-8
"""
internetmeter
https://github.com/ppizarror/internetmeter
MAIN SCRIPT

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

from internetmeter import ConfigLoader, info, DataStore, __version__
from pyfastcom import PyFastCom

if __name__ == '__main__':
    # Load the config
    cfg = ConfigLoader('settings.cfg')
    verbose = cfg.get('verbose')

    info(verbose, 'internetmeter v{0}'.format(__version__))

    # Get the stats from the web
    fast = PyFastCom()
    fast.set_driver_path(cfg.get('webdriver_path'))
    info(verbose, 'Querying from fast.com')

    results = DataStore(
        data_file=cfg.get('results_data_path'),
        dataview_file=cfg.get('results_viewer_path'),
        error_file=cfg.get('error_log_path'),
        fast=fast
    )

    # noinspection PyBroadException
    try:
        fast.run(timeout=cfg.get('timeout_query'))
    except:
        results.log_error('Failed to connect to server')
        exit()

    # Store the data
    info(verbose, 'Storing results')
    results.store()
