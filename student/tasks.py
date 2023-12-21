import time

from task.models import *
from task.util import *
import g4f
from celery import shared_task

@shared_task
def send_student_code(storage_id):
    request = StorageRequests.objects.get(storage_id=storage_id)
    while True:
        rate=request.rate
        model= rate.neural.neural_name
        solution = rate.solution
        task=solution.task
        system_text=task.topic.subsection.system_text


        content ="Дано задание"+"\n"+ get_clean_text(task.formulation)+"\n"+"Дано решение"+"\n"+solution. program_code
        try:
            # Ваш код, который может вызвать исключение
            model_ = getattr(g4f.models, model)
        except  :
            model_=model
        try:
            response = g4f.ChatCompletion.create(
                model=model_,
                messages=[{"role": "system", "content": system_text}, {"role": "user",
                                                                               "content": content}],
            )
            request.neural_answer=response
            request.is_done=True
            request.save()
            request.rate.solution.mark=-3
            request.rate.solution.save()

            break
        except Exception as e:
            time.sleep(10)
            return storage_id

