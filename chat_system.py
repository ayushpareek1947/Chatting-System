while(1):
    
   
    import pyrebase
    config = {
      "apiKey": "apiKey",
      "authDomain": "training-b23f4-default-rtdb.firebaseapp.com",
      "databaseURL": "https://training-b23f4-default-rtdb.firebaseio.com",
      "storageBucket": "training-b23f4-default-rtdb.appspot.com"
    }

    firebase = pyrebase.initialize_app(config)
    db = firebase.database()
    db.child("UserData").update({"Username":"password"})
    db.child("Sender").update({"Username":"name"})

    d=db.child("UserData").get()
    detail=db.child("Sender").get()
    x=input("Press 'e' for enrollment, Press 'a' for authentication, Press 'q' for quit: ")
    x=x.upper()
    if(x=='E'):
        p=0
        q=[]
        
        for i in d.each():
            q.append(i.key())
        while(p==0):
            un=input("Press the Username: ")
             
            if un not in q:
                pw=input("Enter password: ")
                db.child("UserData").update({un:pw}) 
                db.child("Data").update({un:""})
                print("Enrollment complete")
                x=input("Press 'a' for authentication, Press 'q' for quit: ")
                x=x.upper()
                p=1
            else:
                print("Username Already Exist")
                p=0
         
                     

       
    if(x=='A'):
        a,f=0,0
        q=[]
        p=[]
        usrname=""
        for i in d.each():
            q.append(i.key())
            p.append(i.val())
        
        while(f==0):
            un=input('Enter Username: ')
            for w  in range(len(q)):
                if un==q[w]:               
                    f=1
                    username=un
                    while(a==0):
                        pw=input("Enter Password: ")
                        if pw in p:
                            if q.index(un)==p.index(pw):
                                a=1
                                print("Welcome to Chat-api")
                        else:
                            a=0
                            print("Wrong password enter again: ")
            if f==0:
                f=0
                print("Username doesnot exist,enter again: ")
       
        X=input("Press 'r' to receive message,Press 's' to send messege: ")
        X=X.upper()
        if(X=='S'):
            m=0
            while(m==0):
                name=input("Enter receiver name: ")
                
                if name in q:
                    message=input("Enter message: ")
                    db.child("Sender").update({un:name})
                    from datetime import datetime
                    now = datetime.now() # current date and time
                    date_time = now.strftime("%d-%m-%Y, %H-%M-%S")
                    db.child("Data").child(name).child(username).update({ date_time:message})
                    db.child("seen").child(name).child(username).update({ date_time:message})
                    db.child("unseen").child(name).child(username).update({ date_time:message})
                    
                    m=1
                else:
                    m=0
                    print("Please enter correct receiver name: ")
        sender=[]
        receiver=[]
        
        for i in detail.each():
            sender.append(i.key())
            receiver.append(i.val())
            
            

        if(X=='R'):
            
            for n in range(len(receiver)):
                
                if(un==receiver[n]):
                    
                    print("Received Messages from: ",sender[n])
            N=input("Press 's' for specific person's message you want to see, Press 'a' to receive all message: ")
            N=N.upper()
            if(N=='S'):
                name=input("Enter whose message you want to see: ")
                for p in range(len(sender)):
                    if(sender[p]==name):
                        sender.pop(p)
                        receiver.pop(p)
                        z="Sender/"+name
                        db.child(z).remove()
                ra=db.child("Data").child(username).child(name).get()
                rr=db.child("unseen").child(username).child(name).get()
                db.child("unseen").child(username).child(name).remove()
                print(rr.val())
                
            if(N=='A'):
                for k in range(len(q)):
                    if(q[k]==username):
                        continue
                    else:
                        
                        print(q[k])
                        name=q[k]
                        
                        ra=db.child("Data").child(username).child(name).get()
                        rr=db.child("unseen").child(username).child(name).get()
                        db.child("unseen").child(username).child(name).remove()
                        print(ra.val())
                for p in range(len(receiver)):
                    if(receiver[p]==username):
                        nam=sender[p]
                        sender.pop(p)
                        receiver.pop(p)
                        z="Sender/"+nam
                        db.child(z).remove()
            y=input("Enter 'y' to see previous messages: ")
            if(y=='y'):
                rd=db.child("seen").child(username).child(name).get()
                print(rd.val())
            
                        
    if(x=='Q'):
        print("Thank you for visit")
        break
