from django.test import TestCase
from .models import Image,Comment,Profile

class ImageTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.james= Image(image_name = 'James')

    def test_instance(self):
        self.assertTrue(isinstance(self.james,Image))

    def test_save_method(self):
        self.james.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)

    def delete_image_method(self):
        self.james.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) == 0)

    def update_image_method(self):
        self.james.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)
