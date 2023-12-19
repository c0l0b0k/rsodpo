# from rq import get_current_job
# from time import sleep
# from .models import *
# from .util import *
# import g4f
#

#
#
# def long_running_task():
#     make_requests = StorageRequests.objects.filter(is_done=False)
#     for item in make_requests:
#
#         rate=item.rate
#         model=rate.neural.neural_name
#         solution = rate.solution
#         task=solution.task
#         system_text=task.topic.subsection.system_text
#
#
#         content ="Дано задание"+"\n"+ get_clean_text(task.formulation)+"\n"+"Дано решение"+"\n"+solution. program_code
#         try:
#             # Ваш код, который может вызвать исключение
#             model_ = getattr(g4f.models, model)
#         except  :
#             model_=model
#         try:
#             response = g4f.ChatCompletion.create(
#                 model=model_,
#                 messages=[{"role": "system", "content": system_text}, {"role": "user",
#                                                                                "content": content}],
#             )
#             item.neural_answer=response
#             item.is_done=True
#             item.save()
#         except Exception as e:
#             print(e)
#             pass
#
