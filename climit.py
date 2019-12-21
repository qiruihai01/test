from socket import*
import os,sys

def sendto(db,addr,name):
    data=input('大哥请发话：')
    if data == 'quit':
        ms='Q '
        db.sendto(ms.encode(),addr)
        db.close()
        sys.exit()
    else:
        ms='c ' + name+" "+data
        db.sendto(ms.encode(),addr)
    

    

def recvfrom(db):
    data,addr=db.recvfrom(4096)
    print(data.decode())


def main():
    db=socket(AF_INET,SOCK_DGRAM)


    addr=('127.0.0.1',8888)

    #while True:
    m=input('大哥，请输入名字:')
    data='l '+m
    #if not data:
    #    break
    n=db.sendto(data.encode(),addr)
    while True:
        data,addr=db.recvfrom(4069)
        #判断回复的内容是什么类型
        if data.decode() == 'ok':
            print('您已经进入聊天室')
            break
        else:
            print(data.decode())

    pid=os.fork()
    if pid < 0:
        print('进程创建失败！')
    elif pid > 0:
        while True:
            sendto(db,addr,m)
    else:
        while True:
            recvfrom(db)

   #开始聊天了
#增加了一行


            
if __name__ == '__main__':
    main()
