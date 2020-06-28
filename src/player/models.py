from django.db import models
from helper.models import DateModel
from team.models import Team


class PlayerHistory(DateModel):
    """
    schema to manage match played history data
    """
    total_match_played = models.PositiveSmallIntegerField(default=0)
    total_run = models.PositiveSmallIntegerField(default=0)
    highest_score = models.PositiveSmallIntegerField(default=0)
    fifties = models.PositiveSmallIntegerField(default=0)
    hundreds = models.PositiveSmallIntegerField(default=0)
    total_wickets = models.PositiveSmallIntegerField(default=0)
    strike_rate = models.FloatField(default=0.0)

    class Meta:
        db_table = "player_history"


class Player(DateModel):
    """
    schema to manage team players
    """
    player_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50, db_index=True)
    last_name = models.CharField(max_length=50, db_index=True)
    image_uri = models.URLField(null=True, blank=True)
    jersey_number = models.PositiveSmallIntegerField(default=0)
    home_team = models.ForeignKey(Team, null=True, on_delete=models.SET_NULL)
    player_history = models.ForeignKey(PlayerHistory, null=True, on_delete=models.SET_NULL)

    class Meta:
        db_table = "player"
