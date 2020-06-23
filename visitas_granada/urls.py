from django.urls import include, path
from rest_framework import routers
from . import views
from rest_framework_simplejwt import views as jwt_views

router = routers.DefaultRouter()
router.register(r'visitas', views.VisitaViewSet)
router.register(r'comentarios', views.ComentarioViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:visit_id>/', views.detail, name='detail'),
    path('visit_list_view/', views.visit_list_view, name='visit_list_view'),
    path('new_visit/', views.new_visit, name='new_visit'),
    path('edit/<int:visit_id>/', views.edit_visit, name='edit_visit'),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('api/likes/<int:visit_id>/', views.api_likes, name='likes'),
]
