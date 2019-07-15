import asyncio, socket , threading


list_user =[]


async def handle_client(client):
    request = None
    while request != 'quit':
        request = (await loop.sock_recv(client, 255)).decode('utf8')
        response = str(eval(request))+' : name' + '\n'+'conn to server +\n'
        response2 = str(eval(request))+ 'conn to server   | your id : '+str(len(list_user)-1)
        await loop.sock_sendall(client, response2.encode('utf8'))
    client.close()

async def run_server():
    while True:
        conn, addr = await loop.sock_accept(server)
        # print('Connected by', client)
        list_user.append(conn)
        loop.create_task(handle_client(conn))

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 15560))
server.listen(8)
server.setblocking(False)



class mt(threading.Thread) :
    def run(self):
        i=0
        while True:


            s= input("usid")
            s= int(s)
            txt = input("enter text")
            txt= int(txt)
            print(list_user[s])
            list_user[s].sendall(b'%d' %txt)

th = mt()
th.start()


loop = asyncio.get_event_loop()
loop.run_until_complete(run_server())






















# import asyncore
# import socket
#
# class EchoHandler(asyncore.dispatcher_with_send):
#
#     def handle_read(self):
#         data = self.recv(8192)
#         if data:
#             self.send(data)
#
# class EchoServer(asyncore.dispatcher):
#
#     def __init__(self, host, port):
#         asyncore.dispatcher.__init__(self)
#         self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
#         self.set_reuse_addr()
#         self.bind((host, port))
#         self.listen(5)
#
#     def handle_accept(self):
#         pair = self.accept()
#         if pair is not None:
#             sock, addr = pair
#             print ('Incoming connection from %s' % repr(addr))
#             handler = EchoHandler(sock)
#
# server = EchoServer('localhost', 15555)
# asyncore.loop()