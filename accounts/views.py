from django.shortcuts import render
from django.shortcuts import get_object_or_404

from django.http import HttpResponse
from django.http import HttpResponseRedirect

from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
# Create your views here.

def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/')

@login_required
def profile(request):
    template = "pages/profile.html"
    user = request.user
    u_form = UserForm(instance=user)
    ui, ui_created = UserInfo.objects.get_or_create(
            user=user,
            )
    ui_form = UserInfoForm(instance=ui)
    var = {
            'u_form':u_form,
            'ui_form':ui_form,
            }
    return render(request, template, var)

@login_required
def change_user(request):
    if request.method == 'POST':
        print(request.POST)
        user = request.user
        user.email = request.POST['email']
        user.last_name = request.POST['last_name']
        user.first_name = request.POST['first_name']
        user.save()
        return HttpResponse('1')
    else:
        return HttpResponse('0')

@login_required
def change_userinfo(request):
    if request.method == 'POST':
        print(request.POST)
        user = request.user
        ui, ui_created = UserInfo.objects.get_or_create(user=user,)
        ui.gender = int(request.POST['gender'])
        ui.age = int(request.POST['age'])
        ui.edu_type = int(request.POST['edu_type'])
        ui.edu = int(request.POST['edu'])
        ui.art_exp = int(request.POST['art_exp'])
        ui.edu_prof = request.POST['edu_prof']
        ui.phone = request.POST['phone']
        ui.cinema_freq = int(request.POST['cinema_freq'])
        ui.cinema_genre = request.POST['cinema_genre']
        ui.save()
        return HttpResponse('1')
    else:
        return HttpResponse('0')

@login_required
def submit(request):
    if request.method == 'POST':
        print(request.POST)
        stimulus = get_object_or_404(Stimul, pk = int(request.POST['stimulus']))
        images = Image.objects.filter(stimul = stimulus)
        passed, p_created = StimulusPassed.objects.get_or_create(
                user=request.user,
                stimulus = stimulus,
                )

        if p_created == False:
            return HttpResponse('1')

        for image in images:
            a, a_created = Answer.objects.get_or_create(
                    user = request.user,
                    stimulus = stimulus,
                    image = image,
                    defaults = {
                        'pos': int(request.POST['images['+str(image.id)+']']),
                        }
                    )

            if a_created == False:
                return HttpResponse('1')

        return HttpResponse('0')
    else:
        return HttpResponseRedirect('/stimulus/'+stimulus.id)

@login_required
def result(request, stimulus_id):
    stimulus = get_object_or_404(Stimul, id=int(stimulus_id))
    answers = Answer.objects.filter(stimulus = stimulus)
    columns = [
            'stimulus_id',
            'stimulus_name',
            'username',
            'username_full',
            'gender',
            'education',
            'education_type',
            'art_exp',
            'age',
            'image_type',
            'image_position'
            ]
    data = [columns]
    for answer in answers:
        row = []
        gender = '-'
        edu = '-'
        edu_type = '-'
        art_exp = '-'
        age = 0
        row.append(stimulus.id)
        row.append(stimulus.name)
        row.append(answer.user.username)
        row.append(' '.join([answer.user.last_name,answer.user.first_name]))
        if UserInfo.objects.filter(user = answer.user).exists():
            user_info = UserInfo.objects.get(user = answer.user)
            if user_info.gender:
                gender = user_info.gender
            if user_info.edu:
                edu = user_info.edu
            if user_info.edu_type:
                edu_type = user_info.edu_type
            if user_info.art_exp:
                art_exp = user_info.art_exp
        row.append(gender)
        row.append(edu)
        row.append(edu_type)
        row.append(art_exp)
        row.append(user_info.age)
        row.append(answer.image.itype.name)
        row.append(answer.pos)
        data.append(row)

    file_name = "%s_%s_result" % (dt.today().strftime("%Y%m%d"), stimulus.name )
    return ExcelResponse(data, file_name)

@login_required
def stimulus(request, stimulus_id):
    template = 'pages/stimulus.html'
    stimulus = get_object_or_404(Stimul, pk = stimulus_id)
    images = Image.objects.filter(stimul = stimulus).order_by('?')
    var = {
            'stimulus':stimulus,
            'images':images,
            }
    return render(request, template, var)
