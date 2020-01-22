# Matrix / Riot Chat to CSV

This project is totally forked from [matrix-dl](https://gitlab.gnome.org/thiblahute/matrix-dl) by [Thibault Saunier](https://gitlab.gnome.org/thiblahute).

It takes the messages of a Matrix / Riot chat room and outputs it to CSV to easy ingestion and parsing.

## How to Use

1. Make sure have installed Python 3.x.

```
python3 --version

> Python 3.7.5
```

2. Install the script:

```
python3 setup.py install
```

3. Run the script:

Example: (with username `shawntabrizi`)

```
matrix-dl --matrix-url https://matrix.parity.io --start-date 01012016 shawntabrizi "Substrate Technical (Public)"
```
