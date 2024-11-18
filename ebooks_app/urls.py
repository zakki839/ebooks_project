from django.urls import path, re_path, include
#from django.views.generic import RedirectView
#from django.conf.urls.i18n import i18n_patterns
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('blogs/', views.blog_list, name='blog_list'),
    path('books/', views.book_list, name='book_list'),
    re_path(r'^books/(?P<slug>[\w-]+)/$', views.book_detail, name='book_detail'),
    # Uncomment and modify the lines below as needed:
    # path('blogs/', include('ebooks_blogs.urls', namespace='blogs')),
    # path('archive/', RedirectView.as_view(url='/books/')),
]
