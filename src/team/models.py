from django.db import models
from helper.models import DateModel


class Country(models.Model):
    """
    country schema
    """
    country_id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=100)
    short_name = models.CharField(max_length=10)

    class Meta:
        db_table = "country"


class Team(DateModel):
    """
    schema to manage cricket teams
    """
    team_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, db_index=True)
    logo_uri = models.URLField()
    club_state = models.ForeignKey(Country, null=True, on_delete=models.SET_NULL)
    point = models.PositiveSmallIntegerField(default=0)

    class Meta:
        db_table = "cricket_teams"
