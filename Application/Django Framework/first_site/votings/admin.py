from django.contrib import admin
from .models import Question, Choice

#class ChoiceInline(admin.TabularInline):
    #model = Choice
    #extra = 3

class QuestionAdmin(admin.ModelAdmin):
    #fields = ['pub_date', 'question_text']
    fieldsets = [
        ('Questions',               {'fields': ['question_text']}),
        ('Date Information', {'fields': ['pub_date']}),
    ]

    #fieldsets = [
    #    ('Questions', {'fields': ['choice_text']}),
    #    ('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']})
    #]

    #inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)