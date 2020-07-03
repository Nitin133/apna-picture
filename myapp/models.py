from django.db import models

# Create your models here.
# create categories model

class category(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    def __str__(self):
        return self.title
#create image model
class image(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField()
    image=models.ImageField(upload_to="images")
    added_date=models.DateTimeField()
    cat=models.ForeignKey(category,on_delete=models.CASCADE)
    def __str__(self):
        return self.title