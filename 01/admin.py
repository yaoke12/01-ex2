from django.contrib import admin

from DP_Project.models.knapsack import Knapsack
from DP_Project.models.logging import Logging

admin.site.site_header = 'D{0-1}KP 实例数据集算法实验平台'
admin.site.site_title = 'D{0-1}KP 实例数据集算法实验平台'
admin.site.index_title = 'D{0-1}KP 实例数据集算法实验平台'


class KnapsackAdmin(admin.ModelAdmin):
    list_display = ('performance', 'volume', 'worth')


class LoggingAdmin(admin.ModelAdmin):
    list_display = ('id', 'operation', 'time')


admin.site.register(Knapsack, KnapsackAdmin)
admin.site.register(Logging, LoggingAdmin)
