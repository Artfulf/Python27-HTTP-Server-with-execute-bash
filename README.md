# Python27-HTTP-Server-with-execute-bash

## Description
This example run HTTP server by Python 2.7 using CGIHTTPServer and allows to execute a bash script.

## Installation
To clone the repository:
```
$ git clone git@github.com:Artfulf/Python27-HTTP-Server-with-execute-bash.git
$ cd Python27-HTTP-Server-with-execute-bash
```
or download, unzip source and go to uzipped directory(***%ROOT_PATH%***)

## Preparation:
Change permissions from executable files.

For example, run:
```bash 
$ chmod u+x main.py
$ chmod u+x run_bash_script.py
$ chmod u+x script.sh
```
with your favourite terminal emulator.

## Usage:
1. Run `main.py` whith you Python 2.7.
**For example**:

```bash
$ python2.7 main.py
```
1. Check server running
For example, run:
```bash
$ curl "http://localhost:8000"
```
If the response comes with an html page with a title
```html
...
<title>Server is RUNNING!</title>
...
```
It means your server is running successfully.

Your HTTP Server now running on `localhost`, port: `8000`
1. Open a browser to the http://localhost:8000/run_bash_script.py

**Result**: 
In scipts ***%ROOT_PATH%tmp/*** folder you can see file `test2.txt`. It`s file is a copy of test.txt.
1. You can **POST** any params to your script.
For example:
```bash
$ curl -d "param1=test2.txt&param2=test3.txt" -X POST http://localhost:8000/cgi-bin/run_bash_script.py
```

**Result**: 
In scipts ***%ROOT_PATH%/tmp/*** folder you can see file `test3.txt`. It`s file is a copy of test2.txt.

For your purpose, change the `script.sh` and python code if necessary.
