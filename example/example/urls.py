from django.urls import include, path

from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    # Examples:
    # path('', 'example.views.home', name='home'),
    # path('blog/', include('blog.urls')),

    path('admin/', include(admin.site.urls)),
]
