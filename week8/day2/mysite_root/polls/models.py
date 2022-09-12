from django.db import migrations, models

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    birth_date = models.DateField()
    has_pet = models.BooleanField(default=True)
    number_pet = models.IntegerField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"