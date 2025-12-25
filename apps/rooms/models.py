from django.db import models

# Create your models here.

class Rooms(models.Model):
    room_no = models.IntegerField(primary_key=True, null=False,blank=False)
    room_capacity = models.IntegerField(default=0)
    room_type = models.CharField(max_length=100, null=False,blank=False)
    room_price = models.IntegerField(default=0)
    room_status = models.CharField(max_length=100, null=False,blank=False)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        room_no = str(self.room_no)
        return room_no




