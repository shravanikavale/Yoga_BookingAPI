import logging
from pytz import timezone as pytz_timezone
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils.timezone import localtime
from django.db import transaction
from django.conf import settings
from .models import FitnessClass, Bookings
from .serializers import FitnessClassSerializer, BookingsSerializer

# Create your views here.


logger = logging.getLogger(__name__)

class FitnessClassList(APIView):
    def post(self, request):
        serializer = FitnessClassSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.info("Fitness class created.")
            return Response(serializer.data)
    
    def get(self, request):
        classes = FitnessClass.objects.all()
        serializer = FitnessClassSerializer(classes, many=True)
        return Response(serializer.data)

class BookClass(APIView):
    def post(self, request):
        class_id = request.data.get("class_id")
        client_name = request.data.get("client_name")
        client_email = request.data.get("client_email")
        user_timezone = request.data.get("timezone", "Asia/Kolkata")

        if not all([class_id, client_name, client_email]):
            return Response({"error": "All fields are required"}, status.HTTP_400_BAD_REQUEST)

        try:
            with transaction.atomic():
                fitness_class = FitnessClass.objects.select_for_update().get(id=class_id)

                if Bookings.objects.filter(fitness_class=fitness_class, client_email=client_email).exists():
                    return Response({"error": "You have already booked this class"}, status.HTTP_400_BAD_REQUEST)

                if fitness_class.available_slots < 1:
                    return Response({"error": "No slots are available"}, status.HTTP_400_BAD_REQUEST)
                
                fitness_class.available_slots -= 1
                fitness_class.save()

                bookings = Bookings.objects.create(
                    fitness_class=fitness_class,
                    client_name=client_name,
                    client_email=client_email
                )


                local_dt = fitness_class.date_time.astimezone(pytz_timezone(user_timezone))

                logger.info(f"Booking successful for {client_email} in class {class_id}")

                serializer = BookingsSerializer(bookings)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        except FitnessClass.DoesNotExist:
            logger.error(f"Invalid class ID: {class_id}")
            return Response({"error": "Invalid class ID"}, status=status.HTTP_404_NOT_FOUND)
        

        

        
class BookingList(APIView):
    def get(self, request):
        email = request.query_params.get("email")
        if email:
            bookings = Bookings.objects.filter(client_email=email)
        else:
            bookings = Bookings.objects.all()
        serializer = BookingsSerializer(bookings, many=True)
        return Response(serializer.data)