from django.urls import path
from .views import NoteDelete, NoteDetail, NoteList, NoteUpdate ,NoteCreate

urlpatterns = [
    path('',NoteList.as_view(),name='note_list'),
    path('note/create/', NoteCreate.as_view(),name='note_create'),
    path('note/<pk>/',NoteDetail.as_view(),name='note_detail'),
    path('note/<pk>/delete', NoteDelete.as_view(),name='note_delete'),
    path('note/<pk>/update', NoteUpdate.as_view(),name='note_update'),
]
