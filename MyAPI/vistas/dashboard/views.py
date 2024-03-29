from django.views.generic import TemplateView

class DashboardView(TemplateView):
    template_name = 'app/app_dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['panel'] = 'Panel de Administrador'
        return context

