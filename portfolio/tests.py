from django.test import TestCase
from .models import Project
from datetime import date

class ProjectModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Project.objects.create(
            title='E-commerce', 
            description='Nuestro cliente solicitó realizar un sitio web en forma de comercio electrónico llamado AVC IMPORT', 
            image='portfolio/images/e.png', 
            url='https://github.com/Rosaidabhz/avcimport', 
            date=date(2023,2,14)
        )

    def test_title_label(self):
        project = Project.objects.get(id=1)
        field_label = project._meta.get_field('title').verbose_name
        self.assertEqual(field_label, 'title')

    def test_description_max_length(self):
        project = Project.objects.get(id=1)
        max_length = project._meta.get_field('description').max_length
        self.assertEqual(max_length, 250)

    def test_image_upload_to(self):
        project = Project.objects.get(id=1)
        upload_to = project._meta.get_field('image').upload_to
        self.assertEqual(upload_to, 'portfolio/images')

    def test_date_default_value(self):
        project = Project.objects.get(id=1)
        default_value = project._meta.get_field('date').default
        self.assertEqual(default_value, date.today())

    def test_url_blank(self):
        project = Project.objects.get(id=1)
        blank = project._meta.get_field('url').blank
        self.assertTrue(blank)

    def test_url_max_length(self):
        project = Project.objects.get(id=1)
        max_length = project._meta.get_field('url').max_length
        self.assertEqual(max_length, 200)
