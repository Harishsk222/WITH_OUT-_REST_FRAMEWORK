from django.db import models

class Student (models.Model):
    name=models.CharField(max_length=20)
    rollno=models.IntegerField()
    marks=models.FloatField()
    address=models.CharField( max_length=255)
    def __str__(self):
       return self.name

#     def get_absolute_url(self):
#         return reverse("_detail", kwargs={"pk": self.pk})
# )
