import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Auteur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('biographie', models.TextField()),
                ('birthday', models.DateField()),
                ('deadday', models.DateField(blank=True, null=True)),
                ('nationality', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Editeur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('website', models.URLField()),
                ('mail_contact', models.EmailField(max_length=254)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Exemplaire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(max_length=100)),
                ('acquisition_date', models.DateField()),
                ('localisation', models.CharField(max_length=255)),
                ('disponibility', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Emprunt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loan_date', models.DateTimeField(auto_now_add=True)),
                ('expected_return_date', models.DateField()),
                ('effective_return_date', models.DateField(blank=True, null=True)),
                ('state', models.CharField(choices=[('in_progess', 'In progress'), ('complete', 'Complete'), ('late', '  Late')], default='in_progress', max_length=20)),
                ('remarks', models.TextField(blank=True, null=True)),
                ('users', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='emprunts', to=settings.AUTH_USER_MODEL)),
                ('copy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='emprunts', to='gestion_bibliotheque.exemplaire')),
            ],
        ),
        migrations.CreateModel(
            name='Livre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('resume', models.TextField()),
                ('publication_date', models.DateField()),
                ('isbn', models.CharField(max_length=13, unique=True)),
                ('page_number', models.IntegerField()),
                ('language', models.CharField(max_length=50)),
                ('authors', models.ManyToManyField(related_name='livres', to='gestion_bibliotheque.auteur')),
                ('categorie', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='livres', to='gestion_bibliotheque.categorie')),
                ('editors', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='livres', to='gestion_bibliotheque.editeur')),
            ],
        ),
        migrations.AddField(
            model_name='exemplaire',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exemplaires', to='gestion_bibliotheque.livre'),
        ),
        migrations.CreateModel(
            name='Evaluation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('evaluation', models.IntegerField()),
                ('commentary', models.TextField(blank=True, null=True)),
                ('evaluation_date', models.DateTimeField(auto_now_add=True)),
                ('recommended', models.BooleanField(default=False)),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('users', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='evaluations', to=settings.AUTH_USER_MODEL)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='evaluations', to='gestion_bibliotheque.livre')),
            ],
        ),
        migrations.CreateModel(
            name='Commentaire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('publication_date', models.DateTimeField(auto_now_add=True)),
                ('evaluation', models.IntegerField(default=0)),
                ('visible', models.BooleanField(default=True)),
                ('modere', models.BooleanField(default=False)),
                ('users', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commentaires', to=settings.AUTH_USER_MODEL)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commentaires', to='gestion_bibliotheque.livre')),
            ],
        ),
    ]
