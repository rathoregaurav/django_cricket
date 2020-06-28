from django.db import models
from team.models import Team


class Match(models.Model):
    """
    schema to manage team matches history
    """
    match_id = models.AutoField(auto_now_add=True)
    match_timestamp = models.DateTimeField(auto_now=True)
    first_team = models.ForeignKey(Team, related_name="first_team", on_delete=models.CASCADE)
    second_team = models.ForeignKey(Team, related_name="second_team", on_delete=models.CASCADE)
    first_team_score = models.PositiveSmallIntegerField(default=0)
    second_team_score = models.PositiveSmallIntegerField(default=0)
    winner = models.ForeignKey(Team, related_name="winner", on_delete=models.CASCADE)

    class Meta:
        db_table = "matches"
