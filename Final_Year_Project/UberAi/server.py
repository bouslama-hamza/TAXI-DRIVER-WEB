import socket
from csv import writer
from general_visualisation import to_solve
from solver import get_data

HOST = '192.168.100.77'
PORT = 65000

with socket.socket(socket.AF_INET , socket.SOCK_STREAM) as s:

    s.bind((HOST , PORT))
    s.listen(5)
    conn , addr = s.accept()
    
    while True:
        result = conn.recv(1024).decode('utf-8')
        if result:
            print(result)
            if result.split(",")[4] == 'Passed Detection':   
                latest = to_solve()
                print(latest-1)
                if (latest-1) < 0 :
                    make = get_data(result.split(",")[3])
                    with open("static/testing/test.csv" , 'a') as f:
                        object_write = writer(f)
                        object_write.writerow(make.split(','))
                        f.close()

            with open("static/testing/test.csv" , 'a') as f:
                object_write = writer(f)
                object_write.writerow(result.split(','))
                f.close()

        conn , addr = s.accept()
                
    



                

