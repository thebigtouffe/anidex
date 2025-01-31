# Generated by Django 2.0.3 on 2018-04-01 08:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('classification', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Biome',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Entrée',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numéro', models.IntegerField(blank=True, editable=False, null=True)),
                ('nom_cherchable', models.CharField(blank=True, editable=False, max_length=250, null=True)),
                ('nom_latin', models.CharField(max_length=200, unique=True)),
                ('nom_vernaculaire', models.CharField(max_length=200)),
                ('autres_noms', models.CharField(blank=True, max_length=200, null=True)),
                ('conservation', models.CharField(blank=True, choices=[('EX', 'Éteint'), ('EW', 'Éteint dans la nature'), ('CR', 'En danger critique'), ('EN', 'En danger'), ('VU', 'Vulnérable'), ('NT', 'Presque menacée'), ('LC', 'Préoccupation mineure'), ('NE', 'Non évalué')], max_length=2, null=True)),
                ('catégorie', models.CharField(blank=True, choices=[('O', 'Ordre'), ('F', 'Famille'), ('G', 'Genre'), ('E', 'Espèce')], default='E', max_length=2, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('poids_femelle', models.FloatField(default=0.0, verbose_name="Poids moyen d'une femelle en grammes")),
                ('poids_mâle', models.FloatField(default=0.0, verbose_name="Poids moyen d'un mâle en grammes")),
                ('poids', models.FloatField(default=0.0, verbose_name='Poids moyen en grammes')),
                ('taille_femelle', models.FloatField(default=0.0, verbose_name="Taille moyen d'une femelle en centimètres")),
                ('taille_mâle', models.FloatField(default=0.0, verbose_name="Taille moyen d'un mâle en centimètres")),
                ('taille', models.FloatField(default=0.0, verbose_name='Taille moyen en centimètres')),
                ('espérance_vie', models.IntegerField(default=0, verbose_name='Espérance de vie (jours)')),
                ('régime_alimentaire', models.CharField(blank=True, choices=[('O', 'Omnivore'), ('H', 'Herbivore'), ('C', 'Carnivore'), ('Ci', 'Insectivore'), ('Ch', 'Hématophage'), ('Cp', 'Piscivore'), ('Cm', 'Molluscivore'), ('P', 'Planctonivore'), ('A', 'Autre')], max_length=2, null=True)),
                ('miniature_url', models.CharField(blank=True, max_length=250, null=True)),
                ('miniature', models.BinaryField(default=b'')),
                ('photo1_url', models.CharField(blank=True, max_length=250, null=True)),
                ('photo1_droits', models.CharField(blank=True, max_length=250, null=True)),
                ('photo1_source', models.CharField(blank=True, max_length=250, null=True)),
                ('photo2_url', models.CharField(blank=True, max_length=250, null=True)),
                ('photo2_droits', models.CharField(blank=True, max_length=250, null=True)),
                ('photo2_source', models.CharField(blank=True, max_length=250, null=True)),
                ('photo3_url', models.CharField(blank=True, max_length=250, null=True)),
                ('photo3_droits', models.CharField(blank=True, max_length=250, null=True)),
                ('photo3_source', models.CharField(blank=True, max_length=250, null=True)),
                ('biome', models.ManyToManyField(blank=True, to='animals.Biome')),
                ('espèce', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to='classification.Espèce')),
                ('famille', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to='classification.Famille')),
                ('genre', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to='classification.Genre')),
            ],
        ),
        migrations.CreateModel(
            name='Groupe1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Groupe2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Habitat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Territoire',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numéro', models.CharField(max_length=10, unique=True)),
                ('nom', models.CharField(blank=True, max_length=250, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='entrée',
            name='groupe1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='animals.Groupe1'),
        ),
        migrations.AddField(
            model_name='entrée',
            name='groupe2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='animals.Groupe2'),
        ),
        migrations.AddField(
            model_name='entrée',
            name='habitat',
            field=models.ManyToManyField(blank=True, to='animals.Habitat'),
        ),
        migrations.AddField(
            model_name='entrée',
            name='localisation',
            field=models.ManyToManyField(blank=True, to='animals.Territoire'),
        ),
        migrations.AddField(
            model_name='entrée',
            name='ordre',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to='classification.Ordre'),
        ),
    ]
