from rq import get_current_job
from time import sleep
from .models import *

import g4f



def long_running_task():
    #job = get_current_job()
    print(f"Task started")
    make_requests = StorageRequests.objects.filter(is_done=False)

    for item in make_requests:
        #content = make_template(QueryTemplate.objects.get(pk= NeuralStats.objects.get(pk=item.neural_config).query_template), Task.objects.get(pk=item.task), Solution.objects.get(pk=item.solution),Topic.objects.get(pk= NeuralStats.objects.get(pk=item.neural_config).topic))
        rate=item.rate
        model=rate.neural.neural_name
        solution = rate.solution
        task=solution.task
        system_text=task.topic.system_text


        content ="Дано задание"+"\n"+ task.formulation+"\n"+"Дано решение"+"\n"+solution. program_code
        print("--------")
        print(model)

        try:
            response = g4f.ChatCompletion.create(
                model=getattr(g4f.models, model),
                messages=[{"role": "system", "content": system_text}, {"role": "user",
                                                                               "content": content}],
                provider=g4f.Provider.GptForLove

            )
            item.neural_answer=response
            item.is_done=True
            item.save()
            print(response)
        except Exception as e:
            print(e)
            pass

