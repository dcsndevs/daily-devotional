from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "draft"), (1, "published"))


class Post(models.Model):
    """
    Stores a single devotional post entry related to :model:`auth.User`.
    """

    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name="devotional_posts",
                               default=1, null=False)
    slug = models.SlugField(max_length=250, unique=True)
    title = models.CharField(max_length=200, unique=True)
    active_date = models.DateField()
    memory_verse = models.TextField(max_length=1500, null=True, blank=True)
    content = models.TextField(max_length=4000, null=True, blank=True)
    bible_reading_plan1 = models.CharField(max_length=30,
                                           null=True, blank=True)
    bible_reading_plan2 = models.CharField(max_length=30,
                                           null=True, blank=True)
    background_image = CloudinaryField('image', default='placeholder')
    title_image = CloudinaryField('image', default='placeholder2')
    status = models.IntegerField(choices=STATUS, default=1)
    likes = models.ManyToManyField(User, related_name="devotional_likes",
                                   blank=True)

    class Meta:
        ordering = ['-active_date']

    def __str__(self):
        return f"{self.active_date} | {self.title}"

    def number_of_likes(self):
        return self.likes.count()


class Comment(models.Model):
    """
    Stores a single comment entry related to :model:`auth.User`
    and :model:`devotional.Post`.
    """

    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name="comments", null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name="commenter", null=True, blank=True)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=True)
    likes2 = models.ManyToManyField(User,
                                    related_name="comment_likes", blank=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f"Comment by {self.author}"

    def likes2_count(self):
        return self.likes2.count()
