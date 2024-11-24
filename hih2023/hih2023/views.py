from django.contrib.auth import update_session_auth_hash, login
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from django.http import FileResponse, Http404, HttpResponse

from .forms import RegistrationForm, PasswordChangingForm
from main.models import UserModel, User


@login_required
def viewer(request):
    #if request.user.userprofile.role == 'user':
        #return redirect('/')

    if request.method == 'GET':
        filename = request.GET.get('id', '')
        application = filename.split('.')[-1]

        try:
            return FileResponse(open(f'data/files/{filename}', 'rb'), content_type=f'application/{application}')
        except FileNotFoundError:
            raise Http404()


@user_passes_test(lambda u: u.is_superuser)
def permissions(request):
    if request.method == "POST":
        print(request.POST)
        for i in range(len(request.POST.getlist('input_email'))):
            try:
                u = UserModel.objects.get(username=request.POST.getlist('input_email')[i])
                u.userprofile.role = request.POST.getlist('select')[i]
                u.userprofile.save()
            except Exception:
                return redirect('/')
    template = 'search/permissions.html'
    users = User.objects.all()
    context = {'users': users}
    return render(request, template, context)


def registration_view(request):
    template = 'registration/registration_form.html'
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            obj, created = UserProfile.objects.get_or_create(
                user=user,
                role='user'
            )
            obj.save()
            return redirect('search:index')
    else:
        form = RegistrationForm()

    return render(request, template, {'form': form})


@login_required
def change_password(request):
    template = 'registration/password_change_form.html'
    if request.method == "POST":
        form = PasswordChangingForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
    else:
        form = PasswordChangingForm(request.user)
    return render(request, template, {'form': form})


@user_passes_test(lambda u: u.is_superuser)
def permissions(request):
    if request.method == "POST":
        print(request.POST)
        for i in range(len(request.POST.getlist('input_email'))):
            try:
                u = UserModel.objects.get(username=request.POST.getlist('input_email')[i])
                u.userprofile.role = request.POST.getlist('select')[i]
                u.userprofile.save()
            except Exception:
                return redirect('/')
    template = 'search/permissions.html'
    users = UserModel.objects.all()
    context = {'users': users}
    return render(request, template, context)
