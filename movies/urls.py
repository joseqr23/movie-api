from django.contrib import admin
from django.urls import path, include

# Permisos
from rest_framework import permissions

# Yasg Doc
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title = "Movie API",
        default_version= "v1",
        description= "API para recordar Django y buscar trabajo",
        terms_of_service= "https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="jquisper2@gmail.com"),
        license = openapi.License(name="MIT") 
    ),
    public= True,
    permission_classes=[permissions.AllowAny]
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('movie/', include("movie.urls")),
    path('rent/', include("rent.urls")),
    path('user/', include("user.urls")),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-doc'),
]
