from django.urls import path

from user_app import views
urlpatterns = [
    path('list/',views.ListUserView.as_view()),
    path('',views.RegisterView.as_view()),
    path('<int:pk>/',views.RetreivedUserView.as_view()),
]
