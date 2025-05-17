from django.shortcuts import render,redirect
from Admin.models import *
from Guest.models import *
from TravelAgency.models import *
from User.models import *

# Create your views here.

def district(request):
    if "adid" in request.session:
        district = tbl_district.objects.all()
        if request.method == "POST":
            tbl_district.objects.create(district_name=request.POST.get("txtdistrict"))
            return redirect("Admin:District")
        else:
            return render(request, 'Admin/District.html',{'district':district})
    else:
        return redirect("Guest:login")
    
def deletedistrict(request, id):
    tbl_district.objects.get(id=id).delete()
    return redirect("Admin:District")

def editdistrict(request, id):
    dis = tbl_district.objects.get(id=id)
    if request.method == "POST":
        dis.district_name = request.POST.get("txtdistrict")
        dis.save()
        return redirect("Admin:District")
    else:
        return render(request, 'Admin/District.html',{"dis":dis})

def category(request):
    if "adid" in request.session:
        category = tbl_category.objects.all()
        if request.method == "POST":
            tbl_category.objects.create(category_name=request.POST.get("txtcategory"))
            return redirect("Admin:Category")
        else:
            return render(request,'Admin/Category.html',{'category':category})
    else:
        return redirect("Guest:login")

def deletedcategory(request,id):
    tbl_category.objects.get(id=id).delete()
    return redirect("Admin:Category") 

def editcategory(request,id):
    cat = tbl_category.objects.get(id=id)
    if request.method == "POST":
        cat.category_name = request.POST.get("txtcategory")
        cat.save()
        return redirect("Admin:Category")
    else:
        return render(request,'Admin/Category.html',{'cat':cat})

def adminregistration(request):
    if "adid" in request.session:
        adminregistration = tbl_adminregistration.objects.all()
        if  request.method == "POST":
            tbl_adminregistration.objects.create(admin_name=request.POST.get("txtname"),admin_email=request.POST.get("txtemail"),admin_password=request.POST.get("txtpassword"))
            return redirect("Admin:AdminRegistration")
        else:
            return render(request,'Admin/AdminRegistration.html',{'adminregistration':adminregistration})
    else:
        return redirect("Guest:login")
    
def  deletedadmin(request,id):
    tbl_adminregistration.objects.get(id=id).delete()
    return  redirect("Admin:AdminRegistration")

def editadmin(request,id):
    admin  = tbl_adminregistration.objects.get(id=id)
    if request.method == "POST":
        admin.admin_name = request.POST.get("txtname")
        admin.admin_email = request.POST.get("txtemail")
        admin.admin_password = request.POST.get("txtpassword")
        admin.save()
        return redirect("Admin:AdminRegistration")
    else:
        return render(request,'Admin/AdminRegistration.html',{'admin':admin})


def place(request):
    if "adid" in request.session:
        dis=tbl_district.objects.all()
        place=tbl_place.objects.all()
        if request.method=="POST":
            tbl_place.objects.create(
                district=tbl_district.objects.get(id=request.POST.get("seldistrict")),
                place_name=request.POST.get("txtplace")
            )
            return redirect("Admin:Place")
        else:
            return render(request,'Admin/Place.html',{'district':dis,'place':place})
    else:
        return redirect("Guest:login")
    
def deleteplace(request,id):
    place=tbl_place.objects.get(id=id).delete()
    return redirect("Admin:Place")

def editplace(request,id):
    dis=tbl_district.objects.all()
    plac = tbl_place.objects.get(id=id)
    if  request.method == "POST":
        plac.place_name = request.POST.get("txtplace")
        plac.district=tbl_district.objects.get(id=request.POST.get('seldistrict'))
        plac.save()
        return redirect("Admin:Place")
    else:
        return render(request,'Admin/Place.html',{'plac':plac,'district':dis})
    

def subcategory(request):
    if "adid" in request.session:
        cat=tbl_category.objects.all()
        subcat=tbl_subcategory.objects.all()
        if request.method=="POST":
            tbl_subcategory.objects.create(
                category=tbl_category.objects.get(id=request.POST.get("selcategory")),
                subcategory_name=request.POST.get("txtsubcategory")
            )
            return redirect("Admin:SubCategory")
        else:
            return render(request,'Admin/SubCategory.html',{'category':cat,'subcategory':subcat})
    else:
        return redirect("Guest:login")
    
def  deletesubcategory(request,id):
    subcat=tbl_subcategory.objects.get(id=id).delete()
    return redirect("Admin:SubCategory")

def  editsubcategory(request,id):
    cat=tbl_category.objects.all()
    subcat = tbl_subcategory.objects.get(id=id)
    if  request.method == "POST":
        subcat.subcategory_name = request.POST.get("txtsubcategory")
        subcat.category=tbl_category.objects.get(id=request.POST.get('selcategory'))
        subcat.save()
        return redirect("Admin:SubCategory")
    else:
        return render(request,'Admin/SubCategory.html',{'subcat':subcat,'category':cat})
    
def location(request):
    if "adid" in request.session:
        dis= tbl_district.objects.all()
        loc=tbl_location.objects.all()
        if  request.method=="POST":
            tbl_location.objects.create(
                location_name=request.POST.get('txtlocation'),
                location_photo=request.FILES.get('filephoto'),
                place_id= tbl_place.objects.get(id=request.POST.get('selplace'))
            )
            return render(request,'Admin/Location.html', {"msg":"Location Added"})
        else:
            return  render(request,'Admin/Location.html', {'dis':dis,'loc':loc})
    else:
        return redirect("Guest:login")
    
def deletelocation(request,id):
    loc=tbl_location.objects.get(id=id).delete()
    return redirect("Admin:Location")
    
def ajaxplace(request):
    if "adid" in request.session:
        district = tbl_district.objects.get(id=request.GET.get("did"))   
        Place = tbl_place.objects.filter(district=district)
        return render(request,"Admin/Ajaxplace.html",{"place":Place})
    else:
        return redirect("Guest:login")

def locationgallery(request,lid):
    loc=tbl_location.objects.get(id=lid)
    gal=tbl_location_gallery.objects.filter(location=lid)
    if   request.method=="POST":
        tbl_location_gallery.objects.create(
            gallery_file=request.FILES.get('filephoto'),
            gallery_caption=request.POST.get('txtcaption'),
            location= tbl_location.objects.get(id=lid)
        )
        return render(request,'Admin/LocationGallery.html',{"msg":"Photo Added",'gal':gal})
    else:
        return render(request,'Admin/LocationGallery.html',{'loc':loc,'gal':gal})

def deletelocationgallery(request,lid,did):
    tbl_location_gallery.objects.get(id=did).delete()
    return redirect("Admin:locationgallery",lid)
    
def packagetype(request):
    if "adid" in request.session:
        ptype=tbl_package_type.objects.all()
        if  request.method == "POST":
            tbl_package_type.objects.create(
                package_type_name=request.POST.get('txtptype'),
            )
            return render(request,'Admin/PackageType.html',{'msg':"Package Type Added"})
        else:
            return render(request,'Admin/PackageType.html',{'ptype':ptype})
    else:
        return redirect("Guest:login")
    
def deletepackagetype(request,id):
    ptype=tbl_package_type.objects.get(id=id).delete()
    return redirect("Admin:PackageType")

def viewagencies(request):
    if "adid" in request.session:
        agency=tbl_travelagency.objects.filter(agency_status=0)
        return render(request,'Admin/ViewAgencies.html',{'agency':agency})
    else:
        return redirect("Guest:login")

def acceptviewagencies(request,id):
    agency=tbl_travelagency.objects.get(id=id)
    agency.agency_status=1
    agency.save()
    return render(request,'Admin/ViewAgencies.html',{'msg':"Agency Accepted"})

def rejectviewagencies(request,id):
    agency=tbl_travelagency.objects.get(id=id)
    agency.agency_status=2
    agency.save()
    return render(request,'Admin/ViewAgencies.html',{'msg1':"Agency Rejected"})
   
def acceptedagencies(request):
    if "adid" in request.session:
        agency=tbl_travelagency.objects.filter(agency_status=1)
        return render(request,'Admin/AcceptedAgencies.html',{'agency':agency})
    else:
        return redirect("Guest:login")

def rejectedagencies(request):
    if "adid" in request.session:
        agency=tbl_travelagency.objects.filter(agency_status=2)
        return render(request,'Admin/RejectedAgencies.html',{'agency':agency})
    else:
        return redirect("Guest:login")

def homepage(request):
    if "adid" in request.session:
        admin=tbl_adminregistration.objects.get(id=request.session['adid'])
        users=tbl_user.objects.all().count()
        travelcount=tbl_travelagency.objects.filter(agency_status=1).count()
        payment=tbl_packagebooking.objects.filter(packagebooking_status=3).count()
        return render(request, 'Admin/Homepage.html',{'admin':admin,'user':users,'travel':travelcount,'totalpay':payment})
    else:
        return redirect("Guest:login")

def viewagencycomplaints(request):
    if "adid" in request.session:
        complaint=tbl_agencycomplaint.objects.filter(complaint_status=0)
        complaint1=tbl_agencycomplaint.objects.filter(complaint_status=1)
        return render(request,'Admin/ViewAgencyComplaints.html',{'complaint':complaint, 'complaint1':complaint1})
    else:
        return redirect("Guest:login")

def agencyreply(request,id):
    complaint=tbl_agencycomplaint.objects.get(id=id)
    if  request.method == "POST":
        complaint.complaint_reply=request.POST.get("txtreply")
        complaint.complaint_status=1
        complaint.save()
        return render(request,'Admin/AgencyReply.html', {'msg':'Replied'})
    else:
        return render(request,'Admin/AgencyReply.html')


def viewusercomplaints(request):
    if "adid" in request.session:
        complaint=tbl_complaint.objects.filter(complaint_status=0)
        complaint1=tbl_complaint.objects.filter(complaint_status=1)
        return render(request,'Admin/ViewUserComplaints.html',{'complaint':complaint, 'complaint1':complaint1})
    else:
        return redirect("Guest:login")

def userreply(request,id):
    complaint=tbl_complaint.objects.get(id=id)
    if  request.method == "POST":
        complaint.complaint_reply=request.POST.get("txtreply")
        complaint.complaint_status=1
        complaint.save()
        return render(request,'Admin/UserReply.html', {'msg':'Replied'})
    else:
        return render(request,'Admin/UserReply.html')

def viewagencyfeedbacks(request):
    if "adid" in request.session:
        feedback=tbl_agencyfeedback.objects.all()
        return render(request,'Admin/ViewAgencyFeedbacks.html',{'feedback':feedback})
    else:
        return redirect("Guest:login")

def viewuserfeedbacks(request):
    if "adid" in request.session:
        feedback=tbl_feedback.objects.all()
        return render(request,'Admin/ViewUserFeedbacks.html',{'feedback':feedback})
    else:
        return redirect("Guest:login")
    
def bookings(request):
    if "adid" in request.session:
        booking=tbl_packagebooking.objects.filter(packagebooking_status=3)
        return render(request,'Admin/Bookings.html',{'booking':booking})
    else:
        return redirect("Guest:login")
    
def header(request):
    if "adid" in request.session:
        admin=tbl_adminregistration.objects.get(id=request.session['adid'])
        return render(request, 'Admin/Header.html',{'admin':admin})
    else:
        return redirect("Guest:login")

def Logout(request):
    del request.session["adid"]
    return redirect("Guest:login")