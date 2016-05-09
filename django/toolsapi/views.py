from django.views.generic.base import TemplateView


class IndexView(TemplateView):
    """
    Render main template
    """
    template_name = 'index.html'
