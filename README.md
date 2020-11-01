# internetmeter

Internet velocity meter tool that let's graph the speed/latency of your internet connection at intervals.

## Usage

1. Configure the app (settings.cfg)
2. Schedule the run script using Windows Scheduler ([See tutorial](https://datatofish.com/python-script-windows-scheduler/))
3. Profit!

## Dependencies

You need *pyfastcom* python library. Simply install it using pip:

```bash
pip install pyfastcom
```

## Data results format

The basic results file is saved as follows:

```
2020-10-30	14:01:39	290	Mbps	250	Mbps	7	ms	35	ms
2020-10-30	14:16:58	400	Mbps	160	Mbps	11	ms	57	ms
2020-10-30	14:18:36	350	Mbps	150	Mbps	8	ms	33	ms
2020-10-30	17:34:36	350	Mbps	240	Mbps	9	ms	32	ms
2020-10-30	18:11:31	330	Mbps	210	Mbps	7	ms	26	ms
2020-10-30	18:15:36	360	Mbps	160	Mbps	8	ms	51	ms
2020-10-30	19:11:45	370	Mbps	220	Mbps	8	ms	41	ms
...
```

The format is (separated by **\t** - tab):

- Day
- Hour
- Download speed value
- Download speed unit
- Upload speed value
- Upload speed unit
- Download latency value
- Download latency unit
- Upload latency value
- Upload latency unit

## Author

[Pablo Pizarro R.](https://ppizarror.com) | 2020

## License

This project is licensed under MIT [https://opensource.org/licenses/MIT/](https://opensource.org/licenses/MIT/)
