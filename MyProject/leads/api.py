from leads.models import Leads, Todos
from rest_framework import viewsets, permissions
from .serializers import LeadsSerializer, TodosSerializer


# Lead Viewset
class LeadViewSet(viewsets.ModelViewSet):
    #queryset = Leads.objects.all()
    permission_classes = [
        #permissions.AllowAny    # 전체 사용 가능하도록!
        permissions.IsAuthenticated
    ]
    serializer_class = LeadsSerializer


    def get_queryset(self):
        return self.request.user.leads.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


# Todo Viewset
class TodoViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.AllowAny    # 전체 사용 가능하도록!
        #permissions.IsAuthenticated
    ]
    serializer_class = TodosSerializer

    queryset = Todos.objects.all()

    # def get_queryset(self):
    #     return self.request.user.leads.all()

    # def perform_create(self, serializer):
    #     serializer.save(owner=self.request.user)

    