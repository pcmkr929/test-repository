from django.db import models

"""
Link to the Field overwiew:
    https://docs.djangoproject.com/en/2.2/ref/models/fields/#field-types
Some Fields have requirements, but not all
"""

# Create your models here.

class MQTTConfig(models.Model):
    host               = models.CharField(max_length=100)
    port               = models.DecimalField(
                            max_digits=4, 
                            decimal_places=0,
                            )

    certs              = models.BooleanField(default=False)
    cid                = models.CharField(max_length=100)
    # ca/cert/key only if certs==True, else skip them
    ca                 = models.CharField(max_length=100)
    cert               = models.CharField(max_length=100)
    key                = models.CharField(max_length=100)

    tcp                = models.CharField(
                            max_length=100, 
                            default="tcp",
                            )
    name               = models.CharField(max_length=100)
    # "format":"{\"data\":[{\"key\":\"<varname>\",\"timestamp\":<timestamp>,\"value\":\"<value>\"}]}"
    format_mqtt        = models.CharField(
                            max_length=100,
                            default="{\"data\":[{\"key\":\"<varname>\",\"timestamp\":<timestamp>,\"value\":\"<value>\"}]}",
                            )
    storeOffline       = models.BooleanField(default=True)
    offlineLimit       = models.DecimalField(
                            max_digits=10, 
                            decimal_places=3,
                            )
    signedURL          = models.BooleanField(default=False)
    
    # "generalTopic": "rh/reccon/<name>/<special>"
    generalTopic       = models.CharField(max_length=100)
    
    # "alarmTopic": "data/custom/reclis/alarms",  
    alarmTopic         = models.CharField(max_length=100)
    dataTopic          = models.CharField(
                            max_length=100,
                            default="data",
                            )
    alivePing          = models.BooleanField(default=True)
    alivePingInterval  = models.DecimalField(
                            max_digits=4,
                            decimal_places=3,   # down to 1 milisec
                            )
    alivePingTopic     = models.CharField(
                            max_length=100,
                            default="ping",
                            )

class SQLConfig(models.Model):
    connection = models.CharField(max_length=100)
    name       = models.CharField(max_length=50)
    useTables  = models.BooleanField(default=True)
    tableName  = models.CharField(max_length=50)
    poolsize   = models.DecimalField(max_digits=2, decimal_places=0)
    # "type": "send"
    connection_type = models.CharField(max_length=50)

    #tables     = 
    # "tables": [
    #     {"name":"test1", "main":true},
    #     {"name":"test2", "main":false},
    #     {"name":"test3", "main":false}
    # ]


# It should be necessary to chose an instance type,
#   after choosing, the variables related to that specific type
#   pop up and must be filled. Unnecessary variables shouldnt 
#   be displayed (e.g. it shouldnt be possible to fill in 
#   replicator variables if ialarm is chosen.)

class InstanceConfig(models.Model):
    # Defining constants for the chosable values
    # OPC         = 'opc'
    # IALARM      = 'ialarm'
    # REPLICATOR  = 'replicator'

    # The first element in each tuple is the actual value to be set 
    # on the model, and the second element is the human-readable name.
    INSTANCE_CHOICES = (
        ('opc', 'OPC'),
        ('ialarm', 'iAlarm'),
        ('replicator', 'Replicator'),
    )

    instance_type = models.CharField(
                        max_length=10,
                        choices=INSTANCE_CHOICES,
                        default=None,
                        )
    
    # def is_instance(self):
    #     return self.instance_type in 

    # Variables for type OPC:
    name_opc            = models.CharField(max_length=50)
    mqtt_opc            = models.BooleanField(default=False)
    mCon_opc            = models.CharField(max_length=10)
    sCon_opc            = models.CharField(max_length=10)
    sql_opc             = models.BooleanField(default=False)
    host_opc            = models.CharField(max_length=50)
    path_opc            = models.CharField(max_length=100)
    logfile_opc         = models.CharField(max_length=50)
    interval_opc        = models.DecimalField(
                                    max_digits=4,
                                    decimal_places=3,
                                    default=1,
                                    )
    spsVar_opc          = models.CharField(max_length=50)
    checkconfig_opc     = models.BooleanField(default=True)
    reconnect_opc       = models.BooleanField(default=False)

    # Variables for type iAlarm:
    name_ialarm         = models.CharField(max_length=50)
    mqtt_ialarm         = models.BooleanField(default=False)
    mCon_ialarm         = models.CharField(max_length=10)
    sCon_ialarm         = models.CharField(max_length=10)
    database_ialarm     = models.CharField(max_length=50)
    tables_ialarm       = models.CharField(max_length=100)
    logfile_ialarm      = models.CharField(max_length=50)
    interval_ialarm     = models.DecimalField(
                                    max_digits=4,
                                    decimal_places=3,
                                    default=1,
                                    )
    reconnect_ialarm    = models.BooleanField(default=True)
    format_ialarm       = models.CharField(max_length=50)
    machine_name_ialarm = models.CharField(max_length=50)
    dataLimit_ialarm    = models.DecimalField(
                                    max_digits=5,
                                    decimal_places=0,
                                    default=100,
                                    )

    # Variables for type REPLICATOR:
    name_replicator             = models.CharField(max_length=50)                         
    mqtt_replicator             = models.BooleanField(default=False)
    mCon_replicator             = models.CharField(max_length=10)
    sCon_replicator             = models.CharField(max_length=10)
    sql_replicator              = models.BooleanField(default=False)
    database_replicator         = models.CharField(max_length=50)
    tables_replicator           = models.CharField(max_length=50)
    logfile_replicator          = models.CharField(max_length=50)
    interval_replicator         = models.DecimalField(
                                            max_digits=4,
                                            decimal_places=3,
                                            default=1,
                                            )
    reconnect_replicator        = models.BooleanField(default=True)
    savefile_replicator         = models.CharField(max_length=50)
    replicatorConfig_replicator = models.CharField(max_length=50)
    machine_name_replicator     = models.CharField(max_length=50)
    dataLimit_replicator        = models.DecimalField(
                                            max_digits=5,
                                            decimal_places=0,
                                            default=100,
                                            )












# class BasicConfig():



# class FileshareLogConfig():