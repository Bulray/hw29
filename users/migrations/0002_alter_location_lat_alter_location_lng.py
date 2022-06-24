
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='lat',
            field=models.DecimalField(decimal_places=6, max_digits=8, null=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='lng',
            field=models.DecimalField(decimal_places=6, max_digits=8, null=True),
        ),
    ]
