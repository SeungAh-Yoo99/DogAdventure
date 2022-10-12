from django.db import models

# Create your models here.
class AbandonedDog(models.Model) :
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)

    GENDER_CHOICES = (
		('male', '수컷'),
		('female', '암컷')
	)
    gender = models.CharField(max_length=8, choices=GENDER_CHOICES)

    airport = models.CharField(max_length=64)
    time_agreement = models.BooleanField(default=False)
    datetime = models.DateTimeField()
    weight = models.IntegerField()
    info = models.TextField()

    def __str__(self):
        return (self.name + '_' + str(self.id))


class Image(models.Model):
    id = models.AutoField(primary_key=True)
    dog = models.ForeignKey(AbandonedDog, on_delete=models.CASCADE, null=False)
    image = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return self.id