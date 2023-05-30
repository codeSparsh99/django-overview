from django.urls import path
from . import views

urlpatterns = [
    path('get_user/', views.UserRoleView.as_view({'get':'get'}), name="get_user_role")
]