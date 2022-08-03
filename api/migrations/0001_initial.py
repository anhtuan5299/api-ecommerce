from django.db import migrations
from api.user.models import CustomUser

class Migration(migrations.Migration):
    def seed_data(apps,schema_editor):
        user = CustomUser(name='anhtuan',
                          email='anhtuan.dev@dev.dev',
                          is_staff=True,
                          is_superuser=True,
                          phone='0385480629',
                          gender='Male'
                          )
        user.set_password('1')
        user.save()

    dependencies = [

    ]

    operations = [
        migrations.RunPython(seed_data),
    ]
