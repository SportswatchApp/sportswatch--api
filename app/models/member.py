from django.db import models


class Member(models.Model):
    user = models.ForeignKey(
        to='app.User',
        on_delete=models.CASCADE,
        verbose_name='Bruger'
    )
    club = models.ForeignKey(
        to='app.Club',
        on_delete=models.CASCADE,
        verbose_name='Klub'
    )
    joined_date = models.DateTimeField(
        auto_now_add=True
    )

    def is_trainee(self):
        return self.trainee_set.exists()

    def is_coach(self):
        return self.coach_set.exists()

    def is_admin(self):
        return self.admin_set.exists()

    class Meta:
        unique_together = ('user', 'club',)
