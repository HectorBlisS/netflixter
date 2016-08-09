from django.db import models

from django.conf import settings


class Profile(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL)
	date_of_birth = models.DateField(blank=True,null=True)
	# photo = models.ImageField(upload_to="users/%Y/%m/%d",blank=True)
	telefono = models.CharField(max_length=10, null = True)


	def __str__(self):
		return 'Perfil del usuario {}'.format(self.user.username)