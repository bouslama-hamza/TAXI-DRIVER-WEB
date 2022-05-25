import socket
from csv import writer
from general_visualisation import to_solve

HOST = '192.168.43.251'
PORT = 1234

with socket.socket(socket.AF_INET , socket.SOCK_STREAM) as s:

    s.bind((HOST , PORT))
    s.listen(5)
    conn , addr = s.accept()
    print("Connected to : ",addr)
    
    while True:
        result = conn.recv(1024).decode('utf-8')
        if result:
            print(result)
            if result.split(",")[4] == 'Passed Detection':   
                latest = to_solve()
                if (latest-1) >= 0 :
                    with open("static/testing/test.csv" , 'a') as f:
                        object_write = writer(f)
                        object_write.writerow(result.split(','))
                        f.close()
            else:
                with open("static/testing/test.csv" , 'a') as f:
                        object_write = writer(f)
                        object_write.writerow(result.split(','))
                        f.close()

        conn , addr = s.accept()