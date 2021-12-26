
from django.db.models import fields
from rest_framework import serializers

from . import models

class PersonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Person
        fields = ('id', 'username', 'email', 'role' , 'password')

class RecourceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Resource
        fields = ('id', 'submitter', 'title', 'link', 'tags', 'pub_date' , 'image')
        
class LikeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Like
        fields = ('create_date', 'resc', 'pers')
        
class LikecommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.LikeComment
        fields = ('create_date', 'comm', 'pers')


class SubcategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Subcategory
        fields = ('creator', 'title', 'resources' , 'category_id' , 'id')
        

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Category
        fields = ('creator', 'title' , 'categoryId')

class TagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Tag
        fields = ('creator' , 'title')

class NotificationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Notification
        fields = ('sender' , 'reciever' , 'notiftype' , 'likecomment' , 'commentReply')

class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Question
        fields = ('request_text' , 'whoAsk' , 'whoAnswer' , 'id')

class RecursiveField(serializers.Serializer):
    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data

class CommentSerializer(serializers.HyperlinkedModelSerializer):
    reply_comment = RecursiveField()
    class Meta:
        model = models.Commentt
        fields = ('text' , 'pers' , 'resc' , 'reply_comment' , 'create_date' , 'id' )

class NotificationSerializer(serializers.Serializer):
    class Meta :
        model = models.Notification
        fields = ('reciever' , 'sender' , 'notiftype' , 'likecomment' , 'commentReply' , 'id')
        
class ContentQualitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.ContentQuality
        fields = ('create_date', 'resc', 'pers')
        
class CourseDepthAndCovergaeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.CourseDepthAndCovergae
        fields = ('create_date', 'resc', 'pers')
        
class CoursePaceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.CoursePace
        fields = ('create_date', 'resc', 'pers')
        
class VideoQualitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.VideoQuality
        fields = ('create_date', 'resc', 'pers')

class QualifiedInstructorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.QualifiedInstructor
        fields = ('create_date', 'resc', 'pers')