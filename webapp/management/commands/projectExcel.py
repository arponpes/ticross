from django.core.management.base import BaseCommand, CommandError
from core.models import Project
from openpyxl import Workbook


class Command(BaseCommand):
    help = 'Save the project in an excel'

    def handle(self, *args, **options):

        wb = Workbook()
        ws = wb.active
        projects = Project.objects.all()

        for p in projects:
            
            ws.append(['%s' % p.project_name,'  ', '%s' % p.description])
            ws.append([''])
            
        wb.save('project_list.xlsx')
        print('Command executed correctly.')
