from django.urls import path,include
from . import views

urlpatterns = [
    path("", views.faculty),
    path("list", views.FacultyListCreate.as_view()),     
    path("update/<int:pk>/", views.FacultyUpdate.as_view()),
]

#
#from django.urls import path, include
#from rest_framework.routers import DefaultRouter
#from .views import StudentViewSet  # Import your viewset

#router = DefaultRouter()
#router.register(r'students', StudentViewSet)

#urlpatterns = [
#    path('', include(router.urls)),
#]
