from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField


class Personal(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    person = models.ForeignKey(User, on_delete=models.CASCADE) #todo: Place editable = False after logged in user = person config
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    p_summary = models.TextField()
    age = models.IntegerField()

    class Meta:
        verbose_name_plural = 'Personal Details'

    def __str__(self):
        return self.person.username


class Contact(models.Model):
    person = models.ForeignKey(User, on_delete=models.CASCADE) #todo: Place editable = False after logged in user = person config
    email = models.EmailField()
    phone_number = PhoneNumberField()
    address = models.TextField()
    linkedin = models.URLField(null=True, blank=True, verbose_name='Linked-In URL')

    class Meta:
        verbose_name_plural = 'Contact Details'

    def __str__(self):
        return self.person.username


class Skill(models.Model):
    person = models.ForeignKey(User, on_delete=models.CASCADE) #todo: Place editable = False after logged in user = person config
    name = models.CharField(max_length=250)
    rating = models.IntegerField(help_text='Rate this skill as a percentage')

    class Meta:
        verbose_name_plural = 'Career Skills'

    def __str__(self):
        return self.name


class Experience(models.Model):
    person = models.ForeignKey(User, on_delete=models.CASCADE) #todo: Place editable = False after logged in user = person config
    worked_from = models.DateField()
    worked_until = models.DateField()
    position = models.CharField(max_length=250)
    organization = models.CharField(max_length=250)
    description = models.TextField() # todo: insert WYSIWYG editor here

    class Meta:
        verbose_name_plural = 'Working Experience'

    def __str__(self):
        return self.position


class Language(models.Model):
    person = models.ForeignKey(User, on_delete=models.CASCADE) #todo: Place editable = False after logged in user = person config
    name = models.CharField(max_length=250)

    class Meta:
        verbose_name_plural = 'Languages'

    def __str__(self):
        return self.name


class Hobby(models.Model):
    person = models.ForeignKey(User, on_delete=models.CASCADE) #todo: Place editable = False after logged in user = person config
    name = models.CharField(max_length=250)

    class Meta:
        verbose_name_plural = 'Hobbies'

    def __str__(self):
        return self.name


class Education(models.Model):
    person = models.ForeignKey(User, on_delete=models.CASCADE) #todo: Place editable = False after logged in user = person config
    start_date = models.DateField()
    end_date = models.DateField()
    institution = models.CharField(max_length=300)
    qualification = models.CharField(max_length=300)

    class Meta:
        verbose_name_plural = 'Education Attainment'

    def __str__(self):
        return self.qualification


class Reference(models.Model):
    TITLE_CHOICES = (
        ('Mr', 'Mr'),
        ('Miss', 'Miss'),
        ('Mrs', 'Mrs'),
        ('Ms', 'Ms'),
        ('Dr', 'Dr'),
        ('Prof', 'Prof'),
        ('Hon', 'Hon'),
        ('Rev', 'Rev'),
        ('Gen', 'Gen'),
        ('Capt', 'Capt'),
        ('Sister', 'Sister'),
        ('Brother', 'Brother'),
    )
    person = models.ForeignKey(User, on_delete=models.CASCADE) #todo: Place editable = False after logged in user = person config
    title = models.CharField(max_length=10, choices=TITLE_CHOICES)
    fullname = models.CharField(max_length=250, help_text='It is always professional to start with the LastName of the person')
    position = models.CharField(max_length=250)
    organization = models.CharField(max_length=250)
    email = models.EmailField()
    phone_number = PhoneNumberField()

    class Meta:
        verbose_name_plural = 'References'

    def __str__(self):
        return self.fullname
