from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    user= models.ForeignKey(User,on_delete=models.CASCADE, related_name="posts",verbose_name="Usuario")
    image=models.ImageField(upload_to="posts_image/", verbose_name="Imagen")
    caption=models.TextField(max_length=500,blank=True, verbose_name="Descripcion")
    created_at=models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    likes=models.ManyToManyField(User,related_name="liked_posts",blank=True,verbose_name="Nº de likes")

    class Meta:
        verbose_name="post"
        verbose_name_plural="posts"

    def __str__(self):
        return f"{self.user.username} - {self.created_at}"
    
class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name="comments")
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="comments")
    text = models.TextField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name="comentario"
        verbose_name_plural="comentarios"
    
    
    def __str__(self):
        return f"Comento {self.user.username} el post {self.post}"
