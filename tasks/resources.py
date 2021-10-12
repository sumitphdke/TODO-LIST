from django.db.models.base import Model
from import_export import resources
from .models import Task
class TaskResources(resources.ModelResource):
    model=Task
    
