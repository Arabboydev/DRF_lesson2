from django.db import models


class CategorySigns(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        db_table = 'category_signs_road'

    def __str__(self):
        return self.name


class SignsRoad(models.Model):
    category = models.ForeignKey(CategorySigns, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    video = models.FileField(upload_to='video/', blank=True, null=True)
    audio = models.FileField(upload_to='audio/', blank=True, null=True)
    dock = models.FileField(upload_to='dock/', blank=True, null=True)

    class Meta:
        db_table = 'signs_road'

    def __str__(self):
        return f"{self.category.name} <-> {self.name}"
