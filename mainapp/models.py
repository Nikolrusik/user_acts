from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import datetime


class Person(models.Model):
    GENDER_CHOICES: list = [
        ('М', 'Мужчина'),
        ('Ж', 'Женщина')
    ]

    firstname: str = models.CharField(max_length=255, verbose_name='Firstname')
    lastname: str = models.CharField(max_length=255, verbose_name='Lastname')
    gender: str = models.CharField(
        max_length=10, choices=GENDER_CHOICES, verbose_name='Gender')
    blood_type: str = models.CharField(
        max_length=100, verbose_name='Blood type')
    is_jobless: bool = models.BooleanField(
        blank=True, null=True, verbose_name='Is jobless')
    is_married: bool = models.BooleanField(
        default=False, verbose_name='Is married')

    def __repr__(self):
        return f'Person(firstname={self.firstname}, lastname={self.lastname}, gender={self.gender}, blood_type={self.blood_type}, is_jobless={self.is_jobless}, is_married={self.is_married})'

    def __str__(self):
        return f"{self.firstname} {self.lastname}"


class Address(models.Model):
    city: str = models.CharField(max_length=255, verbose_name='City')
    postal_code: int = models.IntegerField(verbose_name='Postal code')
    address: str = models.TextField(verbose_name='Address')
    registered: str = models.CharField(
        max_length=255, verbose_name='Registered name')

    person: Person = models.ForeignKey(Person, on_delete=models.CASCADE,
                                       verbose_name='Person ID',
                                       related_name='address')

    def __str__(self):
        return f"{self.person} {self.city}"


class Action(models.Model):
    description: str = models.TextField(
        blank=True, null=True, verbose_name='Action description')
    estimation: int = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)], verbose_name='Act estimation')
    date: str = models.DateTimeField(
        default=datetime.utcnow, verbose_name='Date act')

    person: Person = models.ForeignKey(
        Person, on_delete=models.CASCADE, verbose_name='Person', related_name='actions')

    def __repr__(self):
        return f"<Action(person={self.person}, estimation={self.estimation})>"

    def __str__(self):
        return f'Person={self.person} - {self.pk}'
