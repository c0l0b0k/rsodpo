from demo.views import run_repeating_task


from django.core.management import BaseCommand


class Command(BaseCommand):
    help = 'The Zen of Python'

    def handle(self, *args, **options):
        run_repeating_task()