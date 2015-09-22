from django.db import models

# Create your models here.

from django.db import models

# Create your models here.

class Provincia(models.Model):
    nombre = models.CharField(max_length=50)

    def __unicode__(self):
        return u'%s' % (self.nombre)

class Cliente(models.Model):
    """Esta es la Base de Datos de cada Cliente"""
    
    nombre = models.CharField(max_length=100, name='Nombre')
    razonsocial = models.CharField(max_length=100,blank=True,null=True, name='RazonSocial')
    direccionfiscal = models.CharField(max_length=200, name='Direccion Fiscal') 
    departamento = models.CharField(max_length=10,blank=True, name='Departamento')
    codigopostal = models.CharField(max_length=10,blank=True,null=True, name='Codigo Postal')
    localidad = models.CharField(max_length=50)
    provincia = models.ForeignKey(Provincia, name='Provincia')
    pais = models.CharField(max_length=50, name='Pais')      
    telefono = models.PositiveSmallIntegerField(blank=True, name='Telefono')
    email = models.EmailField(max_length=254, name='Email')
        
    EFECTIVO = 'EF'
    CUENTACORRIENTE = 'CC'
    CONDICIONES_DE_PAGO = (
        (EFECTIVO, 'efectivo'),
        (CUENTACORRIENTE, 'Cuenta Corriente'),
    )
    condicionpago = models.CharField(max_length=2, choices=CONDICIONES_DE_PAGO, default=EFECTIVO)
    
    cuit = models.IntegerField()
    ingresosbrutos = models.IntegerField()    
    numerodocumento = models.IntegerField()
    
     
    TIPO_DE_DOCS = (
        ('dni','DNI'),
        ('cdi','CDI'),
        ('lc','LC'),
        ('le','LE'),
        ('pasaporte','PASAPORTE'),
        ('cuit','CUIT'),
        ('cuil','CUIL'),
        ('ci','CI Extranjera'),
        ('en_tramite','En tramite'),
        ('acta_nacimiento','Acta nacimiento'),
        ('ci_ba_rpn','CI Bs. As. RNP'),
        ('no_id','Sin identificar venta gbl diaria'),
        ('certificado_migratorio','Certificado de Migracion'),
        ('padron_anses','Usado por Anses para Padron'),
    )
    tipodedocumento = models.CharField(max_length=22, choices=TIPO_DE_DOCS)
    enviarcomprobante = models.BooleanField(default=True)
    percibeiibb = models.BooleanField()
    percibeiiva = models.BooleanField()
    
    TRATAMIENTO_IMPOSITIVO = (
        ('monotributista','Monotributista'),
        ('responsable_inscripto','Responsable Inscripto'),
        ('consumidor_final','Consumidor Final'),
        ('iva_exento','IVA exento'),
    )
    tratamientoimpositivo = models.CharField(max_length=21, choices=TRATAMIENTO_IMPOSITIVO) 


    def get_absolute_url(self):
        return reverse('cliente_edit', kwargs={'pk': self.pk})  

    
    def __unicode__(self):
        return u'%s' % (self.Nombre)

