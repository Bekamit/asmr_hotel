from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework.decorators import action

from my_auth.serializers import UserSerializer, RegisterSerializer, ProfileSerializer, ChangePasswordSerializer
from my_auth.utils import User


# Create your views here.

# class RegisterViewSet(CreateOnlyModelViewSet):
#     queryset = User.objects.order_by('-pk')
#     serializer_class = RegisterSerializer
#     permission_classes = [AllowAny]


# class ProfileViewSet(ListOnlyModelViewSet):
#     queryset = User.objects.order_by('-pk')
#     serializer_class = ProfileSerializer
#
#     def list(self, request, *args, **kwargs):
#         instance = get_object_or_404(User, pk=request.user.pk)
#         serializer = self.get_serializer(instance)
#
#         # serializer = self.get_serializer(request.user)
#         # print(request.user.address)
#         # print(request.user)
#         # print(request.user.pk)
#         # print(request.data)
#         # print(request.method)
#         # print(request.headers)
#         # print(request.query_params)
#
#         return Response(serializer.data)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.order_by('-pk')
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]

    # def get_object(self):
    #     return (
    #         self.request.user if self.action == 'profile' else super().get_object()
    #     )
    def get_object(self):
        if self.action in ['retrieve_profile', 'update_profile', 'change_password']:
            return self.request.user
        else:
            super().get_object()

    @action(
        methods=['post'],
        detail=False,
        serializer_class=RegisterSerializer,
        permission_classes=[AllowAny]
    )
    def register(self, request):
        return super().create(request)

    @action(
        methods=['get'],
        detail=False,
        url_path='profile',
        serializer_class=ProfileSerializer,
        permission_classes=[IsAuthenticated]
    )
    def retrieve_profile(self, request):
        return super().retrieve(request)

    @retrieve_profile.mapping.put
    def update_profile(self, request):
        return super().update(request)

    @action(
        methods=['put'],
        detail=False,
        url_path='change-password',
        serializer_class=ChangePasswordSerializer,
        permission_classes=[IsAuthenticated],
    )
    def change_password(self, request):
        return super().update(request)
