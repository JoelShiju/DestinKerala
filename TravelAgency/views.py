from django.shortcuts import render,redirect
from Guest.models import *
from Admin.models import *
from TravelAgency.models import *
from User.models import *
from datetime import date
from django.http import JsonResponse
# Create your views here.

def homepage(request):
    if "aid" in request.session:
        return render(request, 'TravelAgency/Homepage.html')
    else:
        return redirect("Guest:login")

def myprofile(request):
    if "aid" in request.session:
        agency=tbl_travelagency.objects.get(id=request.session['aid'])
        return render(request, 'TravelAgency/MyProfile.html'  ,{'agency':agency})
    else:
        return redirect("Guest:login")

def editprofile(request):
    if "aid" in request.session:
        agency=tbl_travelagency.objects.get(id=request.session['aid'])
        if request.method == "POST":
            agency.agency_name=request.POST.get("txtname")
            agency.agency_email=request.POST.get("txtemail")
            agency.agency_contact=request.POST.get("txtcontact")
            agency.agency_address=request.POST.get("txtaddress")
            agency.save()
            return render(request, 'TravelAgency/EditProfile.html'  ,{"msg":"Profile Updated"})
        return render(request, 'TravelAgency/EditProfile.html',{'agency':agency})
    else:
        return redirect("Guest:login")

def changepassword(request):
    if "aid" in request.session:
        agency=tbl_travelagency.objects.get(id=request.session['aid'])
        if request.method ==  "POST":
            oldpassword=request.POST.get("txtoldpassword")
            newpassword=request.POST.get("txtnewpassword")
            conformpassword=request.POST.get("txtconformpassword")
            if oldpassword==agency.agency_password:
                if newpassword==conformpassword:
                    agency.agency_password=request.POST.get("txtnewpassword")
                    agency.save()
                    return render(request,  'TravelAgency/ChangePassword.html',{'msg':"Password Changed"})
                else:
                    return render(request,  'TravelAgency/ChangePassword.html',{'msg':"New Password Not Matched"})
            else:
                return render(request,  'TravelAgency/ChangePassword.html',{'msg':"Old Password Not Match"})
        else:
            return render(request, 'TravelAgency/ChangePassword.html')
    else:
        return redirect("Guest:login")
    
def package(request):
    if "aid" in request.session:
        ptype=tbl_package_type.objects.all()
        package=tbl_package.objects.filter(agency=request.session['aid'])
        # agency=tbl_travelagency.objects.get(id=request.session['aid'])
        if  request.method == "POST":
            tbl_package.objects.create(
                package_name=request.POST.get("txtname"),
                package_details=request.POST.get("txtdetails"),
                package_price=request.POST.get("txtprice"),
                package_type_id=tbl_package_type.objects.get(id=request.POST.get('selptype')),
                agency=tbl_travelagency.objects.get(id=request.session['aid'])
            )
            return render(request, 'TravelAgency/Package.html',{'package':package,'ptype':ptype})
        else:
            return render(request, 'TravelAgency/Package.html',{'package':package,'ptype':ptype})
    else:
        return redirect("Guest:login")
    
def deletepackage(request,id):
    tbl_package.objects.get(id=id).delete()
    return redirect("TravelAgency:Package")

def addlocation(request,cid):
    district=tbl_district.objects.all()
    pack=tbl_package.objects.all()
    ploc=tbl_packagelocation.objects.filter(package_id=cid)
    if request.method == "POST":
        tbl_packagelocation.objects.create(
            location_id=tbl_location.objects.get(id=request.POST.get("sellocation")),package_id=tbl_package.objects.get(id=cid)
            )
        return render(request , 'TravelAgency/AddLocation.html' ,{'district':district, 'pack':pack, 'ploc':ploc})
    else:
        return render(request , 'TravelAgency/AddLocation.html' ,{'district':district, 'pack':pack, 'ploc':ploc})
    

def ajaxplace(request):
    if "aid" in request.session:
        district = tbl_district.objects.get(id=request.GET.get("did"))   
        Place = tbl_place.objects.filter(district=district)
        return render(request,"TravelAgency/Ajaxplace.html",{"place":Place})
    else:
        return redirect("Guest:login")

def ajaxlocation(request):
    if "aid" in request.session:
        place = tbl_place.objects.get(id=request.GET.get("pid"))   
        location = tbl_location.objects.filter(place_id=place)
        return render(request,"TravelAgency/Ajaxlocation.html",{"location":location})
    else:
        return redirect("Guest:login")

def deleteaddloc(request,cid,did):
    tbl_packagelocation.objects.get(id=did).delete()
    return redirect('TravelAgency:AddLocation',cid)

def viewbookings(request):
    if "aid" in request.session:
        booking=tbl_packagebooking.objects.filter(packagelocation_id__package_id__agency_id=request.session['aid'],packagebooking_status=0)
        return render(request,'TravelAgency/ViewBookings.html',{'booking':booking})
    else:
        return redirect("Guest:login")

def acceptbookings(request,id):
    booking=tbl_packagebooking.objects.get(id=id)
    booking.packagebooking_status=1
    booking.save()
    return redirect('TravelAgency:ViewBookings')

def rejectbookings(request,id):
    booking=tbl_packagebooking.objects.get(id=id)
    booking.packagebooking_status=2
    booking.save()
    return redirect('TravelAgency:ViewBookings')

def acceptedbookings(request):
    if "aid" in request.session:
        abooking=tbl_packagebooking.objects.filter(packagelocation_id__package_id__agency_id=request.session['aid'],packagebooking_status=1)
        return render(request,'TravelAgency/AcceptedBookings.html',{'abooking':abooking})
    else:
        return redirect("Guest:login")

def rejectedbookings(request):
    if "aid" in request.session:
        rbooking=tbl_packagebooking.objects.filter(packagelocation_id__package_id__agency_id=request.session['aid'],packagebooking_status=2)
        return render(request,'TravelAgency/RejectedBookings.html',{'rbooking':rbooking})
    else:
        return redirect("Guest:login")

def racceptbookings(request,id):
    booking=tbl_packagebooking.objects.get(id=id)
    booking.packagebooking_status=1
    booking.save()
    return redirect('TravelAgency:RejectedBookings')

def arejectbookings(request,id):
    booking=tbl_packagebooking.objects.get(id=id)
    booking.packagebooking_status=2
    booking.save()
    return redirect('TravelAgency:AcceptedBookings')


def complaint(request):
    if "aid" in request.session:
        agency=tbl_travelagency.objects.get(id=request.session['aid'])
        complaint=tbl_agencycomplaint.objects.filter(agency_id=request.session['aid'])
        if request.method ==  "POST":
            tbl_agencycomplaint.objects.create(
                complaint_content =  request.POST.get("txtcontent"),
                agency_id= tbl_travelagency.objects.get(id=request.session['aid'])
            )
            return render(request, 'TravelAgency/Complaint.html',{'complaint':complaint})
        else:
            return render(request, 'TravelAgency/Complaint.html',{'complaint':complaint})
    else:
        return redirect("Guest:login")
    
def deletecomplaint(request,id):

    complaint=tbl_agencycomplaint.objects.get(id=id).delete()
    return redirect('TravelAgency:Complaint')

def feedback(request):
    if "aid" in request.session:
        agency=tbl_travelagency.objects.get(id=request.session['aid'])
        feedback=tbl_agencyfeedback.objects.filter(agency_id=agency.id)
        if request.method == "POST":
            tbl_agencyfeedback.objects.create(
                feedback_content=request.POST.get("txtfeedback"),
                agency_id=tbl_travelagency.objects.get(id=request.session['aid'])
            )
            return render(request, 'TravelAgency/Feedback.html',{'feedback':feedback})
        else:
            return render(request, 'TravelAgency/Feedback.html',{'feedback':feedback})
    else:
        return redirect("Guest:login")
    
def deletefeedback(request,id):
    feedback=tbl_agencyfeedback.objects.get(id=id).delete()
    return redirect('TravelAgency:Feedback')

def pcbookings(request):
    if "aid" in request.session:
        ar=[1,2,3,4,5]
        parry=[]
        avg=0
        booking=tbl_packagebooking.objects.filter(packagelocation_id__package_id__agency_id=request.session['aid'],packagebooking_status=3)
        for i in booking:
            tot=0
            ratecount=tbl_rating.objects.filter(agency_id=i.id).count()
            if ratecount>0:
                ratedata=tbl_rating.objects.filter(agency_id=i.id)
                for j in ratedata:
                    tot=tot+j.rating_value
                    avg=tot//ratecount
                    #print(avg)
                parry.append(avg)
            else:
                parry.append(0)
            # print(parry)
        datas=zip(booking,parry)
        return render(request, 'TravelAgency/PCBookings.html',{"booking":datas,"ar":ar})
        # booking=tbl_packagebooking.objects.filter(packagelocation_id__package_id__agency_id=request.session['aid'],packagebooking_status=3)
        # return render(request,'TravelAgency/PCBookings.html',{'booking':booking})
    else:
        return redirect("Guest:login")

def usercontact(request,id):
    user=tbl_user.objects.get(id=id)
    return render(request,'TravelAgency/UserContact.html',{'user':user})

def bookings(request):
    if "aid" in request.session:
        return render(request,'TravelAgency/Bookings.html')
    else:
        return redirect("Guest:login")


def ajaxstar(request):
    if "aid" in request.session:
        parray=[1,2,3,4,5]
        rating_value=request.GET.get('rating_value')
        user_id=tbl_user.objects.all()
        rating_content=request.GET.get('rating_content')
        pid=request.GET.get('pid')
        # wdata=tbl_booking.objects.get(id=pid)
        tbl_rating.objects.create(user_id=user_id,rating_content=rating_content,rating_value=rating_value,agency_id=tbl_travelagency.objects.get(id=pid))
        stardata=tbl_rating.objects.filter(agency_id=pid).order_by('rating_datetime')
        return render(request,"User/AjaxRating.html",{'data':stardata,'ar':parray})
    else:
        return redirect("Guest:login")
    
def viewratings(request):
    if "aid" in request.session:
        parray=[1,2,3,4,5]
    
        # wdata=tbl_booking.objects.get(id=mid)
        
        counts=0
        counts=stardata=tbl_rating.objects.filter(agency_id=request.session['aid']).count()
        if counts>0:
            res=0
            stardata=tbl_rating.objects.filter(agency_id=request.session['aid']).order_by('rating_datetime')
            for i in stardata:
                res=res+i.rating_value
            avg=res//counts
            # print(avg)
        return render(request,"TravelAgency/ViewRatings.html",{'data':stardata,'ar':parray,'avg':avg,'count':counts})
    else:
        return redirect("Guest:login")

def starrating(request):
    if "aid" in request.session:
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
   
def Logout(request):
    del request.session["aid"]
    return redirect("Guest:login")