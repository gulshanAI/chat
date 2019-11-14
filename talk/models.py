from django.db import models
from django.contrib.auth.models import User


class Baatkare(models.Model):
    userbot = models.ForeignKey(User, related_name="foruserbot", on_delete=models.CASCADE)
    oppsbot = models.ForeignKey(User, related_name="foroppsbot", on_delete=models.CASCADE)
    chatmsg = models.TextField()
    reply = models.ForeignKey(User, related_name="for_reply", on_delete=models.CASCADE)
    msgdate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.chatmsg