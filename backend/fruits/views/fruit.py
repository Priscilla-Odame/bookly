from rest_framework import serializers, viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from fruits.models import Fruit
from fruits.serializers import FruitSerializer


fruits =  {
1: Fruit(id=1, name="Orange", in_season="Yes"),
2: Fruit(id=2, name="Apple", in_season="No"),
3: Fruit(id=3, name="Grapes", in_season="Yes"),
4: Fruit(id=4, name="Mangos", in_season="No"),
} 


class FruitViewSet(viewsets.ViewSet):
    serializer_class = FruitSerializer
    queryset = fruits.items()
    in_season = None
    name = None

    def list(self, request):
        results = []
        for field in ('name','in_season'):
            setattr(self, field, request.GET.get(field, None))
        for k,v in fruits.items():
            if self.in_season:
                if v.in_season == self.in_season:
                    results.append(v)
            else:
                results.append(v)
        print(results)
        serializer = FruitSerializer(results, many=True)
        return Response(serializer.data)

