from django.db import models
from django.contrib.auth import models as auth_models
from django.utils.translation import ugettext_lazy as _

from userena.models import UserenaBaseProfile


class Profile(UserenaBaseProfile):
    user = models.OneToOneField(auth_models.User,
                                unique=True,
                                verbose_name=_('user'),
                                related_name='profile')
