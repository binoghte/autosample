from django.http import HttpResponse
from django.template import loader
from .models import TemplateText


def get_templates(request):
    mytemplates = TemplateText.objects.all().values()
    web_template = loader.get_template('index.html')
    context = {
        'mytemplates': mytemplates,
    }
    return HttpResponse(web_template.render(context, request))
