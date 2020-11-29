from django.db import models
import datetime
import qrcode
from io import BytesIO
from PIL import Image,ImageDraw
from django.core.files import File
from picklefield.fields import PickledObjectField
from django import forms
from django.contrib.auth.models import User

# Create your models here.
class Computadora(models.Model):
    no_Serie_Co= models.CharField(primary_key=True,max_length=30,verbose_name="No. de serie")
    nombre_Co= models.CharField(max_length=30,verbose_name="Nombre")
    marca=models.CharField(max_length=10)
    modelo_com=models.CharField(max_length=30)
    tipo_Choice=(
        ('pce','pcescritorio'),
        ('lap','lap'),
    )
    tipo_com=models.CharField(max_length=3,choices=tipo_Choice)
    Status_Choice=(
        ("disponible","disponible"),
        ("servicio","servicio"),
        ("reparacion","reparación"),
        ("destruccion","destruccion"),
    )
    Status=models.CharField(max_length=15,choices=Status_Choice)
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
    def __str__(self):
        return self.no_Serie_Co
    def save(self, *args, **kwargs):
        qrcode_img = qrcode.make(self.nombre_Co)
        canvas = Image.new('RGB', (290, 290), 'white')
        draw= ImageDraw.Draw(canvas)
        canvas.paste(qrcode_img)
        fnombre_Co = f'qr_code-{self.nombre_Co}.png'
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
    piso=models.IntegerField(max_length=1)
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


























    






