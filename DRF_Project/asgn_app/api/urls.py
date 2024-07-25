from django.urls import path,include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from asgn_app.views import *
from asgn_app.api.views import MovieBulkInsert,MovieViewSet

router = DefaultRouter()
router.register(r'filter', MovieViewSet)
urlpatterns = [
    path('movie/', MovieBulkInsert.as_view(), name='movie'),
    path('', include(router.urls)),
    path('login/', obtain_auth_token, name='login'),
    
]