from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from .models import Timer
from .forms import TimerForm

def front_page(request):
    return render(request, "index.html")
    # return render(request, "index_css.html")

def home_page(request):
    default_data = {
        'name': "Default Pomodoro",
        'minutes': 0,
        'seconds': 4,
    }
    success = False
    added_task = None
    if request.method == "POST":
        form = TimerForm(request.POST)
        if form.is_valid():
            new_task = form.save()
            success = True
            added_task = new_task
            return render(request, "home_page.html", 
            {"form": form,
            "added_task": added_task,
            "success": success,
            "data": default_data},
            )
    else:
        form = TimerForm()
    return render(
        request, "home_page.html",
        {"form": form,
        "added_task": added_task,
        "success": success,
        "data": default_data},
    )
    # return render(request, "home_page_css.html")

def search_task(request):
    page_number = request.GET.get("page", 1)
    name = request.GET.get("name", "").strip()
    segment = request.GET.get("segment", "").strip()

    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        segment = request.POST.get("segment", "").strip()
        # Reset to first page on new search
        page_number = 1

    if name or segment:
        tasks = Timer.objects.filter(
            name__icontains=name, segment__icontains=segment
        ).order_by("id")  # Order by name to ensure consistency
    else:
        tasks = Timer.objects.all().order_by("id")  # Order the results

    paginator = Paginator(tasks, 10)
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        "search_task_css.html",
        {"tasks": page_obj,
         "name_query": name,
         "segment_query": segment},
    )


def edit_task(request, task_id, page_number):
    pn = request.GET.get("page", page_number)
    print(f"[DBG] edit_task {task_id}, {page_number}, {pn} <<<")
    success = False

    if request.method == "POST":
        task = Timer.objects.get(id=task_id)
        name = request.POST.get("name")
        segment = request.POST.get("segment")
        if task.name != task or task.segment != segment:
            task.name = name
            task.segment = segment
            task.save()
            success = True

    task_list = Timer.objects.all()
    paginator = Paginator(task_list, 10)
    page_number = request.POST.get(
        "page", request.GET.get("page", page_number)
    )
    page_obj = paginator.get_page(page_number)
    return render(
        request,
        # "edit_task.html",
        "edit_task_css.html",
        {
            "tasks": page_obj,
            "success": success,
            "updated_tasks_id": task_id,
        },
    )

def delete_task(request, task_id, page_number):
    print("[DBG] delete_task called for ID:", task_id)
    if request.method == "POST":
        task = get_object_or_404(Timer, id=task_id)
        task.delete()
        # Redirect to the same page number after delete
        return redirect("edit_task", task_id=task_id, page_number=page_number)