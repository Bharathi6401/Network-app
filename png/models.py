from django.db import models



class Reg(models.Model):
    company_name = models.CharField(max_length=200)
    company_logo=models.ImageField(upload_to='logos/')
    email=models.EmailField(max_length=100, null=True )
    password=models.CharField(max_length=100, null=True)
    youtube_URL=models.URLField(null=True)


    def __str__(self):
        return self.company_name




class news(models.Model):
    title=models.CharField(max_length=100)
    image=models.ImageField(upload_to='news_img')
    date=models.DateField(auto_now_add=True,null=True)
    details=models.TextField(max_length=250)

    def __str__(self):
        return f"{self.title} {self.date}"




class event(models.Model):
    title=models.CharField(max_length=100)
    event_img = models.ImageField('event_img')
    event_date =models.DateField(auto_now_add=True,null=True)
    details = models.TextField(max_length=250)

    def __str__(self):
        return f"{self.title} {self.event_date}"












