
from django.urls import path,include
from . import views
from django.views.generic import TemplateView
from members.views import Ex2View
#template view within a url
app_name='website'
urlpatterns = [
   path('new',TemplateView.as_view(template_name='new.html', extra_context={'title':'Custom Title'})),
   path('new2',Ex2View.as_view(),name='new2')
]
#template view is used to load static pages, it has an option of extra_content which helps to tweak withing the TemplateView class 

