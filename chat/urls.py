from django.contrib import admin
from django.urls import path, include,re_path
from django.conf import settings
from django.conf.urls.static import static
# from django.conf.urls import url

urlpatterns = [
    path('',include('account.urls')),
    path('post/', include('post.urls')),
    path('admin/', admin.site.urls),
    path('dj-rest-auth/', include('dj_rest_auth.urls'))
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
