from django.db import models

class Client(models.Model):
        name = models.TextField()
        mail = models.EmailField(null =True)
        dateRegistration = models.DateField(null =True)
        address = models.TextField(null =True)
        image = models.FilePathField(null =True)
        password = models.TextField(null =True)
        fladDelete = models.TextField(null = True)
class AdditionalService(models.Model):
    name = models.TextField()
    image = models.FilePathField(null =True)
    price = models.FloatField(null =True)
    description = models.TextField(null =True)
    durationAvg = models.FloatField(null = True)
    durationMin  = models.FloatField(null = True)
    fladDelete = models.TextField(null = True)
class Service(models.Model):
    AdditionalService = models.ManyToManyField(AdditionalService)
    description = models.TextField(null =True)
    image = models.FilePathField(null =True)
    name = models.TextField(null =True)
    fladDelete = models.TextField(null = True)
class Scenario(models.Model):
        name = models.TextField()
        image = models.FilePathField(null =True)
        price = models.FloatField(null =True)
        description = models.TextField(null =True)
        Service = models.ForeignKey(Service,on_delete = models.PROTECT)
        fladDelete = models.TextField(null = True)
class Tariff(models.Model):
        name = models.TextField()
        description = models.TextField(null =True)
        price = models.FloatField(null =True)
        Service = models.ForeignKey(Service,on_delete = models.PROTECT)
        fladDelete = models.TextField(null = True)
class Payment(models.Model):
        AdditionalService = models.ManyToManyField(AdditionalService)
        Client = models.ForeignKey(Client,on_delete = models.PROTECT)
        Service = models.ForeignKey(Service,on_delete = models.PROTECT)
        Tariff= models.ForeignKey(Tariff,on_delete = models.PROTECT)
        dateOfPay = models.DateField(null =True)
        sumOfPayment = models.FloatField(null =True)
        fladDelete = models.TextField(null = True)
class Chip(models.Model):
    name = models.TextField(null = True)
    image = models.FilePathField(null =True)
    desing = models.FilePathField(null =True)
    price = models.FloatField(null =True)
    description = models.TextField(null =True)
    number = models.IntegerField(null = True)
    Service = models.ForeignKey(Service,on_delete = models.PROTECT)
    fladDelete = models.TextField(null = True)
class Order(models.Model):
    Service = models.ForeignKey(Service,on_delete = models.PROTECT)
    Client = models.ForeignKey(Client,on_delete = models.PROTECT)
    dateEnd = models.DateField(null =True)
    dateLastUpdate = models.DateField(null =True)
    dateStart = models.DateField(null =True)
    price = models.FloatField(null =True)
    status = models.IntegerField(null = True)
    Payment = models.ManyToManyField(Payment)
    AdditionalService = models.ManyToManyField(AdditionalService)
    Chip = models.ManyToManyField(Chip)
    fladDelete = models.TextField(null = True)


class Worker(models.Model):
    name = models.TextField()
    gender = models.TextField(null =True)
    image  = models.FilePathField(null =True)
    dateBirth = models.DateField(null =True)
    dateRegistration = models.DateField(null =True)
    direction = models.TextField(null =True)
    mail = models.EmailField(null =True)
    password = models.TextField(null =True)
    AdditionalService = models.ManyToManyField(AdditionalService)
    fladDelete = models.TextField(null = True)
class OrderSchedule(models.Model):
    Order = models.ForeignKey(Order,on_delete = models.PROTECT)
    duration = models.FloatField(null =True)
    startTime = models.DateField(null =True)
    statusOrder = models.IntegerField(null =True)
    AdditionalService =  models.ForeignKey(AdditionalService,on_delete = models.PROTECT)
    price = models.FloatField(null =True)
    Worker =  models.ForeignKey(Worker,on_delete = models.PROTECT)
    fladDelete = models.TextField(null = True)
class Comment(models.Model):
    description = models.TextField(null =True)
    Client = models.ForeignKey(Client,on_delete = models.PROTECT)
    Order = models.ForeignKey(Order, on_delete = models.PROTECT)
    AdditionalService = models.ForeignKey(AdditionalService, on_delete = models.PROTECT)
    Worker = models.ForeignKey(Worker, on_delete = models.PROTECT)
    fladDelete = models.TextField(null = True)
class WorkerPrice(models.Model):
    AdditionalService =  models.ForeignKey(AdditionalService,on_delete = models.PROTECT)
    Worker = models.ForeignKey(Worker,on_delete = models.PROTECT)
    price = models.FloatField(null =True)
    durationMin  = models.FloatField(null = True)
    fladDelete = models.TextField(null = True)
class generalSchedule(models.Model):
    StartDateTime = models.DateTimeField()
    FinishDatetime = models.DateTimeField()
    Worker = models.ForeignKey(Worker,on_delete = models.PROTECT)
    AdditionalService = models.ForeignKey(AdditionalService,on_delete = models.PROTECT)
    fladDelete = models.TextField(null = True)