# AvgDateMicroservice

This Average Date Microservice uses Python and takes a list of dates given in the format of "day-month-year"
and returns the average number of days between those dates. 

ZeroMQ is used for the messenger between the Client and the Server. The Pyzmq package, which is the Python version
of ZeroMQ is easily downloaded by following the directions at https://zeromq.org/languages/python/

An example Client Side Call with a sample list of dates would look like:
------------------------------
```
import zmq

def average_days_between_dates_client(dates_list):
context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5555")

    socket.send_pyobj(dates_list)
    result = socket.recv_pyobj()
    
    socket.close()
    context.term()
    
    return result

dates = ['07-03-2023', '07-13-2023', '07-18-2023', '07-24-2023', '08-02-2023']
result = average_days_between_dates_client(dates)
print(f"The average number of days until your next task is: {result} days")
```
---------------------------------

An example of the Server Side Code:
----------------------------------
```
import zmq
from datetime import datetime

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

def average_days_between_dates(date_list):

    date_objects = [datetime.strptime(date_str, '%m-%d-%Y') for date_str in date_list]

    total_days = 0
    for i in range(len(date_objects) - 1):
        total_days += (date_objects[i + 1] - date_objects[i]).days

    average_days = total_days // (len(date_objects) - 1)
    return average_days
    

while True:
    dates_list = socket.recv_pyobj()
    print("Sending back average days.")
    result = average_days_between_dates(dates_list)
    socket.send_pyobj(result)
```
-------------------------------------------

UML Sequence Diagram:

<img width="631" alt="Screenshot 2023-07-31 at 6 02 43 PM" src="https://github.com/Ben-Romaine/AvgDateMicroservice/assets/107928674/c1eac705-2e5e-42c3-8650-2ea80180d35c">

