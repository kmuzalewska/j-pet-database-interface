from django.db import models


# Create your models here.
class Setup(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    version = models.PositiveIntegerField(blank=True, null=True)
    createDate = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return str(self.name)


class Run(models.Model):
    user = models.ForeignKey('auth.User')
    name = models.CharField(max_length=100)
    filePath = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    startTime = models.DateTimeField(blank=True, null=True)
    endTime = models.DateTimeField(blank=True, null=True)
    setup = models.ForeignKey(Setup)

    def __str__(self):
        return str(self.name)


class StatusType(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.name)


class Status(models.Model):
    dateTime = models.DateTimeField(blank=True, null=True)
    type = models.ForeignKey(StatusType)

    def __str__(self):
        return str(self.type.name)+' '+str(self.dateTime)


class Frame(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    status = models.ForeignKey(Status)

    def __str__(self):
        return str(self.name)


class Layer(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    status = models.ForeignKey(Status)
    radius = models.DecimalField(max_digits=7, decimal_places=2)
    frame = models.ForeignKey(Frame)

    def __str__(self):
        return str(self.name)


class Slot(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    status = models.ForeignKey(Status)
    theta = models.DecimalField(max_digits=7, decimal_places=2)
    inFrame = models.PositiveIntegerField(blank=True, null=True)
    layer = models.ForeignKey(Layer)
    zOffset = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return str(self.name)


class ScinType(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.name)


class Scin(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    type = models.ForeignKey(ScinType)
    length = models.DecimalField(max_digits=7, decimal_places=2)
    width = models.DecimalField(max_digits=7, decimal_places=2)
    height = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return str(self.name)


# class ScinCalibration(models.Model):
#     name = models.CharField(max_length=100)
#     attLength = models.DecimalField(max_digits=7, decimal_places=2)
#     scintillator = models.ForeignKey(Scin)
#     runs = models.ManyToManyField(Run)
#
#     def __str__(self):
#         return self.id+' '+self.name+' '+self.attLength


class ScinInserted(models.Model):
    status = models.ForeignKey(Status)
    slot = models.ForeignKey(Slot)
    setup = models.ForeignKey(Setup)
    scin = models.ForeignKey(Scin)

    def __str__(self):
        return str(self.slot)


class PMModel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.name)


class PM(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    producer = models.CharField(max_length=100, blank=True, null=True)
    purchaseDate = models.DateTimeField(blank=True, null=True)
    serialNumber = models.CharField(max_length=100, blank=True, null=True)
    maxHV = models.DecimalField(max_digits=7, decimal_places=2)
    takesPositiveVoltage = models.BooleanField()
    pmModel = models.ForeignKey(PMModel)

    def __str__(self):
        return str(self.name)


class HV(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    status = models.ForeignKey(Status)
    driverPluginInfo = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.name)


class HVChannel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    idX = models.CharField(max_length=100)
    minV = models.DecimalField(max_digits=7, decimal_places=2)
    maxV = models.DecimalField(max_digits=7, decimal_places=2)
    givesPositiveVoltage = models.BooleanField()
    hv = models.ForeignKey(HV)

    def __str__(self):
        return str(self.name)


class Side(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.name)


class PMInserted(models.Model):
    status = models.ForeignKey(Status)
    side = models.ForeignKey(Side)
    hvChannel = models.ForeignKey(HVChannel)
    pm = models.ForeignKey(PM)
    slot = models.ForeignKey(Slot)
    setup = models.ForeignKey(Setup)

    def __str__(self):
        return str(self.side)+' '+str(self.pm.name)+' '+str(self.slot.name)


# class PMCalibration(models.Model):
#     name = models.CharField(max_length=100)
#     photoMultiplier = models.ForeignKey(PhotoMultiplier)
#     optHV = models.DecimalField(max_digits=7, decimal_places=2)
#     c2e_1 = models.DecimalField(max_digits=7, decimal_places=2)
#     c2e_2 = models.DecimalField(max_digits=7, decimal_places=2)
#     gainAlpha = models.DecimalField(max_digits=7, decimal_places=2)
#     gainBeta = models.DecimalField(max_digits=7, decimal_places=2)
#
#     def __str__(self):
#         return self.id+' '+self.name
