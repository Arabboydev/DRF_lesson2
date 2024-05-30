from django.db import models


class CategorySings(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        db_table = 'category_sings'

    def __str__(self):
        return self.name


class SingsRoad(models.Model):
    category = models.ForeignKey(CategorySings, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    video = models.FileField(upload_to='video/', blank=True, null=True)
    audio = models.FileField(upload_to='audio/', blank=True, null=True)
    dock = models.FileField(upload_to='dock/', blank=True, null=True)

    class Meta:
        db_table = 'sings_road'

    def __str__(self):
        return f"{self.category.name} {self.name}"