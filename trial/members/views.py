from django.views.generic.base import TemplateView
from members.models import Post
# Create your models here.
#wehn you might use template view, to show static pages
#pages that get GET REQUESTs    

class Ex2View(TemplateView):

    #template response mixin
    #this provides a mechanism to construct a TemplateResponse, given suitable context. 
    #Attributes:

    template_name='new.html'
    #template engine
    #response_class
    #content_type
    # are more things that can be changed


    """ 
    get_context_data(** kwargs) is a method inherited from content mixin
    """
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['posts']= Post.objects.get(id=1)
        context['data']= "Context Data for EX2"

        return context
