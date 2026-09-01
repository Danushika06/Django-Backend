from django.urls import path,include
from . import views

urlpatterns = [
    path("create/", views.create_students),
    path("list/", views.Studentlist.as_view()),
    path("detail/<int:id>/",views.StudentDetail.as_view()),
    path("createe/",views.StudentCreate.as_view()),
    path("updatee/<int:id>/",views.StudentUpdate.as_view()),
    path("delete/", views.delete_students),
    path("deleteee/<int:id>/", views.StudentDelete.as_view()),
    path("update/", views.update_students),
    path("students/", views.students),
    path("<int:idd>/",views.student_detail),
    path("<int:idd>/<str:name>/", views.student_details ),
    path("debug/", views.debug_view),
    path("home/",views.home)
]