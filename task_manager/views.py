from django.shortcuts import render
from rest_framework import generics, status
from .models import Client, Project, User
from .serializers import ClientSerializer, ProjectSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import DestroyAPIView, RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class ProjectCreateView(APIView):
    def post(self, request, pk):
        try:
            client = Client.objects.get(id=pk)
        except Client.DoesNotExist:
            return Response(
                {"error": "Client not found"}, status=status.HTTP_404_NOT_FOUND
            )

        data = request.data.copy()
        data["client"] = client.id

        serializer = ProjectSerializer(data=data)
        if serializer.is_valid():
            project = serializer.save()

            users_data = request.data.get("users", [])
            for user_data in users_data:
                try:
                    user = User.objects.get(id=user_data["id"])
                    project.users.add(user)
                except User.DoesNotExist:
                    return Response(
                        {"error": f"User with id {user_data['id']} does not exist."},
                        status=status.HTTP_400_BAD_REQUEST,
                    )

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ClientListCreateView(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class ClientRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [IsAuthenticated]


class ClientDeleteView(DestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class ClientDetailView(RetrieveAPIView):
    queryset = Client.objects.all()  # This will retrieve all clients from the DB
    serializer_class = ClientSerializer  # Specify the serializer for the client
