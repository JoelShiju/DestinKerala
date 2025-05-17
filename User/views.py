from django.shortcuts import render,redirect
from Guest.models import *
from Admin.models import *
from TravelAgency.models import *
from User.models import *
from datetime import date
from django.http import JsonResponse
# Create your views here.
def homepage(request):
    if "uid" in request.session:
        return render(request, 'User/Homepage.html')
    else:
        return redirect("Guest:login")
    
def search(request):
    if "uid" in request.session:
        dis= tbl_district.objects.all()
        loc=tbl_location.objects.all()
        return render(request, 'User/Search.html'  ,{'loc':loc,'dis':dis})
    else:
        return redirect("Guest:login")


def myprofile(request):
    if "uid" in request.session:
        user=tbl_user.objects.get(id=request.session['uid'])
        return render(request, 'User/MyProfile.html', {'user':user})
    else:
        return redirect("Guest:login")

def editprofile(request):
    if "uid" in request.session:
        user=tbl_user.objects.get(id=request.session['uid'])   
        if request.method == "POST":
            user.user_name= request.POST.get("txtname")
            user.user_email= request.POST.get("txtemail")
            user.user_contact= request.POST.get("txtcontact")
            user.save()
            return render(request, 'User/EditProfile.html',{"msg":"Profile Updated"}) 
        return render(request, 'User/EditProfile.html', {'user':user})
    else:
        return redirect("Guest:login")

def changepassword(request):
    if "uid" in request.session:
        user=tbl_user.objects.get(id=request.session['uid'])
        if request.method == 'POST':
            oldpassword = request.POST.get("txtoldpassword")
            newpassword = request.POST.get("txtnewpassword")
            conformpassword = request.POST.get("txtconformnewpassword")
            if oldpassword == user.user_password:
                if newpassword == conformpassword:
                    user.user_password = request.POST.get("txtnewpassword")
                    user.save()
                    return render(request, 'User/ChangePassword.html',{"msg":"Password Changed"})
                else:
                    return render(request, 'User/ChangePassword.html', {"msg": " New Password does not match"})
            else:
                return render(request, 'User/ChangePassword.html', {"msg": " Old Password does not  match"})
        else:
            return render(request, 'User/ChangePassword.html')
    else:
        return redirect("Guest:login")
    
def viewagencies(request):
    if "uid" in request.session:
        user=tbl_user.objects.get(id=request.session['uid'])
        agency=tbl_travelagency.objects.filter(agency_status=1)
        return render(request, 'User/ViewAgencies.html',{'agency':agency})
    else:
        return redirect("Guest:login")
def ajaxsearch(request):
    name=request.GET.get("name")
    agency=tbl_travelagency.objects.filter(agency_name__istartswith=name,agency_status=1)
    return render(request, 'User/AjaxSearch.html',{'agency':agency})


def viewpackages(request,id):
    user=tbl_user.objects.get(id=request.session['uid'])
    package=tbl_package.objects.filter(agency=id)
    return render(request, 'User/ViewPackages.html',{'package':package})

def complaint(request,aid):
    user=tbl_user.objects.get(id=request.session['uid'])
    complaint=tbl_complaint.objects.filter(user_id=user.id, agency_id=aid, complaint_status=0)
    complaint1=tbl_complaint.objects.filter(user_id=user.id, agency_id=aid, complaint_status=1)
    if request.method ==  "POST":
        tbl_complaint.objects.create(
            complaint_content =  request.POST.get("txtcontent"),
            user_id = tbl_user.objects.get(id=request.session['uid']),
            agency_id= tbl_travelagency.objects.get(id=aid)
        )
        return render(request, 'User/Complaint.html',{'complaint':complaint,'complaint1':complaint1})
    else:
        return render(request, 'User/Complaint.html', {'complaint':complaint,'complaint1':complaint1})
    

def deletecomplaint(request,id, aid):

    complaint=tbl_complaint.objects.get(id=id).delete()
    return redirect('User:Complaint', aid)

def feedback(request):
    if "uid" in request.session:
        user=tbl_user.objects.get(id=request.session['uid'])
        feedback=tbl_feedback.objects.filter(user_id=user.id)
        if request.method == "POST":
            tbl_feedback.objects.create(
                feedback_content=request.POST.get("txtfeedback"),
                user_id=tbl_user.objects.get(id=request.session['uid'])
            )
            return render(request, 'User/Feedback.html',{'feedback':feedback, 'msg':"Feedback Sent"})
        else:
            return render(request, 'User/Feedback.html',{'feedback':feedback})
    else:
        return redirect("Guest:login")
    
def deletefeedback(request,id):
    feedback=tbl_feedback.objects.get(id=id).delete()
    return redirect('User:Feedback')

def packagebooking(request,id):
    user=tbl_user.objects.get(id=request.session['uid'])
    ploc=tbl_packagelocation.objects.filter(package_id=id)
    if request.method == "POST":
        tbl_packagebooking.objects.create(
            packagebooking_fordate=request.POST.get("txtfordate"),
            packagelocation_id=tbl_packagelocation.objects.get(id=request.POST.get("selploc")),
            person_count=request.POST.get("txtpcount"),
            user_id=tbl_user.objects.get(id=request.session['uid'])
        )
        return render(request, 'User/PackageBooking.html',{'ploc':ploc,"msg":"Booking successful"})
    else:
        return render(request, 'User/PackageBooking.html',{'ploc':ploc})
    
def viewbookings(request):
    if "uid" in request.session:
        booking=tbl_packagebooking.objects.filter(user_id=request.session['uid'],packagebooking_status=1)
        booking1=tbl_packagebooking.objects.filter(user_id=request.session['uid'],packagebooking_status=0)
        booking2=tbl_packagebooking.objects.filter(user_id=request.session['uid'],packagebooking_status=2)
        booking3=tbl_packagebooking.objects.filter(user_id=request.session['uid'],packagebooking_status=3)
        return render(request,'User/ViewBookings.html',{'booking':booking,'booking1':booking1,'booking2':booking2, 'booking3':booking3})
    else:
        return redirect("Guest:login")
    
def pcbooking(request):
    if "uid" in request.session:
        booking=tbl_packagebooking.objects.filter(user_id=request.session['uid'],packagebooking_status=3)
        return render(request,'User/PCBooking.html',{'booking':booking})
    else:
        return redirect("Guest:login")

def cbooking(request):
    if "uid" in request.session:
        booking=tbl_packagebooking.objects.filter(user_id=request.session['uid'],packagebooking_status=1)
        return render(request,'User/CBooking.html',{'booking':booking})
    else:
        return redirect("Guest:login")
    
def rbooking(request):
    if "uid" in request.session:
        booking=tbl_packagebooking.objects.filter(user_id=request.session['uid'],packagebooking_status=2)
        return render(request,'User/RBooking.html',{'booking':booking})
    else:
        return redirect("Guest:login")

def payment(request,id):
    booking=tbl_packagebooking.objects.get(id=id)
    pb = tbl_packagelocation.objects.get(id=booking.packagelocation_id.id)
    pack = tbl_package.objects.get(id=pb.package_id.id)
    amt = pack.package_price
    if request.method == "POST":
        booking.packagebooking_status=3
        booking.save()
        return redirect("User:loader")
    else:
        return  render(request,'User/Payment.html',{"total":amt})

def loader(request):
    if "uid" in request.session:
        return render(request,"User/Loader.html")
    else:
        return redirect("Guest:login")

def paymentsuc(request):
    if "uid" in request.session:
        return render(request,"User/Payment_suc.html")
    else:
        return redirect("Guest:login")


def viewlocation(request,id):
    loc=tbl_location.objects.get(id=id)
    gal=tbl_location_gallery.objects.filter(location_id=id)
    return render(request,'User/ViewLocation.html',{'gal':gal,'loc':loc})

def ajaxlocation(request):
    if "uid" in request.session:
        if request.GET.get("name"):
            location = tbl_location.objects.filter(location_name__istartswith=request.GET.get("name"))
            return render(request, 'User/AjaxLocation.html',{'location':location})

        if request.GET.get("place") != "":
            location = tbl_location.objects.filter(place_id=request.GET.get("place"))
            return render(request, 'User/AjaxLocation.html',{'location':location})
        elif request.GET.get("district") != "":
            location = tbl_location.objects.filter(place_id__district=request.GET.get("district"))
            return render(request, 'User/AjaxLocation.html',{'location':location})
        else:
            location = tbl_location.objects.all()
            return render(request, 'User/AjaxLocation.html',{'location':location})
    else:
        return redirect("Guest:login")
    
def review(request, id):
    review = tbl_locationreview.objects.filter(location=id)
    if request.method == "POST":
        tbl_locationreview.objects.create(location=tbl_location.objects.get(id=id),user=tbl_user.objects.get(id=request.session["uid"]),location_review=request.POST.get("user_review"))
        return redirect("User:review",id)
    else:
        return render(request, "User/Review.html",{"review":review})
    
def viewlocpackages(request,id):
    locpack=tbl_packagelocation.objects.filter(location_id=id)
    packid = []
    for i in locpack:
        packid.append(i.package_id.id)
    # print(packid)
    pid = list(set(packid))
    # print(pid)
    package = tbl_package.objects.filter(id__in=pid)
    return render(request,'User/ViewLocPackages.html',{'locpack':package})

def rating(request,id):
    return  render(request,'User/Rating.html',{'id':id})

def agencycontact(request,id):
    agency = tbl_travelagency.objects.filter(id=id)
    return render(request,'User/AgencyContact.html',{'agency':agency})

def rating(request,mid):
    parray=[1,2,3,4,5]
    mid=mid
    # wdata=tbl_booking.objects.get(id=mid)
    
    counts=0
    counts=stardata=tbl_rating.objects.filter(agency_id=mid).count()
    if counts>0:
        res=0
        stardata=tbl_rating.objects.filter(agency_id=mid).order_by('rating_datetime')
        for i in stardata:
            res=res+i.rating_value
        avg=res//counts
        # print(avg)
        return render(request,"User/Rating.html",{'mid':mid,'data':stardata,'ar':parray,'avg':avg,'count':counts})
    else:
         return render(request,"User/Rating.html",{'mid':mid})

def ajaxstar(request):
    if "uid" in request.session:
        parray=[1,2,3,4,5]
        rating_value=request.GET.get('rating_value')
        user_id=tbl_user.objects.get(id=request.session['uid'])
        rating_content=request.GET.get('rating_content')
        pid=request.GET.get('pid')
        # wdata=tbl_booking.objects.get(id=pid)
        tbl_rating.objects.create(user_id=user_id,rating_content=rating_content,rating_value=rating_value,agency_id=tbl_travelagency.objects.get(id=pid))
        stardata=tbl_rating.objects.filter(agency_id=pid).order_by('rating_datetime')
        return render(request,"User/AjaxRating.html",{'data':stardata,'ar':parray})
    else:
        return redirect("Guest:login")

def starrating(request):
    if "uid" in request.session:
        r_len = 0
        five = four = three = two = one = 0
        # cdata = tbl_booking.objects.get(id=request.GET.get("pdt"))
        rate = tbl_rating.objects.filter(agency_id=request.GET.get("pdt"))
        ratecount = tbl_rating.objects.filter(agency_id=request.GET.get("pdt")).count()
        for i in rate:
            if int(i.rating_value) == 5:
                five = five + 1
            elif int(i.rating_value) == 4:
                four = four + 1
            elif int(i.rating_value) == 3:
                three = three + 1
            elif int(i.rating_value) == 2:
                two = two + 1
            elif int(i.rating_value) == 1:
                one = one + 1
            else:
                five = four = three = two = one = 0
            # print(i.rating_value)
            # r_len = r_len + int(i.rating_value)
        # rlen = r_len // 5
        # print(rlen)
        result = {"five":five,"four":four,"three":three,"two":two,"one":one,"total_review":ratecount}
        return JsonResponse(result)
    else:
        return redirect("Guest:login")

def viewrating(request,mid):
    parray=[1,2,3,4,5]
    mid=mid
    # wdata=tbl_booking.objects.get(id=mid)
    
    counts=0
    counts=stardata=tbl_rating.objects.filter(agency_id=mid).count()
    if counts>0:
        res=0
        stardata=tbl_rating.objects.filter(agency_id=mid).order_by('rating_datetime')
        for i in stardata:
            res=res+i.rating_value
        avg=res//counts
        # print(avg)
        return render(request,"User/ViewRating.html",{'mid':mid,'data':stardata,'ar':parray,'avg':avg,'count':counts})
    else:
        return render(request,"User/ViewRating.html",{'mid':mid})
    

def Logout(request):
    del request.session["uid"]
    return redirect("Guest:login")