from django.urls import path
from .views import EventView,TicketPurchaseView

urlpatterns = [
    path('', EventView.as_view()),
    path('<int:id>/purchase/', TicketPurchaseView.as_view()),

]