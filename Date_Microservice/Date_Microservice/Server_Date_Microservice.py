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