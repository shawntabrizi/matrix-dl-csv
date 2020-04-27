# Matrix / Riot Chat to CSV

This project is totally forked from [matrix-dl](https://gitlab.gnome.org/thiblahute/matrix-dl) by [Thibault Saunier](https://gitlab.gnome.org/thiblahute).

It takes the messages of a Matrix / Riot chat room and outputs it to CSV to easy ingestion and parsing.

## How to Use

1. Make sure have installed Python 3.x.

```
python3 --version

> Python 3.7.5
```

2. Install `virtualenv`

```
pip3 install virtualenv
```

3. Setup your `virtualenv`

```
mkdir matrix-dl-env
virtualenv -p python3 matrix-dl-env
cd matrix-dl-env
source bin/activate
cd ..
```

4. Install the script:

```
python3 setup.py install
```

5. Run the script

Example: (with username `shawntabrizi`)

```
matrix-dl --matrix-url https://matrix.parity.io --start-date 01012016 shawntabrizi "Substrate Technical (Public)"
```

## Help

```
matrix-dl --help
```

```
usage: matrix-dl [-h] [--password PASSWORD] [--matrix-url MATRIX_URL]
                 [--start-date START_DATE] [--end-date END_DATE]
                 username room

Download backlogs from Matrix as raw test

positional arguments:
  username
  room

optional arguments:
  -h, --help            show this help message and exit
  --password PASSWORD   Will be asked later if not provided via this option or
                        MATRIX_PASSWORD environment variable
  --matrix-url MATRIX_URL
                        [default: https://matrix.igalia.com]
  --start-date START_DATE
                        Starting day to consider (format %d%m%Y) [default:
                        01012017]
  --end-date END_DATE   Last day to consider (format %d%m%Y) [default: None]
```
