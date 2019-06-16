from django.test import TestCase
from .models import Location,Category,Image

class ImageTestCases(TestCase):
    def setUp(self):
        self.new_category = Category(category_name='Travel')
        self.new_category.save_category()
        self.new_location = Location(location_name = 'Diani')
        self.new_location.save_location()
        self.new_image = Image(id=1,image_name='beach', image_description='Beach Life',image_path='media/mygallery/beach-3134828_1920.jpg',image_category=self.new_category,image_location=self.new_location)
    

    def tearDown(self):
        Category.objects.all().delete()
        Location.objects.all().delete()
        Image.objects.all().delete()


    def test_is_instance(self):
        self.assertTrue(isinstance(self.new_image,Image))
        self.assertTrue(isinstance(self.new_category,Category))
        self.assertTrue(isinstance(self.new_location,Location))


    def test_save_method(self):
        self.new_image.save_image()
        all_objects = Image.objects.all()
        self.assertTrue(len(all_objects)>0)


    def test_delete_method(self):
        self.new_image.save_image()
        filtered_object = Image.objects.filter(image_name='beach')
        Image.delete_image(filtered_object)
        all_objects = Image.objects.all()
        self.assertTrue(len(all_objects) == 0)


    def test_display_all_objects_method(self):
        self.new_image.save_image()
        all_objects = Image.retrieve_all()
        self.assertEqual(all_objects.image_name,'beach')


    def test_update_single_object_property(self):
        self.new_image.save_image()
        filtered_object =Image.update_image('beach','Ocean')
        fetched = Image.objects.get(image_name='Ocean')
        self.assertEqual(fetched.image_name,'Ocean')


    def test_get_image_by_id(self):
        self.new_image.save_image()
        fetched_image = Image.get_image_by_id(1)
        self.assertEqual(fetched_image.id,1)


    def test_search_by_category(self):
        self.new_image.save_image()        
        fetch_specific = Category.objects.get(category_name='Travel')
        self.assertTrue(fetch_specific.category_name=='Travel')


    def test_filter_by_location(self):
        self.new_image.save_image()        
        fetch_specific = Location.objects.get(location_name='Diani')
        self.assertTrue(fetch_specific.location_name=='Diani')