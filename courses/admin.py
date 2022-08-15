from django.contrib import admin, messages
from courses.models import Course, CourseSource

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'participants', 'source']
    list_filter = ['source']
    sortable_by = ['price', 'participants']
    search_fields = ['name']
    fieldsets = (
        ('General Info',
        {
            'fields': (('name', 'teacher', 'source'), ('price', 'participants', 'rating'))
        }),
        ('Details', 
        {
            'classes': ('collapse',),
            'fields': (('url', 'image_url'), 'description')
        })
    )


@admin.register(CourseSource)
class CourseSourceAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']

    actions = ['delete_courses']

    def delete_courses(self, request, queryset):
        for source in queryset:
            source.courses.all().delete()
        self.message_user(
            request, 'Related courses deleted successfull!', messages.SUCCESS
        )
    
    delete_courses.short_description = 'Delete Courses'