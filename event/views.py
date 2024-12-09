from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import EventSerializer, TicketPurchaseSerializer
from .models import Event, Ticket
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import BasePermission

class IsAdminRole(BasePermission):
    """
    Custom permission to allow access only to users with the 'admin' role.
    """

    def has_permission(self, request, view):
        # Ensure the user is authenticated and has the 'admin' role
        return request.user.is_authenticated and request.user.role == 'admin'

class IsAdminOrUser(BasePermission):
    """
    Custom permission to allow access only to users with 'admin' or 'user' roles.
    """

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role in ['admin', 'user']

class IsUserRole(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'user'

class EventView(APIView):
    permission_classes = [IsAuthenticated]  # Default permissions for the class

    def get_permissions(self):
        if self.request.method == "POST":
            return [IsAdminRole()]  # Admin-only permission for POST
        return [IsAuthenticated()]
    def post(self, request):

        serializer = EventSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get(self, request):
        # Fetch all events
        events = Event.objects.all()
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)

class TicketPurchaseView(APIView):
    permission_classes = [IsUserRole]

    def post(self, request, id):

        # Validate the request body
        serializer = TicketPurchaseSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        quantity = serializer.validated_data['quantity']

        try:
            event = Event.objects.get(id=id)

            # Check ticket availability
            if event.tickets_sold + quantity > event.total_tickets:
                return Response(
                    {"error": "Not enough tickets available."},
                    status=status.HTTP_400_BAD_REQUEST
                )

            # Update tickets_sold and save
            event.tickets_sold += quantity
            event.save()

            # Create a new Ticket entry
            ticket = Ticket.objects.create(
                user=request.user,
                event=event,
                quantity=quantity
            )

            return Response(
                {
                    "message": "Ticket purchase successful.",
                    "ticket_id": ticket.id,
                    "event": event.name,
                    "quantity": ticket.quantity
                },
                status=status.HTTP_201_CREATED
            )

        except Event.DoesNotExist:
            return Response(
                {"error": "Event not found."},
                status=status.HTTP_404_NOT_FOUND
            )