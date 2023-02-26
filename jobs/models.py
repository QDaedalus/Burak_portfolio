from django.db import models

class Job(models.Model):
    # Image
    image = models.ImageField(upload_to='images/')
    # summary
    summary = models.CharField(max_length=200)

# admin panelinde objelerin tanimlarini icin yaziyoruz
    def __str__(self):
        # print(self.pk)
        return self.summary