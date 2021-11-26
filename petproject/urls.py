from django.contrib                 import admin
from django.urls                    import path, re_path
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from petapp                  import views
from petapp.views.userCreateView import UserCreateView
from petapp.views.userDetailView import UserDetailView
from petapp.views.verifyTokenView import VerifyTokenView
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView



urlpatterns = [
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    path('admin/', admin.site.urls),
    path('login/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path('verifyToken/', views.VerifyTokenView.as_view()),
    path('user/', views.UserCreateView.as_view()),
    path('user/<int:pk>/', views.UserDetailView.as_view()),
    path('user/delate/<int:pk>/', views.UserDelateView.as_view()),
    path('user/update/<int:pk>/', views.UserUpdateView.as_view()),
]
