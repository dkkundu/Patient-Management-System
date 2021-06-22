from django.urls import path
from . import views
from . import registation_view


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
        'registration/doctor/',
        registation_view.DoctorRegistration.as_view(), name="registration_doctor"
    )
]
