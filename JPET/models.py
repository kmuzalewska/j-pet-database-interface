from django.db import models


# Create your models here.
class Setup(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    version = models.PositiveIntegerField(blank=True, null=True, default=1)
    createDate = models.DateTimeField(blank=True, null=True)

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
    generalStatus = models.ForeignKey(StatusType)

    def __str__(self):
        return str(self.name)


class Layer(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    generalStatus = models.ForeignKey(StatusType)
    radius = models.DecimalField(max_digits=7, decimal_places=2)
    frame = models.ForeignKey(Frame)

    def __str__(self):
        return str(self.name)


class Slot(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    theta = models.DecimalField(max_digits=7, decimal_places=2)
    inFrameID = models.PositiveIntegerField(blank=True, null=True)
    generalStatus = models.ForeignKey(StatusType)
    layer = models.ForeignKey(Layer)
    parentSlot = models.ForeignKey('self', default=0)

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


class ScinInserted(models.Model):
    scin = models.ForeignKey(Scin)
    status = models.ForeignKey(Status)
    slot = models.ForeignKey(Slot)
    setup = models.ForeignKey(Setup)
    attLength = models.DecimalField(blank=True, null=True, max_digits=18, decimal_places=9)
    velocity = models.DecimalField(blank=True, null=True, max_digits=18, decimal_places=9)
    zOffset = models.DecimalField(max_digits=7, decimal_places=2, default=0.0)

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


class Run(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.name)


class MeasurementType(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.name)


class Measurement(models.Model):
    fileName = models.CharField(max_length=100)
    checksum = models.CharField(max_length=32)
    run = models.ForeignKey(Run)
    description = models.TextField(blank=True, null=True)
    user = models.ForeignKey('auth.User')
    startDateTime = models.DateTimeField(blank=True, null=True)
    endDateTime = models.DateTimeField(blank=True, null=True)
    type = models.ForeignKey(MeasurementType)
    setup = models.ForeignKey(Setup)

    def __str__(self):
        return str(self.fileName)


class RadiationSourceType(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.name)


class RadiationSource(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    type = models.ForeignKey(RadiationSourceType)
    generalStatus = models.ForeignKey(StatusType)

    def __str__(self):
        return str(self.name)


class RadiationSourceInserted(models.Model):
    source = models.ForeignKey(RadiationSource)
    status = models.ForeignKey(Status)
    measurement = models.ForeignKey(Measurement)
    colimated = models.BooleanField()
    positionX = models.DecimalField(blank=True, null=True, max_digits=7, decimal_places=2)
    positionY = models.DecimalField(blank=True, null=True, max_digits=7, decimal_places=2)
    positionZ = models.DecimalField(blank=True, null=True, max_digits=7, decimal_places=2)

    def __str__(self):
        return str(self.source.name)
