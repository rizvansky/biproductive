from .models import HabitUsage
import django_tables2 as tables


class HabitUsageTable(tables.Table):
    class Meta:
        model = HabitUsage
        template_name = "django_tables2/bootstrap.html"
        fields = ('habit', 'usage_time',)
