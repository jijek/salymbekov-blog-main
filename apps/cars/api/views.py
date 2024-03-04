from rest_framework.viewsets import ModelViewSet

from apps.cars.models import Car
from apps.cars.api.serializers import CarSerializer


class CarApiViewSet(ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer