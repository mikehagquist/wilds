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


class Phylum(models.Model):
    phylum_name = models.CharField(max_length=200)

    def __str__(self):
        return self.phylum_name

    class Meta:
        verbose_name_plural = "1. Phylum"


class ClassA(models.Model):
    class_name = models.CharField(max_length=200)

    def __str__(self):
        return self.class_name

    class Meta:
        verbose_name_plural = "2. Class"
        verbose_name = "class"


class Order(models.Model):
    order_name = models.CharField(max_length=200)

    def __str__(self):
        return self.order_name

    class Meta:
        verbose_name_plural = "3. Order"


class Family(models.Model):
    family_name = models.CharField(max_length=200)

    def __str__(self):
        return self.family_name

    class Meta:
        verbose_name_plural = "4. Family"


class Genus(models.Model):
    genus_name = models.CharField(max_length=200)

    def __str__(self):
        return self.genus_name

    class Meta:
        verbose_name_plural = "5. Genus"


class Species(models.Model):
    species_name = models.CharField(max_length=200)

    def __str__(self):
        return self.species_name

    class Meta:
        verbose_name_plural = "6. Species"


class Animal(models.Model):
    animal_name = models.CharField(max_length=200)
    phylum = models.ForeignKey(Phylum, on_delete=models.CASCADE)
    classa = models.ForeignKey(ClassA, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    family = models.ForeignKey(Family, on_delete=models.CASCADE)
    genus = models.ForeignKey(Genus, on_delete=models.CASCADE)
    species = models.ForeignKey(Species, on_delete=models.CASCADE)

    def __str__(self):
        return self.animal_name
