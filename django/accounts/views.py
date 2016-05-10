from django.views.generic.base import TemplateView

from utils.github import GithubClientApi
from utils.toggl import TogglClientApi
from django.contrib import messages


class GithubRepositoriesView(TemplateView):
    """
    Render main template
    """
    template_name = 'repositories.html'

    def get_context_data(self, **kwargs):
        context = super(GithubRepositoriesView, self).get_context_data(**kwargs)

        if self.request.user.is_authenticated():
            try:
                user = self.request.user.social_auth.get(provider='github')
                api = GithubClientApi(user.access_token)
                context['repositories'] = api.get_repos().json()
            except Exception:
                raise

        return context


class TogglConf(object):
   api_token = '5e0b1105429ae4f29fe60a218046086c'
   workspace = 1235420

class TogglCreateView(TogglConf, TemplateView):
    """
    Render main template
    """
    template_name = 'toggl-create_projects.html'

    def post(self, request, *args, **kwargs):
        context = super(TogglCreateView, self).get_context_data(**kwargs)
        api = TogglClientApi(self.api_token, self.workspace)
        context['project'] = api.create_project(self.request.POST.get('name'))
        messages.info(request, 'Projecto {} creado'.format(self.request.POST.get('name')))
        return super(TogglCreateView, self).render_to_response(context)


class TogglWorkspaceProjectsView(TogglConf, TemplateView):
    """
    Render main template
    """
    template_name = 'toggl-workspace-projects.html'

    def get_context_data(self, **kwargs):
        context = super(TogglWorkspaceProjectsView, self).get_context_data(**kwargs)
        api = TogglClientApi(self.api_token, self.workspace)
        context['projects'] = api.get_workspace_projects().json()
        return context