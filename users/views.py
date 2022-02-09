from django.shortcuts import render
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from users.forms import profileUpdateForm, userUpdateForm
from users.models import Profile as Pro
from users.models import  kerkesat
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from memberships.models import Membership, UserMembership, Subscription
from django.core.mail import send_mail
from django.core.mail import EmailMessage

# Create your views here.

def get_user_membership(request):
    user_membership_qs = UserMembership.objects.filter(user=request.user)
    if user_membership_qs.exists():
        return user_membership_qs.first()
    return None

def get_user_subscription(request):
    user_subscription_qs = Subscription.objects.filter(user_membership = get_user_membership(request))
    if user_subscription_qs.exists():
        return user_subscription_qs.first()
    return None


@login_required
def Profile(request):
    user_membership = get_user_membership(request)
    user_subscription = get_user_subscription(request)
    if request.method == 'POST':
        u_form = userUpdateForm(request.POST,instance=request.user)
        p_form = profileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, '¡Tu cuenta ha sido actualizada exitosamente!')
            return redirect('users:profile')
    else:
        u_form = userUpdateForm(instance=request.user)
        p_form = profileUpdateForm(instance=request.user.profile)

    context= {
        'u_form':u_form,
        'p_form':p_form,
        'user_membership':user_membership,
        'user_subscription': user_subscription
    }
    return render(request,'profile/profile.html',context)


def kerkesa(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('e-mail')
        numri_tel = request.POST.get('phone')
        prof = request.user.profile
        kerkesa = kerkesat(profili=prof, name=name, email=email, numri_tel=numri_tel)
        kerkesa.save()
        prof_id = prof.id
        Pro.objects.filter(id=prof_id).update(is_teacher=True)
        
        message = '¡su kerkesa de cuenta de maestro fue aceptada! Ahora puede volver a MesoOn y cargar cursos y conferencias, ¡buen trabajo!'
        send_mail(
            'MesoOn, kerkesa u pranua.',
            message,
            'mesoon@no-reply.com',
            [email],
            fail_silently=False,
        )
        send_mail(
            'MesoOn',
            'Alguien hizo una kerkesa de cuenta de maestro. Mi información:' + name + ' , ' + email + ' , ' + numri_tel + ' , ' + str(prof) + '.',
            'mesoon@no-reply.com',
            ['redian1marku@gmail.com'],
            fail_silently=False,
        )
        messages.info(
            request,
                'La kerkesa se envió con éxito, se le notificará por correo electrónico.',)
        return redirect('courses:home')


