from rest_framework import serializers
from .models import Project, User
from .models import Client, Project


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ["id", "client_name", "created_at", "updated_at", "created_by"]


# class ProjectSerializer(serializers.ModelSerializer):
#     client = serializers.StringRelatedField()
#     users = serializers.StringRelatedField(many=True)

#     class Meta:
#         model = Project
#         fields = ["id", "project_name", "client", "users", "created_at", "created_by"]


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id"]  # Adjust based on your User model fields


class ProjectSerializer(serializers.ModelSerializer):
    users = UserSerializer(many=True, required=False)  # Optional users

    class Meta:
        model = Project
        fields = ['id', 'project_name', 'client', 'users', 'created_at']

    def create(self, validated_data):
        users_data = validated_data.pop('users', [])  # Extract users from validated_data
        project = Project.objects.create(**validated_data)  # Create the project instance
        
        # Assign users to the project
        for user_data in users_data:
            # Ensure 'id' exists in user_data
            user_id = user_data.get('id')  # Fetch 'id' from user_data
            if user_id:
                try:
                    user = User.objects.get(id=user_id)  # Get user by 'id'
                    project.users.add(user)  # Add user to the project
                except User.DoesNotExist:
                    raise serializers.ValidationError(f"User with id {user_id} does not exist.")
            else:
                raise serializers.ValidationError("'id' field is required for each user.")
        
        return project