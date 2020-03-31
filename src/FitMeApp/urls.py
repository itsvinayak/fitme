from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='index'),
    #path('home', views.home, name='login'),
    # path('registration', views.registration),
    # path('signup', views.signup),
    # path('checkuser', views.checkuser, name='checkuser'),
    path('contact', views.contact, name='contact'),
    path('about',views.about, name='about'),
    path('services',views.services, name='services'),
    path('gallery',views.gallery, name='gallery'),
    path('portal', views.portal, name='portal'),
    path('portal/beginners-routines', views.beginners_routines, name='beginners_routines'),
    path('portal/beginners-routines/day1', views.beginner_day1, name='beginner_day1'),
    path('portal/beginners-routines/day2', views.beginner_day2, name='beginner_day2'),
    path('portal/beginners-routines/day3', views.beginner_day3, name='beginner_day3'),
    path('portal/beginners-routines/day4', views.beginner_day4, name='beginner_day4'),
    path('portal/beginners-routines/day5', views.beginner_day5, name='beginner_day5'),
    path('portal/beginners-routines/day6', views.beginner_day6, name='beginner_day6'),
    path('portal/beginners-routines/day7', views.beginner_day7, name='beginner_day7'),
    path('portal/beginners-routines/day8', views.beginner_day8, name='beginner_day8'),
    path('portal/beginners-routines/day9', views.beginner_day9, name='beginner_day9'),
    path('portal/beginners-routines/day10', views.beginner_day10, name='beginner_day10'),
    path('portal/beginners-routines/day11', views.beginner_day11, name='beginner_day11'),
    path('portal/beginners-routines/day12', views.beginner_day12, name='beginner_day12'),
    path('portal/beginners-routines/day13', views.beginner_day13, name='beginner_day13'),
    path('portal/beginners-routines/day14', views.beginner_day14, name='beginner_day14'),
    path('portal/beginners-routines/day15', views.beginner_day15, name='beginner_day15'),
    path('portal/beginners-routines/day16', views.beginner_day16, name='beginner_day16'),
    path('portal/beginners-routines/day17', views.beginner_day17, name='beginner_day17'),
    path('portal/beginners-routines/day18', views.beginner_day18, name='beginner_day18'),
    path('portal/beginners-routines/day19', views.beginner_day19, name='beginner_day19'),
    path('portal/beginners-routines/day20', views.beginner_day20, name='beginner_day20'),
    path('portal/beginners-routines/day21', views.beginner_day21, name='beginner_day21'),
    path('portal/beginners-routines/day22', views.beginner_day22, name='beginner_day22'),
    path('portal/beginners-routines/day23', views.beginner_day23, name='beginner_day23'),
    path('portal/beginners-routines/day24', views.beginner_day24, name='beginner_day24'),
    path('portal/beginners-routines/day25', views.beginner_day25, name='beginner_day25'),
    path('portal/beginners-routines/day26', views.beginner_day26, name='beginner_day26'),
    path('portal/beginners-routines/day27', views.beginner_day27, name='beginner_day27'),
    path('portal/beginners-routines/day28', views.beginner_day28, name='beginner_day28'),
    path('portal/diet/beginner', views.diet_beginner, name='diet_beginner'),
    path('portal/diet/intermediate', views.diet_intermediate, name='diet_intermediate'),
    path('portal/diet/hardcore', views.diet_hardcore, name='diet_hardcore'),
    path('know_your_BMI_with_standard_unit', views.bmistandard, name='bmistandard'),
    path('know_your_BMI_with_metric_unit', views.bmimetric, name='bmimetric'),
]
