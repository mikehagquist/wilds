from django.db import models


# class Question(models.Model):
#     question_text = models.CharField(max_length=200)
#     pub_date = models.DateTimeField('date published')
#
#
# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)

class Animal(models.Model):
    animal_name = models.CharField(max_length=200)


class Phylum(models.Model):
    phylum_name = models.ForeignKey(Animal, on_delete=models.CASCADE)


class Class(models.Model):
    class_name = models.ForeignKey(Animal, on_delete=models.CASCADE)


class Order(models.Model):
    order_name = models.ForeignKey(Animal, on_delete=models.CASCADE)


class Family(models.Model):
    family_name = models.ForeignKey(Animal, on_delete=models.CASCADE)


class Genus(models.Model):
    genus_name = models.ForeignKey(Animal, on_delete=models.CASCADE)


class Species(models.Model):
    species_name = models.ForeignKey(Animal, on_delete=models.CASCADE)
