from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(default="title*", max_length=255)
    desc = models.TextField(default="desc*")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #books = 

    def __repr__(self):
        return f"Book ID: {self.id}| Title: {self.title}| Desc: {self.desc} ||"

class Author(models.Model):
    first_name = models.CharField(default="first name*", max_length=45)
    last_name = models.CharField(default="last name*", max_length=45)
    notes = models.TextField(default="notes*")
    books = models.ManyToManyField(Book, related_name="authors")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



    def __repr__(self):
        return f"Author ID: {self.id}| First Name: {self.first_name}| Last Name: {self.last_name}| Books: {self.books} ||"