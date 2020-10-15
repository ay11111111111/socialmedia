from django.urls import path, include
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

app_name = 'testtask'
urlpatterns = [
    path('new/', views.PostCreateView.as_view({'post':'create'}), name='post-create'),
    path('list/', views.PostViewSet.as_view({'get':'list'}), name='post-list'),
    path('<int:pk>/like/', views.PostLikeView.as_view({'put':'like'}), name='post-like'),
    path('<int:pk>/unlike/', views.PostLikeView.as_view({'put':'unlike'}), name='post-unlike'),
    path('likeanalytics/', views.LikeAnalyticsView.as_view(), name='likeanalytics'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
