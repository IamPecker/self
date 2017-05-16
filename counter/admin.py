# coding=utf-8
from django.contrib import admin
from django.template.loader import get_template
from django.template import Context
from root.forms import RoomModelForm
from models import RoomReserve


# Register your models here.
from root.models import RoomUseTime


class RoomReserveAdmin(admin.ModelAdmin):
    # change_list_template = 'change_list.html'
    list_display = ('room_number','name', 'type', 'current_use', 'show_room_detail', 'reserve')
    # search_fields = ('is_use',)
    list_filter = ('type',)
    ordering = ('id',)
    # change_form = RoomModelForm

    def get_form(self, request, obj=None, **kwargs):
        return self.change_form

    def show_room_detail(self, obj):
        room_number = obj.room_number
        room_uses = RoomUseTime.objects.filter(room_number=room_number)
        t = get_template('/counter/templates/room_reserve.html.html')
        # t = get_template('<input>12</input>')
        return t.render(Context({
            'room_name': obj.name,
            'room_uses':room_uses
        }))

    show_room_detail.short_description = u'操作'

    def reserve(self, obj):
        t = get_template('/counter/templates/reserve_operation.html.html')
        # t = get_template('<input></input>')
        return t.render(Context({
            'id': obj.id
        }))

    reserve.short_description = u'操作'

admin.site.register(RoomReserve, RoomReserveAdmin)
