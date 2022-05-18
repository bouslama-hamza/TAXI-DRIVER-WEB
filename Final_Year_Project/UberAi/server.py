import socket
from csv import writer

HOST = '192.168.100.77'
PORT = 65000

with socket.socket(socket.AF_INET , socket.SOCK_STREAM) as s:

    s.bind((HOST , PORT))
    s.listen(5)
    conn , addr = s.accept()
    
    while True:
        result = conn.recv(1024).decode('utf-8')
        if result:
            print(result.split(','))
            with open("static/testing/test.csv" , 'a') as f:
                object_write = writer(f)
                object_write.writerow(result.split(','))
                f.close()
        conn , addr = s.accept()
                
    



                

