from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.views import serve
from django.views.decorators.cache import never_cache
from .views import mainpage, board, thread

urlpatterns = [
    path('<str:board_l>/', board, name='board'),
    path('<str:board_l>/<int:thread_n>/', thread, name='thread'),
    path('', mainpage, name='mainpage'),
    path('static/<path:path>', never_cache(serve)),  # DELETE THIS IF setting.DEBUG == True
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += [re_path(r'^captcha/', include('captcha.urls')), ]
