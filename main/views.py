from django.shortcuts import render, redirect
from .forms import ReviewForm, AppointmentForm
from .models import Review, Service, Profile, Appointment
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import permission_required
from django.core.mail import send_mail
from django.conf import settings


# Create your views here.


def services(request):
    services = Service.objects.all()
    return render(request, "services.html", {"services": services})


def reviews(request):
    if request.method == "POST":
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("reviews")
    else:
        form = ReviewForm()

    reviews_list = Review.objects.all()
    return render(request, "reviews.html", {"form": form, "reviews": reviews_list})


def contacts(request):
    profile = Profile.objects.first()
    return render(request, "contacts.html", {"profile": profile})


def review_page(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    return render(request, "review_page.html", {"review": review})


def handler404(request, exception):
    return render(request, "404.html", status=404)


@permission_required("main.add_review")
def submit_review(request):
    if request.method == "POST":
        rating = request.POST.get("rating")
        comment = request.POST.get("comment")
        image = request.FILES.get("image")

        review = Review.objects.create(
            author=request.user,
            rating=rating,
            comment=comment,
            image=image,
        )
        review.save()
        return redirect("reviews")

    form = ReviewForm()
    return render(request, "submit_review.html", {"form": form})


def homepage(request):
    return render(request, "homepage.html")


def confirm_appointment(appointment):
    try:
        send_mail(
            "Подтверждение записи",
            f"Уважаемый {appointment.client_name}, ваша запись подтверждена на {appointment.date}.",
            settings.DEFAULT_FROM_EMAIL,
            [appointment.client_email],
            fail_silently=False,
        )
    except Exception as e:
        print(f"Ошибка отправки email: {e}")


def booking(request):
    if request.method == "POST":
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save()
            messages.success(request, "Вы успешно записались на сеанс!")
            confirm_appointment(appointment)
            return redirect("booking")
        else:
            messages.error(request, "Пожалуйста, исправьте ошибки в форме.")
    else:
        form = AppointmentForm()

    return render(request, "booking.html", {"form": form})
