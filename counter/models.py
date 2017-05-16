#coding=utf-8
from django.db import models

# Create your models here.
from django.utils import timezone

from root.models import RoomUseTime


class RoomReserve(models.Model):
    ROOM_TYPE = (
        ('small', '小包'),
        ('middle', '中包'),
        ('large', '大包')
    )
    ROOM_STATUS = (
        (0, '占用'),
        (1, '空闲')
    )
    type = models.CharField(max_length=10, choices=ROOM_TYPE, verbose_name='种类')
    room_number = models.IntegerField(verbose_name=u'房间编号')
    current_use = models.IntegerField(choices=ROOM_STATUS, verbose_name=u'当前空闲')
    name = models.CharField(max_length=255, choices=ROOM_TYPE, verbose_name='名称')

    def __str__(self):
        return self.type + '_' + str(self.id)

    class Meta:
        managed = False
        db_table = 'room_reserve'
        verbose_name = u'房间预订'
        verbose_name_plural = verbose_name