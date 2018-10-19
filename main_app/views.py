from django.shortcuts import render, redirect, get_object_or_404
from .models import Widget
from .forms import WidgetForm

# Create your views here.
def index(request):
    model = Widget
    widgets = Widget.objects.all()
    form = WidgetForm()
    return render(request, 'index.html', {'widgets': widgets, 'form': form})

def add_widget(request):
   form = WidgetForm(request.POST)
   form.save()
   return redirect('index')

def widget_delete(request, pk, template_name='main_app/widget_confirm_delete.html'):
    widget = get_object_or_404(Widget, pk=pk)    
    if request.method=='POST':
        widget.delete()
        return redirect('index')
    return render(request, template_name, {'widget':widget})