from django.db import models
from django.core.exceptions import FieldDoesNotExist

class Person(models.Model):
    username =      models.CharField(max_length=30)
    password =      models.CharField(max_length=10)
    email =         models.EmailField()
    about =         models.CharField(max_length=1000 , null=True , blank=True)
    location =      models.CharField(max_length=50 ,  null=True , blank=True)
    ROLE =          (('U', 'User'), ('A', 'Admin'))
    role =          models.CharField(max_length=1, choices=ROLE)
    bookmarked =    models.ManyToManyField("Resource" ,  null=True , blank=True )

    def __str__(self):
        return self.username + str(self.pk)
class TagType(models.Model):
    type = models.CharField(max_length=50)
class Tag(models.Model):#we have to change this part 
    # but i dont remember what i wanted to change
    creator =       models.ForeignKey(Person, on_delete=models.CASCADE)
    title =         models.CharField(max_length=40)
    type =          models.ForeignKey(TagType , on_delete=models.CASCADE)

    def __str__(self):
        return self.title + str(self.pk)
    
class Resource(models.Model):
    category =      models.ForeignKey("Category" , on_delete=models.CASCADE )
    submitter =     models.ForeignKey(Person , on_delete=models.CASCADE)
    title =         models.CharField(max_length=500)
    link =          models.URLField(max_length=300)
    tags =          models.ManyToManyField(Tag , null = True , blank = True)
    pub_date =      models.DateTimeField(auto_now_add=True)
    image =         models.ImageField(upload_to = "images" , null = True , blank = True  )
    description=    models.CharField(max_length=500 , null = True , blank=True)
    subcategories=  models.ManyToManyField("Subcategory" , null = True , blank = True)

    def __str__(self):
        return self.title + str(self.pk)
    
class Category(models.Model):
    creator =       models.ForeignKey(Person,on_delete=models.CASCADE)
    title =         models.CharField(max_length=50)
    image =         models.CharField(max_length=200 , null = True , blank = True)
    def __str__(self):
        return self.title + str(self.pk)
    

class Subcategory(models.Model):
    creator =       models.ForeignKey(Person , on_delete=models.CASCADE)
    category =      models.ForeignKey(Category , on_delete=models.CASCADE)
    title =         models.CharField(max_length=100)
    # resources =     models.ManyToManyField(Resource)

    def __str__(self):
        return self.title + str(self.pk)
    

class Like(models.Model):
    create_date =   models.DateTimeField(auto_now_add=True)
    resc =          models.ForeignKey(Resource , on_delete=models.CASCADE)
    pers =          models.ForeignKey(Person , on_delete=models.CASCADE)

class Commentt(models.Model):
    create_date =   models.DateTimeField(auto_now_add=True)
    text =          models.CharField(max_length=500)
    pers =          models.ForeignKey(Person , on_delete=models.CASCADE)
    resc =          models.ForeignKey(Resource , on_delete=models.CASCADE)
    reply_comment = models.ForeignKey('self', on_delete=models.CASCADE , null=True , blank=True  )#im not sure about this one

    def __str__(self):
        return self.text + str(self.pk)
    

class LikeComment(models.Model):
    create_date =   models.DateTimeField('create date' , auto_now_add=True )
    pers =          models.ForeignKey(Person , on_delete=models.CASCADE)
    comm =          models.ForeignKey(Commentt , on_delete=models.CASCADE)

class Question(models.Model):
    request_text =  models.CharField(max_length=600)
    whoAsk =        models.ForeignKey(Person , on_delete=models.CASCADE , related_name= "whoAsk")
    whoAnswer =     models.ForeignKey(Person , on_delete=models.CASCADE , related_name= "whoAnswer" ,null=True , blank=True)

    def __str__(self):
        return self.request_text + str(self.pk)
    
class Notification(models.Model):
    pub_date =      models.DateTimeField(auto_now_add=True ,null=True , blank=True)
    reciever =      models.ForeignKey(Person , on_delete=models.CASCADE , related_name= "reciever")
    sender =        models.ForeignKey(Person , on_delete=models.CASCADE , related_name= "sender")
    NotifType=      (('CR' , 'commentReply') , ('LC' , 'likeComment') , ('R' , "Request"))
    notiftype=      models.CharField(max_length=2 , choices=NotifType)
    likecomment=    models.ForeignKey(LikeComment , on_delete=models.CASCADE , null=True , blank=True)
    commentReply=   models.ForeignKey(Commentt , on_delete=models.CASCADE , null=True , blank=True)

class ContentQuality(models.Model):
    create_date =   models.DateTimeField('create date' , auto_now_add=True)
    pers =          models.ForeignKey(Person , on_delete=models.CASCADE)
    resc =          models.ForeignKey(Resource , on_delete=models.CASCADE)

class CourseDepthAndCovergae(models.Model):
    create_date =   models.DateTimeField('create date' , auto_now_add=True)
    pers =          models.ForeignKey(Person , on_delete=models.CASCADE)
    resc =          models.ForeignKey(Resource , on_delete=models.CASCADE)

class CoursePace(models.Model):
    create_date =   models.DateTimeField('create date' , auto_now_add=True)
    pers =          models.ForeignKey(Person , on_delete=models.CASCADE)
    resc =          models.ForeignKey(Resource , on_delete=models.CASCADE)
    
class VideoQuality(models.Model):
    create_date =   models.DateTimeField('create date' , auto_now_add=True)
    pers =          models.ForeignKey(Person , on_delete=models.CASCADE)
    resc =          models.ForeignKey(Resource , on_delete=models.CASCADE)

class QualifiedInstructor(models.Model):
    create_date =   models.DateTimeField('create date' , auto_now_add=True)
    pers =          models.ForeignKey(Person , on_delete=models.CASCADE)
    resc =          models.ForeignKey(Resource , on_delete=models.CASCADE)

class ReportResource(models.Model):
    create_date =   models.DateTimeField('create date' , auto_now_add=True)
    person =        models.ForeignKey(Person , on_delete=models.CASCADE)
    resource=       models.ForeignKey(Resource , on_delete=models.CASCADE)

class ReportComment(models.Model):
    create_date =   models.DateTimeField('create date' , auto_now_add=True)
    person =        models.ForeignKey(Person , on_delete=models.CASCADE)
    comment =       models.ForeignKey(Commentt , on_delete=models.CASCADE)