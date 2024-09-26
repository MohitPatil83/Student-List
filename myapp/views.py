from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from .forms import StudentForm
from django.contrib.auth.decorators import login_required

# Create (Add a student)

@login_required
def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            student.created_by = request.user  # Assign the logged-in user as the creator
            student.save()
            return redirect('display_students')
    else:
        form = StudentForm()
    
    return render(request, 'myapp/add_student.html', {'form': form})

@login_required
def display_students(request):
    students = Student.objects.filter(created_by=request.user)  # Only fetch students for the logged-in user
    return render(request, 'myapp/display_students.html', {'students': students})

# Update (Edit a student)

# myapp/views.py

@login_required
def edit_student(request, student_id):
    student = get_object_or_404(Student, id=student_id, created_by=request.user)  # Ensure only user's students are editable
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('display_students')
    else:
        form = StudentForm(instance=student)
    
    return render(request, 'myapp/edit_student.html', {'form': form, 'student': student})

# myapp/views.py

@login_required
def delete_student(request, student_id):
    student = get_object_or_404(Student, id=student_id, created_by=request.user)  # Ensure only user's students can be deleted
    if request.method == 'POST':
        student.delete()
        return redirect('display_students')
    
    return render(request, 'myapp/delete_student.html', {'student': student})
