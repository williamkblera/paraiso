from django.db import models
from django.contrib.contenttypes.models import ContentType

class Tag(models.Model):

    nome = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.nome

class TagItem(models.Model):

    class Meta:
        unique_together = ('tag', 'content_type', 'object_id')

    tag = models.ForeignKey('Tag')
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField(db_index=True)

def aplicar_tags(obj, tags):
    tipo_dinamico = ContentType.objects.get_for_model(obj)

    TagItem.objects.filter(
        content_type=tipo_dinamico,
        object_id=obj.id,
    ).delete()

    tags = tags.split(' ')
    for tag_nome in tags:
        tag, nova = Tag.objects.get_or_create(nome=tag_nome)

        TagItem.objects.get_or_create(
            tag=tag,
            content_type=tipo_dinamico,
            object_id=obj.id,
        )

def tags_para_objeto(obj):
    tipo_dinamico = ContentType.objects.get_for_model(obj)

    tags = TagItem.objects.filter(
        content_type=tipo_dinamico,
        object_id=obj.id,
    )

    return ' '.join([item.tag.nome for item in tags])
