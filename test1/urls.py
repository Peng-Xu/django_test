from django.conf.urls import url,include
from django.contrib import admin
from app01 import urls
import app01

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'',include(app01.urls)),
]
