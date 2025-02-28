from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse

CustomUser = get_user_model()

class CustomUserTestCase(APITestCase):
    
    def setUp(self):
        """Set up a test user before each test."""
        self.user = CustomUser.objects.create_user(
            username='testuser', 
            email='test@example.com', 
            password='testpassword', 
            role='IT_FIRM',
            is_verified=True
        )
        self.admin_user = CustomUser.objects.create_superuser(
            username='adminuser', 
            email='admin@example.com', 
            password='adminpassword'
        )
        self.login_url = reverse('token_obtain_pair')
        self.user_list_url = reverse('user-list')
    
    def test_user_creation(self):
        """Test creating a new user."""
        user = CustomUser.objects.create_user(
            username='newuser', 
            email='new@example.com', 
            password='newpassword'
        )
        self.assertEqual(user.username, 'newuser')
        self.assertTrue(user.check_password('newpassword'))
    
    def test_superuser_creation(self):
        """Test creating a superuser."""
        self.assertTrue(self.admin_user.is_superuser)
        self.assertTrue(self.admin_user.is_staff)
    
    def test_user_login(self):
        """Test logging in with valid credentials."""
        response = self.client.post(self.login_url, {
            'username': 'testuser',
            'password': 'testpassword'
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)
    
    def test_user_login_invalid_credentials(self):
        """Test logging in with invalid credentials."""
        response = self.client.post(self.login_url, {
            'username': 'testuser',
            'password': 'wrongpassword'
        })
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    
    def test_get_users_list_authenticated(self):
        """Test retrieving user list as an authenticated admin user."""
        self.client.force_login(self.admin_user)
        response = self.client.get(self.user_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_get_users_list_unauthenticated(self):
        """Test that unauthenticated users cannot retrieve user list."""
        response = self.client.get(self.user_list_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    
    def test_user_permissions(self):
        """Test user permissions field does not interfere with auth.User permissions."""
        self.assertEqual(self.user.groups.count(), 0)
        self.assertEqual(self.user.user_permissions.count(), 0)
    
    def test_update_user_profile(self):
        """Test updating user profile information."""
        self.client.force_login(self.user)
        response = self.client.patch(self.user_list_url + f"{self.user.id}/", {
            'phone_number': '1234567890'
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.user.refresh_from_db()
        self.assertEqual(self.user.phone_number, '1234567890')
    
    def test_delete_user_as_admin(self):
        """Test deleting a user as an admin."""
        self.client.force_login(self.admin_user)
        response = self.client.delete(self.user_list_url + f"{self.user.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(CustomUser.objects.filter(id=self.user.id).exists())
