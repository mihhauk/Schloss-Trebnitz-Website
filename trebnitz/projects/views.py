import models
from django.template import Context
from django.template.loader import get_template
from django.http import HttpResponse

def news(request):
    t = get_template("news.html")
    html = t.render(Context({'articles': models.Article.objects.all()}))
    return HttpResponse(html)