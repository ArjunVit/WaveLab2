from django.urls import re_path
import Wave.views

urlpatterns = [
    re_path(r'^$', Wave.views.index, name='index'),
    re_path(r'^outputsine$',Wave.views.outputsine,name='outputsine'),
    re_path(r'home$',Wave.views.index,name='home'),
]