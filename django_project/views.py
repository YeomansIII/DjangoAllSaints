from django.views.generic import TemplateView
from easypage.models import QuickLink, Carousel, Featurette

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['carousel'] = Carousel.objects.all()[:5]
        context['quicklinks'] = QuickLink.objects.all()[:3]
        context['featurettes'] = Featurette.objects.all()[:3]
        return context
