from django.urls import include, path
from django.views import View
from rest_framework import routers
from . import views

from django.contrib import admin
from django.urls import path
# from rest_framework.authtoken import views
# from assets.views import *

from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register(r'persons', views.PersonViewSet)
router.register(r'resources', views.ResourceViewSet)
router.register(r'Categories', views.CategoryListViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('createResource/' , views.CreateResource.as_view()),
    path('DeleteResource/' , views.DeleteResource.as_view()),
    path('updateResource/' , views.UpdateResource.as_view()),
    #path('ListResources/' , views.ListResources.as_view()),
    path('createLike/' , views.CreateLike.as_view()),
    path('DeleteLike/' , views.DeleteLike.as_view()),
    path('createSubcategory/' , views.CreateSubcategory.as_view()),
    path('DeleteSubcategory/' , views.DeleteSubcategory.as_view()),
    path('updateSubcategory/' , views.UpdateSubcategory.as_view()),
    path('createCategory/' , views.CreateCategory.as_view()),
    path('signup/' , views.SignUpPersonView.as_view()),
    path('login/' , views.LogIn.as_view()),
    path('deletePerson/' , views.DeletePersonView.as_view()),
    path('updatePerson/' , views.UpdatePersonView.as_view()),
    path('createTag/' , views.CreateTag.as_view()),
    path('deleteTag/' , views.DeleteTag.as_view()),
    path('updateTag/' , views.UpdateTag.as_view()),
    path('ListTags/' , views.ListTags.as_view()),
    path('createcomment/' , views.CreateComment.as_view()),
    path('createnotification/' , views.CreateNotification.as_view()),
    path('deletecomment/' , views.DeleteComment.as_view()),
    path('deletenotification/' , views.DeleteNotification.as_view()),
    path('editcomment/' , views.EditComment.as_view()),
    path('createquestion/' , views.CreateQuestion.as_view()),
    path('deletequestion/' , views.DeleteQuestion.as_view()),
    path('editQuestion/' , views.EditQuestion.as_view()),
    path('categoryList/' , views.ListCategories.as_view()),
    path('resourceList/' , views.ListResource.as_view()),
    path('searchResource/' , views.SearchResource.as_view()),
    path('searchCategory/' , views.SearchCategorye.as_view()),
    # path('resourceListt/<int:id>/' , views.sendListResourceByGet)
    path('singleResource/' , views.SingleResourceView.as_view()),
    path('ContentQuality/' , views.CreateContentQuality.as_view()),
    path('CourseDepth/' , views.CreateCourseDepthAndCovergae.as_view()),
    path('CoursePace/' , views.CreateCoursePace.as_view()),
    path('VideoQuality/' , views.CreateVideoQuality.as_view()),
    path('QualifiedInstructor/' , views.CreateQualifiedInstructor.as_view()),
    path('CountContentQuality/' , views.CountContentQuality.as_view()),
    path('CountCourseDepth/' , views.CountCourseDepth.as_view()),
    path('CountCoursePace/' , views.CountCoursePace.as_view()),
    path('CountVideoQuality/' , views.CountVideoQuality.as_view()),
    path('CountQualified/' , views.CountQualifiedInstructor.as_view()),
    path('likecomment/' , views.CreateLikecomment.as_view()),
    path('deleteContentQuality/' , views.DeleteContentQuality.as_view()),
    path('deleteCourseDepth/' , views.DeleteCourseDepthAndCovergae.as_view()),
    path('deleteCoursePace/' , views.DeleteCoursePace.as_view()),
    path('deleteVideoQuality/' , views.DeleteVideoQuality.as_view()),
    path('deleteQualifiedInstructor/' , views.DeleteQualifiedInstructor.as_view()),
    path('subcategoryList/' , views.ListSubcategories.as_view()),
    path('setimage/' , views.setimageinResource.as_view()),
    path('filterResourceList/' , views.FilterResourceList.as_view()),
    path('showProfile/' , views.ShowProfileView.as_view()),
    path('showNotification/' , views.ShowNotifView.as_view()),
    path('submittedResourceList/' , views.SubmittedResourceList.as_view()),
    path('likeResourseList/' , views.LikedResourceList.as_view()),
    path('BookmarkedList/' , views.BookmarkedResourceList.as_view()),
    path('addBookmark/' , views.AddBookmark.as_view()),
    path('deleteBookmark/' , views.DeleteBookmark.as_view()),
    path('reportComment/' , views.ReportingComment.as_view()),
    path('reportResource/' , views.ReportingResource.as_view()),
    path('getCategoryByID/' , views.GetCategoryByID.as_view()),
    path('deleteLike/' , views.RemoveLike.as_view()),
    path('newstResourceList/' , views.latest_resourceList.as_view()),
    path('orderbyLikeResourceList/' , views.orderbyLike_resourceList.as_view()),
    path('deleteCategory/' , views.DeleteCategory.as_view()),
    path('updateCategory/' , views.UpdateCategory.as_view()),
    path('SearchResourceInMainPage/' , views.SearchResourceInMainPage.as_view()),
    path('SendRequestNotification/' , views.SendRequestNotification.as_view())
] 
# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    
