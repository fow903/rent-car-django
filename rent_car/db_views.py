from django.shortcuts import redirect
import logging

from django.db import connection

logger = logging.getLogger("django")

class DBViewRedirectedSave(object):

    def save(self):
        return redirect('/admin')





def exec_create_view(model):
    model_name = model._meta.db_table
    try:
        cursor = connection.cursor()
        cursor.execute(model.get_sql())
        # logger.info("Creada DB View %s...", model_name)
        return True
    except Exception as e:
        logger.info("Error al crear la vista {0} con sql ---> {1}".format(model_name, model.get_sql()))
        return False
