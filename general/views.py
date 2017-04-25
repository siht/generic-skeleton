from django.views.generic import TemplateView

class TemplateViewer(TemplateView):
    def get(self, request, template_name):
        self.template_name = '{}.html'.format(template_name)
        return super(TemplateViewer, self).get(request)
