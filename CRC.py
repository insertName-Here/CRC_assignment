'''correct cases for the checker:'''

#polynomial ='1110'
#received='100100000'

#polynomial ='10011'
#received='11010110111110'

#polynomial ='1101'
#received='100100001'


'''cases for the maker'''
polynomial ='1101'
received='100100'

def CRC_check():
    '''
    On the receiver end
    checks if there is an error in the bit stream
    '''
    dividor=input('please enter the polynomial key:')
    message=input('please enter the recieved data:')
    
    msg=message[len(dividor):]+'0' #there is an exter '0' the result will ignor
    subject=message[:len(dividor)]
    result=''
    
    while msg!='':
        if subject[0]=='1':d=dividor
        else:d='0'*len(dividor)
        
        temp=''
        for index in range(len(dividor)):   #bit wise XOR
            temp+=str(int(d[index])^int(subject[index]))
        
        result=temp
        subject=temp[1:]+msg[0]
        msg=msg[1:]
        
    for i in result:
        if i=='1':
            print('The received message is corrupted. Please ask the sender to resend.')
    else:print('The recived data is correct.')

def CRC_maker():
    '''
    On the sender side
    calulates the crc part that will be added to the data before sending it
    '''
    dividor=input('please enter the polynomial key:')
    message=input('please enter the the data:')
    
    msg=message[len(dividor):]+'0'*len(dividor) #there is an extera '0' the result will ignor
    subject=message[:len(dividor)]
    result=''
    
    while msg!='':
        if subject[0]=='1':d=dividor
        else:d='0'*len(dividor)
        
        temp=''
        for index in range(len(dividor)):   #bit wise XOR
            temp+=str(int(d[index])^int(subject[index]))
        
        result=temp
        subject=temp[1:]+msg[0]
        msg=msg[1:]
    result=result[1:]
    print('the CRC block is '+result+' and the whole data will be '+message+result)
    



'''
tial 1:
'''
#i=0
#msg=[]
#while i<len(message)-len(dividor)+1:
    #msg.append(message[i:i+len(dividor)])
    #i+=1

'''
tial 2:
'''

#i=0
#msg=[]
#subject=message[:len(dividor)]
#result='1101'
#while i<len(message)-len(dividor):
    #temp=''
    #for index in range(len(dividor)):
        #temp+=int(result[index])^int(subject[index])
    #msg.append(temp)
    #result=result[1:]+message[i]
    #i+=1
#print(msg)


'''
trial 3: success
'''
#i=0
#msg=message[len(dividor):]+'0'
#div=dividor
#subject=message[:len(dividor)]
#result=''

##ltemp=[]
##lsubject=[]

#while msg!='':
    #if subject[0]=='1':d=div
    #else:d='0'*len(dividor)
    
    #temp=''
    #for index in range(len(dividor)):
        #temp+=str(int(d[index])^int(subject[index]))
    
    #result=temp
    #subject=temp[1:]+msg[0]
    #msg=msg[1:]
    ##lsubject.append(subject)
    ##ltemp.append(temp)
#print(result)
