from django.db import models

class Animal(models.Model):
    type = models.CharField(max_length=50, null=True)
    kind = models.CharField(max_length=50, null=True)
    name = models.CharField(max_length=50, null=True)
    age = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Owner(models.Model):
    name_surname = models.CharField(max_length=150, null=True)
    animal = models.ManyToManyField(Animal, blank=True, null=True)
    phone = models.CharField(max_length=150, null=True)
    mail = models.CharField(max_length=150, null=True)

    def get_animals(self):
        return ",".join([str(p) for p in self.animal.all()])
    
    def __str__(self):
        return self.name_surname
