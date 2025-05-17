from django.urls import path
from User import views
app_name='User'
urlpatterns = [
    path('Homepage/',views.homepage,name='Homepage'),
    path('Search/',views.search,name='Search'),
    path('MyProfile/',views.myprofile,name='MyProflie'),
    path('EditProfile/',views.editprofile,name='EditProfile'),
    path('ChangePassword/',views.changepassword,name='ChangePassword'),
    path('ViewAgencies/',views.viewagencies,name='ViewAgencies'),
    path('ViewPackages/<int:id>',views.viewpackages,name='ViewPackages'),
    path('Complaint/<int:aid>',views.complaint,name='Complaint'),
    path('deletecomplaint/<int:aid>/<int:id>',views.deletecomplaint,name='deletecomplaint'),
    path('Feedback/',views.feedback,name='Feedback'),
    path('deletefeedback/<int:id>',views.deletefeedback,name='deletefeedback'),
    path('PackageBooking/<int:id>',views.packagebooking,name='PackageBooking'),
    path('ViewBookings/',views.viewbookings,name='ViewBookings'),
    path('Payment/<int:id>',views.payment,name='Payment'),
    path('loader/',views.loader,name='loader'),
    path('paymentsuc/',views.paymentsuc,name='paymentsuc'),
    path('ViewLocation/<int:id>',views.viewlocation,name='ViewLocation'),
    path('AgencyContact/<int:id>',views.agencycontact,name='AgencyContact'),
    path('ajaxlocation/',views.ajaxlocation,name='ajaxlocation'),
    path('review/<int:id>',views.review,name='review'),
    path('ViewLocPackages/<int:id>',views.viewlocpackages,name='ViewLocPackages'),
    path('rating/<int:mid>',views.rating,name="rating"),  
    path('ajaxstar/',views.ajaxstar,name="ajaxstar"),
    path('starrating/',views.starrating,name="starrating"),
    path('ViewRating/<int:mid>',views.viewrating,name='ViewRating'),
    path('PCBooking/',views.pcbooking,name='PCBooking'),
    path('CBooking/',views.cbooking,name='CBooking'),
    path('RBooking/',views.rbooking,name='RBooking'),
    path('Logout/',views.Logout,name="Logout"),
    path('ajaxsearch/',views.ajaxsearch,name="ajaxsearch"),


]