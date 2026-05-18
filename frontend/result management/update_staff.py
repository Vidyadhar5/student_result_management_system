import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'student_management_system.settings')
django.setup()

from student_management_app.models import CustomUser, Staffs

indian_data = [
    ("Amit", "Sharma", "amit.sharma@example.com", "123 MG Road, Bangalore, Karnataka"),
    ("Rahul", "Verma", "rahul.verma@example.com", "456 Anna Salai, Chennai, Tamil Nadu"),
    ("Priya", "Singh", "priya.singh@example.com", "789 Connaught Place, New Delhi"),
    ("Vikram", "Patel", "vikram.patel@example.com", "101 Marine Drive, Mumbai, Maharashtra"),
    ("Sunita", "Reddy", "sunita.reddy@example.com", "202 Banjara Hills, Hyderabad, Telangana"),
    ("Rajesh", "Gupta", "rajesh.gupta@example.com", "303 Salt Lake City, Kolkata, West Bengal"),
]

staffs = CustomUser.objects.filter(user_type=2).order_by('id')

for i, user in enumerate(staffs):
    data = indian_data[i % len(indian_data)]
    user.first_name = data[0]
    user.last_name = data[1]
    # Adding a small unique suffix just in case
    user.username = f"{data[0].lower()}_{data[1].lower()}"
    user.email = data[2]
    user.save()
    
    # Update Staff address
    try:
        staff_profile = Staffs.objects.get(admin=user)
        staff_profile.address = data[3]
        staff_profile.save()
    except Staffs.DoesNotExist:
        pass

    print(f"Updated {user.id} to {user.first_name} {user.last_name}")

print("Successfully updated staff names and addresses.")
