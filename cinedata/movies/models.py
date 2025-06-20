from django.db import models

import uuid

# Create your models here.

class BaseClass(models.Model):

    uuid = models.SlugField(unique=True,default=uuid.uuid4)

    active_status = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:

        abstract = True

class IndustryChoices(models.TextChoices):

    MOLLYWOOD = 'Mollywood' , 'Mollywood'

    KOLLYWOOOD = 'Kollywood' , 'Kollywood'

    TOLLLYWOOD = 'Tollywood' , 'Tollywood'

    BOLLYWOOD = 'Bollywood' , 'Bollywood'

    HOLLYWOOD = 'Hollywood' , 'Hollywood'

    SANDALWOOD = 'Sandalwood' , 'Sandalwood'


class ProffessionChoices(models.TextChoices):

    ACTOR = 'Actor' , 'Actor'

    ACTRESS = ' Actress' , 'Actress'

    DIRECTOR = 'Director' , 'Director'

    MUSIC_DIRECTOR = 'Music Director' , 'Music Director'

    PRODUCER = 'Producer' , 'Producer'

class Artist(BaseClass):

    name = models.CharField(max_length=25)

    dob = models.DateField()

    photo = models.ImageField(upload_to='artist/')

    industry = models.CharField(max_length=20,choices=IndustryChoices.choices)

    proffession = models.CharField(max_length=50,choices=ProffessionChoices.choices)

    def __str__(self):

        return f'{self.name}-{self.proffession}'
    
    class Meta:

        verbose_name = 'Artist'

        verbose_name_plural = 'Artist'
    
class Genre(BaseClass):

    name = models.CharField(max_length=20)

    def __str__(self):

        return self.name
    
    class Meta:

        verbose_name = 'Genre'

        verbose_name_plural = 'Genre'

class Production(BaseClass):

    comp_name = models.CharField(max_length=50)

    owner = models.ForeignKey('Artist',on_delete=models.CASCADE)

    def __str__(self):

        return self.comp_name
    
    class Meta :

        verbose_name = 'Production'

        verbose_name_plural = 'Production'

class Movies(BaseClass):

    name = models.CharField(max_length=50)

    released_year = models.CharField(max_length=4)

    description = models.TextField()

    run_time = models.TimeField()

    genre = models.ForeignKey('Genre',on_delete=models.CASCADE)

    industry = models.CharField(max_length=20,choices=IndustryChoices.choices)

    photo = models.ImageField(upload_to = 'movies/')

    cast = models.ManyToManyField('Artist', related_name = 'cast')

    director = models.ForeignKey('Artist',on_delete=models.CASCADE,related_name='director')

    production = models.ForeignKey('Production',on_delete=models.CASCADE)

    music_director = models.ForeignKey('Artist',on_delete=models.CASCADE,related_name='music_director')

    def __str__(self):

        return f'{self.name}-{self.released_year}'
    
    class Meta :

        verbose_name = 'Movies'

        verbose_name_plural = 'Movies'