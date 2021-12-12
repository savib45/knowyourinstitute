from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    contactNumber = models.CharField(max_length=15)
    userCollegeName = models.CharField(max_length=30)
    photos = models.ImageField(upload_to='images/', default='https://mpchsschool.in/wp-content/uploads/2019/10/default-profile-picture.png')


    def __str__(self):
        return self.user.first_name


class College(models.Model):
    college_id = models.AutoField(primary_key=True)
    college_name = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    website_url = models.CharField(max_length=40)
    college_description = models.TextField(max_length=500)
    contact_number = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    program = models.CharField(max_length=50)
    college_photos = models.ImageField(upload_to='images/')

    def reviews(self):
        return Review.objects.filter(college = self).all()

    def __str__(self):
        return self.college_name

class Review(models.Model):
    college = models.ForeignKey(College,on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    text = models.TextField(max_length=3000, blank=True)
    rating = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.college.college_name




