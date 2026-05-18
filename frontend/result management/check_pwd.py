import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'student_management_system.settings')
django.setup()

from student_management_app.models import CustomUser

users = CustomUser.objects.all()[:10]
common_passwords = ['123456', '12345678', 'password', 'staff', 'student', 'admin', '12345']

print("Checking passwords for users...")
for u in users:
    found = False
    for p in common_passwords:
        if u.check_password(p):
            print(f"User: {u.username} (Type: {u.user_type}) -> Password: '{p}'")
            found = True
            break
    if not found:
        print(f"User: {u.username} -> Password not in common list")
