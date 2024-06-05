import pandas as pd
from django.contrib.auth.models import User
from .models import Roles, Speciality, User, Module, Course, Score, Course_type, Absence


def import_data(request):
    # Read CSV file into a DataFrame
    csv_file_path = 'static/file.csv'
    df = pd.read_csv(csv_file_path)

    # Iterate through the DataFrame and create model instances
    for index, row in df.iterrows():
        
        # Create the Product instance
        user = User(
            first_name =row['first_name'],
            last_name =row['last_name'],
            roles = row['status'],
            date_of_birth = row['date_of_birth'],
            speciality_id = row['speciality_id'],
            photo = row['photo'],
            email = row['E-mail'],
            password = row['password'],
            student_id = row['student_id'],
            year = row['year'],
        )
        #to save the current product
        user.save()

    print("CSV data has been loaded into the Django database.")
