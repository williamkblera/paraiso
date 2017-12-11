from django.shortcuts import render

from taggit.models import Tag

def tags(request):
    tags = Tag.objects.all()
    return render(request, 'tags/lista_tags.html', {'tags':tags})
