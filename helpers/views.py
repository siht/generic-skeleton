from django.views.generic import TemplateView

class MytemplateView(TemplateView):
    def get(self, request, template_name):
        self.template_name = '{}.html'.format(template_name)
        return super(MytemplateView, self).get(request)
