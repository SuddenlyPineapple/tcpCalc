# tcpCalc

## How to run
Note: Application default needs Python3.6 to work properly as it was testet at this version

To run as server: `python main.py -a server_ip -S` <br>
To run as client: `python main.py -a server_ip -S`

If address and mode are not supplied, the default values are `127.0.0.1`(localhost) and application ask about working mode.

## help
<pre>
usage: main.py [-h] [-a ADDR] [-S] [-C]
optional arguments:
  -h, --help            show this help message and exit
  -a ADDR, --addr ADDR  valid ip address for working
  -S, --server          working as server
  -C, --client          working as client
</pre>

## TCP Segment description (ASCII version)

<pre>
OPERATION TYPE  |  Status  |  ID token  |  Timestamp  |   NumberA   |   NumberB   |   Result
#1:O=___+         #2:S=___+   #3:I=___+    #4:T=___+      #5:A=___+     #6:B=___+     #7:R=___+
</pre>

OPERATION TYPES (ex. if #1:O=1, then operation between numberA and numberB is addition):
<ul>
    <li>addition = 1</li>
    <li>substraction = 2</li>
    <li>multiplication = 3</li>
    <li>division = 4</li>
    <li>exponentation = 5</li>
    <li>negation = 6</li>
    <li>root = 7</li>
    <li>combination = 8</li>
    <li>factorial = 9</li>

</ul>
