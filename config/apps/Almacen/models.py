from django.db import models
import datetime
import qrcode
from io import BytesIO
from PIL import Image,ImageDraw
from django.core.files import File
from picklefield.fields import PickledObjectField
from django import forms
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
#from multiselectfield import MultiSelectField
import os
from field_history.tracker import FieldHistoryTracker
from twilio.rest import Client






# Create your models here.


class Computadora(models.Model):
    no_Serie_Co= models.CharField(primary_key=True,max_length=30,verbose_name="No. de serie")
    nombre_Co= models.CharField(max_length=30,verbose_name="Nombre")
    marca=models.CharField(max_length=10)
    modelo_com=models.CharField(max_length=30,verbose_name="Modelo")
    tipo_Choices=(
        (1, 'pcescritorio'),
        (2, 'laptop'),
    )
    tipo_com = models.IntegerField(choices=tipo_Choices, default=1)
    Status_Choice=(
        ("disponible","disponible"),
        ("servicio","servicio"),
        ("reparacion","reparación"),
        ("destruccion","destruccion"),
    )
    Status=models.CharField(max_length=30,choices=Status_Choice)
    Ram_Choice=(
        ('2GB','2GB'),
        ('4GB','4GB'),
        ('8GB', '8GB'),
        ('16GB', '16GB'),
    )
    Ram = models.CharField(max_length=5, choices=Ram_Choice, null=True)
    Dd_Choice=(
        ('500Gb','500Gb'),
        ('1TB', '1TB'),
        ('1.5TB', '1.5TB'),
        ('2TB', '2TB'),
        ('2.5TB', '2.5TB'),
        ('3TB', '3TB'),
    )
    Disco_Duro = models.CharField(max_length=6, choices=Dd_Choice, verbose_name='Disco Duro',null=True)
    Procesador= models.CharField(max_length=20,null=True)
    Ano=models.IntegerField(verbose_name="Año",null=True)      
    qr_code= models.ImageField(upload_to='qr_codes',blank=True, null=True)
    field_history = FieldHistoryTracker(['Status'])
    
    def __str__(self):
        return self.no_Serie_Co
    def __unicode__(self):
        return self.nombre_Co

    
    def save(self, *args, **kwargs):
        dicttionary = {"Num.Serie": self.no_Serie_Co, "Nombre": self.nombre_Co, "Marca":self.marca,"Modelo":self.modelo_com,"Disco Duro":self.Disco_Duro,"Procesador":self.Procesador,"Ram":self.Ram}
        qrcode_img = qrcode.make(dicttionary)
        canvas = Image.new('RGB', (590, 590), 'white')
        draw= ImageDraw.Draw(canvas)
        canvas.paste(qrcode_img)
        fnombre_Co = f'qr_code-{dicttionary}.png'
        buffer= BytesIO()
        canvas.save(buffer,'PNG')
        self.qr_code.save(fnombre_Co, File(buffer), save=False)
        canvas.close()
        super(Computadora, self ).save(*args,**kwargs)
        


class Area(models.Model):
    Nombre_Area_Choice=(
        ("JUR","juridico"), 
        ("RH","RecursosHumanos"),
        ("CEC","CEC"),
        ("Pro","Proyectos"),
        ("INC","Ingeniería de costos"),
        ("DIR","Direccion"),
        ("SIS","Sistemas"),
        ("SAP","SAP"),
        ("Adm","Administracion"),
        ("Aud","Auditoria"),
        ("Com","Compras"),
        ("Cns","Concesiones"),
        ("Con","Contabilidad"),
        ("Cnt","Contraloria"),
        ("Fis","Fiscal"),
        ("Ctr","Control"),
        ("MCo","Manejo de contrato"),
        ("PVV","Provivan"),
        ("SUB","Subcontratos"),
    )
    nombre_Area=models.CharField(primary_key=True,max_length=30,choices=Nombre_Area_Choice)
    piso=models.IntegerField()
    def __str__(self):
        return self.nombre_Area

    
class Teclado(models.Model):
    computadora = models.OneToOneField(Computadora, null=True, on_delete=models.SET_NULL)
    no_Serie_Te = models.CharField(primary_key=True, max_length=30)
    nombre_Te = models.CharField(max_length=30)
    marca = models.CharField(max_length=10)
    tipo_entrada_Choice=(
        ('usb', 'usb'),
        ('PS/2', 'PS/2'),
    )
    tipo_entrada = models.CharField(max_length=4, choices=tipo_entrada_Choice)
    qr_code = models.ImageField(upload_to='qr_codes', blank=True)
    
    def __str__(self):
        return self.no_Serie_Te

    def save(self, *args, **kwargs):
        qrcode_img = qrcode.make(self.no_Serie_Te)
        canvas = Image.new('RGB', (290, 290), 'white')
        draw = ImageDraw.Draw(canvas)
        canvas.paste(qrcode_img)
        fno_Serie_Te = f'qr_code-{self.no_Serie_Te}.png'
        buffer = BytesIO()
        canvas.save(buffer, 'PNG')
        self.qr_code.save(fno_Serie_Te, File(buffer), save=False)
        canvas.close()
        super().save(*args,**kwargs)


class Mouse(models.Model):
    computadora = models.OneToOneField(Computadora, null=True, on_delete=models.SET_NULL)
    no_Serie_Mo = models.CharField(primary_key=True, max_length=30)
    nombre_Mo = models.CharField(max_length=30)
    marca = models.CharField(max_length=10)
    tipo_entrada_Choice=(
        ('usb', 'usb'),
        ('PS/2', 'PS/2'),
    )
    tipo_entrada = models.CharField(max_length=4, choices=tipo_entrada_Choice)
    qr_code = models.ImageField(upload_to='qr_codes', blank=True)
    

    def __str__(self):
        return self.no_Serie_Mo

    def save(self, *args, **kwargs):
        qrcode_img = qrcode.make(self.no_Serie_Mo)
        canvas = Image.new('RGB', (290, 290), 'white')
        draw = ImageDraw.Draw(canvas)
        canvas.paste(qrcode_img)
        fno_Serie_Mo = f'qr_code-{self.no_Serie_Mo}.png'
        buffer = BytesIO()
        canvas.save(buffer, 'PNG')
        self.qr_code.save(fno_Serie_Mo, File(buffer), save=False)
        canvas.close()
        super().save(*args,**kwargs)
        verbose_name='Mouse'
        verbose_name_plural = 'Mouse'

   
class Monitor(models.Model):
    computadora = models.OneToOneField(Computadora, null=True, on_delete=models.SET_NULL)
    no_Serie_Pa = models.CharField(primary_key=True, max_length=30)
    nombre_Pa = models.CharField(max_length=30)
    marca = models.CharField(max_length=10)
    qr_code = models.ImageField(upload_to='qr_codes', blank=True)
    
    def __str__(self):
        return self.no_Serie_Pa
    def save(self, *args, **kwargs):
        qrcode_img = qrcode.make(self.no_Serie_Pa)
        canvas = Image.new('RGB', (290, 290), 'white')
        draw = ImageDraw.Draw(canvas)
        canvas.paste(qrcode_img)
        fno_Serie_Pa = f'qr_code-{self.no_Serie_Pa}.png'
        buffer = BytesIO()
        canvas.save(buffer, 'PNG')
        self.qr_code.save(fno_Serie_Pa, File(buffer), save=False)
        canvas.close()
        super().save(*args,**kwargs)

    class Meta:
        verbose_name = 'Monitor'
        verbose_name_plural = 'Monitores'

class Empleado(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True,verbose_name="Usuario")
    Area = models.ForeignKey(Area, on_delete=models.CASCADE)
    Id_Empleado=models.CharField(primary_key=True,max_length=8,verbose_name="Id")
    nombre_Emp=models.CharField(max_length=30,verbose_name="Nombre",null=True)
    ApellidoP_Emp = models.CharField(max_length=30, verbose_name="Apellido Paterno",null=True)
    ApellidoM_Emp = models.CharField(max_length=30,verbose_name="Apellido Materno",null=True)
    puesto=models.CharField(max_length=30)
    Office_Choice=(
        ("O365","Office365"),
        ("Win7","Windows7"),
    )
    Office=models.CharField(max_length=4,choices=Office_Choice)
    correo_Emp = models.EmailField(verbose_name="E-mail",null=True)
    telefono = models.BigIntegerField()
    ext=models.IntegerField(verbose_name="Extensión")
    #password = forms.CharField(max_length=32, widget=forms.PasswordInput)

    def __unicode__(self):
        return self.nombre_Emp
    def __str__(self):
        return self.Id_Empleado
class Proyecto(models.Model):
    Id_proyecto =models.CharField(primary_key=True,max_length=5,verbose_name="Id")
    nombre_proyecto=models.CharField(max_length=50)
    direccion=models.CharField(max_length=200)
    telefono=models.IntegerField()
    def __str__(self):
        return self.nombre_proyecto
class Proyecto_empleado(models.Model):
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    Proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
    fecha_ingreso = models.DateTimeField()
    fecha_egreso = models.DateTimeField(null=True, blank=True)
    def __str__(self):
        return str(self.Proyecto)

    class Meta:
        verbose_name = 'Empledos por proyecto'
        verbose_name_plural = 'Empledos por proyecto'

    
    
class Prestamo_Computadora(models.Model):
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    computadora = models.ForeignKey(Computadora, on_delete=models.CASCADE)
    fecha_inicio = models.DateField(default=datetime.date.today)
    fecha_fin = models.DateField(null=True, blank=True)

    class Meta:
        verbose_name = 'Prestamos de computadoras'
        verbose_name_plural = 'Prestamos de computadoras'


class Impresora(models.Model):
    no_Serie_Im = models.CharField(primary_key=True, max_length=30, verbose_name="No. de Serie")
    nombre_Im = models.CharField(max_length=30, verbose_name="Nombre")
    marca = models.CharField(max_length=10)
    modelo_Im = models.CharField(max_length=30, verbose_name="Modelo")
    qr_code = models.ImageField(upload_to='qr_codes', blank=True)
    Status_Choice = (
        ("disponible", "disponible"),
        ("servicio", "servicio"),
        ("reparacion", "reparación"),
        ("destruccion", "destruccion"),
    )
    Status = models.CharField(max_length=15, choices=Status_Choice)
    field_history = FieldHistoryTracker(['Status'])

    def __str__(self):
        return self.no_Serie_Im

    def save(self, *args, **kwargs):
        qrcode_img = qrcode.make(self.no_Serie_Im)
        canvas = Image.new('RGB', (290, 290), 'white')
        draw = ImageDraw.Draw(canvas)
        canvas.paste(qrcode_img)
        fno_Serie_Im = f'qr_code-{self.no_Serie_Im}.png'
        buffer = BytesIO()
        canvas.save(buffer, 'PNG')
        self.qr_code.save(fno_Serie_Im, File(buffer), save=False)
        canvas.close()
        super().save(*args,**kwargs)
    


class Celular(models.Model):
    no_Serie_Cel = models.CharField(primary_key=True, max_length=30, verbose_name="No. de Serie")
    nombre_Cel = models.CharField(max_length=30, verbose_name="Nombre")
    marca = models.CharField(max_length=10)
    modelo_Cel = models.CharField(max_length=30, verbose_name="Modelo")
    Status_Choice = (
        ("disponible", "disponible"),
        ("servicio", "servicio"),
        ("reparacion", "reparación"),
        ("destruccion", "destruccion"),
    )
    Status = models.CharField(max_length=15, choices=Status_Choice)
    field_history = FieldHistoryTracker(['Status'])
    qr_code = models.ImageField(upload_to='qr_codes', blank=True)

    def __str__(self):
        return self.no_Serie_Cel

    def save(self, *args,**kwargs):
        qrcode_img = qrcode.make(self.no_Serie_Cel)
        canvas = Image.new('RGB', (290, 290), 'white')
        draw = ImageDraw.Draw(canvas)
        canvas.paste(qrcode_img)
        fno_Serie_Cel = f'qr_code-{self.no_Serie_Cel}.png'
        buffer = BytesIO()
        canvas.save(buffer, 'PNG')
        self.qr_code.save(fno_Serie_Cel, File(buffer), save=False)
        canvas.close()
        super().save(*args,**kwargs)

    class Meta:
        verbose_name = 'Celular'
        verbose_name_plural = 'Celulares'


class Radio(models.Model):
    no_Serie_Rad = models.CharField(primary_key=True, max_length=30, verbose_name="No. de Serie")
    nombre_Rad = models.CharField(max_length=30, verbose_name="Nombre")
    marca = models.CharField(max_length=10)
    modelo_Cel = models.CharField(max_length=30, verbose_name="Nombre")
    Status_Choice = (
        ("disponible", "disponible"),
        ("servicio", "servicio"),
        ("reparacion", "reparación"),
        ("destruccion", "destruccion"),
    )
    Status = models.CharField(max_length=15, choices=Status_Choice)
    field_history = FieldHistoryTracker(['Status'])
    qr_code = models.ImageField(upload_to='qr_codes', blank=True)

    def __str__(self):
        return self.no_Serie_Rad

    def save(self, *args, **kwargs):
        qrcode_img = qrcode.make(self.no_Serie_Rad)
        canvas = Image.new('RGB', (290, 290), 'white')
        draw = ImageDraw.Draw(canvas)
        canvas.paste(qrcode_img)
        fno_Serie_Rad = f'qr_code-{self.no_Serie_Rad}.png'
        buffer = BytesIO()
        canvas.save(buffer, 'PNG')
        self.qr_code.save(fno_Serie_Rad, File(buffer), save=False)
        canvas.close()
        super().save(*args,**kwargs)


class Prestamo_Impresoras(models.Model):
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    Impresora = models.ForeignKey(Impresora, on_delete=models.CASCADE)
    fecha_inicio = models.DateField(default=datetime.date.today)
    fecha_fin = models.DateField(null=True, blank=True)

    class Meta:
        verbose_name = 'Prestamos de Impresoras'
        verbose_name_plural = 'Prestamos de Impresoras'


class Prestamo_Celular(models.Model):
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    celular = models.ForeignKey(Celular, on_delete=models.CASCADE)
    fecha_inicio = models.DateField(default=datetime.date.today)
    fecha_fin = models.DateField(null=True, blank=True)

    class Meta:
        verbose_name = 'Prestamos de Celulares'
        verbose_name_plural = 'Prestamos de Celulares'


class Prestamo_Radio(models.Model):
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    Radio = models.ForeignKey(Radio, on_delete=models.CASCADE)
    fecha_inicio = models.DateTimeField(default=datetime.date.today)
    fecha_fin = models.DateField(null=True, blank=True)

    class Meta:
        verbose_name = 'Prestamos de Radios'
        verbose_name_plural = 'Prestamos de Radios'


class Multifuncional(models.Model):
    no_Serie_Mul = models.CharField(primary_key=True, max_length=30, verbose_name="No. de Serie")
    nombre_Mul = models.CharField(max_length=30, verbose_name="Nombre")
    marca = models.CharField(max_length=10)
    modelo_Mul = models.CharField(max_length=30, verbose_name="Modelo")
    field_history = FieldHistoryTracker(['Status'])
    Status_Choice = (
        ("disponible", "disponible"),
        ("servicio", "servicio"),
        ("reparacion", "reparación"),
        ("destruccion", "destruccion"),
    )
    Status = models.CharField(max_length=15, choices=Status_Choice)
    qr_code = models.ImageField(upload_to='qr_codes', blank=True)

    def __str__(self):
        return self.no_Serie_Mul

    def save(self, *args, **kwargs):
        qrcode_img = qrcode.make(self.no_Serie_Mul)
        canvas = Image.new('RGB', (290, 290), 'white')
        draw = ImageDraw.Draw(canvas)
        canvas.paste(qrcode_img)
        fno_Serie_Mul = f'qr_code-{self.no_Serie_Mul}.png'
        buffer = BytesIO()
        canvas.save(buffer, 'PNG')
        self.qr_code.save(fno_Serie_Mul, File(buffer), save=False)
        canvas.close()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Multifuncional'
        verbose_name_plural = 'Multifuncionales'


class Proyector(models.Model):
    no_Serie_Pro = models.CharField(primary_key=True, max_length=30, verbose_name="No. de Serie")
    nombre_Pro = models.CharField(max_length=30, verbose_name="Nombre")
    marca = models.CharField(max_length=10)
    modelo_Pro = models.CharField(max_length=30, verbose_name="Modelo")
    field_history = FieldHistoryTracker(['Status'])
    Status_Choice = (
        ("disponible", "disponible"),
        ("servicio", "servicio"),
        ("reparacion", "reparación"),
        ("destruccion", "destruccion"),
    )
    Status = models.CharField(max_length=15, choices=Status_Choice)
    qr_code = models.ImageField(upload_to='qr_codes', blank=True)

    def __str__(self):
        return self.no_Serie_Pro

    def save(self, *args, **kwargs):
        qrcode_img = qrcode.make(self.no_Serie_Pro)
        canvas = Image.new('RGB', (290, 290), 'white')
        draw = ImageDraw.Draw(canvas)
        canvas.paste(qrcode_img)
        fno_Serie_Pro = f'qr_code-{self.no_Serie_Pro}.png'
        buffer = BytesIO()
        canvas.save(buffer, 'PNG')
        self.qr_code.save(fno_Serie_Pro, File(buffer), save=False)
        canvas.close()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Proyector'
        verbose_name_plural = 'Proyectores'

class Eq_Vid(models.Model):
    no_Serie_Vid = models.CharField(primary_key=True, max_length=30,verbose_name="No. de Serie")
    nombre_Vid = models.CharField(max_length=30,verbose_name="Nombre")
    marca = models.CharField(max_length=10)
    modelo_Vid = models.CharField(max_length=30,verbose_name="Modelo")
    field_history = FieldHistoryTracker(['Status'])
    Status_Choice = (
        ("disponible", "disponible"),
        ("servicio", "servicio"),
        ("reparacion", "reparación"),
        ("destruccion", "destruccion"),
    )
    Status = models.CharField(max_length=15, choices=Status_Choice)
    qr_code = models.ImageField(upload_to='qr_codes', blank=True)

    def __str__(self):
        return self.no_Serie_Vid

    def save(self, *args, **kwargs):
        qrcode_img = qrcode.make(self.no_Serie_Vid)
        canvas = Image.new('RGB', (290, 290), 'white')
        draw = ImageDraw.Draw(canvas)
        canvas.paste(qrcode_img)
        fno_Serie_Vid = f'qr_code-{self.no_Serie_Vid}.png'
        buffer = BytesIO()
        canvas.save(buffer, 'PNG')
        self.qr_code.save(fno_Serie_Vid, File(buffer), save=False)
        canvas.close()
        super().save(*args,**kwargs)

    class Meta:
        verbose_name = 'Equipo de video'
        verbose_name_plural = 'Equipo de video'


class Prestamo_Eq_Pub(models.Model):
    Proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
    Eq_Video = models.ForeignKey(Eq_Vid, null=True, blank=True, on_delete=models.CASCADE, verbose_name="Equipo de video")
    Responsable=models.OneToOneField(Empleado,on_delete=models.CASCADE)
    Proyector = models.ForeignKey(Proyector, null=True, blank=True, on_delete=models.CASCADE)
    Multifuncional = models.ForeignKey(Multifuncional, null=True, blank=True, on_delete=models.CASCADE)
    fecha_inicio = models.DateField(default=datetime.date.today)
    fecha_fin = models.DateField(null=True, blank=True)

    class Meta:
        verbose_name = 'Prestamos de Equipo de video'
        verbose_name_plural = 'Prestamos de Equipo de video'


class Solicitud_Equipo(models.Model):
    nombre_Emp = models.CharField(
        max_length=30, verbose_name="Nombre")
    ApellidoP_Emp = models.CharField(
        max_length=30, verbose_name="Apellido Paterno")
    ApellidoM_Emp = models.CharField(
        max_length=30, verbose_name="Apellido Materno")
    Area = models.ForeignKey(Area, on_delete=models.CASCADE)
    Proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
    tipo_Choice = (
        ('pce', 'pcescritorio'),
        ('lap', 'lap'),
    )
    tipo_com = models.CharField(max_length=3, choices=tipo_Choice,verbose_name="Tipo de computadora")
    Office_Choice = (
        ("O365", "Office365"),
        ("Win7", "Windows7"),
    )
    Office = models.CharField(max_length=4, choices=Office_Choice)
    App_Choices=(
        ('ERP','SAP 7.4'),
        ('Costos','Costos unitarios'),
        ('Autocad','Autocad 2018'),
        ('Adobe reader','Adobe'),
        ('VPN','Cliente VPN'),
        ('DoPDF','DoPDF'),
        ('7-zip','7-zip'),
        ('Control','Software de control Proyecto'),
        ('Diagramación','Software de diagramación'),
    )
    teclado_Choices=(
        ('aplica','aplica'),
        ('no aplica','no aplica'),
    )
    teclado=models.CharField(max_length=15,choices=teclado_Choices)
    monitor_Choices = (
        ('aplica', 'aplica'),
        ('no aplica', 'no aplica'),
    )
    monitor = models.CharField(max_length=15, choices=monitor_Choices)
    Aplicaciones = models.CharField(max_length=100,blank=True,null=True)
    Equipo_Adicional_choices=(
        ('IP', 'Telefonia IP'),
        ('Movil','Celular'),
        ('Radio', 'Radio'),
        ('N/A','No aplica'),
        )
    #Equipo_Adicional = SelectMultipleField(max_length=20,choices=Equipo_Adicional_choices)
    Status_choice=(
        ('Solicitado','Solicitado'),
        ('En proceso','En proceso'),
        ('Atendida','Atendida'),
    )
    Status= models.CharField(max_length=15,choices=Status_choice)
    Fecha_inicio=models.DateField(default=datetime.date.today,verbose_name='Fecha de entrega de equipo')
    field_history = FieldHistoryTracker(['Status'])

    class Meta:
        verbose_name = 'Solicitud de Equipo'
        verbose_name_plural = 'Solicitud de Equipo'
    def save(self, *args, **kwargs):
        if self.Aplicaciones:
            self.Aplicaciones= eval(self.Aplicaciones)
        if self.Status=='Solicitado':
            account_sid = os.environ.get('AC6882f5c66eedb6b8a6e733b24df48618')
            auth_token = os.environ.get('70a0acdeae855e8f4843b735c8a48de2')
            client = Client('AC6882f5c66eedb6b8a6e733b24df48618',
                            '70a0acdeae855e8f4843b735c8a48de2')
            message = client.messages.create(
                body='Se ha enviado una solicitud de computadoras',
                from_='+12059648210',
                to='+525511546778',
            )
            print(message.sid)
        return super().save(*args, **kwargs)

class Clave_Impresion(models.Model):
    clave=models.PositiveIntegerField(primary_key=True)
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.clave)
    class Meta:
        verbose_name="Clave de impresión"
        verbose_name_plural="Claves de impresión"
        
        
    


class Peticion_Impresiones_Color(models.Model):
    nombre_Emp = models.CharField(
        max_length=30, verbose_name="Nombre")
    ApellidoP_Emp = models.CharField(
        max_length=30, verbose_name="Apellido Paterno")
    ApellidoM_Emp = models.CharField(
        max_length=30, verbose_name="Apellido Materno")
    Clave=models.ManyToManyField(Clave_Impresion)
    saldo=models.PositiveIntegerField()
    Fecha = models.DateField(
        default=datetime.date.today, verbose_name='Fecha')
    Status_choice=(
        ('Solicitado','Solicitado'),
        ('En proceso','En proceso'),
        ('Atendida','Atendida'),
    )
    Status = models.CharField(
        max_length=15, choices=Status_choice, default='Solicitado')
    field_history = FieldHistoryTracker(['Status'])

    class Meta:
        verbose_name = "Petición de impresiones"
        verbose_name_plural = "Peticiones de impresiones"


    def save(self, *args, **kwargs):
        if self.Status == 'Solicitado':
            account_sid = os.environ.get('AC6882f5c66eedb6b8a6e733b24df48618')
            auth_token = os.environ.get('70a0acdeae855e8f4843b735c8a48de2')
            client = Client('AC6882f5c66eedb6b8a6e733b24df48618',
                            '70a0acdeae855e8f4843b735c8a48de2')
            message = client.messages.create(
                body='Se ha enviado una solicitud de computadoras',
                from_='+12059648210',
                to='+525511546778',
            )
            print(message.sid)
        return super().save(*args, **kwargs)

class Ordenes_Servicio(models.Model):
    nombre_Emp = models.CharField(
        max_length=30, verbose_name="Nombre")
    ApellidoP_Emp = models.CharField(
        max_length=30, verbose_name="Apellido Paterno")
    ApellidoM_Emp = models.CharField(
        max_length=30, verbose_name="Apellido Materno")
    Proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
    Area = models.ForeignKey(Area, on_delete=models.CASCADE)
    Atencion=models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True,verbose_name="Ingeniero Responsable")
    clasificacion_equipo_revisar_choices=(
        ("CPU","CPU"),
        ("LAPTOP","LAPTOP"),
        ("TelefoniaIP","TelefoníaIP"),
        ("Celuslar","Celular"),
        )
    clasificacion_equipo=models.CharField(choices=clasificacion_equipo_revisar_choices,null=True,blank=True,max_length=15,verbose_name="Equipo",)
    tipo_atencion_choices=(
        ("Telefónica","Telefónica"),
        ("Remota","Remota"),
        ("Presencial","Presencial"),
             

    )
    tipo_atencion = models.CharField(
        choices=tipo_atencion_choices, null=True, blank=True, max_length=15, verbose_name="Tipo de atención")
    cuestionario_choices=(
        ("si","si"),
        ("no","no"),
        ("no aplica","no aplica")
    )
    dano_fisico = models.CharField(choices=cuestionario_choices, max_length=10, null=True, blank=True,
                                   help_text="El equipo presenta daño por uso o descuido", verbose_name="Daño físico")
    retirar=models.CharField(choices=cuestionario_choices,max_length=10,null=True, blank=True,help_text="¿Se retiró el equipo?",verbose_name="Retirar equipo")
    codigo_error=models.CharField(choices=cuestionario_choices,max_length=10,null=True, blank=True,help_text="¿Presenta código de error?")
    solucion = models.CharField(choices=cuestionario_choices, max_length=10,
                                help_text="¿Se soluciono la incidencia?", verbose_name="Solucion")
    fecha_inicidencia=models.DateTimeField(auto_now_add=True)
    fecha_resolucion = models.DateField(null=True, blank=True,)
    reporte_usuario = models.TextField(
        blank=True, null=True, help_text="Indique detalladamente su problema", verbose_name="Descripción de la incidencia")
    reporte_resolucion = models.TextField(
        blank=True,null=True, help_text="Indique detalladamente la resolución del problema", verbose_name="Descripción de la solución")
    observaciones=models.TextField(verbose_name="Obsevaciones",null=True,blank=True)
    Status_choice = (
        ('Solicitado', 'Solicitado'),
        ('En proceso', 'En proceso'),
        ('Atendida', 'Atendida'),
    )
    Status = models.CharField(
        max_length=15, choices=Status_choice, default='Solicitado',null=True,blank=True)
    field_history = FieldHistoryTracker(['Status'])

    class Meta:
        verbose_name = "Orden de servicio"
        verbose_name_plural = "Ordenes de servicio"

    def save(self, *args, **kwargs):
        if self.Status == 'Solicitado':
            account_sid = os.environ.get('AC6882f5c66eedb6b8a6e733b24df48618')
            auth_token = os.environ.get('70a0acdeae855e8f4843b735c8a48de2')
            client = Client('AC6882f5c66eedb6b8a6e733b24df48618',
                            '70a0acdeae855e8f4843b735c8a48de2')
            message = client.messages.create(
                body='Se ha enviado una orden de servicio',
                from_='+12059648210',
                to='+525511546778',
            )
            print(message.sid)
        return super().save(*args, **kwargs)
    
class Contacto_directo(models.Model):
    nombre=models.ForeignKey(User,on_delete=models.CASCADE)
    numero_celular=PhoneNumberField(verbose_name="Número de celular")
    
    def __str__(self):
        return str(self.numero_celular)
    class Meta:
        verbose_name="Contactos de soporte técnico"
        verbose_name_plural="Contactos de soporte técnico"
    #get_absolute_url

    

    


































    






