import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'student_management_system.settings')
django.setup()

from student_management_app.models import CustomUser, Staffs, Students, AdminHOD

for u in CustomUser.objects.filter(user_type=2):
    try:
        Staffs.objects.get(admin=u)
    except Staffs.DoesNotExist:
        print(f"ERROR: Staff profile missing for user: {u.email} (ID: {u.id})")
        # Let's create it to fix it!
        Staffs.objects.create(admin=u, address="")
        print(f"Created missing Staff profile for {u.email}")

for u in CustomUser.objects.filter(user_type=3):
    try:
        Students.objects.get(admin=u)
    except Students.DoesNotExist:
        print(f"ERROR: Student profile missing for user: {u.email} (ID: {u.id})")

for u in CustomUser.objects.filter(user_type=1):
    try:
        AdminHOD.objects.get(admin=u)
    except AdminHOD.DoesNotExist:
        print(f"ERROR: Admin profile missing for user: {u.email} (ID: {u.id})")

print("Check completed.")
