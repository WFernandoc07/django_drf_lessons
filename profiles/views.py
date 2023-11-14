from rest_framework import viewsets
from .serializers import ProfileSerializer
from .models import Profile

class ProfileViewSet(viewsets.ModelViewSet):
    # ForeignKey - OneToOne
    queryset = Profile.objects.select_related('author').all()
    # ManyTomany -> prefetch_related
    serializer_class = ProfileSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        print(queryset.query)
        return queryset
