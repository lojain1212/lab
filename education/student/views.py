from django.shortcuts import render, redirect, get_object_or_404
from .models import Student, Course
from .forms import StudentForm, CourseForm

def students_view(request):
    students = Student.objects.all()
    form = StudentForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('students')
    return render(request, 'students.html', {'students': students, 'form': form})

def courses_view(request):
    courses = Course.objects.all()
    form = CourseForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('courses')
    return render(request, 'courses.html', {'courses': courses, 'form': form})

def student_details_view(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    enrolled_courses = student.courses.all()
    available_courses = Course.objects.exclude(id__in=enrolled_courses)
    
    if request.method == 'POST':
        course_id = request.POST.get('course_id')
        if course_id:
            course = get_object_or_404(Course, id=course_id)
            student.courses.add(course)
            return redirect('student_details', student_id=student_id)

    return render(request, 'student_details.html', {
        'student': student,
        'enrolled_courses': enrolled_courses,
        'available_courses': available_courses
    })