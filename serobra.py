def prower(d):

    s = d
    pr=0
    
    if d[0] in ('\t',' ') or pr==2:
             return 406


    for i in range(len(d)):
        if d[len(d)-1-i] not  in (' ','\t'):
            break
        s=d[:len(d)-1-i]
    
    d=s
    s=''

    for i in range(len(d)):
        s2 = ' ' if d[i]=='\t' else d[i]
        if  not('a'<=s2.lower()<='z') and not('а'<=s2.lower()<='я') and s2!=' ' and s2.lower()!='ё':
                return 405
        if s2==' ':    
            if len(s)>0 and s[len(s)-1]!=s2:
                s+=s2
                pr+=1
        else:
            s+=s2

        if len(s)>=32:
            return 404

    
    if  len(s)<3:
           return 404


    return s
        

def ser(d):
    k=len(d)//2
    k=30-k   
    return ' '*k+d+'\n'
   


def obrsob(d):
    s = ''
    s2 = ' '
    
    for i in d:
        i=' ' if i=='\t' else i
        
        if (i==' ' and i!=s2) or i!=' ':
            s+=i
        
        s2=i
    
    return s+'\n'
          

        
