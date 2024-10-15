from django.db import models
from django.utils.text import slugify
from django.db.models.signals import pre_save
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=50, default="")
    image = models.ImageField(upload_to = 'Category Image/', default = "")
    cat_slug = models.SlugField(max_length=500, null=True, blank=True, unique=True)


    def __str__(self):
        return self.name

class Post(models.Model):
    STATUS = (
        ('0', 'Draft'),
        ('1', 'Publish'),
    )

    SECTION = (
        ('Popular','Popular'),
        ('Recent','Recent'),
        ('Editors_Pick','Editors_Pick'),
        ('Treanding','Treanding'),
        ('Inspiration','Inspiration'),
        ('Latest_Post','Latest_Post'),
        ('Main_Post', 'Main_Post'),
    )
    Featured_Image = models.ImageField(upload_to = 'Featured Image')
    Title = models.CharField(max_length=200)
    Author = models.CharField(max_length=50)
    Category = models.ForeignKey(Category, on_delete=models.CASCADE)
    Date = models.DateField(auto_now_add=True)
    # Content = models.TextField()
    Content = RichTextField()
    slug = models.SlugField(max_length=500, null=True, blank=True, unique=True)
    Status = models.CharField(choices=STATUS, max_length=100)
    Section = models.CharField(choices=SECTION, max_length=200)
    Main_Post = models.BooleanField(default=False)
    

    def __str__(self):
        return self.Title
    
def create_slug(instance, new_slug = None):
    slug = slugify(instance.Title)
    if new_slug is not None:
        slug = new_slug
    qs = Post.objects.filter(slug = slug).order_by('-id')
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" %(slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug




def pre_save_post_reciever(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)
pre_save.connect (pre_save_post_reciever, Post)


class Tag(models.Model):
    Name  = models.CharField(max_length=100)
    Post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.Name


class ContactSubmission(models.Model):
    name = models.CharField(max_length=30, default="")
    email = models.EmailField()
    subject = models.CharField(max_length=50, default="")
    message = models.TextField()

    def __str__(self):
        return self.subject


