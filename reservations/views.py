import datetime
from django.views.generic import View
from django.contrib import messages
from django.shortcuts import redirect, reverse
from rooms import models as room_models
from . import models


class CreateError(Exception):
    pass


def create(request, room, year, month, day):
    try:
        redirect_response = None
        date_obj = datetime.datetime(year, month, day)
        room = room_models.Room.objects.get(pk=room)
        models.BookedDay.objects.get(day=date_obj, reservation__room=room)
        raise CreateError()
    except (room_models.Room.DoesNotExist, CreateError):
        messages.error(request, "Can't Reserve Fuckin Room!")
        redirect_response = redirect(reverse("core:home"))
    except models.BookedDay.DoesNotExist:
        reservation = models.Reservation.objects.create(
            guest=request.user,
            room=room,
            check_in=date_obj,
            check_out=date_obj + datetime.timedelta(days=1),
        )
        redirect_response = redirect(
            reverse("reservations:detail", kwargs={"pk": reservation.pk})
        )

    return redirect_response


class ReservationDetailView(View):
    pass
