from django.shortcuts import render,get_object_or_404 , redirect ,HttpResponse
from django.views.generic import ListView,DetailView,UpdateView , View , CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Note
from .forms import NoteForm
# Create your views here.

class NoteList(LoginRequiredMixin,ListView):
    model = Note
    template_name='notes/list.html'
    context_object_name='notes'
    def get_queryset(self):
        return Note.objects.filter(user=self.request.user).order_by('-created_at')
    

class NoteCreate(LoginRequiredMixin,CreateView):
    model = Note
    template_name = 'notes/create.html'
    form_class = NoteForm
    success_url = "/"

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        return super().form_valid(form)
    

class NoteDetail(LoginRequiredMixin,DetailView):
    model = Note
    template_name = 'notes/detail.html'
    context_object_name = 'note'
    def dispatch(self, request, *args, **kwargs):
        note = self.get_object()
        if note.user == self.request.user:
            return super().dispatch(request, *args, **kwargs)
        return HttpResponse('bro stop its not your note')
    

class NoteDelete(LoginRequiredMixin,View):
    def get (self, request, pk):
        note = get_object_or_404(Note,pk=pk)
        if note.user == self.request.user:
            note.delete()
            return redirect('note_list')
        else:
            return HttpResponse('not yours')


class NoteUpdate(LoginRequiredMixin,UpdateView):
    model = Note
    form_class = NoteForm
    template_name = 'notes/update.html'
    success_url = '/'
    def dispatch(self, request, *args, **kwargs):
        note = self.get_object()
        if note.user == self.request.user:
            return super().dispatch(request, *args, **kwargs)
        return HttpResponse('not yours boy')

    
    