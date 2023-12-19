from task.models import *
from task.util import *
import g4f
from django_rq import enqueue, job
import time, schedule




def sent_neuro_task(storage_id):
    print(f"Task started{storage_id}")
    request = StorageRequests.objects.get(pk=storage_id)

    rate=request.rate
    model= "gpt-3.5-turbo-16k"        #rate.neural.neural_name
    solution = rate.solution
    task=solution.task
    system_text=task.topic.system_text
    content ="Дано задание"+"\n"+ get_clean_text(task.formulation)+"\n"+"Дано решение"+"\n"+solution. program_code
    # print(content)
    # print("--------")

    try:
        # Ваш код, который может вызвать исключение
        model_ = getattr(g4f.models, model)
    except  :
        model_=model
    while True:
        try:
            response = g4f.ChatCompletion.create(
                model=model_,
                messages=[{"role": "system", "content": system_text}, {"role": "user",
                                                                               "content": content}],
            )
            request.neural_answer=response
            request.is_done=True
            request.save()
            print(response)
        except Exception as e:
            print("00000000000000")
            print(storage_id)
            print(e)
            print("00000000000000")
            time.sleep(5)
            pass