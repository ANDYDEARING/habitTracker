from django.db import models
from datetime import date
from django.contrib.auth.models import User


class Habit(models.Model):
    verb = models.CharField(max_length=200)
    over = models.BooleanField(default=True)
    quantity = models.PositiveIntegerField(default=0)
    unit = models.CharField(max_length=200)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    buddies = models.ManyToManyField(User, related_name="habits")

    def __str__(self):
        if self.over == True:
            over_str = "over"
        else:
            over_str = "under"
        return f'{self.verb} {over_str} {self.quantity} {self.unit} per day'
    
    def last_update(self):
        """returns the DailyRecord object of the last update"""
        return self.dailyrecord_set.order_by('-date').first()


class DailyRecord(models.Model):
    date = models.DateField(default=date.today)
    quantity = models.PositiveIntegerField(default=0)
    habit = models.ForeignKey(Habit, on_delete=models.CASCADE)
    
    def meets_goal(self):
        """returns True if goal is met or exceeded, otherwise False"""
        if self.habit.over:
            return self.quantity >= self.habit.quantity
        else:
            return self.quantity <= self.habit.quantity

    def __str__(self):
        return f"{self.date}|{self.quantity}|{self.habit}"

class Buddy(models.Model):
    pass

class Comment(models.Model):
    pass


