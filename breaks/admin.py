from django.contrib import admin
from django.contrib.admin import TabularInline, StackedInline
from django.db.models import Count
from django.urls import reverse
from django.utils.html import format_html

from breaks.models import organisations, groups, replacements, dicts, breaks


#####################################################
# INLINES
#####################################################
class ReplacementEmployeeInline(StackedInline):  # noqa
    model = replacements.ReplacementEmployee
    fields = ('employee', 'status',)


##################################################### noqa
# MODELS
#####################################################
@admin.register(organisations.Organisation)  # noqa
class OrganisationsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'director',)
    filter_horizontal = ('employees',)


@admin.register(groups.Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'manager', 'min_active', 'replacement_count')
    list_display_links = ('id', 'name',)
    search_fields = ('name',)

    def replacement_count(self, obj):
        return obj.replacement_count

    replacement_count.short_description = 'Кол-во смен'
    # replacement_count.empty_value_display = 'Кол-во смен'

    def get_queryset(self, request):
        queryset = groups.Group.objects.annotate(
            replacement_count=Count('replacements__id')
        )
        return queryset


@admin.register(dicts.ReplacementStatus)
class ReplacementStatusAdmin(admin.ModelAdmin):
    list_display = (
        'code', 'name', 'sort', 'is_active',)


@admin.register(dicts.BreakStatus)
class BreakStatusAdmin(admin.ModelAdmin):
    list_display = (
        'code', 'name', 'sort', 'is_active',)


@admin.register(replacements.Replacement)
class ReplacementAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'group', 'date', 'break_start', 'break_end', 'break_max_duration',)
    autocomplete_fields = ('group',)
    inlines = (
        ReplacementEmployeeInline,
    )


# @admin.register(breaks.Break)
# class BreakAdmin(admin.ModelAdmin):
#     list_display = (
#         'id', 'replacement', 'break_start', 'break_end',)
#
@admin.register(breaks.Break)
class BreakAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'replacement_link', 'break_start', 'break_end', 'status',)

    list_filter = ('status',)
    empty_value_display = 'Unknown '
    radio_fields = {'status': admin.VERTICAL}

    def replacement_link(self, obj): # noqa
        link = reverse(
            'admin:breaks_replacement_change', args=[obj.replacement.id]
        )
        return format_html('<a href="{}">{}</a>', link, obj.replacement)
