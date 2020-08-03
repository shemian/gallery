from django.test import TestCase
from .models import Image,Category,Location


# Create your tests here.
class TestImage(TestCase):
    #Setup Method
    def setUp(self):
        self.location = Location(name='Moringa')
        self.location.save_location()

        self.category = Category(name='home')
        self.category.save_category()

        self.image_test = Image(id=1, name='image', description='this is a test image', location=self.location, category=self.category)
    
    #Test save image
    def test_save_image(self):
        self.image_test.save_image()
        after = Image.objects.all()
        self.assertTrue(len(after) > 0)

    #Test delete image
    def test_delete_image(self):
        self.image_test.delete_image()
        images = Image.objects.all()
        self.assertTrue(len(images) == 0)

    #Test Update Image
    def test_update_image(self):
        self.image_test.save_image()
        self.image_test.update_image(self.image_test.id, 'photos/test.jpg')
        changed_img = Image.objects.filter(image='photos/test.jpg')
        self.assertTrue(len(changed_img) > 0)

    #Test get image by id
    def test_get_image_by_id(self):
        found_image = self.image_test.get_image_by_id(self.image_test.id)
        image = Image.objects.filter(id=self.image_test.id)
        self.assertTrue(found_image, image)

    #Test search image bu location
    def test_search_image_by_location(self):
        self.image_test.save_image()
        found_images = self.image_test.filter_by_location(location='moringa')
        self.assertTrue(len(found_images) == 1)

    #Test search image by category
    def test_search_image_by_category(self):
        category = 'home'
        found_img = self.image_test.search_by_category(category)
        self.assertTrue(len(found_img) > 1)

    def tearDown(self):
        Image.objects.all().delete()
        Location.objects.all().delete()
        Category.objects.all().delete()


class TestLocation(TestCase):
    #Setup Method
    def setUp(self):
        self.location = Location(name='Moringa')
        self.location.save_location()

    #Test instance
    def test_instance(self):
        self.assertTrue(isinstance(self.location, Location))

    #Test save location
    def test_save_location(self):
        self.location.save_location()
        locations = Location.get_locations()
        self.assertTrue(len(locations) > 0)

    #Test search location
    def test_get_locations(self):
        self.location.save_location()
        locations = Location.get_locations()
        self.assertTrue(len(locations) > 1)

    #Test update location
    def test_update_location(self):
        new_location = 'kericho'
        self.location.update_location(self.location.id, new_location)
        changed_location = Location.objects.filter(name='kericho')
        self.assertTrue(len(changed_location) > 0)

    #Test delete location
    def test_delete_location(self):
        self.location.delete_location()
        location = Location.objects.all()
        self.assertTrue(len(location) == 0)


class TestCategory(TestCase):
    #Set up Method
    def setUp(self):
        self.category = Category(name='creativity')

    def tearDown(self):

        Category.objects.all().delete()

    # Testing instance
    def test_instances(self):
        self.assertTrue(isinstance(self.category, Category))

     #Test for saving method
    def test_save_category(self):
        self.category.save_category()
        categories = Category.objects.all()
        self.assertFalse(len(categories)>0)


    #Test for updating category    
    def test_update_category(self):
        new_category_name = 'Art'
        self.category.update_category(self.category.id,new_category_name)
        updated_category = Category.objects.filter(name='Art')
        self.assertFalse(len(updated_category)>0)


    #Test for deleting category
    def test_delete_category(self):
        self.category.delete_category()
        category = Category.objects.all()
        self.assertTrue(len(category)==0)

