# Create your views here.
from django import contrib
from django.shortcuts import redirect, render, HttpResponse
from datetime import datetime 
from firebase import firebase
from requests import post,get
from firebase.firebase import FirebaseApplication, FirebaseAuthentication
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth import SESSION_KEY, authenticate
from django.contrib.auth import logout,login
import pyrebase 
from pyrebase.pyrebase import Database
import firebase_admin
from firebase_admin import auth ,credentials, db
from datetime import date
from datetime import datetime 
import uuid

config = {    
    "apiKey": "AIzaSyDxtgOS-lNR5iHH-35xjs9r1gIwiLDW6E8",
    "authDomain": "neemeesh-trial.firebaseapp.com",
    "databaseURL": "https://neemeesh-trial-default-rtdb.firebaseio.com",
    "projectId": "neemeesh-trial",
    "storageBucket": "neemeesh-trial.appspot.com",
    "messagingSenderId": "608861234921",
    "appId": "1:608861234921:web:2792a40a8e9cf8611c7278",
    'measurementId': "G-67HDRQV9KN"
}
firebase = pyrebase.initialize_app(config) 
authe = firebase.auth() 
database = firebase.database()
cred = credentials.Certificate('neemeesh-trial-firebase-adminsdk-kl0a5-1cf2f25008.json')
firebase_admin.initialize_app(cred)
def index(request):
    #context = {"variable1": "Harry is great", "variable2": "Rohan is great"}
    #return HttpResponse("This is homepage")
    return render(request, 'index.html')
def contact(request):
    return render(request, 'contact.html')
def about(request):
    return render(request, 'about.html')
def services(request):
    return render(request, 'services.html')    
def prelogin(request):
    return render(request,'prelogin.html')  
def adminlogin(request):
    return render(request,'adminlogin.html')    
def dispatchlogin(request):
    return render(request,'dispatchlogin.html')    
def mislogin(request):
    return render(request,'mislogin.html')    
def bookinglogin(request):
    return render(request,'bookinglogin.html')
def registeradmin (request) :
    return render(request , "registeradmin.html")    
def registerbooking (request) :
    return render(request , "registerbooking.html")    
def registerdispatch (request) :
    return render(request , "registerdispatch.html")    
def registermis (request) :
    return render(request , "registermis.html")
def lh3render(request):
    user_id=request.POST.get('hiddenuserid3')
    return render (request , "lh3.html" , {'user_id':user_id})

def postregisteradmin (request) :
    email = request.POST.get('email')
    passw1 = request.POST.get('pass')
    try:
        user=authe.create_user_with_email_and_password(email,passw1)
        session_id=user['idToken']
        request.session['uid']=str(session_id)
    except:
        msg="Email Already Exists!"
        return render(request,"registeradmin.html",{"msg":msg}) 
        #push data 
    data={
        "Name" : request.POST.get('name') ,
        "Email" : email ,
        "Address" : request.POST.get('add') ,
        "User Id": request.POST.get('id'),
        "State": request.POST.get('state'),
        "City": request.POST.get('city'),
        "Pincode": request.POST.get('pin'),
        "Phone Number": request.POST.get('phone'),
        }
    database.child("Data").child("Signup").child("Admin").push(data)
    print("User created")
    msg="You have successfully registered a new Admin!"
    return render(request,"registernewuser.html",{"msg":msg})
    # messages.success(request, 'Your have successfully registered!')
    # return render(request,"registernewuser.html")
def postregisterbooking (request) :
    email = request.POST.get('email')
    passw1 = request.POST.get('pass')
    try:
        user=authe.create_user_with_email_and_password(email,passw1)
        session_id=user['idToken']
        request.session['uid']=str(session_id)
    except:
        msg="Email Already Exists!"
        return render(request,"registerbooking.html",{"msg":msg}) 
        #push data 
    data={
        "Name" : request.POST.get('name') ,
        "Email" : email ,
        "Address" : request.POST.get('add') ,
        "User Id": request.POST.get('id'),
        "State": request.POST.get('state'),
        "City": request.POST.get('city'),
        "Pincode": request.POST.get('pin'),
        "Phone Number": request.POST.get('phone'),
        }
    database.child("Data").child("Signup").child("Booking").push(data)
    print("User created")
    msg="You have successfully registered a new Booking User!"
    return render(request,"registernewuser.html",{"msg":msg})
def postregistermis (request) :
    email = request.POST.get('email')
    passw1 = request.POST.get('pass')
    try:
        user=authe.create_user_with_email_and_password(email,passw1)
        session_id=user['idToken']
        request.session['uid']=str(session_id)
        #msg="Email Already Exists!"
        #return render(request,"registermis.html",{"msg":msg})
    except:
        msg="Email Already Exists!"
        return render(request,"registermis.html",{"msg":msg}) 
        #push data 
    data={
        "Name" : request.POST.get('name') ,
        "Email" : email ,
        "Address" : request.POST.get('add') ,
        "User Id": request.POST.get('id'),
        "State": request.POST.get('state'),
        "City": request.POST.get('city'),
        "Pincode": request.POST.get('pin'),
        "Phone Number": request.POST.get('phone'),
        }
    database.child("Data").child("Signup").child("MIS").push(data)
    msg="You have successfully registered a new MIS User!"
    return render(request,"registernewuser.html",{"msg":msg})
def postregisterdispatch (request) :
    email = request.POST.get('email')
    passw1 = request.POST.get('pass')
    try:
        user=authe.create_user_with_email_and_password(email,passw1)
        session_id=user['idToken']
        request.session['uid']=str(session_id)
    except:
        msg="Email Already Exists!"
        return render(request,"registerdispatch.html",{"msg":msg}) 
        #push data 
    data={
        "Name" : request.POST.get('name') ,
        "Email" : email ,
        "Address" : request.POST.get('add') ,
        "User Id": request.POST.get('id'),
        "State": request.POST.get('state'),
        "City": request.POST.get('city'),
        "Pincode": request.POST.get('pin'),
        "Phone Number": request.POST.get('phone'),
        }
    database.child("Data").child("Signup").child("Dispatch").push(data)
    msg="You have successfully registered a new Dispatch User!"
    return render(request,"registernewuser.html",{"msg":msg})

def registercourier (request) :
    email = request.POST.get('email')
    passw1 = request.POST.get('pass')
    try:
        user=authe.create_user_with_email_and_password(email,passw1)
        session_id=user['idToken']
        request.session['uid']=str(session_id)
    except:
        msg="Email Already Exists!"
        return render(request,"registercourier.html",{"msg":msg}) 
        #push data 
    data={
        "Name1" : request.POST.get('name') ,
        "Email" : email ,
        "Address" : request.POST.get('add') ,
        "User Id": request.POST.get('id'),
        "City": request.POST.get('city'),
        "Phone Number": request.POST.get('phone'),
        }
    database.child("Data").child("Signup").child("Courier").push(data)
    msg="You have successfully registered a new Courier User!"
    return render(request,"registercourier.html",{"msg":msg})


def postloginadmin (request) :
    email = request.POST.get('username')
    passwd =  request.POST.get('password')
    firebase=FirebaseApplication("https://neemeesh-trial-default-rtdb.firebaseio.com/", None)
    result=firebase.get('/Data/Signup/Admin', None) 
    flag=0
    tempmail='0'
    msg='0'
    for userid,user in result.items():
        if email==user['Email'] :    
            flag=1
            # if there is no error then signin the user with given email and password
            try:
                user=authe.sign_in_with_email_and_password(email,passwd)
                session_id=user['idToken']
                request.session['uid']=str(session_id)
                return render(request , 'adminhome.html')
            except:
                tempmail=email
                msg="Invalid Password!!"
                return render(request,"adminlogin.html",{"msg":msg,"tempmail":tempmail})   
    if flag==0:       
        msg="Invalid Credentials!!Please ChecK your Data"
        return render(request,"adminlogin.html",{"msg":msg}) 
def postloginbooking(request) :
    email=request.POST.get('username')
    passwd =request.POST.get('password1')
    user_id=request.POST.get('bookinguserid')
    firebase=FirebaseApplication("https://neemeesh-trial-default-rtdb.firebaseio.com/", None)
    result=firebase.get('/Data/Signup/Booking', None)
    flag=0
    tempmail='0'
    msg='0'
    for userid,user in result.items():
        if user_id==user['User Id'] :
            
            if email==user['Email'] :

                flag=1
                    # if there is no error then signin the user with given email and password
                try:


                    user=authe.sign_in_with_email_and_password(email,passwd)
                    session_id=user['idToken']
                    request.session['uid']=str(session_id)
                    firebase=FirebaseApplication("https://neemeesh-trial-default-rtdb.firebaseio.com/", None)
                    companies=list(firebase.get("/Data/Company",None).values())
                    compnames=[]
                    for compdetails in companies:
                        for eachcompkey,eachcompval in compdetails.items():
                            if eachcompkey=='Company Name':
                                compnames.append(eachcompval)
                    return render(request , 'bookingorder1.html' , {"compnames":compnames , "user_id":user_id})
                except :
                    tempmail=email
                    msg="Invalid Password!!"
                    return render(request,"bookinglogin.html",{"msg":msg,"tempmail":tempmail})   
    if flag==0:       
        msg="Invalid Credentials!!Please ChecK your Data"
        return render(request,"bookinglogin.html",{"msg":msg})
def postloginmis(request) :
    email = request.POST.get('username')
    passwd =  request.POST.get('password')
    firebase=FirebaseApplication("https://neemeesh-trial-default-rtdb.firebaseio.com/", None)
    result=firebase.get('/Data/Signup/MIS', None)
    flag=0
    tempmail='0'
    msg='0'
    for userid,user in result.items():
        if email==user['Email'] :    
            flag=1
            # if there is no error then signin the user with given email and password
            try:
                user=authe.sign_in_with_email_and_password(email,passwd)
                session_id=user['idToken']
                request.session['uid']=str(session_id)
                firebase=FirebaseApplication("https://neemeesh-trial-default-rtdb.firebaseio.com/", None)
                admindata=list(firebase.get("/Data/BookingOrder/Orders",None).values())
                return render(request , 'lh2.html' , {"admindata":admindata})
            except :
                tempmail=email
                msg="Invalid Password!!"
                return render(request,"mislogin.html",{"msg":msg,"tempmail":tempmail})   
    if flag==0:       
        msg="Invalid Credentials!!Please ChecK your Data"
        return render(request,"mislogin.html",{"msg":msg})
def postlogindispatch(request) :
    email = request.POST.get('username')
    passwd =  request.POST.get('password')
    user_id = request.POST.get('userid')
    firebase=FirebaseApplication("https://neemeesh-trial-default-rtdb.firebaseio.com/", None)
    result=firebase.get('/Data/Signup/Dispatch', None)
    flag=0
    tempmail='0'
    msg='0'
    for userid,user in result.items():
        if user_id == user['User Id'] :
            if email==user['Email'] :    
                flag=1
                # if there is no error then signin the user with given email and password
                try:
                    user=authe.sign_in_with_email_and_password(email,passwd)
                    session_id=user['idToken']
                    request.session['uid']=str(session_id)
                    fromcity=list(firebase.get("/Data/BookingOrder/Orders",None).values())
                    fromcitylist=[]
                    for citydetails in fromcity:
                        for eachcitykey,eachcityval in citydetails.items():
                            if eachcitykey=='fromcity':
                                if eachcityval not in fromcitylist:
                                    fromcitylist.append(eachcityval)
                    

                    return render(request , 'lh3.html' , {"fromcitylist" : fromcitylist , "user_id" : user_id})
                except :
                    tempmail=email
                    msg="Invalid Password!!"
                    return render(request,"dispatchlogin.html",{"msg":msg,"tempmail":tempmail })   
    if flag==0:      
        msg="Invalid Credentials!!Please ChecK your Data"
        return render(request,"dispatchlogin.html",{"msg":msg})
def registernewuser(request):
    return render(request , "registernewuser.html")
def registernewproduct(request):
    return render(request , "registernewproduct.html")
def lh1(request):
     pass
def lh2(request):
     pass  
def lh3(request):
     messages.success(request, 'You have successfully logged in')  
     pass
def dispatchpanel(request):
    return render(request , "dispatchpanel.html") 
def dispatchconfirm(request):
  
    return render(request , "dispatchconfirm.html" )
def postreset(request) :
    email = request.POST.get("email")
    try :
        authe.send_password_reset_email(email)
        message  = "A email to reset password is succesfully sent"
        return render(request, "bookingreset.html", {"msg":message})
    except:
        message  = "Something went wrong, Your Email is not registered!!"
        return render(request, "bookingreset.html", {"msg":message})

def forget(request) :
    return render (request ,"bookingreset.html")


def registernewcompany(request):
    return render(request , "registernewcompany.html")

def postregisternewcompany(request):
    firebase=FirebaseApplication("https://neemeesh-trial-default-rtdb.firebaseio.com/", None)
    result=firebase.get('/Data/Company/', None) 
    company_id=request.POST.get('compid')
    company_ids = []
    for userid,user in result.items():
        company_ids.append(user['Company id'])
    print(company_ids)
    if company_id not in company_ids  :    
    
        Data={
                'Company id': request.POST.get('compid'),
                'Company Name': request.POST.get('compname'),
                'Email id': request.POST.get('compmail'),
                'Contact Number 1': request.POST.get('compcont1'),
                'Contact Number 2': request.POST.get('compcont2'),
                'Address': request.POST.get('compadd'),
                'City': request.POST.get('compcity'),
                'Pincode' : request.POST.get('pincode'),
                'State': request.POST.get('compstate'),
                'Cost per': request.POST.get('costper'),
                'Cost' : request.POST.get('cost')
                
            }
        firebase.post('/Data/Company/', Data)
        msg="Company is Registered Successfully!"
        return render(request,"registernewcompany.html",{"msg":msg})
    else : 
        msg="Company Already Exists!!"
        return render(request,"registernewcompany.html",{"msg":msg})
            
def usertable (request) :
    firebase=FirebaseApplication("https://neemeesh-trial-default-rtdb.firebaseio.com/", None)
    admindata=list(firebase.get("/Data/Signup/Admin",None).values())
    dispatchdata=list(firebase.get("/Data/Signup/Dispatch",None).values())
    bookingdata=list(firebase.get("/Data/Signup/Booking",None).values())
    misdata=list(firebase.get("/Data/Signup/MIS",None).values())
    #print(data[0]['address'])
    return render (request ,"usertable.html",{'admindata':admindata,'dispatchdata':dispatchdata,'bookingdata':bookingdata,'misdata':misdata,})
def checkuserupdate(request)  :
    return  render(request ,"checkuserupdate.html" )
def postcheckuserupdate (request) :
    user_type = request.POST.get("usertype")
    old_email = request.POST.get("email")
    db = database.child("Data").child("Signup").child(user_type).get()
    for user in db.each() :
        if user.val()['Email']==old_email and auth.get_user_by_email(old_email) : 
            return render(request , "updateuser.html" ,{"old_email":old_email, "user_type": user_type})
    return render(request , "checkuserupdate.html" , {"msg" : "User not Found!"})
    
def postuserupdate(request):
    email = request.POST.get("old_email")
    user_type = request.POST.get("usertype")
    db = database.child("Data").child("Signup").child(user_type).get()
    new_address = request.POST.get("newaddress")
    new_city = request.POST.get("newcity")
    new_userid = request.POST.get("newuserid")
    new_name = request.POST.get("newname")
    new_phone= request.POST.get("newphone")
    new_pincode = request.POST.get("newpincode")
    new_state = request.POST.get("newstate")
    '''user=authe.create_user_with_email_and_password(new_email,passw1)
    session_id=user['idToken']
    request.session['uid']=str(session_id)'''
    for i in db.each() :
                database.child("Data").child("Signup").child(user_type).child(i.key()).update({
                "Address" : new_address ,
                 "City"   : new_city ,
                 "User Id": new_userid ,
                 "Name"   : new_name ,
                 "Phone Number"  : new_phone ,
                 "Pincode": new_pincode ,
                 "State"  :  new_state ,
                 "Email": email,
                })
    return render(request , "adminupdate.html" , {"msg1" : "The details of the required user have been updated !!"})
        
def deleteuser(request)  :
    return render(request,"deleteuser.html")
def postdeleteuser(request):
    user_type = request.POST.get("usertype")
    email = request.POST.get("email")
    db = database.child("Data").child("Signup").child(user_type).get()
    for user in db.each() :
        if user.val()['Email']==email : 
            database.child("Data").child("Signup").child(user_type).child(user.key()).remove()
            user = auth.get_user_by_email(email)
            auth.delete_user(user.uid)
            return render(request , "deleteuser.html" , {"msg" : "The User is deleted succesfully!"})
    return render(request , "deleteuser.html" , {"msg" : "User not Found!"})
# def productdetails(request):
#     firebase=FirebaseApplication("https://neemeesh-trial-default-rtdb.firebaseio.com/", None)
#     compdetails=list(firebase.get("/Data/Product",None).values())
#     return render (request ,"productdetails.html",{'compdetails':compdetails})


def bookingorder1 (request) :
    firebase=FirebaseApplication("https://neemeesh-trial-default-rtdb.firebaseio.com/", None)
    companies=list(firebase.get("/Data/Company",None).values())
    compnames=[]
    for compdetails in companies:
        for eachcompkey,eachcompval in compdetails.items():
            if eachcompkey=='Company Name':
                compnames.append(eachcompval)
    
    return render(request, 'bookingorder1.html' , {"compnames" : compnames })

def postbookingorder1 (request) :
    user_id=request.POST.get('hiddenbookinguserid')
    firebase=FirebaseApplication("https://neemeesh-trial-default-rtdb.firebaseio.com/", None)
    companies=list(firebase.get("/Data/Company",None).values())
    compnames=[]
    for compdetails in companies:
        for eachcompkey,eachcompval in compdetails.items():
            if eachcompkey=='Company Name':
                compnames.append(eachcompval)
    fromcity = request.POST.get("fromcity")
    company_name = request.POST.get("compname1")
    datee = request.POST.get("date")
    docket_no = request.POST.get("docno")
    return render(request , "bookingorder.html"  , {"fromcity":fromcity , "company_name" : company_name , "datee" : datee , "docket_no" : docket_no ,"user_id":user_id})




def postbookingorder(request):
    fromcity=request.POST.get("fromcity")
    company_name = request.POST.get("company_name")
    datee = request.POST.get("datee")
    docket_no = request.POST.get("docno")
    destination = request.POST.get("destination")
    partyname= request.POST.get("partyname")
    invoice_no = request.POST.get("invcno")
    noofpckg= request.POST.get("noofpckg")
    description = request.POST.get("description")
    user_id=request.POST.get("hiddenbookinguserid")

    bill_id = uuid.uuid4()
    return render (request , "confirmbookingorder.html" , {        
                                                                    "fromcity" : fromcity ,
                                                                    "company_name" : company_name,
                                                                    "datee" : datee , 
                                                                    "docket_no" : docket_no ,
                                                                    "destination" : destination ,
                                                                    "partyname" : partyname ,
                                                                    "invoice_no" : invoice_no ,
 
                                                                    "noofpckg" : noofpckg,
                                                                     
                                                                    "description" : description ,
                                                                    "bill_id" : bill_id,
                                                                    "user_id" : user_id    })
   






def postconfirmbookingorder (request) : 

    company_name = request.POST.get("company_name")
    db9 = database.child("Data").child("Product").get()
    for i in db9.each() :
        if i.val()["Company Name"] == company_name : 
             cost=database.child("Data").child("Product").child(i.key()).child("Cost").get().val()


    user_id = request.POST.get('hiddenbookinguserid')
    bill_id = request.POST.get("bill_id")
    # totalcost= request.POST.get("totalcost")
    fromcity = request.POST.get("fromcity")
    # company_name = request.POST.get("company_name")
    datee = request.POST.get("datee")
    docket_no = request.POST.get("docket_no")
    destination = request.POST.get("destination")
    partyname = request.POST.get("partyname")
    noofpckg= request.POST.get("noofpckg")
    invcno = request.POST.get("invoice_no")    
    description = request.POST.get("description")
    totalcost = int(cost)*int(noofpckg)
    data = {
        
        "fromcity" : fromcity ,
        "company_name" : company_name ,
        "date"     : datee , 
        "docket_no" : docket_no ,
        "destination" : destination ,
        "partyname" : partyname ,
        "invcno"   : invcno , 
        "noofpckg" : noofpckg,
        "description" : description,
        "bill_id" : bill_id ,
        "totalcost" : totalcost 
    }

    database.child("Data").child("BookingOrder").child("Orders").push(data)
    # from twilio.rest import Client

    # # Your Account SID from twilio.com/console
    # account_sid = "ACa146b54a52c221a9a0b309438c3171c5"
    # # Your Auth Token from twilio.com/console
    # auth_token  = "5923edfc1be640f998dc9a3d237294a7"

    # client = Client(account_sid, auth_token)
     
    # message = client.messages.create(
    #     to="+917588069659", 
    #     from_="+16308844509",
    #     body="Your Order has been Confirmed Your Bill Id is :"+bill_id+"\n"+"You Booked your order on :"+datee)

    # print(message.sid)
    msg = "Your Order Has Been Placed Successfully !!"
    return render (request , "bookingorder.html" , {"msg" : msg,"fromcity" : fromcity ,
                                                                    "company_name" : company_name,
                                                                    "datee" : datee , 
                                                                    "docket_no" : docket_no ,"user_id":user_id})

def postmis (request) :
    return render (request , "lh2.html")






def producttable(request):


    if request.method == "POST":
            
            
            confirmed = request.POST.get('txtt')
            Pending = request.POST.get('txtt2')
            Cancle = request.POST.get('txtt3')
            Delete = request.POST.get('txtt4')

            if confirmed == "":
                pass
            else:
                
                confirmed1 = eval(confirmed)  #seprate dict's from tuple
                if type(confirmed1) == dict: #datatype checkout 
                    billid1=confirmed1.get("bill_id")
                    a=True
                    if a:
                        dbbillid1= database.child("Data").child("Mis").child("Confirmed").get()
                        for dbbillid11 in dbbillid1.each():
                            dbbillid111=dbbillid11.val().get("bill_id")
                            if billid1==dbbillid111:
                                database.child("Data").child("Mis").child("Confirmed").child(dbbillid11.key()).remove()        
                    if a:            
                        dbbillid2= database.child("Data").child("Mis").child("Pending").get()
                        for dbbillid22 in dbbillid2.each():
                            dbbillid222=dbbillid22.val().get("bill_id")
                            if billid1==dbbillid222:
                                database.child("Data").child("Mis").child("Pending").child(dbbillid22.key()).remove()
                    if a: 
                        dbbillid3= database.child("Data").child("Mis").child("Cancle").get()
                        for dbbillid33 in dbbillid3.each():
                            dbbillid333=dbbillid33.val().get("bill_id")
                            if billid1==dbbillid333:
                                database.child("Data").child("Mis").child("Cancle").child(dbbillid33.key()).remove()
                    database.child("Data").child("Mis").child("Confirmed").push(confirmed1)
            
                else:
                    for dict1 in confirmed1:
                        billid11=dict1.get("bill_id")
                        a=True
                        if a:
                            dbbillid1= database.child("Data").child("Mis").child("Confirmed").get()
                            for dbbillid11 in dbbillid1.each():
                                dbbillid111=dbbillid11.val().get("bill_id")
                                if billid11==dbbillid111:
                                    database.child("Data").child("Mis").child("Confirmed").child(dbbillid11.key()).remove()
                        if a:            
                            dbbillid2= database.child("Data").child("Mis").child("Pending").get()
                            for dbbillid22 in dbbillid2.each():
                                dbbillid222=dbbillid22.val().get("bill_id")
                                if billid11==dbbillid222:
                                    database.child("Data").child("Mis").child("Pending").child(dbbillid22.key()).remove()
                        if a: 
                            dbbillid3= database.child("Data").child("Mis").child("Cancle").get()
                            for dbbillid33 in dbbillid3.each():
                                dbbillid333=dbbillid33.val().get("bill_id")
                                #print("dbbillid333",dbbillid333)
                                if billid11==dbbillid333:
                                    database.child("Data").child("Mis").child("Cancle").child(dbbillid33.key()).remove()
                        database.child("Data").child("Mis").child("Confirmed").push(dict1)
                        # print("pushed",billid11)    
                    
                    
                    #for single data,for multiple data
                    #     delete1=database.child("Data").child("Mis").child("Confirmed").remove(dbbillid11.key())
                    #     delete1=database.child("Data").child("Mis").child("Pending").remove(dbbillid22.key())
                    #     delete1=database.child("Data").child("Mis").child("Cancle").remove(dbbillid33.key())
                    #     print(delete1)

            
            if Pending == "":
                pass
            else:
                Pending1 = eval(Pending)
                if type(Pending1) == dict:
                    #print("confirm 1 is list")
                    billid2=Pending1.get("bill_id")
                    #print(billid2)
                    a=True
                    
                    if a:
                        dbbillid1= database.child("Data").child("Mis").child("Confirmed").get()
                        for dbbillid11 in dbbillid1.each():
                            dbbillid111=dbbillid11.val().get("bill_id")
                            if billid2==dbbillid111:
                                database.child("Data").child("Mis").child("Confirmed").child(dbbillid11.key()).remove()
                            #     print("billid1",billid2)
                            #     print("dbbillid111",dbbillid111)
                            #     print("delete order from confirm1")
                            # else:
                            #     print("pending bill id not matched from confirmed 1")
                    if a:            
                        dbbillid2= database.child("Data").child("Mis").child("Pending").get()
                        for dbbillid22 in dbbillid2.each():
                            dbbillid222=dbbillid22.val().get("bill_id")
                            if billid2==dbbillid222:
                                database.child("Data").child("Mis").child("Pending").child(dbbillid22.key()).remove()
                            #     print("billid1",billid2)
                            #     print("dbbillid222",dbbillid222)
                            #     print("delete order from pending 1")
                            # else:
                            #     print("pending bill id not matched from pending 1") 
                    if a: 
                        dbbillid3= database.child("Data").child("Mis").child("Cancle").get()
                        for dbbillid33 in dbbillid3.each():
                            dbbillid333=dbbillid33.val().get("bill_id")
                            #print("dbbillid333",dbbillid333)
                            if billid2==dbbillid333:
                                database.child("Data").child("Mis").child("Cancle").child(dbbillid33.key()).remove()
                            #     print("billid1",billid2)
                                
                            #     print("delete order from cancle 1")
                            # else:
                            #     print("pending bill id not matched from Cancle 1")                           
                    #print("Pending single we can push to data base")
                    database.child("Data").child("Mis").child("Pending").push(Pending1)
                else:
                    for dict2 in Pending1:
                        billid22=dict2.get("bill_id")
                        a=True
                        if a:
                            dbbillid1= database.child("Data").child("Mis").child("Confirmed").get()
                            for dbbillid11 in dbbillid1.each():
                                dbbillid111=dbbillid11.val().get("bill_id")
                                if billid22==dbbillid111:
                                    database.child("Data").child("Mis").child("Confirmed").child(dbbillid11.key()).remove()
                                #     print("billid1 frm 2",billid22)
                                #     print("bill id matched")
                                #     print("dbbillid111 frm 2",dbbillid111)
                                #     print("delete order from confirm2")
                                # else:
                                #     print("Pending bill id not matched from confirmed2")
                        if a:            
                            dbbillid2= database.child("Data").child("Mis").child("Pending").get()
                            for dbbillid22 in dbbillid2.each():
                                dbbillid222=dbbillid22.val().get("bill_id")
                                if billid22==dbbillid222:
                                    database.child("Data").child("Mis").child("Pending").child(dbbillid22.key()).remove()
                                #     print("billid frm 2 in pending",billid22)
                                #     print("dbbillid222",dbbillid222)
                                #     print("delete order from pending 2")
                                # else:
                                #     print("Pending bill id not matched from pending 2")    
                                
                        if a: 
                            dbbillid3= database.child("Data").child("Mis").child("Cancle").get()
                            for dbbillid33 in dbbillid3.each():
                                dbbillid333=dbbillid33.val().get("bill_id")
                                #print("dbbillid333",dbbillid333)
                                if billid22==dbbillid333:
                                    database.child("Data").child("Mis").child("Cancle").child(dbbillid33.key()).remove()          
                        #print("Pending Multi: We can push confirmed frm 2",billid22)
                        database.child("Data").child("Mis").child("Pending").push(dict2)
            if Cancle == "":
                pass
            else:
                Cancle1 = eval(Cancle)
                if type(Cancle1) == dict:
                    print("confirm 1 is list")
                    billid3=Cancle1.get("bill_id")
                    print(billid3)
                    a=True
                    if a:
                        dbbillid1= database.child("Data").child("Mis").child("Confirmed").get()
                        for dbbillid11 in dbbillid1.each():
                            dbbillid111=dbbillid11.val().get("bill_id")
                            if billid3==dbbillid111:
                                database.child("Data").child("Mis").child("Confirmed").child(dbbillid11.key()).remove()
                    if a:            
                        dbbillid2= database.child("Data").child("Mis").child("Pending").get()
                        for dbbillid22 in dbbillid2.each():
                            dbbillid222=dbbillid22.val().get("bill_id")
                            if billid3==dbbillid222:
                                database.child("Data").child("Mis").child("Pending").child(dbbillid22.key()).remove() 
                    if a: 
                        dbbillid3= database.child("Data").child("Mis").child("Cancle").get()
                        for dbbillid33 in dbbillid3.each():
                            dbbillid333=dbbillid33.val().get("bill_id")
                            print("dbbillid333",dbbillid333)
                            if billid3==dbbillid333:
                                database.child("Data").child("Mis").child("Cancle").child(dbbillid33.key()).remove()
                    database.child("Data").child("Mis").child("Cancle").push(Cancle1)
                    
                
                else:
                    for dict3 in Cancle1:
                        billid33=dict3.get("bill_id")
                        a=True
                        if a:
                            dbbillid1= database.child("Data").child("Mis").child("Confirmed").get()
                            for dbbillid11 in dbbillid1.each():
                                dbbillid111=dbbillid11.val().get("bill_id")
                                if billid33==dbbillid111:
                                    database.child("Data").child("Mis").child("Confirmed").child(dbbillid11.key()).remove()
                        if a:            
                            dbbillid2= database.child("Data").child("Mis").child("Pending").get()
                            for dbbillid22 in dbbillid2.each():
                                dbbillid222=dbbillid22.val().get("bill_id")
                                if billid33==dbbillid222:
                                    database.child("Data").child("Mis").child("Pending").child(dbbillid22.key()).remove()
                        if a: 
                            dbbillid3= database.child("Data").child("Mis").child("Cancle").get()
                            for dbbillid33 in dbbillid3.each():
                                dbbillid333=dbbillid33.val().get("bill_id")
                                print("dbbillid333",dbbillid333)
                                if billid33==dbbillid333:
                                    database.child("Data").child("Mis").child("Cancle").child(dbbillid33.key()).remove()
                        database.child("Data").child("Mis").child("Confirmed").push(dict3)
                        
            if Delete == "":
                pass
            else:
                
                Delete1 = eval(Delete)  #seprate dict's from tuple
                if type(Delete1) == dict: #datatype checkout 
                    billid4=Delete1.get("bill_id")
                    a=True
                    if a:
                        dbbillid1= database.child("Data").child("Mis").child("Confirmed").get()
                        for dbbillid11 in dbbillid1.each():
                            dbbillid111=dbbillid11.val().get("bill_id")
                            if billid4==dbbillid111: 
                                database.child("Data").child("Mis").child("Confirmed").child(dbbillid11.key()).remove()        
                    if a:            
                        dbbillid2= database.child("Data").child("Mis").child("Pending").get()
                        for dbbillid22 in dbbillid2.each():
                            dbbillid222=dbbillid22.val().get("bill_id")
                            if billid4==dbbillid222:
                                database.child("Data").child("Mis").child("Pending").child(dbbillid22.key()).remove()
                    if a: 
                        dbbillid3= database.child("Data").child("Mis").child("Cancle").get()
                        for dbbillid33 in dbbillid3.each():
                            dbbillid333=dbbillid33.val().get("bill_id")
                            if billid4==dbbillid333:
                                database.child("Data").child("Mis").child("Cancle").child(dbbillid33.key()).remove()
                    
            
                else:
                    for dict4 in Delete1:
                        billid44=dict4.get("bill_id")
                        a=True
                        if a:
                            dbbillid1= database.child("Data").child("Mis").child("Confirmed").get()
                            for dbbillid11 in dbbillid1.each():
                                dbbillid111=dbbillid11.val().get("bill_id")
                                if billid44==dbbillid111:
                                    database.child("Data").child("Mis").child("Confirmed").child(dbbillid11.key()).remove()
                        if a:            
                            dbbillid2= database.child("Data").child("Mis").child("Pending").get()
                            for dbbillid22 in dbbillid2.each():
                                dbbillid222=dbbillid22.val().get("bill_id")
                                if billid44==dbbillid222:
                                    database.child("Data").child("Mis").child("Pending").child(dbbillid22.key()).remove()
                        if a: 
                            dbbillid3= database.child("Data").child("Mis").child("Cancle").get()
                            for dbbillid33 in dbbillid3.each():
                                dbbillid333=dbbillid33.val().get("bill_id")
                                if billid44==dbbillid333:
                                    database.child("Data").child("Mis").child("Cancle").child(dbbillid33.key()).remove()
                                    






            



    firebase = FirebaseApplication(
        "https://neemeesh-trial-default-rtdb.firebaseio.com/", None)
    admindata = list(firebase.get("/Data/BookingOrder/Orders", None).values())
    
    return render(request, "product_table.html", {'admindata': admindata})




def producttablestatus(request):

    
    


    firebase = FirebaseApplication(
        "https://neemeesh-trial-default-rtdb.firebaseio.com/", None)
    #admindata = list(firebase.get("/Data/BookingOrder/Orders", None).values())
    admindata11 = list(firebase.get("/Data/Mis/Confirmed", None).values())
    admindata22 = list(firebase.get("/Data/Mis/Pending", None).values())
    admindata33 = list(firebase.get("/Data/Mis/Cancle", None).values())
    # print("confirmed",admindata11)
    # print("pending",admindata22)
    # print("cancle",admindata33)

        
    
    
        


    
    bill_id = database.child("Data").child("BookingOrder").child("Orders").get()
    # print("from admindata2",admindata2)
    # print("typeis",type(admindata1))
    
    


    return render(request, "product_table2.html", {'admindata11':admindata11,'admindata22':admindata22,'admindata33':admindata33,'bill_id': bill_id})



def dispatchuser (request) :
    firebase=FirebaseApplication("https://neemeesh-trial-default-rtdb.firebaseio.com/", None)
    fromcity=list(firebase.get("/Data/BookingOrder/Orders",None).values())
    fromcitylist=[]
    for citydetails in fromcity:
        for eachcitykey,eachcityval in citydetails.items():
            if eachcitykey=='fromcity':
                if eachcityval not in fromcitylist:
                    fromcitylist.append(eachcityval)
    
    
    return render (request , "lh3.html" , {"fromcitylist" : fromcitylist})

def dispatchuser1 (request) :
    
    return render (request , "dispatchuser.html" )

# def postdispatchuser (request) :
#     date1 = request.POST.get("date1")
#     date2 = request.POST.get("date2")
#     userid1 = request.POST.get("hiddenuserid")
#     firebase1=FirebaseApplication("https://neemeesh-trial-default-rtdb.firebaseio.com/", None)
#     dates = list(firebase1.get("Data/BookingOrder/Orders" , None).values())
#     orderdates=[]
#     for i in dates :
#         for datename,dateval in i.items() : 
#             if datename == "date" :
#                 orderdates.append(dateval)

                
#     fromcity = request.POST.get("cityname")
#     booking_db1 = database.child("Data").child("BookingOrder").child("Orders").get()
#     list1=[]
#     temp=[]
#     billid =[]
#     for x in orderdates :
#         if(x>=date1 and x<=date2) :
#             for bookingdb in booking_db1.each() :
#                 bill_id=database.child("Data").child("BookingOrder").child("Orders").child(bookingdb.key()).child("bill_id").get().val()
#                 if (bookingdb.val()["fromcity"] == fromcity and bookingdb.val()["date"] == x and bill_id not in temp) :   
#                         list1=list1+[{"bill_id": database.child("Data").child("BookingOrder").child("Orders").child(bookingdb.key()).child("bill_id").get().val(),
#                                      'from_city' : database.child("Data").child("BookingOrder").child("Orders").child(bookingdb.key()).child("fromcity").get().val(),
#                                      'companyname12' :database.child("Data").child("BookingOrder").child("Orders").child(bookingdb.key()).child("company_name").get().val(),
#                                      'datee' : database.child("Data").child("BookingOrder").child("Orders").child(bookingdb.key()).child("date").get().val(),
#                                      'destination' : database.child("Data").child("BookingOrder").child("Orders").child(bookingdb.key()).child("destination").get().val(),
#                                      'partyname' : database.child("Data").child("BookingOrder").child("Orders").child(bookingdb.key()).child("partyname").get().val(),
#                                      'invcno' : database.child("Data").child("BookingOrder").child("Orders").child(bookingdb.key()).child("invcno").get().val()
#                                      }]
#                         temp.append(bill_id)
#                         billid.append(bill_id)
#     return render (request , "dispatchuser.html", {'list1' : list1 , "temp" : temp , "hiddenuserid1":userid1})

def postdispatchuser (request) :
    fromcity = request.POST.get("cityname")
    destination = request.POST.get("destination")
    booking_db1 = database.child("Data").child("BookingOrder").child("Orders").get()
    list1=[]
    temp=[]
    billid =[]
    for bookingdb in booking_db1.each() :
                bill_id=database.child("Data").child("BookingOrder").child("Orders").child(bookingdb.key()).child("bill_id").get().val()
                if (bookingdb.val()["fromcity"] == fromcity and bookingdb.val()["destination"] == destination and bill_id  not in temp) :   
                        list1=list1+[{"bill_id": database.child("Data").child("BookingOrder").child("Orders").child(bookingdb.key()).child("bill_id").get().val(),
                                     'from_city' : database.child("Data").child("BookingOrder").child("Orders").child(bookingdb.key()).child("fromcity").get().val(),
                                     'companyname12' :database.child("Data").child("BookingOrder").child("Orders").child(bookingdb.key()).child("company_name").get().val(),
                                     'datee' : database.child("Data").child("BookingOrder").child("Orders").child(bookingdb.key()).child("date").get().val(),
                                     'destination' : database.child("Data").child("BookingOrder").child("Orders").child(bookingdb.key()).child("destination").get().val(),
                                     'partyname' : database.child("Data").child("BookingOrder").child("Orders").child(bookingdb.key()).child("partyname").get().val(),
                                     'invcno' : database.child("Data").child("BookingOrder").child("Orders").child(bookingdb.key()).child("invcno").get().val()
                                     }]
                        temp.append(bill_id)
                        billid.append(bill_id)
    return render (request , "dispatchuser.html", {'list1' : list1 , "temp" : temp ,"destination" :destination
    })

def confirmdispatch(request):  
   
    destination=request.POST.get("destination")
    bill_id=request.POST.get("bill_id" , None)
    userid2=request.POST.get("hiddenuserid2")
    firebase=FirebaseApplication("https://neemeesh-trial-default-rtdb.firebaseio.com/", None)
    courierusers=list(firebase.get("/Data/Signup/Courier",None).values())
    courieruser=[]
    couriernames=[]
    # for courierdetails in courierusers:
    #     for eachcompkey,eachcompval in courierdetails.items():
    #         if eachcompkey=='City' and eachcompval == destination :
              
    #                 courieruser.append(courierdetails.items())
    for courierdetails in courierusers:
        for eachcompkey,eachcompval in courierdetails.items():
            if eachcompkey=='City' and eachcompval == destination :
              
                courieruser.append(courierdetails)
           
           
    for couriername in courieruser:
        couriernames.append(couriername['Name1'])

    print(couriernames)
    print(destination)   
         
    return render (request , "confirmdispatch.html",{"bill_id":bill_id , "userid2":userid2, "couriernames":couriernames})



def postconfirmdispatch (request) :
    courier = request.POST.get("courier")  
    bill_id = request.POST.get("bill_id")
    userid = request.POST.get("hiddenuserid3")
    dbdispatch = database.child("Data").child("BookingOrder").child("Orders").get()
    
    for pcdispatch in dbdispatch.each() :
        if pcdispatch.val()["bill_id"] == bill_id : 
            fromcity = database.child("Data").child("BookingOrder").child("Orders").child(pcdispatch.key()).child("fromcity").get().val()
            companyname12=database.child("Data").child("BookingOrder").child("Orders").child(pcdispatch.key()).child("company_name").get().val()
            datee = database.child("Data").child("BookingOrder").child("Orders").child(pcdispatch.key()).child("date").get().val()
            destination = database.child("Data").child("BookingOrder").child("Orders").child(pcdispatch.key()).child("destination").get().val()
            partyname = database.child("Data").child("BookingOrder").child("Orders").child(pcdispatch.key()).child("partyname").get().val()
            invcno = database.child("Data").child("BookingOrder").child("Orders").child(pcdispatch.key()).child("invcno").get().val()
            data = {
                "courier":courier,
                "Bill Id":bill_id,
                "fromcity" : fromcity ,
                "company_name" : companyname12 ,
                "date" : datee ,
                "destination" : destination ,
                "partyname" : partyname ,
                "invcno" : invcno,
                "User Confirmed Order": userid
                }
            print(data)    
            database.child("Data").child("ConfirmedOrders").child("OrderDetails").child(userid).push(data)
           

    for deletedispatch in dbdispatch.each():
        if deletedispatch.val()['bill_id'] == bill_id :
            database.child("Data").child("BookingOrder").child("Orders").child(deletedispatch.key()).remove()
        firebase=FirebaseApplication("https://neemeesh-trial-default-rtdb.firebaseio.com/", None)
    fromcity=list(firebase.get("/Data/BookingOrder/Orders",None).values())
    fromcitylist=[]
    for citydetails in fromcity:
        for eachcitykey,eachcityval in citydetails.items():
            if eachcitykey=='fromcity':
                if eachcityval not in fromcitylist:
                    fromcitylist.append(eachcityval)
    msg = "Your Dispatch Confirmed !! Message has been sent to Admin !!"
    return render (request ,"lh3.html", {"msg" : msg ,"fromcitylist" : fromcitylist , "user_id":userid})

def viewdispatchorders (request) : 
    user_id12 = request.POST.get("hiddenuserid12")
    
    confirmedorders12 = []
    dispatchinfo = database.child("Data").child("ConfirmedOrders").child("OrderDetails").child(user_id12).get()
    for i in dispatchinfo.each() :
        i.val().pop('User Confirmed Order')
        confirmedorders12.append(i.val())

    return render (request ,"viewdispatchuser.html" , {"user_id" : user_id12 ,"COlist": confirmedorders12})


def postviewdispatchuser (request) :
    bill_id=request.POST.get('bill_id')
    user_id12 = request.POST.get("hiddenuserid5")
    postdispatchinfo = database.child("Data").child("ConfirmedOrders").child("OrderDetails").child(user_id12).get()
    for i in postdispatchinfo.each():

        if i.val()['Bill Id']==bill_id :
            i.val().pop('User Confirmed Order') 
            dispatchdate=i.val()['date']
            dispatchfromcity=i.val()['fromcity']
            dispatchbillid =i.val()['Bill Id']
    context = {
    "dispatchdate":dispatchdate ,
    "dispatchfromcity":dispatchfromcity,
    "user_id":user_id12,
    "dispatchbillid":dispatchbillid
    }
    return render (request , "postviewdispatchuser.html",context)     

def ordersconfirmedbydispatch(request):
    user_id=request.POST.get('hiddenbookinguserid')
    bill_id_dispatch = request.POST.get('bill_id_dispatch')
    fromcity_dispatch = request.POST.get('fromcity_dispatch')
    date_dispatch  = request.POST.get('date_dispatch')
    # receiver data 
    fromcity_booking = request.POST.get('fromcity_booking')
    date_booking  = request.POST.get('date_booking')
     
    #pushing data 

    data= {
        "bill_id_dispatch":bill_id_dispatch,
        "fromcity_dispatch":fromcity_dispatch,
        "date_dispatch":date_dispatch,
        "fromcity_booking":fromcity_booking,
        "date_booking":date_booking
    }
    database.child("Data").child("dispatchedorders").child(user_id).push(data)
    
    from twilio.rest import Client

    # Your Account SID from twilio.com/console
    account_sid = "ACa146b54a52c221a9a0b309438c3171c5"
    # Your Auth Token from twilio.com/console
    auth_token  = "5923edfc1be640f998dc9a3d237294a7"

    client = Client(account_sid, auth_token)
     
    message = client.messages.create(
        to="+917588069659", 
        from_="+16308844509",
        body="Your Order has been Dispatched ,\n having Bill ID(Note this Bill id for Future Use):"+bill_id_dispatch+"\n"+"Dispatched From:"+fromcity_dispatch+"\n"+"Dispatching Date:"+date_dispatch+"\n"+"Your Order is Arriving on:"+date_booking+"\n Your Order is arriving at the location:"+fromcity_booking+"\nas Booked by you")

    print(message.sid)
    msg = " Order Dispatched Successfully !!"
    return render (request , "lh3.html" ,{"user_id":user_id})