from django.urls import include, path
from rest_framework import routers
from project.quickstart import views

# router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    # path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('users/', views.user_list),
 
]
