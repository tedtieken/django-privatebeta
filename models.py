import datetime
from django.db import models
from django.utils.translation import ugettext_lazy as _

class InviteRequest(models.Model):
    email = models.EmailField(_('Email address'), unique=True)
    created = models.DateTimeField(_('Created'), default=datetime.datetime.now)
    note = models.TextField(_('Note'), max_length=5000, blank=True, null=True)
    invited = models.BooleanField(_('Invited'), default=False)

    def __unicode__(self):
        return _('Invite for %(email)s') % {'email': self.email}
