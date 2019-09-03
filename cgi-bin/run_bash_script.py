#!/usr/bin/env python

print "Content-type: text/html"
print ""
import subprocess
import sys
import os
import cgi
import cgitb
import re
import logging
from subprocess import CalledProcessError

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)

arguments = cgi.FieldStorage()

for i in arguments.keys():
    logging.info("key : %s -- value : %s " % (i, arguments.getvalue(i)))
params=[]
if "param1" in arguments and "param2"  in arguments:
    logging.info("param1 =  %s" % arguments.getvalue('param1'))
    logging.info("param2 =  %s" % arguments.getvalue('param2'))
    params.append(arguments.getvalue('param1'))
    params.append(arguments.getvalue('param2'))
else:
    logging.warning("param1 or param2 is not exists or empty")

pattern = re.compile("^\/?([A-z0-9-_+]+\/)*([A-z0-9]+\.(\w{0,4}))$")
for p in params:
    if !pattern.match(string):
        logging.warning("%s not match as file path" % p)
        params = []
        break



logging.info("Your Python version =  %s" % sys.version)

cgitb.enable()  # Error reporting
result = -1
logging.info("params: %s" % params)
try:
    if not params:
        logging.info("params is empty")
        result = subprocess.call(['./script.sh'], shell=True)
    else:
        logging.info("params not empty")
        result = subprocess.check_call(['./script.sh', params[0], params[1]]) # Using shell=True can be a security hazard. See the warning under Frequently Used Arguments(https://docs.python.org/2/library/subprocess.html#frequently-used-arguments) for details.
except CalledProcessError as e:
    logging.error("Error while execute bash script")
finally:
    if result!=0:
        logging.info("Bash script return %d code" % result)



print """
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN"
        "http://www.w3.org/TR/html4/strict.dtd">
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html;charset=utf-8">
        <title>Run Bash Script</title>
    </head>
    <body>
        <h1>BaseHTTPServer Python2.7 is running</h1>
        <br>
        <strong>Your Python version =  %s</strong>
        <br>
        <h2>Your bash-script has been executed. </h2>
        <a href = '/'>Go back</a>
    </body>
</html>""" % sys.version
