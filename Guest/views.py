from django.shortcuts import render,redirect
from Guest.models import *
from Admin.models import *
# Create your views here.

def userregistration(request):
    dis= tbl_district.objects.all()
    if request.method=='POST':
        tbl_user.objects.create(
            user_name=request.POST.get('txtname'),
            user_email=request.POST.get('txtemail'),
            user_contact=request.POST.get('txtcontact'),
            user_photo=request.FILES.get('filephoto'),
            user_password=request.POST.get('txtpassword'),
            user_place=tbl_place.objects.get(id=request.POST.get('selplace'))
        )
        return render(request,"Guest/UserRegistration.html", {"msg":"User Registered"})
    else:
        return render(request,'Guest/UserRegistration.html',{'dis':dis})
     
def ajaxplace(request):
    district = tbl_district.objects.get(id=request.GET.get("did"))   
    Place = tbl_place.objects.filter(district=district)
    return render(request,"Guest/Ajaxplace.html",{"place":Place})

def login(request):
    if request.method=='POST':
        email=request.POST.get('txtemail')
        password=request.POST.get('txtpassword')
        usercount=tbl_user.objects.filter(user_email=email,user_password=password).count()
        agencycount=tbl_travelagency.objects.filter(agency_email=email,agency_password=password).count()
        admincount=tbl_adminregistration.objects.filter(admin_email=email,admin_password=password).count()
        if usercount >0:
            user=tbl_user.objects.get(user_email=email,user_password=password)
            request.session['uid']=user.id
            request.session['uname']=user.user_name
            return redirect('User:Homepage')
        elif agencycount >0:
            agency=tbl_travelagency.objects.get(agency_email=email,agency_password=password)
            if agency.agency_status==1:
                request.session['aid']=agency.id
                request.session['aname']=agency.agency_name
                return redirect('TravelAgency:Homepage')
            elif  agency.agency_status==2:
                return render(request,'Guest/Login.html',{'msg':'Your Account is Blocked'})
            else:
                return render(request,'Guest/Login.html',{'msg':'Your Account is Not Verified'})
        elif admincount > 0:
            admin =tbl_adminregistration.objects.get(admin_email=email,admin_password=password)
            request.session['adid']=admin.id
            request.session['adname']=admin.admin_name
            return redirect('Admin:Homepage')
        else:
            return render(request,'Guest/Login.html',{'msg':"Invalid login"})
    else:
        return render(request,'Guest/Login.html')
    

def travelagencyregistration(request):
    dis= tbl_district.objects.all()
    if request.method=='POST':
        tbl_travelagency.objects.create(
            agency_name=request.POST.get('txtname'),
            agency_email=request.POST.get('txtemail'),
            agency_contact=request.POST.get('txtcontact'),
            agency_address=request.POST.get('txtaddress'),
            agency_photo=request.FILES.get('filephoto'),
            agency_license=request.FILES.get('filelicense'),
            agency_password=request.POST.get('txtpassword'),
            agency_place=tbl_place.objects.get(id=request.POST.get('selplace'))
        )
        return render(request,'Guest/TravelAgencyRegistration.html',{'msg':"Travel Agency Registered"})
    else:
        return render(request,'Guest/TravelAgencyRegistration.html',{'dis':dis})
    
def index(request):
    return render(request,'Guest/index.html')

def search(request):
    dis= tbl_district.objects.all()
    loc=tbl_location.objects.all()
    return render(request, 'Guest/Search.html'  ,{'loc':loc,'dis':dis})

def viewlocation(request,id):
    loc=tbl_location.objects.get(id=id)
    gal=tbl_location_gallery.objects.filter(location_id=id)
    return render(request,'Guest/ViewLocation.html',{'gal':gal,'loc':loc})

def ajaxlocation(request):
    if request.GET.get("name"):
        location = tbl_location.objects.filter(location_name__istartswith=request.GET.get("name"))
        return render(request, 'Guest/AjaxLocation.html',{'location':location})

    if request.GET.get("place") != "":
        location = tbl_location.objects.filter(place_id=request.GET.get("place"))
        return render(request, 'Guest/AjaxLocation.html',{'location':location})
    elif request.GET.get("district") != "":
        location = tbl_location.objects.filter(place_id__district=request.GET.get("district"))
        return render(request, 'Guest/AjaxLocation.html',{'location':location})
    else:
        location = tbl_location.objects.all()
        return render(request, 'Guest/AjaxLocation.html',{'location':location})