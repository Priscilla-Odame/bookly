from projectapp.models.project import Project
from django.views.generic import TemplateView, ListView 
from django.db.models import Q

class HomePageView(TemplateView):
    template_name = 'searchtype.html'

class SearchResultsView(ListView):
    model = Project
    template_name = 'search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Project.objects.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        )
        return object_list