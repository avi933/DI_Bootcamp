from django.db import migrations, models

class Family(models.Model):
    class Meta:
        verbose_name_plural = "Families"
    name = models.CharField(max_length=50)
    def __str__ (self):
        return f"{self.name}"

class Animal(models.Model):
    name = models.CharField(max_length=50 ,default="")
    legs = models.IntegerField()
    weight = models.FloatField()
    height = models.IntegerField()
    speed = models.FloatField()
    # family = models.CharField(max_length=50)
    family =models.ForeignKey(Family, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.name}"