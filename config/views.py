from django.http import HttpResponse

def landing_page(request):
    # Foydalanuvchi haqida ba'zi ma'lumotlar
    user_agent = request.META.get('HTTP_USER_AGENT', 'Noma’lum brauzer')
    path = request.path  # Foydalanuvchi kirgan URL yo'li
    method = request.method  # GET yoki POST ekanligi
    
    html_content = f"""
        <h1>Django muvaffaqiyatli ishlamoqda!</h1>
        <p><b>Sizning brauzeringiz:</b> {user_agent}</p>
        <p><b>Siz turgan sahifa:</b> {path}</p>
        <p><b>So'rov turi:</b> {method}</p>
    """
    
    return HttpResponse(html_content)