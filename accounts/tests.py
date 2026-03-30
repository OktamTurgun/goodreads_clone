from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

class RegisterViewTest(TestCase):

  def setUp(self):
    # Har bir test oldindan ishga tushadi
    self.client = Client()
    self.url = reverse('accounts:register')

  # ---- GET testlar ---

  def test_register_page_loads(self):
    """Sahifa ochiladi va to'g'ti template ishlatiladi"""
    response = self.client.get(self.url)

    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'accounts/register.html')

  def test_register_page_has_form(self):
    """Sahifda forma bor"""

    response = self.client.get(self.url)

    self.assertIn('form', response.context)

  # ---- POST testlar ---

  def test_register_success(self):
    """To'g'ri ma'lumot bilan ro'yxatdan o'tish ishlaydi"""
    response = self.client.post(self.url, {
      'username': 'testuser',
      'email': 'testuser@example.com',
      'password1': 'password123!',
      'password2': 'password123!',
    })

    # Bazada user yaratildimi?
    self.assertTrue(User.objects.filter(username='testuser').exists())

    # Bosh sahifaga redirect qildimi?
    self.assertRedirects(response, reverse('landing_page'))

  def test_register_auto_login(self):
    """Ro'yxatdan o'tgach auto login bo'ladi"""
    self.client.post(self.url, {
      'username': 'testuser',
      'email': 'testuser@example.com',
      'password1': 'password123!',
      'password2': 'password123!',
    })

    # Sessionda user bormi? 
    self.assertTrue('_auth_user_id' in self.client.session)

  def test_register_invalid_password(self):
    """Parollar mos kelmasa xato beradi"""
    response = self.client.post(self.url, {
      'username': 'testuser',
      'email': 'testuser@example.com',
      'password1': 'password123!',
      'password2': 'wrongpass123!',
    })

    # Sahifa qayta ko'rsatiladi
    self.assertEqual(response.status_code, 200)

    # Bazada user yaratilmadi
    self.assertFalse(User.objects.filter(username='testuser').exists())

  def test_register_dublicate_username(self):
    """Bir hil username bilan ikki marta ro'yxatdan o'tib bo'lmaydi"""

    # Avvar user yaratamiz
    User.objects.create_user(username='testuser', password='password123!')

    response = self.client.post(self.url, {
      'username': 'testuser',
      'email': 'testuser@example.com',
      'password1': 'password123!',
      'password2': 'password123!',
    })

    self.assertEqual(response.status_code, 200)
    self.assertEqual(User.objects.filter(username='testuser').count(), 1)


class LoginViewTest(TestCase):
  
  def setUp(self):
    self.url = reverse('accounts:login')

    self.user = User.objects.create_user(
      username = 'testuser',
      password = 'password123!'
    )

  def test_login_page_loads(self):
    response = self.client.get(self.url)

    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'accounts/login.html')

  def test_login_success(self):
    response = self.client.post(self.url, {
      'username': 'testuser',
      'password': 'password123!'
    })

    self.assertRedirects(response, reverse('landing_page'))

  def test_login_auto_session(self):
    self.client.post(self.url, {
      'username': 'testuser',
      'password': 'password123!'
    })

    self.assertTrue('_auth_user_id' in self.client.session)

  def test_login_wrong_password(self):
    response = self.client.post(self.url, {
      'username': 'testuser',
      'password': 'wrongPass123!'
    })

    self.assertEqual(response.status_code, 200)
    self.assertFalse('_auth_user_id' in self.client.session)

  def test_login_wrong_username(self):
    response = self.client.post(self.url, {
      'username': 'wrongname',
      'password': 'password123!'
    })

    self.assertEqual(response.status_code, 200)
    self.assertFalse('_auth_user_id' in self.client.session)
    