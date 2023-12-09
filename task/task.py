from rq import get_current_job
from time import sleep
from .models import *
from .util import *
import g4f



def long_running_task():
    #job = get_current_job()
    print(f"Task started")
    make_requests = StorageRequests.objects.filter(is_done=False)

    for item in make_requests:

        rate=item.rate
        model=rate.neural.neural_name
        solution = rate.solution
        task=solution.task
        system_text=task.topic.system_text


        content ="Дано задание"+"\n"+ get_clean_text(task.formulation)+"\n"+"Дано решение"+"\n"+solution. program_code
        print("--------")
        print(model)
        try:
            # Ваш код, который может вызвать исключение
            model_ = getattr(g4f.models, model)
        except  :
            pass
        try:
            response = g4f.ChatCompletion.create(
                model=getattr(g4f.models, model),
                messages=[{"role": "system", "content": system_text}, {"role": "user",
                                                                               "content": content}],
            )
            item.neural_answer=response
            item.is_done=True
            item.save()
            print(response)
        except Exception as e:
            print(e)
            pass

