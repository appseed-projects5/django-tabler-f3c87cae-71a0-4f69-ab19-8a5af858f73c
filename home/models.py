# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Roles(models.Model):

    #__Roles_FIELDS__
    nom = models.CharField(max_length=255, null=True, blank=True)

    #__Roles_FIELDS__END

    class Meta:
        verbose_name        = _("Roles")
        verbose_name_plural = _("Roles")


class Users(models.Model):

    #__Users_FIELDS__
    prenoms = models.CharField(max_length=255, null=True, blank=True)
    nom = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)
    passwordhashed = models.CharField(max_length=255, null=True, blank=True)
    id = models.CharField(max_length=255, null=True, blank=True)

    #__Users_FIELDS__END

    class Meta:
        verbose_name        = _("Users")
        verbose_name_plural = _("Users")


class Etablissements(models.Model):

    #__Etablissements_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)

    #__Etablissements_FIELDS__END

    class Meta:
        verbose_name        = _("Etablissements")
        verbose_name_plural = _("Etablissements")


class Caosp(models.Model):

    #__Caosp_FIELDS__
    service = models.CharField(max_length=255, null=True, blank=True)
    adresse = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    responsable = models.CharField(max_length=255, null=True, blank=True)

    #__Caosp_FIELDS__END

    class Meta:
        verbose_name        = _("Caosp")
        verbose_name_plural = _("Caosp")



#__MODELS__END
