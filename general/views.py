from django.views.generic import TemplateView

class TemplateViewer(TemplateView):
    def get(self, request, template_name):
    	template_name = template_name[:-1] if template_name.endswith('/') else template_name
        self.template_name = '{}.html'.format(template_name)
        return super(TemplateViewer, self).get(request)
