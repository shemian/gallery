from django.db import models

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=30)
    id =models.IntegerField()
    
    def __str__(self):
        return self.name
    
    def save_location(self):
        self.save
        
    def delete_location(self):
        self.delete
        
        
    @classmethod
    def update_location(cls,id,value):
        cls.objects.filter(id=id).update(name=value)
    
    @classmethod
    def get_location(cls):
        locations = Location.objects.all()
        return locations
    
class Category(models.Model):
    name = models.CharField(max_length=30)
    id = models.IntegerField()
    
    def __str__(self):
        return self.name
    
    def save_category(self):
        self.save
        
    def delete_category(self):
        self.delete
        
    @classmethod
    def update_category(cls,id,value):
        cls.objects.filter(id=id).update(name=value)
    
    @classmethod 
    def get_category(cls):
        categorys = Category.objects.all()
        return categorys
    
    
class Image(models.Model):
    id =models.IntegerField()
    image = models.ImageField(upload_to='pics')
    name = models.CharField(max_length=60)
    description = models.TextField()
    author = models.CharField(max_length=40,default='admin')
    date = models.DateTimeField(auto_now_add=True,)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    location = models.ForeignKey(Location,on_delete=models.CASCADE)
     
    def __str__(self):
        return self.name
    
    def save_image(self):
        self.save
        
    def delete_image(self):
        self.delete
        
    @classmethod
    def get_all_images(cls):
        images = cls.objects.all()
        return images
    
    @classmethod
    def update_image(cls,id,value):
        cls.objects.filter(id=id).update(image=value,)
    
    
    @classmethod
    def get_image_by_id(cls):
        image = cls.objects.filter(id= id).all()
        return image

    @classmethod
    def filter_by_location(cls, location):
        image_location = Image.objects.filter(location__name=location).all()
        return image_location

    @classmethod
    def filter_by_category(cls, category):
        image_category = Image.objects.filter(category__name=category).all()
        return image_category

    @classmethod
    def search_by_category(cls, category):
        images = cls.objects.filter(category__name__icontains=category)
        return images