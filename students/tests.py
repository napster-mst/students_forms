from django.test import TestCase
from students.models import (
    Student,
    Gender,
    Department
)


# Create your tests here.
class StudentTestCase(TestCase):
    def setUp(self):
        gen = Gender.objects.create(sex="Male")
        dept = Department.objects.create(title="Mechanical Engg")
        Student.objects.create(first_name="Abc", last_name="Def", mobile="8793596487",
                               gender=gen,
                               department=dept,
                               city="Pune", state="Maharashtra")
        # Animal.objects.create(name="cat", sound="meow")

    def test_student(self):
        """Animals that can speak are correctly identified"""
        student1 = Student.objects.get(first_name="Abc")
        self.assertEqual(student1.last_name, 'Def')
