from __future__ import unicode_literals

from django.db import models


class Players(models.Model):
    pid = models.CharField(db_column='PID', primary_key=True, max_length=20)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=255, blank=True, null=True)  # Field name made lowercase.
    team = models.CharField(db_column='TEAM', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PLAYERS'


class PlayerVals(models.Model):
    pid = models.ForeignKey(Players,db_column='PID',primary_key=True)
    value = models.FloatField(db_column='VALUE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PLAYER_VALS'


class Stats(models.Model):
    pid = models.ForeignKey(Players,db_column='pid')
    gameid = models.CharField(db_column='gameid',max_length=20, blank=True, null=True)
    points = models.IntegerField(db_column='POINTS', blank=True, null=True)  # Field name made lowercase.
    steals = models.IntegerField(db_column='STEALS', blank=True, null=True)  # Field name made lowercase.
    rebounds = models.IntegerField(db_column='REBOUNDS', blank=True, null=True)  # Field name made lowercase.
    assists = models.IntegerField(db_column='ASSISTS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'STATS'


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class Pf(models.Model):
    user   = models.ForeignKey(AuthUser,db_column='user')
    pid    = models.ForeignKey(Players,db_column='pid')
    shares = models.IntegerField(db_column="shares")
    id     = models.CharField(max_length=20,primary_key=True)

    # calculated field
    @property
    def player_pf_val(self):
        return self.shares * PlayerVals.objects.get(pid=self.pid.pid).value

    class Meta:
        managed = False
        db_table = 'PF'
        unique_together = (('user', 'pid'),)


class PfValue(models.Model):
    user = models.ForeignKey(AuthUser,db_column='user',primary_key=True)
    cash = models.FloatField(db_column='cash')

    @property
    def assets(self):
        return sum([player.player_pf_val for player in Pf.objects.filter(user=self.user_id).all()])

    @property
    def net_worth(self):
        return self.assets + self.cash

    class Meta:
        managed = False
        db_table = 'PF_VALUE'

