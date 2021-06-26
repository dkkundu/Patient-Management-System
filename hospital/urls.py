from django.urls import path
from . import views
from . import registation_view
from address.views import (
    load_district,
    load_upazila
)


urlpatterns = [
    path('', views.HomeView.as_view(), name='index'),
    path('services/', views.ServiceListView.as_view(), name="services"),
    path('services/<int:pk>/', views.ServiceDetailView.as_view(),
         name="service_details"),
    path('doctors/', views.DoctorListView.as_view(), name="doctors"),
    path('doctors/<int:pk>/', views.DoctorDetailView.as_view(),
         name="doctor_details"),
    path('faqs/', views.FaqListView.as_view(), name="faqs"),
    path('gallery/', views.GalleryListView.as_view(), name="gallery"),
    path('contact/', views.ContactView.as_view(), name="contact"),
    path(
        'registration/type/',
        registation_view.RegistrationPages.as_view(), name="registration_type"
    ),
    path(
        'login/',
        views.LoginView.as_view(), name="login"
    ),
    path(
        'logout/',
        views.logout_request, name="logout"
    ),


    path('load-district/', load_district, name='load_district'),
    path('load-upazila/', load_upazila, name='load_upazila'),
]
