# Create your tasks here
from __future__ import absolute_import, unicode_literals
from os import listdir
from os import path
import subprocess

from celery.utils.log import get_task_logger


from django.conf import settings
from celery import shared_task

from api.models import Test
ENV = settings.VIRTUAL_ENV_PATH

logger = get_task_logger(__name__)
@shared_task()
def run_script(test_id):
    cmd_list = []
    status = "P"
    test_output = ""
    instance = Test.objects.filter(id=test_id).first()
    if path.isdir(instance.get_script()):
        cmd_list = ["{}{}".format(instance.get_script(), f) for f in listdir(instance.get_script())
                    if path.isfile(path.join(instance.get_script(), f)) and f is not "__init__.py"]
    else:
        cmd_list.append(instance.get_script())

    for cmd in cmd_list:
        cmd = "pytest {}".format(cmd)
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True,
                               env={'PATH': ENV})
        out, err = process.communicate()
        out_str = "".join(map(chr, out))

        if "failed" in out_str or err:
            status = "F"
        test_output = test_output + out_str

    instance.status = status
    instance.log_information = test_output
    instance.save()
