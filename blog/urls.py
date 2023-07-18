from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    # # 게시글
    path('', views.BlogIndex.as_view(), name='list'),
    path('error', views.BlogError.as_view(), name='error'),
    path('write/', views.PostWrite.as_view(), name='write'),
    path('<int:post_id>/', views.PostDetail.as_view(), name='detail'),
    path('edit/<int:post_id>', views.PostUpdate.as_view(), name='edit'),
    path('delete/<int:post_id>/', views.PostDelete.as_view(), name='delete'),
    # # 코멘트
    # path('<int:post_id>/comment/write', views.CommentWrite.as_view(), name='cm-write'),
    # path('comment/delete/<int:comment_id>', views.CommentDelete.as_view(), name='cm-delete'),
    # # 태그
    # path('<int:post_id>/tag/write', views.HashTagWrite.as_view(), name='tag-write'),
    # path('tag/delete/<int:hashTag_id>', views.HashTagDelete.as_view(), name='tag-delete'),
    # # 검색
    # path('search/<str:tag>', views.SearchTag,as_view(), name='tag-search'),
]