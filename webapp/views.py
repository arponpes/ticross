from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import login as login_view
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DetailView
from core.models import Project, ActivityJournal, Registry
from .forms import ProjectForm
from django.views.generic.edit import DeleteView, CreateView, UpdateView, FormView
from django.views.generic.list import ListView
from django.utils import timezone
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib.auth.views import LoginView, LogoutView


class LoginWithCheckIn(LoginView):

    def form_valid(self, form):
        resp = super().form_valid(form)
        check_in(self)
        return resp


class LoginWithCheckOut(LogoutView):

    def dispatch(self, request, *args, **kwargs):
        check_out(self)
        resp = super().dispatch(request, *args, **kwargs)
        
        return resp


class ProjectListView(ListView):
    model = Project
    template_name = 'webapp/projects_list.html'

    def get_context_data(self, **kwargs):
        context = super(ProjectListView, self).get_context_data(**kwargs)
        total_time = Registry.objects.get(user=self.request.user, end__isnull=True)
        context.update({
            'activity_journal_list': ActivityJournal.objects.filter(end__isnull=True, user=self.request.user),
            'total_worked_time': str(total_time.total_worked_today())[:-10]
        })
        return context

    def get_queryset(self):
        qs = super().get_queryset().filter(user=self.request.user)

        for p in qs:
            p.total_time = p.time_calculator(self.request.user)[:-3]

        return qs


class ProjectDetail(DetailView):
    model = Project
    template_name = 'webapp/project_detail.html'


class ProjectCreate(CreateView):
    model = Project
    fields = ['project_name', 'description', 'user']
    template_name = 'webapp/project_edit.html'
    success_url = reverse_lazy('projects_list')


class ProjectUpdate(UpdateView):
    model = Project
    fields = ['project_name', 'description', 'user']
    template_name = 'webapp/project_edit.html'
    success_url = reverse_lazy('projects_list')


class ProjectDelete(DeleteView):
    model = Project
    template_name = 'forms/project_confirm_delete.html'
    success_url = reverse_lazy('projects_list')


@login_required
def project_start(request, pk):
    user = request.user
    activitys = ActivityJournal.objects.filter(
        end__isnull=True, user=user)

    for activity in activitys:
        activity.close_activity()

    proyecto = Project.objects.get(id=pk)
    activity_journal = ActivityJournal(
        user=user, project=proyecto, start=timezone.now())
    activity_journal.save()

    return redirect('projects_list')


@login_required
def project_stop(request, pk):
    proyecto = Project.objects.get(id=pk)
    activitys = ActivityJournal.objects.filter(
        end__isnull=True, user=request.user, project=proyecto)
    for activity in activitys:
        activity.close_activity()

    return redirect('projects_list')



def check_in(self):
    records = Registry.objects.filter(user=self.request.user, end__isnull=True)

    if len(records) == 0:
        new_registry = Registry(start=timezone.now(), user=self.request.user)
        new_registry.save()



def check_out(self):
    records = Registry.objects.filter(user=self.request.user, end__isnull=True)
    records.update(end=timezone.now())