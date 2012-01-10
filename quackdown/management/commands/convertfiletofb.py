from django.core.management.base import BaseCommand, CommandError
from quackdown.models import Document

class Command(BaseCommand):
    help = 'Updates old file fields to filebrowser fields.'

    def handle(self, *args, **options):
        for document in Document.objects.all():
            document.file.path = u'/media/' + document.file.path 
            document.save()


