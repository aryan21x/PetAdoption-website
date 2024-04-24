from django.contrib.auth.backends import BaseBackend
import mysql.connector
from django.conf import settings
from django.contrib.auth import get_user_model

class MySQLBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None):
        try:
            # Connect to MySQL database
            mydb = mysql.connector.connect(
                host=settings.DB_HOST,
                user=settings.DB_USER,
                password=settings.DB_PASSWORD,
                database=settings.DB_NAME
            )

            cursor = mydb.cursor(dictionary=True)
            cursor.execute("SELECT * FROM user_table WHERE username = %s", (username,))
            user_row = cursor.fetchone()

            if user_row:
                # Check password
                if user_row['password'] == password:
                    # Get or create the user
                    User = get_user_model()
                    user, created = User.objects.get_or_create(username=username)
                    return user

        except Exception as e:
            print(e)
            return None

    def get_user(self, user_id):
        User = get_user_model()
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
