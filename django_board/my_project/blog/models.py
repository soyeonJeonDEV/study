from django.db import models

# Create your models here.
class Post(models.Model):

    title = models.CharField(max_length=300)

    writer = models.CharField(max_length=30)

    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "[id="+str(self.id)+",title="+self.title+",writer="+self.writer+",content="+self.content+",created_at="+str(self.created_at)+"]"
