import socket,select,threading,serobra

d=input('Веведите ip')
soc=socket.socket()
soc.bind((d,9090))
soc.listen(5)

a=[soc]#пидоры 
b=[]#пытающися подключится
nik={}#Ники
sob={}#приемник сообшеня

sob1=serobra.ser("Server запущен").encode()


while True:
    k,m1,m2=select.select(a+b,[],[])
    for i in k:
        if i==a[0]:
            b.append(i.accept()[0])
        else:
         try:
            d=i.recv(1024)
            
            
            if d==b'':
            
                if i in nik:
                    d=serobra.ser(nik[i]+' отсоединился').encode()
                    sob1+=d
                    j=1
                    while j<len(a):
                        if a[j]==i:
                            del a[j]
                        else:
                            try:
                               a[j].sendall(d)
                               j+=1
                            except:
                                j+=1
                                continue
                        

                    del sob[i]
                    del nik[i]

                else: 
                    for j in range(len(b)):
                        if b[j]==i:
                            del b[j]
                            break
                    
            else:

                if i in a:
                   
                       d = sob[i]+d
                       d = list(d.split(b'\n'))
                       sob[i] = d[len(d)-1]
                       del d[len(d)-1]

                       for  j in range(len(d)):
                           d[j]=serobra.obrsob(d[j].decode())
                           if d[j]!='':
                               sob1+=(nik[i]+":"+d[j]).encode()


                       
                       

                       for j in range(1,len(a)):
                          
                           s= "Вы:" if a[j]==i else nik[i]+':'
                           

                           for ji in range(len(d)):
                               try:
                                  if d[ji]!='':
                                      a[j].sendall((s+d[ji]).encode())
                               except:
                                   break



                    
                
                else:
                    
                    try:
                          d=d.decode()
                          
                          s=serobra.prower(d)
                  
                          if type(s)==int:
                                i.sendall(str(s).encode())
                                continue

                          for j in nik:
                              if nik[j]==s:
                                   i.sendall(b'502')
                                   break
                          else:

                             nik[i]=s
                             sob[i]=b''
                             a.append(i)

                             for j in range(len(b)):
                                   if b[j]==i:
                                     del b[j]
                                     break

                             s=serobra.ser(s+" присоеденился").encode()

                             for j in range(1,len(a)):
                                 try:
                                       if a[j]==i:
                                           a[j].sendall(sob1)
                                       a[j].sendall(s)
                                 except:
                                     continue

                             sob1+=s

                             
                    
                    except UnicodeDecodeError:
                        i.sendall(b'404')


         
         
         except:
             continue
                    





