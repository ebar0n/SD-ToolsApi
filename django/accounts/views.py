from django.views.generic.base import TemplateView

from utils.github import GithubClientApi


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
