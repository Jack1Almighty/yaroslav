from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Tasks
from django.views.generic import DetailView


def tasks(request):
    view_tasks = Tasks.objects.values('TaskName', 'TaskDescription', 'Task_difficulty', 'Task_category',
                                      'id', 'Task_author')
    return render(request, 'tasks/tasks.html', {'title': 'web_huck3r\'s tasks',
                                                'view_tasks': view_tasks})


class EachTask(LoginRequiredMixin, DetailView):
    model = Tasks
    template_name = 'tasks/eachtask.html'
    context_object_name = 'task_information'

    def post(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        user = request.user
        if user.is_authenticated:
            obj = self.model.objects.get(id=pk)
            flag = request.POST.get("flag")
            check_flag = 'Неверный флаг'
            if obj.Task_key == flag:
                check_flag = 'Поздравляем вы решили задачу'
                if obj.id not in user.user_data["completed_tasks"]:
                    self.correct_flag(user, obj)
            return render(request, 'tasks/eachtask.html',{'task_information': obj, 'response': check_flag, 'user': user})
        else:
            return redirect('login')

    def correct_flag(self, user, task):
        difficulty = {
            'Easy': 10,
            'Medium': 50,
            'Hard': 200,
            'Extreme': 500
        }

        t_dif = task.Task_difficulty
        if t_dif in difficulty:
            match task.Task_category:
                case 'Osint': user.osint_points += difficulty.get(t_dif)
                case 'Reverse': user.reverse_points += difficulty.get(t_dif)
                case 'Web': user.web_points += difficulty.get(t_dif)
                case 'Crypto': user.crypto_points += difficulty.get(t_dif)
                case 'Other': user.other_points += difficulty.get(t_dif)
            data = user.user_data
            data["completed_tasks"].append(task.id)
            user.save()
