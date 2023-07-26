# -*- coding:utf-8 -*-

import socket
import image_preprocess
from number_ocr import NumberOCR

BUFSIZE = 1024

HOST = 'localhost'
PORT = 6601
ADDR = (HOST, PORT)
sub_threads = []

listen_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
# listen_sock.settimeout(5.0)  # 设定超时时间后，socket其实内部变成了非阻塞，但有一个超时时间
listen_sock.bind(ADDR)
listen_sock.listen(2)
print('build connect when new TCP comes')

while True:
    connected_sock, client_addr = listen_sock.accept()
    if connected_sock:
        print('%s from fanuc robot connected' % client_addr[0])
        while True:
            try:
                data = connected_sock.recv(BUFSIZE)
            except Exception as e:
                print('Error occured:', repr(e))
                connected_sock.close()
                break
            else:
                if len(data) > 0:
                    # print('receive order:', data)
                    order = str(data.decode())
                    print('receive data:', data)
                    print('receive order:', order)
                    if order == 'Q':
                        send_data = ''
                        # for item in cur_time_spl:
                        #     send_data += item
                        #     send_data += ','

                        send_data += '1,'
                        send_data += '9,'
                        input_id = int(input('> '))
                        if input_id == 1:
                            send_data += '1'
                        elif input_id == 2:
                            send_data += '2'
                        else:
                            send_data += '0'
                        send_data += 'A'
                        print('feedback ready:', send_data)
                        connected_sock.sendall(send_data.encode())
                        print('send feedback:', send_data)
                    else:
                        try:
                            # print('./image_archive/' + order + '.bmp')
                            send_data = NumberOCR('./image_archive/' + order + '.bmp', 'LeNet')
                            connected_sock.sendall(send_data.encode())
                        except Exception as e:
                            print(e)
                            send_data = 'no action'
                            connected_sock.sendall(send_data.encode())
                else:
                    print('close the connected socket and terminate sub thread')
                    connected_sock.close()
                    break
    else:
        continue
