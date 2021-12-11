from django.db import models

# Create your models here.


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=40)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=30)
    contactNumber = models.CharField(max_length=15)
    userCollegeName = models.CharField(max_length=30)
    photos = models.ImageField(upload_to='images/')

    USERNAME_FIELD = 'full_name'

    def __str__(self):
        return self.user_id


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=40)
    date = models.DateTimeField(auto_now_add=True)
    text = models.TextField(max_length=3000, blank=True)
    rating = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.user.user_id


class College(models.Model):
    college_id = models.AutoField(primary_key=True)
    college_name = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    website_url = models.CharField(max_length=40)
    college_reviews = models.ForeignKey(Review, on_delete=models.CASCADE)
    college_rating = models.IntegerField
    college_description = models.TextField(max_length=150)
    contact_number = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    program = models.CharField(max_length=10)
    college_photos = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.college_id
