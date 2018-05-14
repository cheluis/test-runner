# Create your tasks here
from __future__ import absolute_import, unicode_literals
import subprocess

from celery.utils.log import get_task_logger


from django.conf import settings
from celery import shared_task

from api.models import Test
ENV = settings.VIRTUAL_ENV_PATH

logger = get_task_logger(__name__)
@shared_task()
def run_script(test_id):
    logger.info("En la tarea")
    instance = Test.objects.filter(id=test_id).first()
    cmd = "pytest {}".format(instance.get_script())
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True,
                               env={'PATH': ENV})
    out, err = process.communicate()
    out_str = "".join(map(chr, out))
    if "failed" in out_str or err:
        instance.status = "F"
    else:
        instance.status = "P"

    logger.info("En la tarea: {}".format(out_str))
    instance.log_information = out_str
    instance.save()
