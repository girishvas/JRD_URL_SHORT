from django_elasticsearch_dsl import DocType, fields
from django_elasticsearch_dsl.registries import registry
from .models import urldetails
from django.contrib.auth.models import User


@registry.register_document
class urldetailsDocument(DocType):
    user = fields.ObjectField(properties={
            'pk': fields.IntegerField(),
            'username': fields.TextField(),
        })
        
    class Index:
        name = 'urldetails'
        settings = {'number_of_shards': 1,
                    'number_of_replicas': 0}

    class Django:
        model = urldetails 
        fields = [
            'full_url',
            'name',
            'short_url',
            'key',
            'created_on',
            'updated_on',
            
        ]
        related_models = [User]
    
    def get_queryset(self):
        return super(urldetailsDocument, self).get_queryset().select_related(
            'user',
        )
           
    def get_instances_from_related(self, related_instance):
        if isinstance(related_instance, User):
            return related_instance.urldetails_set.all()
