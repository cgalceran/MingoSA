# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Nombre', models.CharField(max_length=100)),
                ('Razon Social', models.CharField(max_length=100, null=True, blank=True)),
                ('Direccion Fiscal', models.CharField(max_length=200)),
                ('Departamento', models.CharField(max_length=10, blank=True)),
                ('Codigo Postal', models.CharField(max_length=10, null=True, blank=True)),
                ('localidad', models.CharField(max_length=50)),
                ('Pais', models.CharField(max_length=50)),
                ('Telefono', models.PositiveSmallIntegerField(blank=True)),
                ('Email', models.EmailField(max_length=254)),
                ('condicionpago', models.CharField(default=b'EF', max_length=2, choices=[(b'EF', b'efectivo'), (b'CC', b'Cuenta Corriente')])),
                ('cuit', models.IntegerField()),
                ('ingresosbrutos', models.IntegerField()),
                ('numerodocumento', models.IntegerField()),
                ('tipodedocumento', models.CharField(max_length=22, choices=[(b'dni', b'DNI'), (b'cdi', b'CDI'), (b'lc', b'LC'), (b'le', b'LE'), (b'pasaporte', b'PASAPORTE'), (b'cuit', b'CUIT'), (b'cuil', b'CUIL'), (b'ci', b'CI Extranjera'), (b'en_tramite', b'En tramite'), (b'acta_nacimiento', b'Acta nacimiento'), (b'ci_ba_rpn', b'CI Bs. As. RNP'), (b'no_id', b'Sin identificar venta gbl diaria'), (b'certificado_migratorio', b'Certificado de Migracion'), (b'padron_anses', b'Usado por Anses para Padron')])),
                ('enviarcomprobante', models.BooleanField(default=True)),
                ('percibeiibb', models.BooleanField()),
                ('percibeiiva', models.BooleanField()),
                ('tratamientoimpositivo', models.CharField(max_length=21, choices=[(b'monotributista', b'Monotributista'), (b'responsable_inscripto', b'Responsable Inscripto'), (b'consumidor_final', b'Consumidor Final'), (b'iva_exento', b'IVA exento')])),
            ],
        ),
        migrations.CreateModel(
            name='Provincia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='cliente',
            name='Provincia',
            field=models.ForeignKey(to='clientes.Provincia'),
        ),
    ]
