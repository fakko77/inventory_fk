from django.core.management.base import BaseCommand, no_translations
from django.core.exceptions import ObjectDoesNotExist
from app_inventory_fk.models import Marque, Type, Department


class Command(BaseCommand):
    @no_translations
    def handle(self, *args, **options):
        file = open("app_inventory_fk/management/commands/doc/marque.txt", "r")
        line = file.readline()
        while line:
            tab = line.split("	")
            name = tab[0]
            url = tab[1]
            logo_img_url = tab[2]
            print(name, url, logo_img_url)
            marque_add = Marque(name=name, url=url, logo_img_url=logo_img_url, optional_info="")
            marque_add.save()
            line = file.readline()
        file.close()

        file = open("app_inventory_fk/management/commands/doc/type.txt", "r")
        line = file.readline()
        while line:
            tab = line.split("	")
            name = tab[0]
            print(name)
            type_add = Type(name=name)
            type_add.save()
            line = file.readline()
        file.close()

        file = open("app_inventory_fk/management/commands/doc/department.txt", "r")
        line = file.readline()
        while line:
            tab = line.split("	")
            name = tab[0]
            print(name)
            department_add = Department(name=name, optional_info="")
            department_add.save()
            line = file.readline()
        file.close()








