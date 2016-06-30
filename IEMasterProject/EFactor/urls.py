from django.conf.urls import patterns, url
import EFactor.views as views

urlpatterns = [
       # url(r'^$', views.ExioVisuals, name='ExioVisuals'),
        url(r'^Abs/Throughput/Validation1/$', views.DataRetrieval, name='DataRetrieval'),
        url(r'^Abs/Throughput/Validation1/form2/Throughput2/Validation2/$', views.DataRetrieval2, name='DataRetrieval2'),
        url(r'^Abs/Throughput/Validation1/form2/Throughput2/Validation2/form3/Throughput3/Validation3/$', views.DataRetrieval3, name='DataRetrieval2'),
        url(r'^Abs/Throughput/Validation1/form2/Throughput2/Validation2/form3/Throughput3/Validation3/form4/Results/$', views.Calculation, name='DataRetrieval2'),
        url(r'^Throughput/calc/$', views.Calculation, name='Calculation'),
        url(r'^Abs/$', views.create_user, name='inputForm1'),
        url(r'^$', views.home, name='inputForm1'),
        url(r'^Abs/Throughput/$', views.checkSNP, name='getUserAmountReactant'),
        url(r'^Abs/Throughput/Validation1/form2/Throughput2/$', views.auxiliaries, name='getUserAmountAuxiliaries'),
        url(r'^Abs/Throughput/Validation1/form2/Throughput2/Validation2/form3/Throughput3/$', views.solvents, name='getUserAmountAuxiliaries'),
        url(r'^Abs/Throughput/Validation1/form2/$', views.create_user2, name='testsd'),
        url(r'^Abs/Throughput/Validation1/form2/Throughput2/Validation2/form3/$', views.create_user3, name='solventsStart'),
        url(r'^Abs/Throughput/Validation1/form2/Throughput2/Validation2/form3/Throughput3/Validation3/form4/$', views.create_user4, name='calcStart'),
        url(r'^Throughput/PageObjects', views.dropTest, name='test'),
        url(r'^Concentration/$', views.concentration, name='test'),
         url(r'^Concentration/buildForm$', views.buildForm, name='test'),
        url(r'^Concentration/calcResults/$', views.calculateItAll, name='test'),
]
