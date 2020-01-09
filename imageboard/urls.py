from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from .views import mainpage, board, thread

urlpatterns = [
    path('<str:board_l>/', board, name='board'),
    path('<str:board_l>/<int:thread_n>/', thread, name='thread'),
    path('', mainpage, name='mainpage'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += [re_path(r'^captcha/', include('captcha.urls')), ]
