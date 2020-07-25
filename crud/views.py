from django.shortcuts import render
from .forms import NewUserForm


# Create your views here.
def index(request):
    return render(request, 'crud/index.html')


def user_info(request):
    form = NewUserForm()

    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('form invalid!')
    return render(request, 'crud/users.html', {'form': form})
