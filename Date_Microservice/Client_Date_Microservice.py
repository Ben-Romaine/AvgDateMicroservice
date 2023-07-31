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

dates = ['2023-07-03', '2023-07-13', '2023-07-18', '2023-07-24', '2023-08-02']
result = average_days_between_dates_client(dates)
print(f"The average number of days is: {result}")