# from asyncio.windows_events import NULL
from datetime import date, datetime
from itertools import count
from os import name
from pyexpat import model
from unicodedata import category
from django.db.models import query
from rest_framework import viewsets
from rest_framework.generics import GenericAPIView, CreateAPIView, ListAPIView, RetrieveAPIView

from . import serializers
from . import models
from . import forms
from django.shortcuts import render, redirect
import json
import base64

from django.db.models import Count


from django.shortcuts import render
from rest_framework.generics import GenericAPIView, CreateAPIView, ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from django.http import HttpResponse, response
from django.contrib.auth.admin import User
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
class PersonViewSet(viewsets.ModelViewSet):
    queryset = models.Person.objects.all()
    serializer_class = serializers.PersonSerializer
    paginate_by = 10
    
    

class SignUpPersonView(CreateAPIView): #create person
    serializer_class =serializers.PersonSerializer
    allowed_methods = ['POST']
    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        email = request.data.get('email')
        allusernames = models.Person.objects.values_list('username' , flat=True)
        allemails = models.Person.objects.values_list('email' , flat=True)
        if (username in allusernames or email in allemails):
            return Response({"msg":"Username or email exists" , "status" : 500 })
        else:
            print("in else")
            newPerson = models.Person(username=username , password = request.data.get("password"),
                                      email = request.data.get('email') , role = request.data.get('role'))
            newPerson.save()
            print("newperson added to datebase")
            return Response({"username" : newPerson.username , "email" : newPerson.email , "id" : newPerson.id , "role" : newPerson.role, "status" : 200} )

class LogIn(CreateAPIView):
    serializer_class =serializers.PersonSerializer
    allowed_methods = ['POST']
    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        user = models.Person.objects.filter(username =username , password = password)
        if user.exists() :
            return Response({"username" : user[0].username , "email" : user[0].email , "id" : user[0].id , "role" : user[0].role ,"status" : 200} )
        else:
            return Response({"msg":"Username or Password is wronge" , "status" : 500 })

class DeletePersonView(CreateAPIView):
    serializer_class =serializers.PersonSerializer
    allowed_methods = ['POST']

    def post(self, request, *args, **kwargs):
        id = request.data.get("id")
        prs = models.Person.objects.filter(pk = id)
        prs.delete()
        return HttpResponse({"status": 200})

class UpdatePersonView(CreateAPIView):
    serializer_class =serializers.PersonSerializer
    allowed_methods = ['POST']

    def post(self, request, *args, **kwargs):
        id = request.data.get("id")
        prs = models.Person.objects.get(pk = id)
        prs.username = request.data.get("username" )
        prs.password = request.data.get("password" )
        prs.email = request.data.get("email" )
        prs.location = request.data.get("location" )
        prs.about = request.data.get("about" )

        prs.save()
        print("hey it was successful")
        return HttpResponse({"status": 200})

class CreateTag(CreateAPIView):
    serializer_class =serializers.TagSerializer
    allowed_methods = ['POST']
    def post(self, request, *args, **kwargs):
        id = request.data.get("id")
        prs = models.Person.objects.get(pk = id)
        typeid = request.data.get("type")
        typeoftag = models.TagType.objects.get(pk = typeid)
        tag = models.Tag(creator= prs,
                         title= request.data.get("title"),
                         type = typeoftag)
        tag.save()
        return HttpResponse({"status": 200})

class DeleteTag(CreateAPIView):
    serializer_class =serializers.TagSerializer
    allowed_methods = ['POST']
    def post(self, request, *args, **kwargs):
        id = request.data.get("id")
        tag = models.Tag.objects.get(pk = id)
        tag.delete()
        return HttpResponse({"status": 200})

class UpdateTag(CreateAPIView):
    serializer_class =serializers.TagSerializer
    allowed_methods = ['POST']

    def post(self, request, *args, **kwargs):
        id = request.data.get("id")
        tag = models.Tag.objects.get(pk = id)
        tag.title = request.data.get("title")
        return HttpResponse({"status": 200})
    
class ListTags(APIView):
    serializer_class =serializers.TagSerializer
    allowed_methods = ['GET']

    def get(self, request, *args, **kwargs):
        tags1 = models.Tag.objects.all()
        tags_dic =[]
        for tag in tags1:
            response_data = {}
            response_data['id'] = tag.id
            response_data['title'] = tag.title
            response_data['type'] = tag.type.type
            tags_dic.append(response_data)
        return HttpResponse(json.dumps(tags_dic), content_type="application/json")
        

class ResourceViewSet(viewsets.ModelViewSet):
    queryset = models.Resource.objects.all()
    serializer_class = serializers.RecourceSerializer

class CategoryListViewSet(viewsets.ModelViewSet):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer

class ListCategories(APIView):
    serializer_class =serializers.CategorySerializer
    allowed_methods = ['Get']

    def get(self, request, *args, **kwargs):
        cat = models.Category.objects.all()
        cats_dic =[]
        for category in cat:
            response_data = {}
            response_data['image'] = category.image
            response_data['creator_id'] = category.creator.id
            response_data['creator'] = category.creator.username
            response_data['title'] = category.title
            response_data['category_id'] = category.id
        

            cats_dic.append(response_data)
        return HttpResponse(json.dumps(cats_dic), content_type="application/json")

# class deleteResourceView(viewsets.ModelViewSet , id):
#     serializer_class = serializers.RecourceSerializer
#     event = models.Resource.objects.delete(pk = id)
class setimageinResource(CreateAPIView):
    serializer_class = serializers.RecourceSerializer
    allowed_methods = ['POST']
    def post(self, request, *args, **kwargs):
        image = request.file('img')
        
        idresource = request.data.get('id' , None)
        resource = models.Resource.objects.get(pk = idresource)
        resource.image = image
        resource.save()
        return HttpResponse({"status": 200})

class CreateResource(CreateAPIView):

    serializer_class = serializers.RecourceSerializer
    allowed_methods = ['POST']
    def post(self, request, *args, **kwargs):
        id = request.data.get('submitter' , None)
        print("ssssssssssssssssssssssssssssssss" + str(id))
        pr = models.Person.objects.get(pk = id)
        catid = request.data.get('category' , None)
        cat = models.Category.objects.get(pk = catid)
        print("this id pr:" + str(pr))
        tags = request.data.get('tags' , None)
        subcategories = request.data.get('subs' , None)
        # image = request.file('file')
        rc = models.Resource(submitter= pr, 
                            title= request.data.get('title' , None),
                            link=request.data.get('link' , None),
                            pub_date= datetime.now(),
                            # image = image ,
                            description = request.data.get('description' , None),
                            category = cat )
        rc.save()

        for tag_id in tags:
            tag = models.Tag.objects.get(pk = tag_id)
            rc.tags.add(tag)

        for sub_id in subcategories:
            sb = models.Subcategory.objects.get(pk = sub_id)
            rc.subcategories.add(sb)
        rc.save()
        print("recource tags are :")
        print(rc.tags.all())
        
        return HttpResponse({"status": 200})



class sendListResourceByGet():
    serializer_class =serializers.CategorySerializer
    allowed_methods = ['get']  
    def get(self , request , id):
        querySet = models.Resource.objects.all()
        cat = models.Category.objects.get(pk=id)
        querySet = querySet.filter(category = cat )
        querySet = querySet.filter(category = cat )
        resources_dic =[]
        for res in querySet:
            response_data = {}
            response_data['resource_id'] = res.id
            response_data['creator'] = res.submitter.username
            response_data['title'] = res.title
            response_data['link'] = res.link
            response_data['image'] = res.image
            response_data['pub_date'] = res.pub_date

            resources_dic.append(response_data)
        return Response(resources_dic)


class ListResource(APIView):
    serializer_class =serializers.CategorySerializer
    allowed_methods = ['Post']
    
    def post(self, request, *args, **kwargs):
        querySet = models.Resource.objects.all()
        id = request.data.get('categoryId')
        personid = request.data.get('personId' , None)
        if (personid != None):
            person = models.Person.objects.get(pk = personid)
        # id =1/
        cat = models.Category.objects.get(pk=id)
        querySet = querySet.filter(category = cat )
        resources_dic =[]
        for res in querySet:
            response_data = {}
            response_data['resource_id'] = res.id
            response_data['creator'] = res.submitter.username
            response_data['title'] = res.title
            response_data['link'] = res.link
            # response_data['image'] = res.image
            likeCount = models.Like.objects.filter(resc = res).count()
            response_data['likeCount'] = likeCount
            if personid == None :
                response_data['isbookmark'] = 0
                response_data['isliked'] = 0
            else:
                likeobject = models.Like.objects.filter(resc = res , pers = person )
                allbookmarked = person.bookmarked.all()
                print("like object")
                print(likeobject)
                if(likeobject):
                    response_data['isliked'] = 1
                else :
                    response_data['isliked'] = 0
                    
                if allbookmarked.exists():
                    if res in allbookmarked:
                        response_data['isbookmark'] = 1
                    else :
                        response_data['isbookmark'] = 0
                else:
                    response_data['isbookmark'] = 0

            print("callong all objects ")
            tags = res.tags.all()
            tagg = []
            print("befor for")
            print(tags)
            if tags.exists():
                for tag in tags :
                    # tagg.append(tag)
                    dic = {}
                    dic['id'] = tag.id
                    dic['title'] = tag.title
                    tagg.append(dic)
                    print("inside for")

            response_data['tags'] = tagg 
            print("tag added successfuly")
            response_data['pub_date'] = res.pub_date

            resources_dic.append(response_data)
        return Response(resources_dic)

class latest_resourceList(APIView):
    serializer_class =serializers.CategorySerializer
    allowed_methods = ['Post']
    
    def post(self, request, *args, **kwargs):
        querySet = models.Resource.objects.all().order_by('-pub_date')
        id = request.data.get('categoryId')
        personid = request.data.get('personId' , None)
        if (personid != None):
            person = models.Person.objects.get(pk = personid)
        # id =1/
        cat = models.Category.objects.get(pk=id)
        querySet = querySet.filter(category = cat )
        resources_dic =[]
        for res in querySet:
            response_data = {}
            response_data['resource_id'] = res.id
            response_data['creator'] = res.submitter.username
            response_data['title'] = res.title
            response_data['link'] = res.link
            # response_data['image'] = res.image
            likeCount = models.Like.objects.filter(resc = res).count()
            response_data['likeCount'] = likeCount
            if personid == None :
                response_data['isbookmark'] = 0
                response_data['isliked'] = 0
            else:
                likeobject = models.Like.objects.filter(resc = res , pers = person )
                allbookmarked = person.bookmarked.all()
                print("like object")
                print(likeobject)
                if(likeobject):
                    response_data['isliked'] = 1
                else :
                    response_data['isliked'] = 0
                    
                if allbookmarked.exists():
                    if res in allbookmarked:
                        response_data['isbookmark'] = 1
                    else :
                        response_data['isbookmark'] = 0
                else:
                    response_data['isbookmark'] = 0

            print("callong all objects ")
            tags = res.tags.all()
            tagg = []
            print("befor for")
            print(tags)
            if tags.exists():
                for tag in tags :
                    # tagg.append(tag)
                    dic = {}
                    dic['id'] = tag.id
                    dic['title'] = tag.title
                    tagg.append(dic)
                    print("inside for")

            response_data['tags'] = tagg 
            print("tag added successfuly")
            response_data['pub_date'] = res.pub_date

            resources_dic.append(response_data)
        return Response(resources_dic)

class orderbyLike_resourceList(APIView):
    serializer_class =serializers.CategorySerializer
    allowed_methods = ['Post']
    
    def post(self, request, *args, **kwargs):
        querySet = models.Resource.objects.all()
        # querySet = models.Resource.objects.annotate(count = Count(Like)).order_by('count')
        id = request.data.get('categoryId')
        personid = request.data.get('personId' , None)
        if (personid != None):
            person = models.Person.objects.get(pk = personid)
        # id =1/
        cat = models.Category.objects.get(pk=id)
        querySet = querySet.filter(category = cat )

        resources_dic =[]
        newList = []
        for res in querySet:
            response_data = {}
            response_data['resource_id'] = res.id
            response_data['creator'] = res.submitter.username
            response_data['title'] = res.title
            response_data['link'] = res.link
            # response_data['image'] = res.image
            print("before like count")
            likeCount = models.Like.objects.filter(resc = res).count()
            response_data['likeCount'] = likeCount
            print("we count the like count")
            if personid == None :
                response_data['isbookmark'] = 0
                response_data['isliked'] = 0
            else:
                likeobject = models.Like.objects.filter(resc = res , pers = person )
                allbookmarked = person.bookmarked.all()
                print("like object")
                print(likeobject)
                if(likeobject):
                    response_data['isliked'] = 1
                else :
                    response_data['isliked'] = 0
                    
                if allbookmarked.exists():
                    if res in allbookmarked:
                        response_data['isbookmark'] = 1
                    else :
                        response_data['isbookmark'] = 0
                else:
                    response_data['isbookmark'] = 0

            print("callong all objects ")
            tags = res.tags.all()
            tagg = []
            print("befor for")
            print(tags)
            if tags.exists():
                for tag in tags :
                    # tagg.append(tag)
                    dic = {}
                    dic['id'] = tag.id
                    dic['title'] = tag.title
                    tagg.append(dic)
                    print("inside for")

            response_data['tags'] = tagg 
            print("tag added successfuly")
            response_data['pub_date'] = res.pub_date

            resources_dic.append(response_data)
            # resources_dic.sort('likeCount')
            if resources_dic :
                newList = sorted(resources_dic , key = lambda dic : dic['likeCount'] , reverse=True)
                print("hey not empty")
            else :
                newList = resources_dic
                print("hey this is empty")
        return Response(newList)
class CreateComment(CreateAPIView): 
    serializer_class = serializers.CommentSerializer
    allowed_methods = ['POST']

    def post(self, request, *args, **kwargs):

        personId = request.data.get("pers")
        resourceId = request.data.get("resc")
        replycommentId = request.data.get("reply_comment" , None)

        person = models.Person.objects.get(pk = personId)
        resource = models.Resource.objects.get(pk = resourceId)
        if (replycommentId != None):
            replycomment = models.Commentt.objects.get(pk = replycommentId)
        else:
            replycomment = None

        comment = models.Commentt(pers = person , resc = resource , text = request.data.get("text") , reply_comment = replycomment )
        comment.save()
        if (replycommentId != None):
            repcom = models.Commentt.objects.get(pk = replycommentId)
            notif = models.Notification( reciever = repcom.pers , sender = person , commentReply = comment,likecomment =None , notiftype ='CR')
            notif.save()
            print("notif saved successfully!!")


        return Response({"msg":"comment created"} , status=status.HTTP_200_OK)

class DeleteComment(APIView):
    serializer_class = serializers.CommentSerializer
    allowed_methods = ['POST']

    def post(self, request, *args, **kwargs):
        id = request.data.get('id')
        cm = models.Commentt.objects.get(pk = id)
        cm.delete()
        return Response({"msg":"comment deleted"} , status=status.HTTP_200_OK)

class EditComment(APIView):
    serializer_class = serializers.CommentSerializer
    allowed_methods = ['POST']

    def post(self, request, *args, **kwargs):
        commentId = request.data.get('id')
        comment = models.Commentt.objects.get(pk = commentId)
        comment.text = request.data.get('text')
        comment.save()
        return Response({"msg":"comment edited"} , status=status.HTTP_200_OK)


        
class DeleteResource(APIView):
    allowed_methods = ['POST']
    def post(self, request, *args, **kwargs):
        id = request.data.get('id' , None)
        pr = models.Resource.objects.get(pk = id)
        pr.delete()
        
        return HttpResponse({"status": 200})
    
class UpdateResource(CreateAPIView):
    serializer_class =serializers.RecourceSerializer
    allowed_methods = ['POST']
    def post(self, request, *args, **kwargs):
        idsrc = request.data.get("id")
        idcategory = request.data.get("category")
        category = models.Category.objects.get(pk = idcategory)
        
        description = request.data.get("description")
        rsc = models.Resource.objects.get(pk = idsrc)
        rsc.category = category
        rsc.description = description
        tagids= request.data.get("tags")
        subids= request.data.get("subs")
        # id = request.data.get('submitter' , None)
        # pr = models.Person.objects.get(pk = id)
        # rsc.submitter = pr
        rsc.title = request.data.get("title" )
        rsc.link = request.data.get("link" )
        if rsc.tags.all().exists():
            print("yes this is here")
            tags = rsc.tags.all()
            for tag in tags :
                rsc.tags.remove(tag)
                print("tag deleted")
        for tagid in tagids :
            newtag = models.Tag.objects.get(pk = tagid)
            rsc.tags.add(newtag)
            
        
        if rsc.subcategories.all().exists():
            subcategories = rsc.subcategories.all()
            for sub in subcategories:
                rsc.subcategories.remove(sub)
        for subid in subids :
            newsub = models.Subcategory.objects.get(pk = subid)
            rsc.subcategories.add(newsub)
            
        
        rsc.save()
        print("hey it was successful")
        
        return HttpResponse({"status": 200})

class CreateLike(CreateAPIView):
    serializer_class = serializers.LikeSerializer
    allowed_methods = ['POST']
    def post(self, request, *args, **kwargs):
        idperson = request.data.get('pers' , None)
        pr = models.Person.objects.get(pk = idperson)
        print("teeeeeeeeeeessssssssssssssssssst")
        idresource = request.data.get('resc' , None)
        rc = models.Resource.objects.get(pk = idresource)
        temp = models.Like.objects.filter(pers = pr , resc = rc)
        if temp.exists() :
            return Response("Already exists!")
        print("this is " + idperson + idresource)
        like = models.Like(pers= pr, 
                            resc= rc,
                            create_date= datetime.now())
        like.save()
        
        return HttpResponse({"status": 200})

class DeleteLike(APIView):
    allowed_methods = ['POST']
    def post(self, request, *args, **kwargs):
        idperson = request.data.get('pers' , None)
        pr = models.Person.objects.get(pk = idperson)
        print("teeeeeeeeeeessssssssssssssssssst")
        idresource = request.data.get('resc' , None)
        rc = models.Resource.objects.get(pk = idresource)
        temp = models.Like.objects.get(pers = pr , resc = rc)
        like = models.Like.objects.get(pk = temp.id)
        like.delete()
        
        return HttpResponse({"status": 200})
    
    
class CreateLikecomment(CreateAPIView):
    serializer_class = serializers.LikecommentSerializer
    allowed_methods = ['POST']
    def post(self, request, *args, **kwargs):
        idperson = request.data.get('pers' , None)
        pr = models.Person.objects.get(pk = idperson)
        print("teeeeeeeeeeessssssssssssssssssst")
        idcomment = request.data.get('comment' , None)
        cm = models.Commentt.objects.get(pk = idcomment)
        print("this is " + idperson + idcomment)
        temp = models.LikeComment.objects.filter(pers = pr , comm = cm)
        if temp.exists() :
            return Response("Already exists!")
        likecm = models.LikeComment(pers= pr, 
                            comm= cm,
                            create_date= datetime.now())
        likecm.save()
        reciever = cm.pers
        notif = models.Notification(reciever = reciever , sender = pr , notiftype = 'LC' , likecomment = likecm , commentReply = None)
        notif.save()
        print("likecomment notification added successfully !!")
        
        return HttpResponse({"status": 200})
    
class DeleteLikecomment(APIView):
    allowed_methods = ['POST']
    def post(self, request, *args, **kwargs):
        id = request.data.get('id' , None)
        like = models.LikeComment.objects.get(pk = id)
        like.delete()
        
        return HttpResponse({"status": 200})
    
class CreateSubcategory(CreateAPIView):
    serializer_class = serializers.SubcategorySerializer
    allowed_methods = ['POST']
    def post(self, request, *args, **kwargs):
        idperson = request.data.get('creator' , None)
        pr = models.Person.objects.get(pk = idperson)
        idcat = request.data.get('categort_id' , None)
        cat = models.Category.objects.get(pk = idcat)
        subcat = models.Subcategory(creator= pr, 
                            title = request.data.get('title' , None),
                            category = cat)
        subcat.save()
        
        return HttpResponse({"status": 200})

class DeleteSubcategory(APIView):
    allowed_methods = ['POST']
    def post(self, request, *args, **kwargs):
        id = request.data.get('id' , None)
        subcat = models.Subcategory.objects.get(pk = id)
        subcat.delete()
        
        return HttpResponse({"status": 200})
    
class UpdateSubcategory(CreateAPIView):
    serializer_class =serializers.SubcategorySerializer
    allowed_methods = ['POST']
    def post(self, request, *args, **kwargs):
        idsub = request.data.get("id")
        sub = models.Subcategory.objects.get(pk = idsub)
        id = request.data.get('creator' , None)
        pr = models.Person.objects.get(pk = id)
        sub.creator = pr
        sub.title = request.data.get("title" )
        sub.save()
        print("hey it was successful")
        return HttpResponse({"status": 200})
    
class CreateCategory(CreateAPIView):
    serializer_class = serializers.CategorySerializer
    allowed_methods = ['POST']
    def post(self, request, *args, **kwargs):
        idperson = request.data.get('creator' , None)
        pr = models.Person.objects.get(pk = idperson)
        cat = models.Category(creator= pr, 
                            title = request.data.get('title' , None) )
        cat.save()
        
        return HttpResponse({"status": 200})

class DeleteCategory(APIView):
    allowed_methods = ['POST']
    def post(self, request, *args, **kwargs):
        id = request.data.get('id' , None)
        cat = models.Category.objects.get(pk = id)
        cat.delete()
        
        return HttpResponse({"status": 200})


class UpdateCategory(CreateAPIView):
    serializer_class =serializers.CategorySerializer
    allowed_methods = ['POST']
    def post(self, request, *args, **kwargs):
        idcat = request.data.get("category_id")
        cat = models.Category.objects.get(pk = idcat)
        id = request.data.get('creator_id' , None)
        pr = models.Person.objects.get(pk = id)
        cat.creator = pr
        cat.title = request.data.get("title" )
        cat.save()
        print("hey it was successful")
        return HttpResponse({"status": 200})


class CreateNotification(CreateAPIView):
    serializer_class =serializers.NotificationSerializer
    allowed_methods = ['POST']

    def post(self, request, *args, **kwargs):
        commentReplyId = request.data.get("commentReply" , None)
        likecommentId = request.data.get("likecomment" , None)
        notiftype = request.data.get("notiftype")
        senderId = request.data.get("sender")
        recieverId = request.data.get("reciever")

        if (commentReplyId !=None):
            commentReply = models.Commentt.objects.get(pk = commentReplyId)
        else:
            commentReply = None
        
        if (likecommentId != None):
            likecomment = models.LikeComment.objects.get(pk = likecommentId)
        else :
            likecomment = None

        sender = models.Person.objects.get(pk = senderId)
        reciever = models.Person.objects.get(pk = recieverId)

        notif = models.Notification( reciever = reciever , sender = sender , commentReply =commentReply ,likecomment =likecomment , notiftype =notiftype)
        notif.save()

        return Response({"msg":"notif created"} , status=status.HTTP_200_OK)

class DeleteNotification(CreateAPIView):
    serializer_class =serializers.NotificationSerializer
    allowed_methods = ['POST']
    def post(self, request, *args, **kwargs):
        id = request.data.get('id')
        notif = models.Notification.objects.get(pk = id)
        notif.delete()
        return Response({"msg":"Notification deleted"} , status=status.HTTP_200_OK)

class CreateQuestion(CreateAPIView):
    serializer_class =serializers.QuestionSerializer
    allowed_methods = ['POST']
    def post(self, request, *args, **kwargs):
        txt = request.data.get('request_text')
        whoAskId = request.data.get('whoAsk')
        whoAsk = models.Person.objects.get(pk = whoAskId)
        question = models.Question.objects.create(whoAsk = whoAsk , request_text = txt)
        question.save()
        return Response({"msg":"Question created"} , status=status.HTTP_200_OK)

class DeleteQuestion(CreateAPIView):
    serializer_class =serializers.QuestionSerializer
    allowed_methods = ['POST']
    def post(self, request, *args, **kwargs):
        id = request.data.get('id')
        question = models.Question.objects.get(pk = id)
        question.delete()
        return Response({"msg":"Question deleted"} , status=status.HTTP_200_OK)


class EditQuestion(CreateAPIView):
    serializer_class =serializers.QuestionSerializer
    allowed_methods = ['POST']
    def post(self, request, *args, **kwargs):
        id = request.data.get("id")
        question = models.Question.objects.get(pk = id)
        txt = request.data.get("request_text")
        question.request_text = txt
        question.save()
        return Response({"msg":"Question edited"} , status=status.HTTP_200_OK)


class SearchResource(APIView):
    serializer_class =serializers.RecourceSerializer
    allowed_methods = ['POST']
    def post(self, request, *args, **kwargs):
        text = request.data.get("text")
        cat = request.data.get("categoryID")
        personid = request.data.get('personId' , None)
        if (personid != None):
            person = models.Person.objects.get(pk = personid)
        resources = models.Resource.objects.filter(category = cat , title__icontains=text) 
        result = []
        print("seeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee")
        for resc in resources :
            dic = {}
            dic['resource_id'] = resc.id
            dic['title'] = resc.title    
            dic['submitterId'] = resc.submitter.id 
            dic['categoryId'] = resc.category.id 

            likeCount = models.Like.objects.filter(resc = resc).count()
            dic['likeCount'] = likeCount
            if personid == None :
                dic['isbookmark'] = 0
                dic['isliked'] = 0
            else:
                likeobject = models.Like.objects.filter(resc = resc , pers = person )
                allbookmarked = person.bookmarked.all()
                print("like object")
                print(likeobject)
                if(likeobject):
                    dic['isliked'] = 1
                else :
                    dic['isliked'] = 0
                    
                if allbookmarked.exists():
                    if resc in allbookmarked:
                        dic['isbookmark'] = 1
                    else :
                        dic['isbookmark'] = 0
                else:
                    dic['isbookmark'] = 0


            tags = []
            taglist = resc.tags.all()
            print(taglist )
            print(str(resc.title ))
            if taglist.exists():
                for tag in taglist:
                    tg = {}
                    tg['title'] = tag.title
                    tg['tagid'] = tag.id
                    tags.append(tg)
            dic['tags'] = tags
            dic['link'] = resc.link
            dic['pub_date'] = resc.pub_date
            # with open(resc.image.path , "rb") as image_file:
            #     image_data = base64.b64encode(image_file.read()).decode('utf-8')
            # dic['image'] = image_data
            result.append(dic)
        
        return Response(result)

    
class SearchCategorye(APIView):
    serializer_class =serializers.CategorySerializer
    allowed_methods = ['POST']
    def post(self, request, *args, **kwargs):
        text = request.data.get("text")
        categories = models.Category.objects.filter(title__icontains=text) 
        result = []
        for cat in categories :
            dic = {}
            dic['title'] = cat.title    
            dic['creatorId'] = cat.creator.id 
            dic['image'] = cat.image
            dic['category_id'] = cat.id
            result.append(dic)
        
        
        return Response(result)

class SingleResourceView(APIView):
    serializer_class =serializers.RecourceSerializer
    allowed_methods = ['POST']
    def post(self, request, *args, **kwargs):
        resourceId = request.data.get("resourceId")
        resource = models.Resource.objects.get(pk = resourceId)
        comments = models.Commentt.objects.filter(resc=resource)
        result = []
        # for res in resources:
        dic = {}
        dic['category'] = resource.category.id
        dic['description'] = resource.description
        dic['title'] = resource.title
        dic['submitter'] = resource.submitter.username
        dic['link'] = resource.link
        # dic['image'] = resource.image
        dic['pub_date'] = resource.pub_date
        cms = []
        for cm in comments :
            com = {}
            com['text'] = cm.text
            com['create_date'] = cm.create_date
            com['person_name'] = cm.pers.username
            com['person_id'] = cm.pers.id
            com['comment_id'] = cm.id
            likecommentcount = models.LikeComment.objects.filter(comm = cm).count()
            print(likecommentcount)
            com['likecommentcount'] = likecommentcount

            # com['tags']
            if (cm.reply_comment != None):
                com['reply_comment'] = cm.reply_comment.id
            else:
                com['reply_comment'] = None
            cms.append(com)
        dic['comment'] = cms
        tags = []
        subs = []
        tagids = []
        taglist = resource.tags.all()
        subslist = resource.subcategories.all()

        if subslist.exists():
            for sub in subslist :
                subs.append(sub.id)
        dic['subs'] = subs


        if taglist.exists():
            for tag in taglist:
                tagids.append(tag.id)
        dic['tagids'] = tagids
          
        print(taglist)
        if taglist.exists():
            for tag in taglist:
                tg = {}
                tg['title'] = tag.title
                tg['tagid'] = tag.id
                tags.append(tg)
        dic['tags'] = tags
        contenqualitycount = models.ContentQuality.objects.filter(resc = resource).count()
        coursedepthCount = models.CourseDepthAndCovergae.objects.filter(resc = resource).count()
        courpacethCount = models.CoursePace.objects.filter(resc = resource).count()
        videoqualityCount = models.VideoQuality.objects.filter(resc = resource).count()
        qualifiedinstructorCount = models.QualifiedInstructor.objects.filter(resc = resource).count()
        rating = 3
        dic ['contenqualitycount'] = contenqualitycount
        dic['coursedepthCount'] = coursedepthCount
        dic['courpacethCount'] = courpacethCount
        dic['videoqualityCount'] = videoqualityCount
        dic['qualifiedinstructorCount'] = qualifiedinstructorCount
        dic['rating'] = rating

        # result.append(dic)
        return Response(dic)


class CreateContentQuality(CreateAPIView):
    serializer_class = serializers.ContentQualitySerializer
    allowed_methods = ['POST']
    def post(self, request, *args, **kwargs):
        idperson = request.data.get('pers' , None)
        pr = models.Person.objects.get(pk = idperson)
        idresource = request.data.get('resc' , None)
        rc = models.Resource.objects.get(pk = idresource)
        print("this is " + idperson + idresource)
        temp = models.ContentQuality.objects.filter(pers = pr , resc = rc)
        if temp.exists() :
            return Response("Already exists!")
        rating = models.ContentQuality(pers= pr, 
                            resc= rc,
                            create_date= datetime.now())
        rating.save()
        
        return HttpResponse({"status": 200})
    
class CreateCourseDepthAndCovergae(CreateAPIView):
    serializer_class = serializers.CourseDepthAndCovergaeSerializer
    allowed_methods = ['POST']
    def post(self, request, *args, **kwargs):
        idperson = request.data.get('pers' , None)
        pr = models.Person.objects.get(pk = idperson)
        idresource = request.data.get('resc' , None)
        rc = models.Resource.objects.get(pk = idresource)
        print("this is " + idperson + idresource)
        temp = models.CourseDepthAndCovergae.objects.filter(pers = pr , resc = rc)
        if temp.exists() :
            return Response("Already exists!")
        rating = models.CourseDepthAndCovergae(pers= pr, 
                            resc= rc,
                            create_date= datetime.now())
        rating.save()
        
        return HttpResponse({"status": 200})
    
class CreateCoursePace(CreateAPIView):
    serializer_class = serializers.CoursePaceSerializer
    allowed_methods = ['POST']
    def post(self, request, *args, **kwargs):
        idperson = request.data.get('pers' , None)
        pr = models.Person.objects.get(pk = idperson)
        idresource = request.data.get('resc' , None)
        rc = models.Resource.objects.get(pk = idresource)
        print("this is " + idperson + idresource)
        temp = models.CoursePace.objects.filter(pers = pr , resc = rc)
        if temp.exists() :
            return Response("Already exists!")
        rating = models.CoursePace(pers= pr, 
                            resc= rc,
                            create_date= datetime.now())
        rating.save()
        
        return HttpResponse({"status": 200})
    
class CreateVideoQuality(CreateAPIView):
    serializer_class = serializers.VideoQualitySerializer
    allowed_methods = ['POST']
    def post(self, request, *args, **kwargs):
        idperson = request.data.get('pers' , None)
        pr = models.Person.objects.get(pk = idperson)
        idresource = request.data.get('resc' , None)
        rc = models.Resource.objects.get(pk = idresource)
        print("this is " + idperson + idresource)
        temp = models.VideoQuality.objects.filter(pers = pr , resc = rc)
        if temp.exists() :
            return Response("Already exists!")
        rating = models.VideoQuality(pers= pr, 
                            resc= rc,
                            create_date= datetime.now())
        rating.save()
        
        return HttpResponse({"status": 200})
    
class CreateQualifiedInstructor(CreateAPIView):
    serializer_class = serializers.QualifiedInstructorSerializer
    allowed_methods = ['POST']
    def post(self, request, *args, **kwargs):
        idperson = request.data.get('pers' , None)
        pr = models.Person.objects.get(pk = idperson)
        idresource = request.data.get('resc' , None)
        rc = models.Resource.objects.get(pk = idresource)
        print("this is " + idperson + idresource)
        temp = models.QualifiedInstructor.objects.filter(pers = pr , resc = rc)
        if temp.exists() :
            return Response("Already exists!")
        rating = models.QualifiedInstructor(pers= pr, 
                            resc= rc,
                            create_date= datetime.now())
        rating.save()
        
        return HttpResponse({"status": 200})
    
class CountContentQuality(CreateAPIView):
    serializer_class = serializers.ContentQualitySerializer
    allowed_methods = ['POST']
    def post(self, request, *args, **kwargs):
        idresource = request.data.get('resc' , None)
        rc = models.Resource.objects.get(pk = idresource)
        count = models.ContentQuality.objects.filter(resc = rc).count()
        countjson = {}
        countjson["count"] = count
        
        return Response(countjson)
    
class CountCourseDepth(CreateAPIView):
    serializer_class = serializers.CourseDepthAndCovergaeSerializer
    allowed_methods = ['POST']
    def post(self, request, *args, **kwargs):
        idresource = request.data.get('resc' , None)
        rc = models.Resource.objects.get(pk = idresource)
        count = models.CourseDepthAndCovergae.objects.filter(resc = rc).count()
        countjson = {}
        countjson["count"] = count
        
        return Response(countjson)
    
class CountCoursePace(CreateAPIView):
    serializer_class = serializers.CoursePaceSerializer
    allowed_methods = ['POST']
    def post(self, request, *args, **kwargs):
        idresource = request.data.get('resc' , None)
        rc = models.Resource.objects.get(pk = idresource)
        count = models.CoursePace.objects.filter(resc = rc).count()
        countjson = {}
        countjson["count"] = count
        
        return Response(countjson)   
    
class CountVideoQuality(CreateAPIView):
    serializer_class = serializers.VideoQualitySerializer
    allowed_methods = ['POST']
    def post(self, request, *args, **kwargs):
        idresource = request.data.get('resc' , None)
        rc = models.Resource.objects.get(pk = idresource)
        count = models.VideoQuality.objects.filter(resc = rc).count()
        countjson = {}
        countjson["count"] = count
        
        return Response(countjson)   
    
class CountQualifiedInstructor(CreateAPIView):
    serializer_class = serializers.QualifiedInstructorSerializer
    allowed_methods = ['POST']
    def post(self, request, *args, **kwargs):
        idresource = request.data.get('resc' , None)
        rc = models.Resource.objects.get(pk = idresource)
        count = models.QualifiedInstructor.objects.filter(resc = rc).count()
        countjson = {}
        countjson["count"] = count
        
        return Response(countjson) 

class DeleteContentQuality(APIView):
    allowed_methods = ['POST']
    def post(self, request, *args, **kwargs):
        idperson = request.data.get('pers' , None)
        pr = models.Person.objects.get(pk = idperson)
        idresource = request.data.get('resc' , None)
        rc = models.Resource.objects.get(pk = idresource)
        temp = models.ContentQuality.objects.get(pers = pr , resc = rc)
        rate = models.ContentQuality.objects.get(pk = temp.id)
        rate.delete()
        
        return HttpResponse({"status": 200})
    


class DeleteCourseDepthAndCovergae(APIView):
    allowed_methods = ['POST']
    def post(self, request, *args, **kwargs):
        idperson = request.data.get('pers' , None)
        pr = models.Person.objects.get(pk = idperson)
        idresource = request.data.get('resc' , None)
        rc = models.Resource.objects.get(pk = idresource)
        temp = models.CourseDepthAndCovergae.objects.get(pers = pr , resc = rc)
        rate = models.CourseDepthAndCovergae.objects.get(pk = temp.id)
        rate.delete()
        
        return HttpResponse({"status": 200})
    
    
class DeleteCoursePace(APIView):
    allowed_methods = ['POST']
    def post(self, request, *args, **kwargs):
        idperson = request.data.get('pers' , None)
        pr = models.Person.objects.get(pk = idperson)
        idresource = request.data.get('resc' , None)
        rc = models.Resource.objects.get(pk = idresource)
        temp = models.CoursePace.objects.get(pers = pr , resc = rc)
        rate = models.CoursePace.objects.get(pk = temp.id)
        rate.delete()
        
        return HttpResponse({"status": 200})

    
class DeleteVideoQuality(APIView):
    allowed_methods = ['POST']
    def post(self, request, *args, **kwargs):
        idperson = request.data.get('pers' , None)
        pr = models.Person.objects.get(pk = idperson)
        idresource = request.data.get('resc' , None)
        rc = models.Resource.objects.get(pk = idresource)
        temp = models.VideoQuality.objects.get(pers = pr , resc = rc)
        rate = models.VideoQuality.objects.get(pk = temp.id)
        rate.delete()
        
        return HttpResponse({"status": 200})
    
class DeleteQualifiedInstructor(APIView):
    allowed_methods = ['POST']
    def post(self, request, *args, **kwargs):
        idperson = request.data.get('pers' , None)
        pr = models.Person.objects.get(pk = idperson)
        idresource = request.data.get('resc' , None)
        rc = models.Resource.objects.get(pk = idresource)
        temp = models.QualifiedInstructor.objects.get(pers = pr , resc = rc)
        rate = models.QualifiedInstructor.objects.get(pk = temp.id)
        rate.delete()
        
        return HttpResponse({"status": 200})
    
    
class ListSubcategories(CreateAPIView):

    serializer_class =serializers.SubcategorySerializer
    allowed_methods = ['Post']
    
    def post(self, request, *args, **kwargs):
        querySet = models.Subcategory.objects.all()
        id = request.data.get('categoryId')
        # id =1/
        cat = models.Category.objects.get(pk=id)
        querySet = querySet.filter(category = cat )
        resources_dic =[]
        for res in querySet:
            response_data = {}
            response_data['id'] = res.id
            response_data['title'] = res.title

            resources_dic.append(response_data)
        return Response(resources_dic)

class FilterResourceList(CreateAPIView):
    serializer_class =serializers.CategorySerializer
    allowed_methods = ['Post']
    
    def post(self, request, *args, **kwargs):
        querySet = models.Resource.objects.all()
        id = request.data.get('categoryId')
        cat = models.Category.objects.get(pk=id)
        querySet = querySet.filter(category = cat )
        personid = request.data.get('personId' , None)
        if (personid != None):
            person = models.Person.objects.get(pk = personid)
        tagsIDsList = request.data.get('tags')
        tagsList=[]
        for tagid in tagsIDsList:
            tagsList.append(models.Tag.objects.get(pk = tagid))
            print("in first foooooor")
        for tag in tagsList:
            querySet = querySet.filter(tags = tag)
        print("querySet :" + str(querySet))

        subcategoriesIDsList = request.data.get('subcategories')
        subcategoryList = []
        for subcatid in subcategoriesIDsList:
            if subcatid != None:
                subcategoryList.append(models.Subcategory.objects.get(pk = subcatid))

        sourceListFilteredBySubcategory = []
        for subcat in subcategoryList :
            querySet = querySet.filter(subcategories = subcat)
            # sourceListFilteredBySubcategory.append(subcat.resources)
        print('sourceListFilteredBySubcategory :' + str(sourceListFilteredBySubcategory ))
        finalQuerySet = []
        # for resource in sourceListFilteredBySubcategory:
        #     if resource in querySet:
        #         finalQuerySet.append(resource)
        
        resources_dic =[]
        for res in querySet:
            response_data = {}
            response_data['resource_id'] = res.id
            response_data['creator'] = res.submitter.username
            response_data['title'] = res.title
            response_data['link'] = res.link

            likeCount = models.Like.objects.filter(resc = res).count()
            response_data['likeCount'] = likeCount
            if personid == None :
                response_data['isbookmark'] = 0
                response_data['isliked'] = 0
            else:
                likeobject = models.Like.objects.filter(resc = res , pers = person )
                allbookmarked = person.bookmarked.all()
                print("like object")
                print(likeobject)
                if(likeobject):
                    response_data['isliked'] = 1
                else :
                    response_data['isliked'] = 0
                    
                if allbookmarked.exists():
                    if res in allbookmarked:
                        response_data['isbookmark'] = 1
                    else :
                        response_data['isbookmark'] = 0
                else:
                    response_data['isbookmark'] = 0


            tags = []
            taglist = res.tags.all()
            print(taglist )
            print(str(res.title ))
            if taglist.exists():
                for tag in taglist:
                    tg = {}
                    tg['title'] = tag.title
                    tg['tagid'] = tag.id
                    tags.append(tg)
            response_data['tags'] = tags

            # response_data['image'] = res.image

            # print("callong all objects ")
            # tags = res.tags
            # tagg = []
            # print("befor for")
            # print(tags)
            # for tag in tags :
            #     # tagg.append(tag)
            #     dic = {}
            #     dic['id'] = tag.id
            #     dic['title'] = tag.title
            #     tagg.append(dic)
            #     print("inside for")

            # response_data['tags'] = tagg 
            # print("tag added successfuly")
            response_data['pub_date'] = res.pub_date
            print("in the second foooor")
            resources_dic.append(response_data)
        return Response(resources_dic)

class ShowProfileView(CreateAPIView):
    serializer_class =serializers.PersonSerializer
    allowed_methods = ['Post']
    def post(self, request, *args, **kwargs):
        personId = request.data.get('id')
        person = models.Person.objects.get(pk = personId)
        dic = {}
        dic['username'] = person.username
        dic['email'] = person.email
        dic['password'] = person.password
        dic['location'] = person.location
        dic['about'] = person.about
        return Response(dic , status=status.HTTP_200_OK)

class ShowNotifView(CreateAPIView):
    serializer_class =serializers.NotificationSerializer
    allowed_methods = ['Post']
    def post(self, request, *args, **kwargs):
        personId = request.data.get('id')
        reciever = models.Person.objects.get(pk = personId)
        notiflist = models.Notification.objects.filter(reciever = reciever)
        resualt = []
        for notif in notiflist:
            dic = {}
            dic['senderId'] = notif.sender.id
            dic['senderUsername'] = notif.sender.username
            dic['notifType'] = notif.notiftype
            dic['date'] = notif.pub_date
            likecomment = notif.likecomment
            commentReply = notif.commentReply
            commentid = 1
            commentText = ''
            if commentReply != None : #we have comment reply
                commentid = commentReply.id
                commentText = models.Commentt.objects.get(pk = commentid).text
            else :
                commentid = likecomment.id
                commentText = models.Commentt.objects.get(pk = commentid).text
            dic['commentid'] = commentid
            dic['commentText'] = commentText
            resualt.append(dic)

        return Response( resualt , status=status.HTTP_200_OK)

class SubmittedResourceList(CreateAPIView):
    serializer_class =serializers.RecourceSerializer
    allowed_methods = ['Post']
    def post(self, request, *args, **kwargs):
        personId = request.data.get('id')
        person = models.Person.objects.get(pk = personId)
        resourseList = models.Resource.objects.filter(submitter = person)
        # resualt = []
        # for resource in resourseList:
        #     dic = {}
        #     dic['resource_id'] = resource.id
        #     dic['title'] = resource.title
        #     dic['link'] = resource.link
        #     likeCount = models.Like.objects.filter(resc = resource).count()
        #     dic['likeCount'] = likeCount
        #     tags = resource.tags.all()
        #     taglist=[]
        #     if tags.exists():
        #         for tag in tags:
        #             tg = {}
        #             tg['title'] = tag.title
        #             tg['tagid'] = tag.id
        #             tg['type'] = tag.type.type
        #             taglist.append(tg)
        #     dic['tags'] = taglist
        #     resualt.append(dic)
        resources_dic =[]
        for res in resourseList:
            response_data = {}
            response_data['resource_id'] = res.id
            response_data['creator'] = res.submitter.username
            response_data['title'] = res.title
            response_data['link'] = res.link
            # response_data['image'] = res.image
            likeCount = models.Like.objects.filter(resc = res).count()
            response_data['likeCount'] = likeCount
            if personId == None :
                response_data['isbookmark'] = 0
                response_data['isliked'] = 0
            else:
                likeobject = models.Like.objects.filter(resc = res , pers = person )
                allbookmarked = person.bookmarked.all()
                print("like object")
                print(likeobject)
                if(likeobject):
                    response_data['isliked'] = 1
                else :
                    response_data['isliked'] = 0
                    
                if allbookmarked.exists():
                    if res in allbookmarked:
                        response_data['isbookmark'] = 1
                    else :
                        response_data['isbookmark'] = 0
                else:
                    response_data['isbookmark'] = 0

            print("callong all objects ")
            tags = res.tags.all()
            tagg = []
            print("befor for")
            print(tags)
            if tags.exists():
                for tag in tags :
                    # tagg.append(tag)
                    dic = {}
                    dic['id'] = tag.id
                    dic['title'] = tag.title
                    tagg.append(dic)
                    print("inside for")

            response_data['tags'] = tagg 
            print("tag added successfuly")
            response_data['pub_date'] = res.pub_date

            resources_dic.append(response_data)
        return Response(resources_dic , status=status.HTTP_200_OK)
        
class LikedResourceList(CreateAPIView):
    serializer_class =serializers.RecourceSerializer
    allowed_methods = ['Post']
    def post(self, request, *args, **kwargs):
        personId = request.data.get('id')
        person = models.Person.objects.get(pk = personId)
        likedlist = models.Like.objects.filter(pers= person)
        resourceList = []
        for like in likedlist:
            resource = models.Resource.objects.get(pk = like.resc.id)
            resourceList.append(resource)

        # resualt = []
        # for res in resourceList:
        #     dic = {}
        #     dic['resource_id'] = res.id
        #     dic['title'] = res.title
        #     dic['link'] = res.link
        #     likeCount = models.Like.objects.filter(resc = res).count()
        #     dic['likeCount'] = likeCount
        #     tags = res.tags.all()
        #     taglist=[]
        #     if tags.exists():
        #         for tag in tags:
        #             tg = {}
        #             tg['title'] = tag.title
        #             tg['tagid'] = tag.id
        #             tg['type'] = tag.type.type
        #             taglist.append(tg)
        #     dic['tags'] = taglist
        #     resualt.append(dic)
        resources_dic =[]
        for res in resourceList:
            response_data = {}
            response_data['resource_id'] = res.id
            response_data['creator'] = res.submitter.username
            response_data['title'] = res.title
            response_data['link'] = res.link
            # response_data['image'] = res.image
            likeCount = models.Like.objects.filter(resc = res).count()
            response_data['likeCount'] = likeCount
            if personId == None :
                response_data['isbookmark'] = 0
                response_data['isliked'] = 0
            else:
                likeobject = models.Like.objects.filter(resc = res , pers = person )
                allbookmarked = person.bookmarked.all()
                print("like object")
                print(likeobject)
                if(likeobject):
                    response_data['isliked'] = 1
                else :
                    response_data['isliked'] = 0
                    
                if allbookmarked.exists():
                    if res in allbookmarked:
                        response_data['isbookmark'] = 1
                    else :
                        response_data['isbookmark'] = 0
                else:
                    response_data['isbookmark'] = 0

            print("callong all objects ")
            tags = res.tags.all()
            tagg = []
            print("befor for")
            print(tags)
            if tags.exists():
                for tag in tags :
                    # tagg.append(tag)
                    dic = {}
                    dic['id'] = tag.id
                    dic['title'] = tag.title
                    tagg.append(dic)
                    print("inside for")

            response_data['tags'] = tagg 
            print("tag added successfuly")
            response_data['pub_date'] = res.pub_date

            resources_dic.append(response_data)
        return Response(resources_dic , status=status.HTTP_200_OK)
        
class BookmarkedResourceList(CreateAPIView):
    serializer_class =serializers.RecourceSerializer
    allowed_methods = ['Post']
    def post(self, request, *args, **kwargs):
        personId = request.data.get('id')
        person = models.Person.objects.get(pk = personId)
        bookmarkedList = person.bookmarked.all()
        # resualt = []
        # for res in bookmarkedList:
        #     dic = {}
        #     dic['resource_id'] = res.id
        #     dic['title'] = res.title
        #     dic['link'] = res.link
        #     tags = res.tags.all()
        #     taglist=[]
        #     if tags.exists():
        #         for tag in tags:
        #             tg = {}
        #             tg['title'] = tag.title
        #             tg['tagid'] = tag.id
        #             tg['type'] = tag.type.type
        #             taglist.append(tg)
        #     dic['tags'] = taglist
        #     likeCount = models.Like.objects.filter(resc = res).count()
        #     dic['likeCount'] = likeCount
        #     resualt.append(dic)
        resources_dic =[]
        for res in bookmarkedList:
            response_data = {}
            response_data['resource_id'] = res.id
            response_data['creator'] = res.submitter.username
            response_data['title'] = res.title
            response_data['link'] = res.link
            # response_data['image'] = res.image
            likeCount = models.Like.objects.filter(resc = res).count()
            response_data['likeCount'] = likeCount
            if personId == None :
                response_data['isbookmark'] = 0
                response_data['isliked'] = 0
            else:
                likeobject = models.Like.objects.filter(resc = res , pers = person )
                allbookmarked = person.bookmarked.all()
                print("like object")
                print(likeobject)
                if(likeobject):
                    response_data['isliked'] = 1
                else :
                    response_data['isliked'] = 0
                    
                if allbookmarked.exists():
                    if res in allbookmarked:
                        response_data['isbookmark'] = 1
                    else :
                        response_data['isbookmark'] = 0
                else:
                    response_data['isbookmark'] = 0

            print("callong all objects ")
            tags = res.tags.all()
            tagg = []
            print("befor for")
            print(tags)
            if tags.exists():
                for tag in tags :
                    # tagg.append(tag)
                    dic = {}
                    dic['id'] = tag.id
                    dic['title'] = tag.title
                    tagg.append(dic)
                    print("inside for")

            response_data['tags'] = tagg 
            print("tag added successfuly")
            response_data['pub_date'] = res.pub_date

            resources_dic.append(response_data)

        return Response(resources_dic , status=status.HTTP_200_OK)

class AddBookmark(CreateAPIView):
    allowed_methods = ['Post']
    def post(self, request, *args, **kwargs):
        personId = request.data.get('person_id')
        resourceId = request.data.get('resource_id')
        person = models.Person.objects.get(pk = personId)
        resource = models.Resource.objects.get(pk = resourceId)
        person.bookmarked.add(resource)
        person.save()
        return Response(status= status.HTTP_200_OK)

class DeleteBookmark(CreateAPIView):
    allowed_methods = ['Post']
    def post(self, request, *args, **kwargs):
        personId = request.data.get('person_id')
        resourceId = request.data.get('resource_id')
        resource = models.Resource.objects.get(pk = resourceId)
        person = models.Person.objects.get(pk = personId)
        person.bookmarked.remove(resource)
        person.save()
        return Response(status= status.HTTP_200_OK)

class ReportingComment(CreateAPIView):
    allowed_methods = ['Post']
    def post(self, request, *args, **kwargs):
        personId = request.data.get('person_id')
        person = models.Person.objects.get(pk = personId)
        commentId = request.data.get('comment_id')
        print("catch comment")
        print(commentId)
        comment = models.Commentt.objects.get(pk = commentId)
        print ('hey comment')
        print (comment)
        report_record = models.ReportComment.objects.filter(person = person , comment = comment)
        if report_record.exists() :
            return Response({"msg":"Reported" , "status" : 500 })
            
        else:
            report = models.ReportComment(person = person , comment = comment)
            report.save()
            #check the number of reports of a comment if it is more than 10 the comment should be deleted
            count_report = models.ReportComment.objects.filter(comment = comment).count()
            if (count_report > 10 ):
                comment.delete()
                print("comment deleted")
            return Response(status= status.HTTP_200_OK)

class ReportingResource(CreateAPIView):
    allowed_methods = ['Post']
    def post(self, request, *args, **kwargs):
        personId = request.data.get('person_id')
        person = models.Person.objects.get(pk = personId)
        resourceId = request.data.get('resource_id')
        resource = models.Resource.objects.get(pk = resourceId)
        report_record = models.ReportResource.objects.filter(person = person , resource = resource)

        if report_record.exists() :
            return Response({"msg":"Reported" , "status" : 500 })
            
        else:
            report = models.ReportResource(person = person , resource = resource)
            report.save()
            #check the number of reports of a resource if it is more than 10 the resource should be deleted
            count_report = models.ReportResource.objects.filter(resource = resource).count()
            if (count_report > 10 ):
                resource.delete()
                print("resource deleted")
            return Response(status= status.HTTP_200_OK)

class GetCategoryByID(CreateAPIView):
    allowed_methods = ['Post']
    def post(self, request, *args, **kwargs):
        categoryId = request.data.get('category_id')
        category = models.Category.objects.get(pk = categoryId)
        subcategorylist = models.Subcategory.objects.filter(category = category)
        print("this is subcategory list")
        print(subcategorylist)
        dic = {}
        subcatList = []
        dic['name'] = category.title
        for subcat in subcategorylist :
            dic_sub = {}
            dic_sub['title'] = subcat.title
            dic_sub['id'] = subcat.id
            subcatList.append(dic_sub)
        dic['subcategories'] = subcatList
        return Response(dic , status=status.HTTP_200_OK)


class RemoveLike(CreateAPIView):
    allowed_methods = ['Post']
    def post(self, request, *args, **kwargs):
        personId = request.data.get('person_id')
        resourceId = request.data.get('resource_id')
        person = models.Person.objects.get(pk = personId)
        resource = models.Resource.objects.get(pk = resourceId)
        likeobject = models.Like.objects.get(resc = resource , pers= person )
        likeobject.delete()
        return Response(status=status.HTTP_200_OK)

class SearchResourceInMainPage(APIView):
    serializer_class =serializers.RecourceSerializer
    allowed_methods = ['POST']
    def post(self, request, *args, **kwargs):
        text = request.data.get("text")
        # cat = request.data.get("categoryID")
        personid = request.data.get('personId' , None)
        if (personid != None):
            person = models.Person.objects.get(pk = personid)
        resources = models.Resource.objects.filter(title__icontains=text) 
        result = []
        print("seeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee")
        for resc in resources :
            dic = {}
            dic['resource_id'] = resc.id
            dic['title'] = resc.title    
            dic['submitterId'] = resc.submitter.id 
            dic['categoryId'] = resc.category.id 

            likeCount = models.Like.objects.filter(resc = resc).count()
            dic['likeCount'] = likeCount
            if personid == None :
                dic['isbookmark'] = 0
                dic['isliked'] = 0
            else:
                likeobject = models.Like.objects.filter(resc = resc , pers = person )
                allbookmarked = person.bookmarked.all()
                print("like object")
                print(likeobject)
                if(likeobject):
                    dic['isliked'] = 1
                else :
                    dic['isliked'] = 0
                    
                if allbookmarked.exists():
                    if resc in allbookmarked:
                        dic['isbookmark'] = 1
                    else :
                        dic['isbookmark'] = 0
                else:
                    dic['isbookmark'] = 0


            tags = []
            taglist = resc.tags.all()
            print(taglist )
            print(str(resc.title ))
            if taglist.exists():
                for tag in taglist:
                    tg = {}
                    tg['title'] = tag.title
                    tg['tagid'] = tag.id
                    tags.append(tg)
            dic['tags'] = tags
            dic['link'] = resc.link
            dic['pub_date'] = resc.pub_date
            # with open(resc.image.path , "rb") as image_file:
            #     image_data = base64.b64encode(image_file.read()).decode('utf-8')
            # dic['image'] = image_data
            result.append(dic)
        
        return Response(result)


class SendRequestNotification(APIView):
    serializer_class =serializers.RecourceSerializer
    allowed_methods = ['POST']
    def post(self, request, *args, **kwargs):
        personId = request.data.get("personId")

        queryset = models.Question.objects.all().order_by("-id")
        finalList = []
        for question in queryset :
            dic = {}
            dic['request_text'] = question.request_text
            dic['whoAskID'] = question.whoAsk.id
            dic['whoAskName'] = question.whoAsk.username
            finalList.append(dic)
        return Response(finalList , status=status.HTTP_200_OK)
        