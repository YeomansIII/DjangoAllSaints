from django.views.generic import TemplateView
from django.http import HttpResponse
from easypage.models import QuickLink, Carousel, Featurette
from blanc_basic_news.models import Post

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['carousel'] = Carousel.objects.all()[:5]
        context['quicklinks'] = QuickLink.objects.all()[:3]
        context['featurettes'] = Featurette.objects.all()[:3]
        return context

def NewsText(request, year1, month1, day1, slug1):
    post_text = Post.objects.filter(year=year1,month=month1,day=day1,slug=slug1)[0].content
    return HttpResponse(post_text)
