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

