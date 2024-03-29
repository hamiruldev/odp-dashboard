from django.contrib import admin
from django.http import HttpResponse
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from core.admin import admin_site

from users.views import signup


urlpatterns = [
    
    path('', lambda request: HttpResponse('200 Welcome to REST API Interface: Agent-Inventory'), name='home'),
    
    path('admin/clearcache/', include('clearcache.urls')),

    path('admin/', admin.site.urls),
    path('signup/', signup, name='signup'),


    # API V1
    path('api/v1/', include(([

        # path('login', TokenObtainPairView.as_view(), name='token_obtain_pair'),
        path('login/refresh', TokenRefreshView.as_view(), name='token_refresh'),

        path('user/', include('users.urls')),
        path('profile/', include('profiles.urls')),
        # path('blog/', include('blog_api.urls')),
        path('branch/', include('branchs.urls')),
        path('inventory/', include('inventory_api.urls')),

    ], 'api'), namespace='api-v1')),

    path('api-auth/', include('rest_framework.urls')),
    path('docs', include_docs_urls(title='Agent-Inventory API')),
    path('schema', get_schema_view(
        title="Agent-Inventory API",
        description="",
        version="1.0.1",
    ), name='schema')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)




admin.site.site_header = 'One Dream Property | Listing System'
admin.site.site_title = 'Administration'
admin.site.site_url = 'http://onedreamproperty.com.my/'
admin.site.index_title = 'Dashboard'
    



# Replace the default admin site with your custom site



# urlpatterns += [ re_path(r'^.*', TemplateView.as_view(template_name='index.html')) ]
