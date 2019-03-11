from django.test import TestCase
from .models import Image,Comment,Profile

class ImageTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.james= Image(image_name = 'James')
        self.james.save_image()

    # self.new_profile = Profile(name = 'testing')
    # self.new_profile.save()

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


# class ProfileTestClass(TestCase):

#     # Set up method
#     def setUp(self):
#         self.james = Profile(profile_photo = 'James')
#         self.james = Profile(name = 'James')
#         self.james = Profile(bio = 'James')
#         self.jamesmusyoka.save_profile()

#     self.new_profile = tags(name = 'testing')
#     self.new_profile.save()

#     def test_instance(self):
#         self.assertTrue(isinstance(self.james,Profile))

#     def test_save_method(self):
#         self.james.save_profile()
#         profiles = Profile.objects.all()
#         self.assertTrue(len(profiles) > 0)

#     def delete_profile_method(self):
#         self.james.save_Profile()
#         profiles = Profile.objects.all()
#         self.assertTrue(len(profiles) == 0)

#     def update_profile_method(self):
#         self.james.save_profile()
#         profiles = Profile.objects.all()
#         self.assertTrue(len(profiles) > 0)



class CommentTestClass(TestCase):

    def test_save_method(self):
        self.comment.save_comment()
        comments = Comment.objects.all()
        self.assertTrue(len(comments) > 0)  

    # def delete_comment_method(self):
    #     self.comment.save_comment()
    #     self.comment.delete_comment()
    #     self.assertTrue(len(comments) == 0)
