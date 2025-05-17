from django.urls import path
from TravelAgency import views
app_name='TravelAgency'

urlpatterns=[
    path('Homepage/',views.homepage,name='Homepage'),
    path('MyProfile/',views.myprofile,name='MyProfile'),
    path('EditProfile/',views.editprofile,name='EditProfile'),
    path('ChangePassword/',views.changepassword,name='ChangePassword'),
    path('Package/',views.package,name='Package'),
    path('deletepackage/<int:id>',views.deletepackage,name='deletepackage'),
    path('AddLocation/<int:cid>',views.addlocation,name='AddLocation'),
    path('Ajaxplace/',views.ajaxplace,name='ajaxplace'),
    path('Ajaxlocation/',views.ajaxlocation,name='ajaxlocation'),
    path('deleteaddloc/<int:cid>/<int:did>',views.deleteaddloc,name='deleteaddloc'),
    path('ViewBookings/',views.viewbookings,name='ViewBookings'),
    path('acceptbookings/<int:id>',views.acceptbookings,name='acceptbookings'),
    path('rejectbookings/<int:id>',views.rejectbookings,name='rejectbookings'),
    path('AcceptedBookings/',views.acceptedbookings,name='AcceptedBookings'),
    path('RejectedBookings/',views.rejectedbookings,name='RejectedBookings'),
    path('racceptbookings/<int:id>',views.racceptbookings,name='racceptbookings'),
    path('arejectbookings/<int:id>',views.arejectbookings,name='arejectbookings'),
    path('Complaint/',views.complaint,name='Complaint'),
    path('deletecomplaint/<int:id>',views.deletecomplaint,name='deletecomplaint'),
    path('Feedback/',views.feedback,name='Feedback'),
    path('deletefeedback/<int:id>',views.deletefeedback,name='deletefeedback'),
    path('PCBookings/',views.pcbookings,name='PCBookings'),
    path('UserContact/<int:id>',views.usercontact,name='UserContact'),
    path('Bookings/',views.bookings,name='Bookings'),
    path('ajaxstar/',views.ajaxstar,name="ajaxstar"),
    path('ViewRatings/',views.viewratings,name='ViewRatings'),
    path('starrating/',views.starrating,name="starrating"),
    path('Logout/',views.Logout,name="Logout"),
]