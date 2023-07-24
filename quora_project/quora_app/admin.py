from django.contrib import admin
from .models import Question,Answer,Like
# Register your models here.
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['id','title','content','created_at','user']
class AnswerAdmin(admin.ModelAdmin):
    list_display = ['content','created_at','user','question']
class LikeAmdin(admin.ModelAdmin):
    list_display = ['user','answer']

admin.site.register(Question,QuestionAdmin)
admin.site.register(Answer,AnswerAdmin)
admin.site.register(Like,LikeAmdin)
