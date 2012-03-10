from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    email = models.EmailField()

    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)


class Organiser(Person):
    pass
    

class Participant(Person):
    pass


class Project(models.Model):
    name = models.CharField(max_length=30)
    organiser = models.ManyToManyField(Organiser)
    participants = models.ManyToManyField(Participant)
    start_date = models.DateField()
    max_participants_number = models.IntegerField()
    
    def __unicode__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=30)   
    
    def __unicode__(self):
        return self.name    


class Article(models.Model):
    title = models.CharField(max_length=30, blank=True)
    author = models.CharField(max_length=30)
    text = models.TextField()
    publication_date = models.DateField(max_length=1000)
    tags = models.ManyToManyField(Tag)
    
    def __unicode__(self):
        return self.title
