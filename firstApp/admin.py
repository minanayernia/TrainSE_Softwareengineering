from django.contrib import admin
from . import  models


admin.site.register(models.Person)
admin.site.register(models.Notification)
admin.site.register(models.Tag)
admin.site.register(models.Resource)
admin.site.register(models.Category)
admin.site.register(models.Subcategory)
admin.site.register(models.Commentt)
admin.site.register(models.Question)
admin.site.register(models.Like)
admin.site.register(models.LikeComment)
admin.site.register(models.VideoQuality)
admin.site.register(models.QualifiedInstructor)
admin.site.register(models.CoursePace)
admin.site.register(models.CourseDepthAndCovergae)
admin.site.register(models.ContentQuality)
admin.site.register(models.TagType)
