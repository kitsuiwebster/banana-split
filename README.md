# Banana Split

## Purpose

This Python script splits a large text file into multiple smaller files, based on a user-specified maximum number of lines per file. It provides a loading spinner for process tracking and outputs the total number of files created. This can be useful for handling large datasets by breaking them into manageable pieces.

## Prerequisites

### Python

Ensure you have Python 3.6 or higher installed. You can download Python from the official site: [Download Python](https://www.python.org/downloads/)

### Pip

Windows:

`python get-pip.py`

Debian/Ubuntu:

`sudo apt install python3-pip`

Fedora:

`sudo dnf install python3-pip`

CentOS:

`sudo yum install python3-pip`

Arch Linux:

`sudo pacman -S python-pip`

## Installing Dependencies

You need to install `yaspin`, a terminal spinner library for Python. Open your terminal and run:

```bash
pip install yaspin
```

## Install and run the script

```bash
git clone https://gitlab.com/kitsuiwebster/banana-split.git
```

```bash
cd banana-split
```

Windows:

`python banana-split.py`

Linux: 

`python3 banana-split.py`

