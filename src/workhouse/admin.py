from django.contrib import admin
from workhouse.models import *
from warehouse.models import *
from django.urls import reverse
from django.utils.html import format_html
from django.db.models import Count


# admin.site.register(Cut)
@admin.register(Cut)
class CutAdmin(admin.ModelAdmin):
    list_display = [
        'code',
        'date',
        'model_name',
        'clothroll_count',
    ]
    prepopulated_fields = {"slug": ("code", "date")}

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(clothroll_count=Count("clothroll"))

    @admin.display(ordering="clothroll_count")
    def clothroll_count(self, cut):
        #              admin:APP_MODEL_PAGE
        url = reverse("admin:warehouse_clothroll_changelist") + \
            f"?cut_id={cut.id}"
        # return f"<a href='{url}'>{cut.clothroll_count}</a>"
        return format_html("<a href='{}'>{}</a>", url, cut.clothroll_count)
