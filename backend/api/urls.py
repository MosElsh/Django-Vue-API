"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/stable/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import employees_api, employee_api, projects_api, project_api, assignments_api, assignment_api, get_models


urlpatterns = [
    # API entry points should be defined here
    path("getModels", get_models, name="Get Models Structure"),
    path("assignmentsAPI", assignments_api, name="Assignments API"),
    path("assignmentAPI/<int:assignment_id>", assignment_api, name="Assignment API"),
    path("projectsAPI", projects_api, name="Projects API"),
    path("projectAPI/<int:project_id>", project_api, name="Project API"),
    path("employeesAPI", employees_api, name="Emplyees API"),
    path("employeeAPI/<int:employee_id>", employee_api, name="Employee API"),
]
