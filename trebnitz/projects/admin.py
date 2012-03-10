from django.contrib import admin
from trebnitz.projects.models import *

admin.site.register(Person)
admin.site.register(Project)
admin.site.register(Article)
admin.site.register(Tag)