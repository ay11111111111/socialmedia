from django.urls import path, include
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView,
                                        )
from .token import MyTokenObtainPairView

app_name = 'users'
urlpatterns = [
    path('signup/', views.UserCreateView.as_view(), name='signup'),
    path('<int:pk>/activity', views.UserViewSet.as_view({'get':'retrieve'}), name='list'),
    path('list/', views.UserViewSet.as_view({'get':'list'}), name='list'),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]

urlpatterns = format_suffix_patterns(urlpatterns)
