def login(request):
    return render(request,"loginindex.html")


def login_post(request):
    username=request.POST['textfield']
    password=request.POST['textfield2']
    lobj=Login.objects.filter(username=username,password=password)
    if lobj.exists():
        lobj2=Login.objects.get(username=username,password=password)
        request.session['lid']=lobj2.id
        if lobj2.type=='admin':
            return redirect('/myapp/adminhome/')
            # return HttpResponse("<script>alert('login ok');window.location='/myapp/adminhome/'</script>")
        elif lobj2.type=='user':
            return redirect('/myapp/userhome/')
            # return HttpResponse("<script>alert('login ok');window.location='/myapp/userhome/'</script>")
        else:
            return HttpResponse("<script>alert('invalid username & password'));window.location='/myapp/login/'</script>")
    else:
        return HttpResponse('''<script>alert('user not found');window.location="/myapp/login/"</script>''')


def add_profile(request):
    return render(request,"admin/ADDPROFILE.html")

def addprofile_post(request):
    name = request.POST['textfield']
    email = request.POST['textfield2']
    phone = request.POST['textfield3']
    place = request.POST['textfield4']
    post = request.POST['textfield5']
    pin = request.POST['textfield6']
    dist = request.POST['textfield7']
    photo = request.FILES.get('image')  # Use get to avoid KeyError

    # Check if an Adminprofile with the same email or phone already exists
    if Adminprofile.objects.filter(email=email).exists() or Adminprofile.objects.filter(phone=phone).exists():
        return HttpResponse('''<script>alert('Already Exists');window.location="/myapp/adminhome/"</script>''')

    else:
        obj = Adminprofile()

        if photo:
            fs = FileSystemStorage()
            date = datetime.now().strftime('%Y%m%d-%H%M%S') + ".jpg"
            fs.save(date, photo)
            path = fs.url(date)
            obj.photo = path

        obj.name = name
        obj.email = email
        obj.phone = phone
        obj.place = place
        obj.post = post
        obj.pin = pin
        obj.dist = dist
        obj.save()

        return HttpResponse('''<script>alert('Successfully added');window.location="/myapp/adminhome/"</script>''')
def editprofile(request,id):
    data = Adminprofile.objects.get(id=id)
    return render(request, "admin/EDITPROFILE.html", {'data': data})

def editprofile_post(request):
    id=request.POST['id']
    name = request.POST['textfield']
    email = request.POST['textfield2']
    phone = request.POST['textfield3']
    place = request.POST['textfield4']
    post = request.POST['textfield5']
    pin = request.POST['textfield6']
    dist = request.POST['textfield7']
    photo = request.FILES.get('image')

    # Check if an Adminprofile with the same email or phone already exists
    # if Adminprofile.objects.filter(email=email).exists() or Adminprofile.objects.filter(phone=phone).exists():
    #     return HttpResponse('''<script>alert('Already Exists');window.location="/myapp/adminhome/"</script>''')

    # else:
    obj = Adminprofile.objects.get(id=id)

    if photo:
        fs = FileSystemStorage()
        date = datetime.now().strftime('%Y%m%d-%H%M%S') + ".jpg"
        fs.save(date, photo)
        path = fs.url(date)
        obj.photo = path

    obj.name = name
    obj.email = email
    obj.phone = phone
    obj.place = place
    obj.post = post
    obj.pin = pin
    obj.dist = dist
    obj.save()

    return HttpResponse('''<script>alert('Successfully edited');window.location="/myapp/view_profile/"</script>''')


def view_profile(request):
    data = Adminprofile.objects.all()
    return render(request,"admin/VIEWPOFILE.html",{'data': data})



def add_product(request):
    return render(request,"admin/addproduct.html")

def addproduct_post(request):
    productname=request.POST['textfield2']
    price=request.POST['textfield']
    photo1=request.FILES['fileField']
    photo2=request.FILES['fileField2']
    date=datetime.now().strftime('%Y%m%d-%H%M%S')+"1.jpg"
    fs=FileSystemStorage()
    fs.save(date, photo1)
    photopath = fs.url(date)

    date2 = datetime.now().strftime('%Y%m%d-%H%M%S') + "2.jpg"
    fs2 = FileSystemStorage()
    fs2.save(date2, photo2)
    photopath2 = fs2.url(date2)

    obj=Product()
    obj.productname=productname
    obj.price=price
    obj.photo1=photopath
    obj.photo2=photopath2
    obj.save()

    return HttpResponse('''<script>alert('Successfull');window.location="/myapp/add_product"</script>''')

def edit_product(request,id):
    res = Product.objects.get(id=id)
    return render(request,'admin/Edit Product.html',{'data':res})

def edit_product_post(request):

    id = request.POST['ids']
    productname = request.POST['textfield2']
    price = request.POST['textfield']
    photo1 = request.FILES['fileField']
    photo2 = request.FILES['fileField2']

    res = Product.objects.get(id=id)

    res.productname = productname
    res.price = price

    res.photo1 = photo1
    if 'fileField' in request.FILES:
        photo1 = request.FILES['fileField']
        fs = FileSystemStorage()
        date = datetime.now().strftime("%Y%m%d%H%M%S" + "1.jpg")
        fn = fs.save(date, photo1)
        path = fs.url(date)
        res.photo1=path
    res.save()

    res.photo2 = photo2
    if 'fileField2' in request.FILES:
        photo2 = request.FILES['fileField2']
        fs = FileSystemStorage()
        date = datetime.now().strftime("%Y%m%d%H%M%S" + "2.jpg")
        fn = fs.save(date, photo2)
        path = fs.url(date)
        res.photo2=path
    res.save()

    return HttpResponse('''<script>alert('Edited Successfully');window.location='/myapp/view_product/'</script>''')

def search_product(request):
    SEARCH=request.POST['textfield']
    data=Product.objects.filter(productname__icontains=SEARCH)
    return render(request,"admin/VIEWPRODUCT.html",{'data':data})


def view_product(request):

    data=Product.objects.all()
    return render(request,"admin/VIEWPRODUCT.html",{'data':data})

def delete_product(request,id):
    Product.objects.get(id=id).delete()
    return HttpResponse('''<script>alert('Deleted Successfully');window.location='/myapp/view_product/'</script>''')

def view_product_user(request):
    res=Product.objects.all()
    return render(request,"user/USERVIEWPRODUCT.html",{'data':res})



def viewproduct_post(request):
    search=request.POST['textfield']
    res = Product.objects.filter(productname__icontains=search)
    return render(request, "user/USERVIEWPRODUCT.html", {'data': res})


def update_product(request):
    return render(request,"admin/UPDATEPRODUCT.html")

def updateproduct_post(request):
    productname=request.POST['textfield2']
    price=request.POST['textfield']
    photo1=request.FILES['fileField']
    photo2=request.FILES['fileField2']
    return HttpResponse('''<script>alert('Successfull');window.location="/myapp/"</script>''')

def view_order(request):
    data = Order.objects.all()
    return render(request,"admin/vieworder.html",{'data':data})

def view_order_post(request):
    fd = request.POST['textfield']
    td = request.POST['textfield2']

    data=Order.objects.filter(date__range=[fd,td])
    return render(request,"admin/vieworder.html",{'data':data})

def approved_order(request,id):
    res = Order.objects.filter(id=id).update(status="approved",paystatus='approved')

    return HttpResponse('''<script>alert('Successfull');window.location="/myapp/adminhome/"</script>''')

def reject_order(request,id):
    res = Order.objects.filter(id=id).update(status="rejected",paystatus='rejected')
    return HttpResponse('''<script>alert('Successfull');window.location="/myapp/adminhome/"</script>''')
def approved_cust(request,id):
    res = customisationrequest.objects.filter(id=id).update(status="approved")

    return HttpResponse('''<script>alert('Successfull');window.location="/myapp/adminhome/"</script>''')


def addamount(request, id):
    return render(request, 'admin/Add Amount.html', {'id': id})


def addamount_post(request):
    amount = request.POST['textfield']
    id = request.POST['id']
    res = customisationrequest.objects.filter(id=id).update(amount=amount,status='approved')
    return HttpResponse('''<script>alert('Successfull');window.location="/myapp/adminhome/"</script>''')


def reject_cust(request,id):
    res = customisationrequest.objects.filter(id=id).update(status="rejected")
    return HttpResponse('''<script>alert('Successfull');window.location="/myapp/adminhome/"</script>''')

def view_complaint(request):
    res=Complaint.objects.all()
    return render(request,"admin/VIEWCOMPLAINT.html",{"data":res})

def viewcomplaint_post(request):
    fromdate=request.POST['textfield']
    to=request.POST['textfield2']
    res = Complaint.objects.filter(date__range=[fromdate,to])
    return render(request,"admin/VIEWCOMPLAINT.html",{"data":res})


def send_reply(request,id):
    return render(request,"admin/SENDREPLY.html",{'id':id})

def sendreply_post(request):
    reply=request.POST['textfield']
    id=request.POST['id']

    res = Complaint.objects.get(id=id)
    res.status="replied"
    res.reply=reply
    res.save()
    return HttpResponse('''<script>alert('Successfull');window.location="/myapp/viewcomplaint_admin/"</script>''')


def view_customisationrequest(request):
    res=customisationrequest.objects.filter(status="pending")
    return render(request,"admin/viewcustomisationrequest.html",{"data":res})

def viewcustomisationrequest_post(request):
    fromdate=request.POST['textfield']
    todate=request.POST['textfield2']
    res = customisationrequest.objects.filter(status="pending",date__range=[fromdate,todate])
    return render(request, "admin/viewcustomisationrequest.html", {"data": res})


def view_approvedcustomisationrequest(request):
    res = customisationrequest.objects.filter(status="approved")
    return render(request,"admin/viewapprovedcustomisationrequest.html",{"data":res})

def viewapprovedcustomisationrequest_post(request):
    fromdate=request.POST['textfield']
    todate=request.POST['textfield2']
    obj=customisationrequest.objects.filter(date__range=[fromdate,todate],status='approved')
    return render(request, "admin/viewapprovedcustomisationrequest.html",{"data":obj})

def view_rejectedcustomisationrequest(request):
    res = customisationrequest.objects.filter(status="rejected")
    return render(request,"admin/viewrejectedcustomisationrequest.html",{"data":res})

def viewrejectedcustomisationrequest_post(request):
    fromdate=request.POST['textfield']
    todate=request.POST['textfield2']
    res = customisationrequest.objects.filter(date__range=[fromdate,todate],status='rejected')
    return render(request, "admin/viewrejectedcustomisationrequest.html",{"data":res})


def change_password(request):
    return render(request,"admin/CHANGEPASSWORD.html")

def changepassword_post(request):
    currentpassword=request.POST['textfield']
    newpassword=request.POST['textfield2']
    confirmpassword=request.POST['textfield3']
    res=Login.objects.filter(id=request.session['lid'],password=currentpassword)
    if res.exists():
        res2=Login.objects.get(id=request.session['lid'],password=currentpassword)
        if newpassword==confirmpassword:
            res3=Login.objects.filter(id=request.session['lid']).update(password=confirmpassword)
            return HttpResponse('''<script>alert('Changepassword Successfull');window.location="/myapp/login/"</script>''')
        else:
            return HttpResponse('''<script>alert('password mismatch');window.location="/myapp/change_password/"</script>''')
    else:
        return HttpResponse('''<script>alert('please check your current password');window.location="/myapp/change_password/"</script>''')


def view_registereduser(request):
    res=User.objects.all()
    return render(request,"admin/VIEWREGISTEREDUSER.html",{"data":res})

def view_payment(request):
    res=Payment.objects.all()
    return render(request,"admin/VIEWPAYMENT.html",{"data":res})

def view_review(request):
    data = Review.objects.all()
    return render(request,"admin/VIEWREVIEW.html",{'data':data})

def viewreview_post(request):
    fromdate=request.POST['textfield']
    to=request.POST['textfield2']
    data = Review.objects.filter(date__range=[fromdate,to])
    return render(request, "admin/VIEWREVIEW.html", {'data': data})


def adminhome(request):
    return render(request, 'admin/new_index.html')
    # return render(request, "admin/adminhome.html")


###################################################################################

def addorder(request,id):

    # p = Product.objects.all()
    return render(request,"user/ADDORDER.html",{'id':id})

def addorder_post(request,id):
    # ID = request.POST['id']
    OrdObj = Order()
    OrdObj.PRODUCT_id = id
    OrdObj.date = datetime.now()
    OrdObj.date2= datetime.now()+timedelta(days=7)
    OrdObj.status = 'pending'
    OrdObj.USER = User.objects.get(LOGIN_id=request.session['lid'])
    OrdObj.paystatus='pending'
    OrdObj.save()
    return HttpResponse('''<script>alert('Addorder Successfull');window.location='/myapp/userhome/'</script>''')

def u_changepassword(request):
    return render(request,"user/CHANGEPASSWORD.html")


def u_changepassword_post(request):
    currentpassword=request.POST['textfield2']
    newpassword=request.POST['textfield']
    confirmpassword=request.POST['textfield3']
    res = Login.objects.filter(id=request.session['lid'], password=currentpassword)
    if res.exists():
        res2 = Login.objects.get(id=request.session['lid'], password=currentpassword)
        if newpassword == confirmpassword:
            res3 = Login.objects.filter(id=request.session['lid']).update(password=confirmpassword)
            return HttpResponse(
                '''<script>alert('Changepassword Successfull');window.location="/myapp/login/"</script>''')
        else:
            return HttpResponse(
                '''<script>alert('password mismatch');window.location="/myapp/u_changepassword/"</script>''')
    else:
        return HttpResponse(
            '''<script>alert('please check your current password');window.location="/myapp/u_changepassword/"</script>''')



def edit_order(request):
    return render(request,"user/EDITORDER.html")

def editorder_post(request):
    housename=request.POST['textfield']
    place=request.POST['textfield2']
    post=request.POST['textfield3']
    pin=request.POST['textfield4']
    dist=request.POST['textfield5']
    return HttpResponse('''<script>alert('Successfull');window.location="/myapp/"</script>''')


def forgetpassword(request):
    return render(request,"user/FORGETPASSWORD.html")

def forgetpassword_post(request):
    email=request.POST['textfield']
    return HttpResponse('''<script>alert('Successfull');window.location="/myapp/"</script>''')

def reg(request):
    return render(request,"user/signupindex.html")

def reg_post(request):
    name=request.POST['textfield']
    phoneno=request.POST['textfield2']
    email=request.POST['textfield3']
    home=request.POST['textfield4']
    place=request.POST['textfield5']
    post=request.POST['textfield6']
    pin=request.POST['textfield7']
    dist=request.POST['textfield8']
    password=request.POST['textfield9']
    confirmpassword=request.POST['textfield10']

    o = Login.objects.filter(username=email)
    oo = User.objects.filter(phoneno=phoneno)

    if o.exists():
        return HttpResponse('''<script>alert('email already exist');window.location="/myapp/reg/"</script>''')
    elif oo.exists():
        return HttpResponse('''<script>alert('phone number already exist');window.location="/myapp/reg/"</script>''')


    lobj = Login()
    lobj.username=email
    lobj.password=password
    lobj.type='user'
    lobj.save()

    if password==confirmpassword:
        obj=User()
        obj.name=name
        obj.phoneno=phoneno
        obj.email=email
        obj.houseno=home
        obj.place=place
        obj.post=post
        obj.pin=pin
        obj.dist=dist
        obj.LOGIN=lobj
        obj.save()
        return HttpResponse('''<script>alert('Reg Successfull');window.location="/myapp/login/"</script>''')
    else:
        return HttpResponse('''<script>alert('password must be same');window.location="/myapp/"</script>''')


def reviewview(request):
    data = Review.objects.all()
    return render(request,"user/REVIEWVIEW.html",{'data':data})


def sendcomplaint(request):
    return render(request,"user/SENDCOMPLAINT.html")

def sendcomplaint_post(request):
    complaint=request.POST['textfield']
    obj=Complaint()
    obj.complaint=complaint
    obj.reply='pending'
    obj.status='pending'
    obj.date=datetime.now().date()
    obj.USER=User.objects.get(LOGIN_id=request.session['lid'])
    obj.save()
    return HttpResponse('''<script>alert('Successfull');window.location="/myapp/userhome/"</script>''')



def viewcomplaint_admin(request):
    data=Complaint.objects.all()
    return render(request,"admin/VIEWCOMPLAINT.html",{'data':data})

# def Send_replay(request):
#     replay=request.POST['replay']


def sendreview(request,id):
    da=Product.objects.get(id=id)

    return render(request,"user/SENDREVIEW.html",{'pid':da.id})

def sendreview_post(request):
    print(request.POST)
    sid=request.POST['id']
    review=request.POST['textfield']
    rating=request.POST['textfield2']

    try:
        x=User.objects.get(LOGIN=request.session["lid"])
        print(x.id,"---------------------------")
        ob=Review()
        ob.date=datetime.now().date()
        ob.review=review
        ob.rating=rating
        ob.USER_id=x.id
        ob.PRODUCT_id=sid
        ob.save()
    except :
        print("----")
    return HttpResponse("<script>alert('success');window.location='/myapp/view_product_user/'</script>")


def updateprofile(request):
    data=User.objects.get(LOGIN_id=request.session['lid'])
    return render(request,"user/UPDATE PROFILE.html",{'data':data})

def updateprofile_post(request):
    name=request.POST['textfield']
    phoneno=request.POST['textfield2']
    email=request.POST['textfield3']
    home=request.POST['textfield4']
    place=request.POST['textfield5']
    post=request.POST['textfield6']
    pin=request.POST['textfield7']
    dist=request.POST['textfield8']

    lobj = Login.objects.get(id=request.session['lid'])
    lobj.username = name
    lobj.save()


    obj = User.objects.get(LOGIN_id=request.session['lid'])
    obj.name = name
    obj.phoneno = phoneno
    obj.email = email
    obj.houseno = home
    obj.place = place
    obj.post = post
    obj.pin = pin
    obj.dist = dist

    obj.save()
    return HttpResponse('''<script>alert('update profile successfull');window.location="/myapp/viewprofile/"</script>''')

def logout(request):
    request.session['lid']=''
    return redirect('/myapp/login/')



def userviewproduct(request):
    return render(request,"user/USERVIEWPRODUCT.html")

def userviewproduct_post(request):
    search=request.POST['textfield']
    return HttpResponse('''<script>alert('update profile successfull');window.location="/myapp/"</script>''')

def vieworder(request):
    data = Order.objects.all()
    return render(request,"user/VIEWORDER.html",{'data':data})

def vieworderstatus(request):
    data = Order.objects.filter(USER__LOGIN_id=request.session['lid'])
    return render(request,"user/VIEWORDERSTATUS.html",{'data':data})

def customizedviewstatus(request):
    data = customisationrequest.objects.filter(USER__LOGIN_id=request.session['lid'])
    return render(request, "user/customizedrequest.html", {'data': data})


def viewprofile(request):
    obj=User.objects.get(LOGIN_id=request.session['lid'])
    return render(request,"user/VIEWPROFILE.html",{"data":obj})

def viewreply(request):
    data=Complaint.objects.filter(USER__LOGIN_id=request.session['lid'])
    return render(request,"user/VIEWREPLY.html",{'data':data})

def viewreview(request,id):
    data = Review.objects.filter(PRODUCT_id=id)
    request.session['pid']=id
    # data = Review.objects.filter(USER__LOGIN_id = request.session['lid'])
    return render(request,"user/VIEWREVIEW.html",{'data': data})

def user_viewreview_post(request):
    fromdate=request.POST['textfield']
    todate=request.POST['textfield2']
    data = Review.objects.filter(PRODUCT_id=request.session['pid'],date__range=[fromdate,todate])
    return render(request, "user/VIEWREVIEW.html", {'data': data})

def userviewcustomization(request):
    res=customisationrequest.objects.filter(USER__LOGIN_id=request.session['lid'])
    return render(request,"user/userviewcustomization.html",{'data':res})

def userviewcustomization_post(request):
    fromdate=request.POST['textfield']
    todate=request.POST['textfield2']
    obj=customisationrequest.objects.filter(date__range=[fromdate,todate])
    return render(request, "user/userviewcustomization.html", {'data': obj})


def userhome(request):
    return render(request, "user/new_index.html")

def SendCustomizationRequest(request,id):
    return render(request, "user/SendCustomizationRequest.html",{"id":id})

def SendCustomizationRequest_post(request):
    Description=request.POST['textfield']
    Reference=request.FILES['file']
    id=request.POST['id']
    fs = FileSystemStorage()
    date = datetime.now().strftime("%Y%m%d%H%M%S" + "2.jpg")
    fn = fs.save(date, Reference)
    path = fs.url(date)
    obj=customisationrequest()
    obj.date=datetime.now().date()
    obj.USER=User.objects.get(LOGIN_id=request.session['lid'])
    obj.description=Description
    obj.PRODUCT_id=id
    obj.reference=path
    obj.status="pending"
    obj.save()
    return HttpResponse('''<script>alert('successfull');window.location="/myapp/view_product_user/"</script>''')




def raz_pay(request,amount,id):
    import razorpay
    razorpay_api_key = "rzp_test_MJOAVy77oMVaYv"
    razorpay_secret_key = "MvUZ03MPzLq3lkvMneYECQsk"

    razorpay_client = razorpay.Client(auth=(razorpay_api_key, razorpay_secret_key))

    # amount = 200
    amounts= float(amount)*100

    # Create a Razorpay order (you need to implement this based on your logic)
    order_data = {
        'amount': amounts,
        'currency': 'INR',
        'receipt': 'order_rcptid_11',
        'payment_capture': '1',  # Auto-capture payment
    }

    # Create an order
    order = razorpay_client.order.create(data=order_data)

    context = {
        'razorpay_api_key': razorpay_api_key,
        'amount': order_data['amount'],
        'currency': order_data['currency'],
        'order_id': order['id'],
    }

    obj = Payment()
    obj.ORDER_id = id
    obj.date = datetime.now().strftime('%Y-%m-%d')
    obj.amount = float(amount)


    obj.status = 'paid'
    obj.USER=User.objects.get(LOGIN=request.session['lid'])
    obj.save()
    Order.objects.filter(id=id).update(paystatus='paid')



    ss=Order.objects.get(id=id)
    ss.date2=  ss.date2 +timedelta(days=7
                                   )

    return render(request, 'USER/payment.html',{ 'razorpay_api_key': razorpay_api_key,
        'amount': order_data['amount'],
        'currency': order_data['currency'],
        'order_id': order['id'],"id":id})




def raz_pay2(request,amount,id):
    import razorpay
    razorpay_api_key = "rzp_test_MJOAVy77oMVaYv"
    razorpay_secret_key = "MvUZ03MPzLq3lkvMneYECQsk"

    razorpay_client = razorpay.Client(auth=(razorpay_api_key, razorpay_secret_key))

    # amount = 200
    amounts= float(amount)*100

    # Create a Razorpay order (you need to implement this based on your logic)
    order_data = {
        'amount': amounts,
        'currency': 'INR',
        'receipt': 'order_rcptid_11',
        'payment_capture': '1',  # Auto-capture payment
    }

    # Create an order
    order = razorpay_client.order.create(data=order_data)

    context = {
        'razorpay_api_key': razorpay_api_key,
        'amount': order_data['amount'],
        'currency': order_data['currency'],
        'order_id': order['id'],
    }

    obj = CustomPayment()
    obj.CUSTOMREQUEST_id = id
    obj.date = datetime.now().strftime('%Y-%m-%d')
    obj.amount = float(amount)
    obj.status = 'paid'
    obj.USER=User.objects.get(LOGIN=request.session['lid'])
    obj.save()

    customisationrequest.objects.filter(id=id).update(paystatus='paid')

    return render(request, 'USER/payment.html',{ 'razorpay_api_key': razorpay_api_key,
        'amount': order_data['amount'],
        'currency': order_data['currency'],
        'order_id': order['id'],"id":id})
