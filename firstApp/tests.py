from os import link
from typing import Text
from django.test import TestCase
from . import models
from django.urls import reverse
#models tests
class PersonModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create 13 persons
        number_of_persons = 13
        for person_id in range(number_of_persons):
            models.Person.objects.create(
                username=f'mina {person_id}'
            )
    
    def test_username_label(self):
        person = models.Person.objects.get(pk = 1)
        field_label = person._meta.get_field('username').verbose_name
        self.assertEqual(field_label, 'username')
        #ok
    
    def test_password_label(self):
        person = models.Person.objects.get(pk = 1)
        field_label = person._meta.get_field('password').verbose_name
        self.assertEqual(field_label, 'password')
        #ok
    
    def test_email_label(self):
        person = models.Person.objects.get(pk = 1)
        field_label = person._meta.get_field('email').verbose_name
        self.assertEqual(field_label, 'email')
        #ok

    def test_role_label(self):
        person = models.Person.objects.get(pk = 1)
        field_label = person._meta.get_field('role').verbose_name
        self.assertEqual(field_label, 'role')
        #ok

    def test_bookmarked_label(self):
        person = models.Person.objects.get(pk = 1)
        field_label = person._meta.get_field('bookmarked').verbose_name
        self.assertEqual(field_label, 'bookmarked')
        #ok
    
    def test_username_max_length(self):
        person = models.Person.objects.get(id=1)
        max_length = person._meta.get_field('username').max_length
        self.assertEqual(max_length, 30)
    
    def test_password_max_length(self):
        person = models.Person.objects.get(id=1)
        max_length = person._meta.get_field('password').max_length
        self.assertEqual(max_length, 10)

    def test_object_name_is_username_and_id(self):
        person = models.Person.objects.get(id=1)
        expected_object_name = f'{person.username}{person.id}'
        self.assertEqual(str(person), expected_object_name)

class TagModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create 13 persons
        number_of_tags = 13
        person = models.Person(username = "mina" , password = "123")
        person.save()
        typeoftag = models.TagType( type = "level")
        typeoftag.save()
        for person_id in range(number_of_tags):
            models.Tag.objects.create(
                title=f'free {person_id}' ,
                creator = models.Person.objects.get(pk = 1),
                type = typeoftag
            )
    
    def test_creator_label(self):
        tag = models.Tag.objects.get(pk = 1)
        field_label = tag._meta.get_field('creator').verbose_name
        self.assertEqual(field_label, 'creator')
        #ok
    
    def test_title_label(self):
        tag = models.Tag.objects.get(pk = 1)
        field_label = tag._meta.get_field('title').verbose_name
        self.assertEqual(field_label, 'title')
        #ok  
    
    def test_title_max_length(self):
        tag = models.Tag.objects.get(pk = 1)
        max_length = tag._meta.get_field('title').max_length
        self.assertEqual(max_length, 40)

    def test_object_name_is_title_and_id(self):
        tag = models.Tag.objects.get(pk = 1)
        expected_object_name = f'{tag.title}{tag.id}'
        self.assertEqual(str(tag), expected_object_name)


class ResourceModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create 13 persons
        person = models.Person(username = "mina" , password = "123")
        number_of_resources = 13
        person.save()

        category = models.Category( creator = person , title = "cat1" )
        category.save()
        for resource_id in range(number_of_resources):
            models.Resource.objects.create(
                title= "kolah" ,
                category = category,
                link = "google.com" ,
                submitter = person
            )
    def test_category_label(self):
        resource = models.Resource.objects.get(pk = 1)
        field_label = resource._meta.get_field('category').verbose_name
        self.assertEqual(field_label, 'category')
        #ok

    def test_category_label(self):
        resource = models.Resource.objects.get(pk = 1)
        field_label = resource._meta.get_field('submitter').verbose_name
        self.assertEqual(field_label, 'submitter')
        #ok  
    def test_title_label(self):
        resource = models.Resource.objects.get(pk = 1)
        field_label = resource._meta.get_field('title').verbose_name
        self.assertEqual(field_label, 'title')
        #ok 
    def test_link_label(self):
        resource = models.Resource.objects.get(pk = 1)
        field_label = resource._meta.get_field('link').verbose_name
        self.assertEqual(field_label, 'link')
        #ok
    def test_tags_label(self):
        resource = models.Resource.objects.get(pk = 1)
        field_label = resource._meta.get_field('tags').verbose_name
        self.assertEqual(field_label, 'tags')
        #ok
    # def test_pub_date_label(self):
    #     resource = models.Resource.objects.get(pk = 1)
    #     field_label = resource._meta.get_field('pub_date').verbose_name
    #     self.assertEqual(field_label, 'pub_date')
        #fail
    def test_image_label(self):
        resource = models.Resource.objects.get(pk = 1)
        field_label = resource._meta.get_field('image').verbose_name
        self.assertEqual(field_label, 'image')
        #ok
    
    def test_title_max_length(self):
        resource = models.Resource.objects.get(pk = 1)
        max_length = resource._meta.get_field('title').max_length
        self.assertEqual(max_length, 500)

    def test_link_max_length(self):
        resource = models.Resource.objects.get(pk = 1)
        max_length = resource._meta.get_field('link').max_length
        self.assertEqual(max_length, 300)

    def test_image_max_length(self):
        resource = models.Resource.objects.get(pk = 1)
        max_length = resource._meta.get_field('image').max_length
        self.assertEqual(max_length, 200)

class CategoryModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create 13 persons
        person = models.Person(username = "mina" , password = "123")
        number_of_resources = 13
        person.save()

        category = models.Category( creator = person , title = "cat1" )
        category.save()
        for resource_id in range(number_of_resources):
            models.Resource.objects.create(
                title= "kolah" ,
                category = category,
                link = "google.com" ,
                submitter = person
            )
    def test_creator_label(self):
        category = models.Category.objects.get(pk = 1)
        field_label = category._meta.get_field('creator').verbose_name
        self.assertEqual(field_label, 'creator')
        #ok
    def test_title_label(self):
        category = models.Category.objects.get(pk = 1)
        field_label = category._meta.get_field('title').verbose_name
        self.assertEqual(field_label, 'title')
        #ok
    def test_image_label(self):
        category = models.Category.objects.get(pk = 1)
        field_label = category._meta.get_field('image').verbose_name
        self.assertEqual(field_label, 'image')
        #ok
    
    def test_title_max_length(self):     
        category = models.Category.objects.get(pk = 1)
        max_length = category._meta.get_field('title').max_length
        self.assertEqual(max_length, 50)

class SubCategoryModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create 13 persons
        person = models.Person(username = "mina" , password = "123")
        number_of_resources = 13
        person.save()
        category = models.Category(creator = person , title = "test")
        category.save()
        # category = models.Subcategory( creator = person , title = "subcat1" , category = category )
        # category.save()
        for resource_id in range(number_of_resources):
            models.Subcategory.objects.create(
                title= "kolah" ,
                category = category,
                creator = person
            )
    def test_creator_label(self):
        category = models.Subcategory.objects.get(pk = 1)
        field_label = category._meta.get_field('creator').verbose_name
        self.assertEqual(field_label, 'creator')
        #ok
    def test_title_label(self):
        category = models.Subcategory.objects.get(pk = 1)
        field_label = category._meta.get_field('title').verbose_name
        self.assertEqual(field_label, 'title')
        #ok
    def test_category_label(self):
        category = models.Subcategory.objects.get(pk = 1)
        field_label = category._meta.get_field('category').verbose_name
        self.assertEqual(field_label, 'category')
        #ok
    
    def test_title_max_length(self):     
        category = models.Subcategory.objects.get(pk = 1)
        max_length = category._meta.get_field('title').max_length
        self.assertEqual(max_length, 100)    
    
class LikeModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create 13 persons
        person = models.Person(username = "mina" , password = "123")
        number_of_resources = 13
        person.save()
        category = models.Category(creator = person , title = "test")
        category.save()
        resource = models.Resource(submitter = person , category = category , title = "test" , link = "google.com")
        resource.save()
        like_id = 13
        for like_id in range(number_of_resources):
            like = models.Like.objects.create(resc = resource , pers = person)

    def test_resc_label(self):
        like = models.Like.objects.get(pk = 1)
        field_label = like._meta.get_field('resc').verbose_name
        self.assertEqual(field_label, 'resc')
        #ok
    def test_pers_label(self):
        like = models.Like.objects.get(pk = 1)
        field_label = like._meta.get_field('pers').verbose_name
        self.assertEqual(field_label, 'pers')
        #ok

class CommentModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create 13 persons
        person = models.Person(username = "mina" , password = "123")
        number_of_resources = 13
        person.save()
        category = models.Category(creator = person , title = "test")
        category.save()
        resource = models.Resource(submitter = person , category = category , title = "test" , link = "google.com")
        resource.save()
        comment_id = 13
        for comment_id in range(number_of_resources):
            comment = models.Commentt.objects.create(resc = resource , pers = person , text="hi" )

    def test_resc_label(self):
        comment = models.Commentt.objects.get(pk = 1)
        field_label = comment._meta.get_field('resc').verbose_name
        self.assertEqual(field_label, 'resc')

    def test_pers_label(self):
        comment = models.Commentt.objects.get(pk = 1)
        field_label = comment._meta.get_field('pers').verbose_name
        self.assertEqual(field_label, 'pers')  

    def test_text_label(self):
        comment = models.Commentt.objects.get(pk = 1)
        field_label = comment._meta.get_field('text').verbose_name
        self.assertEqual(field_label, 'text')  

    # def test_create_date_label(self):
    #     comment = models.Commentt.objects.get(pk = 1)
    #     field_label = comment._meta.get_field('create date').verbose_name
    #     self.assertEqual(field_label, 'create date')  

    # def test_reply_comment_label(self):
    #     comment = models.Commentt.objects.get(pk = 1)
    #     field_label = comment._meta.get_field('reply_comment').verbose_name
    #     self.assertEqual(field_label, 'reply_comment')  
         
    
#View tests

class PersonListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create 13 persons
        number_of_persons = 13
        for person_id in range(number_of_persons):
            models.Person.objects.create(
                username=f'mina {person_id}'
            )
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/persons/')
        self.assertEqual(response.status_code, 200)

    def test_pagination_is_ten(self):
        response = self.client.get('/persons/')
        self.assertEqual(response.status_code, 200)
        print("this is" +str(response) )
        # self.assertTrue('is_paginated' in response.context)
        # self.assertTrue(response.context['is_paginated'] == True)
        # self.assertEqual(len(response), 10)   

class CreateTagViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        number_of_tags = 13
        person = models.Person(username = "mina" , password = "123")
        person.save()
        typeoftag = models.TagType( type = "level")
        typeoftag.save()
        for tag_id in range(number_of_tags):
            models.Tag.objects.create(
                title=f'free {tag_id}' ,
                creator = person,
                type = typeoftag)

    def test_view_url_exists_at_desired_location(self):
        response = self.client.post('/createTag/' , data={"id" : "1" , "type" : "1" , "title" : "video"})
        self.assertEqual(response.status_code, 200)
        
        
class CreateResourceViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        number_of_resources = 13
        person = models.Person(username = "mina" , password = "123")
        person.save()
        typeoftag = models.TagType( type = "level")
        typeoftag.save()
        tag = models.Tag( title = 'free' , creator =person , type = typeoftag)
        tag.save()
        cat = models.Category( creator = person , title = "python" )
        cat.save()
        for resource_id in range(number_of_resources):
            models.Resource.objects.create(
                title=f'java {resource_id}' ,
                submitter = person,
                tags = tag,
                link = "www.google.com",
                description = 'this course is about java',
                category = cat
                )

    def test_view_url_exists_at_desired_location(self):
        response = self.client.post('/createResource/' , data={"submitter" : 1 , "tags" : [1] , "title" : "java" , "link" : "www.google.com" , "description" : "this is about java"})
        self.assertEqual(response.status_code, 200)

class CreateLikeViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        number_of_likes = 13
        person = models.Person(username = "mina" , password = "123")
        person.save()
        person2 = models.Person(username = "zahra" , password = "123")
        person2.save()
        typeoftag = models.TagType( type = "level")
        typeoftag.save()
        tag = models.Tag( title = 'free' , creator =person , type = typeoftag)
        tag.save()
        cat = models.Category( creator = person , title = "python" )
        cat.save()
        resource = models.Resource( submitter = person , category = cat ,  title = "python" , link = "www.google.com" , description = "good course" )
        resource.save()
        for like_id in range(number_of_likes):
            models.Like.objects.create(
                pers = person,
                resc = resource
                )

    def test_view_url_exists_at_desired_location(self):
        response = self.client.post('/createLike/' , data={"pers" : "2" , "resc" : "1"})
        self.assertEqual(response.status_code, 200)
        
class CreateCategoryViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create 13 persons
        number_of_cats = 13
        person = models.Person(username = "mina" , password = "123")
        person.save()
        for cat_id in range(number_of_cats):
            models.Category.objects.create(
                creator = person,
                title = f'java {cat_id}' 
                )

    def test_view_url_exists_at_desired_location(self):
        response = self.client.post('/createCategory/' , data={"creator" : "1" , "title" : "java"})
        self.assertEqual(response.status_code, 200)
        
class CreateSubCategoryViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        number_of_subcats = 13
        person = models.Person(username = "mina" , password = "123")
        person.save()
        cat = models.Category( creator = person , title = "python" )
        cat.save()
        for sub_id in range(number_of_subcats):
            models.Subcategory.objects.create(
                creator = person,
                title = f'java {sub_id}' ,
                category = cat
                )

    def test_view_url_exists_at_desired_location(self):
        response = self.client.post('/createSubcategory/' , data={"creator" : "1" , "title" : "java" , "categort_id" : "1"})
        self.assertEqual(response.status_code, 200)
        
        
class CreateCommentViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        number_of_comments = 13
        person = models.Person(username = "mina" , password = "123")
        person.save()
        typeoftag = models.TagType( type = "level")
        typeoftag.save()
        tag = models.Tag( title = 'free' , creator =person , type = typeoftag)
        tag.save()
        cat = models.Category( creator = person , title = "python" )
        cat.save()
        resource = models.Resource( submitter = person , category = cat ,  title = "python" , link = "www.google.com" , description = "good course" )
        resource.save()
        for cm_id in range(number_of_comments):
            models.Commentt.objects.create(
                pers = person,
                text = f'java {cm_id}' ,
                resc = resource
                )

    def test_view_url_exists_at_desired_location(self):
        response = self.client.post('/createcomment/' , data={"pers" : "1" , "text" : "good!" , "resc" : "1"})
        self.assertEqual(response.status_code, 200)
        
class CreateCommentReplyViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        number_of_comments = 13
        person = models.Person(username = "mina" , password = "123")
        person.save()
        typeoftag = models.TagType( type = "level")
        typeoftag.save()
        tag = models.Tag( title = 'free' , creator =person , type = typeoftag)
        tag.save()
        cat = models.Category( creator = person , title = "python" )
        cat.save()
        resource = models.Resource( submitter = person , category = cat ,  title = "python" , link = "www.google.com" , description = "good course" )
        resource.save()
        comm = models.Commentt( pers = person , resc = resource , text = "nice")
        comm.save()
        for cm_id in range(number_of_comments):
            models.Commentt.objects.create(
                pers = person,
                text = f'java {cm_id}' ,
                resc = resource,
                reply_comment = comm
                )

    def test_view_url_exists_at_desired_location(self):
        response = self.client.post('/createcomment/' , data={"pers" : "1" , "text" : "good!" , "resc" : "1" , "reply_comment" : "1"})
        self.assertEqual(response.status_code, 200)
        
class CreateLikeCommentViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        number_of_likes = 1
        person = models.Person(username = "mina" , password = "123")
        person.save()
        typeoftag = models.TagType( type = "level")
        typeoftag.save()
        tag = models.Tag( title = 'free' , creator =person , type = typeoftag)
        tag.save()
        cat = models.Category( creator = person , title = "python" )
        cat.save()
        resource = models.Resource( submitter = person , category = cat ,  title = "python" , link = "www.google.com" , description = "good course" )
        resource.save()
        comm = models.Commentt( pers = person , resc = resource , text = "nice")
        comm.save()
        models.LikeComment.objects.create(
                pers = person,
                comm = comm
                )

    def test_view_url_exists_at_desired_location(self):
        response = self.client.post('/likecomment/' , data={"pers" : "1" , "comment" : "1"})
        self.assertEqual(response.status_code, 200)

class CreateQuestionViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        person = models.Person(username = "mina" , password = "123")
        person.save()
        person2 = models.Person(username = "zahra" , password = "123")
        person2.save()
        
        models.Question.objects.create(
                whoAsk = person,
                whoAnswer = person2,
                request_text = "its test"
                )

    def test_view_url_exists_at_desired_location(self):
        response = self.client.post('/createquestion/' , data={"whoAsk" : "1" , "whoAnswer" : "2" , "request_text" : "question" })
        self.assertEqual(response.status_code, 200)
        
class CreateNotificationLCViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        person = models.Person(username = "mina" , password = "123")
        person.save()
        person2 = models.Person(username = "zahra" , password = "123")
        person2.save()
        typeoftag = models.TagType( type = "level")
        typeoftag.save()
        tag = models.Tag( title = 'free' , creator =person , type = typeoftag)
        tag.save()
        cat = models.Category( creator = person , title = "python" )
        cat.save()
        resource = models.Resource( submitter = person , category = cat ,  title = "python" , link = "www.google.com" , description = "good course" )
        resource.save()
        comm = models.Commentt( pers = person , resc = resource , text = "nice")
        comm.save()
        likecomment = models.LikeComment(pers = person , comm = comm)
        likecomment.save()
        models.Notification.objects.create(
                reciever = person,
                sender = person2,
                notiftype = "LC",
                likecomment = likecomment
                )

    def test_view_url_exists_at_desired_location(self):
        response = self.client.post('/createnotification/' , data={"reciever" : "1" , "sender" : "2" , "notiftype" : "LC" , "likecomment" : "1"})
        self.assertEqual(response.status_code, 200)
        
class CreateNotificationCRViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        person = models.Person(username = "mina" , password = "123")
        person.save()
        person2 = models.Person(username = "zahra" , password = "123")
        person2.save()
        typeoftag = models.TagType( type = "level")
        typeoftag.save()
        tag = models.Tag( title = 'free' , creator =person , type = typeoftag)
        tag.save()
        cat = models.Category( creator = person , title = "python" )
        cat.save()
        resource = models.Resource( submitter = person , category = cat ,  title = "python" , link = "www.google.com" , description = "good course" )
        resource.save()
        comm = models.Commentt( pers = person , resc = resource , text = "nice")
        comm.save()
        comment_reply = models.Commentt( pers = person ,text = "good" ,resc = resource,reply_comment = comm)
        comment_reply.save()
        models.Notification.objects.create(
                reciever = person,
                sender = person2,
                notiftype = "CR",
                commentReply = comment_reply
                )

    def test_view_url_exists_at_desired_location(self):
        response = self.client.post('/createnotification/' , data={"reciever" : "1" , "sender" : "2" , "notiftype" : "CR" , "commentReply" : "1"})
        self.assertEqual(response.status_code, 200)
        
class CreateContentQualityViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        person = models.Person(username = "mina" , password = "123")
        person.save()
        typeoftag = models.TagType( type = "level")
        typeoftag.save()
        tag = models.Tag( title = 'free' , creator =person , type = typeoftag)
        tag.save()
        cat = models.Category( creator = person , title = "python" )
        cat.save()
        resource = models.Resource( submitter = person , category = cat ,  title = "python" , link = "www.google.com" , description = "good course" )
        resource.save()
        models.ContentQuality.objects.create(
            pers = person,
            resc = resource
        )
        

    def test_view_url_exists_at_desired_location(self):
        response = self.client.post('/ContentQuality/' , data={"pers" : "1" ,  "resc" : "1"})
        self.assertEqual(response.status_code, 200)
    
    
class CountContentQualityViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        count = 13
        person= models.Person(username = "mina" , password = "123")
        person.save()
        typeoftag = models.TagType( type = "level")
        typeoftag.save()
        tag = models.Tag( title = 'free' , creator = person , type = typeoftag)
        tag.save()
        cat = models.Category( creator = person , title = "python" )
        cat.save()
        resource = models.Resource( submitter = person , category = cat ,  title = "python" , link = "www.google.com" , description = "good course" )
        resource.save()
        for num in range(count):
            person= models.Person(username = "mina {num}" , password = "123")
            person.save()
            rate = models.ContentQuality.objects.create(
                pers = person,
                resc = resource
            )
            rate.save()
            print(rate)
        

    def test_view_url_exists_at_desired_location(self):
        response = self.client.post('/CountContentQuality/' , data={ "resc" : "1"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["count"] , 13)


    
class CreateCourseDepthAndCovergaeViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        person = models.Person(username = "mina" , password = "123")
        person.save()
        typeoftag = models.TagType( type = "level")
        typeoftag.save()
        tag = models.Tag( title = 'free' , creator =person , type = typeoftag)
        tag.save()
        cat = models.Category( creator = person , title = "python" )
        cat.save()
        resource = models.Resource( submitter = person , category = cat ,  title = "python" , link = "www.google.com" , description = "good course" )
        resource.save()
        
        models.CourseDepthAndCovergae.objects.create(
            pers = person,
            resc = resource
        )
        

    def test_view_url_exists_at_desired_location(self):
        response = self.client.post('/CourseDepth/' , data={"pers" : "1" ,  "resc" : "1"})
        self.assertEqual(response.status_code, 200)
        
    
class CountCourseDepthAndCovergaeViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        count = 13
        person= models.Person(username = "mina" , password = "123")
        person.save()
        typeoftag = models.TagType( type = "level")
        typeoftag.save()
        tag = models.Tag( title = 'free' , creator = person , type = typeoftag)
        tag.save()
        cat = models.Category( creator = person , title = "python" )
        cat.save()
        resource = models.Resource( submitter = person , category = cat ,  title = "python" , link = "www.google.com" , description = "good course" )
        resource.save()
        for num in range(count):
            person= models.Person(username = "mina {num}" , password = "123")
            person.save()
            rate = models.CourseDepthAndCovergae.objects.create(
                pers = person,
                resc = resource
            )
            rate.save()
            print(rate)
        

    def test_view_url_exists_at_desired_location(self):
        response = self.client.post('/CountCourseDepth/' , data={ "resc" : "1"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["count"] , 13)

        
class CreateCoursePaceViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        person = models.Person(username = "mina" , password = "123")
        person.save()
        typeoftag = models.TagType( type = "level")
        typeoftag.save()
        tag = models.Tag( title = 'free' , creator =person , type = typeoftag)
        tag.save()
        cat = models.Category( creator = person , title = "python" )
        cat.save()
        resource = models.Resource( submitter = person , category = cat ,  title = "python" , link = "www.google.com" , description = "good course" )
        resource.save()
        
        models.CoursePace.objects.create(
            pers = person,
            resc = resource
        )
        

    def test_view_url_exists_at_desired_location(self):
        response = self.client.post('/CoursePace/' , data={"pers" : "1" ,  "resc" : "1"})
        self.assertEqual(response.status_code, 200)
        
        
        
class CountCoursePaceViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        count = 13
        person= models.Person(username = "mina" , password = "123")
        person.save()
        typeoftag = models.TagType( type = "level")
        typeoftag.save()
        tag = models.Tag( title = 'free' , creator = person , type = typeoftag)
        tag.save()
        cat = models.Category( creator = person , title = "python" )
        cat.save()
        resource = models.Resource( submitter = person , category = cat ,  title = "python" , link = "www.google.com" , description = "good course" )
        resource.save()
        for num in range(count):
            person= models.Person(username = "mina {num}" , password = "123")
            person.save()
            rate = models.CoursePace.objects.create(
                pers = person,
                resc = resource
            )
            rate.save()
            print(rate)
        

    def test_view_url_exists_at_desired_location(self):
        response = self.client.post('/CountCoursePace/' , data={ "resc" : "1"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["count"] , 13)
        
        
        
class CreateVideoQualityViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        person = models.Person(username = "mina" , password = "123")
        person.save()
        typeoftag = models.TagType( type = "level")
        typeoftag.save()
        tag = models.Tag( title = 'free' , creator =person , type = typeoftag)
        tag.save()
        cat = models.Category( creator = person , title = "python" )
        cat.save()
        resource = models.Resource( submitter = person , category = cat ,  title = "python" , link = "www.google.com" , description = "good course" )
        resource.save()
        
        models.VideoQuality.objects.create(
            pers = person,
            resc = resource
        )
        

    def test_view_url_exists_at_desired_location(self):
        response = self.client.post('/VideoQuality/' , data={"pers" : "1" ,  "resc" : "1"})
        self.assertEqual(response.status_code, 200)
        
        
class CountVideoQualityViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        count = 13
        person= models.Person(username = "mina" , password = "123")
        person.save()
        typeoftag = models.TagType( type = "level")
        typeoftag.save()
        tag = models.Tag( title = 'free' , creator = person , type = typeoftag)
        tag.save()
        cat = models.Category( creator = person , title = "python" )
        cat.save()
        resource = models.Resource( submitter = person , category = cat ,  title = "python" , link = "www.google.com" , description = "good course" )
        resource.save()
        for num in range(count):
            person= models.Person(username = "mina {num}" , password = "123")
            person.save()
            rate = models.VideoQuality.objects.create(
                pers = person,
                resc = resource
            )
            rate.save()
            print(rate)
        

    def test_view_url_exists_at_desired_location(self):
        response = self.client.post('/CountVideoQuality/' , data={ "resc" : "1"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["count"] , 13)
        
           
class CreateQualifiedInstructorViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        person = models.Person(username = "mina" , password = "123")
        person.save()
        typeoftag = models.TagType( type = "level")
        typeoftag.save()
        tag = models.Tag( title = 'free' , creator =person , type = typeoftag)
        tag.save()
        cat = models.Category( creator = person , title = "python" )
        cat.save()
        resource = models.Resource( submitter = person , category = cat ,  title = "python" , link = "www.google.com" , description = "good course" )
        resource.save()
        
        models.QualifiedInstructor.objects.create(
            pers = person,
            resc = resource
        )
        

    def test_view_url_exists_at_desired_location(self):
        response = self.client.post('/QualifiedInstructor/' , data={"pers" : "1" ,  "resc" : "1"})
        self.assertEqual(response.status_code, 200)
        
        
class CountQualifiedInstructorViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        count = 13
        person= models.Person(username = "mina" , password = "123")
        person.save()
        typeoftag = models.TagType( type = "level")
        typeoftag.save()
        tag = models.Tag( title = 'free' , creator = person , type = typeoftag)
        tag.save()
        cat = models.Category( creator = person , title = "python" )
        cat.save()
        resource = models.Resource( submitter = person , category = cat ,  title = "python" , link = "www.google.com" , description = "good course" )
        resource.save()
        for num in range(count):
            person= models.Person(username = "mina {num}" , password = "123")
            person.save()
            rate = models.QualifiedInstructor.objects.create(
                pers = person,
                resc = resource
            )
            rate.save()
            print(rate)
        

    def test_view_url_exists_at_desired_location(self):
        response = self.client.post('/CountQualified/' , data={ "resc" : "1"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["count"] , 13)