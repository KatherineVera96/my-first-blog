from django.conf.urls import url
from . import views

app_name = 'logictree'

urlpatterns = [

    url(r'^$', views.index, name='index'),
    #conversores/bases
    url(r'^conversores/bases/$', views.bases, name='bases'),
    #conversores/ieee
    url(r'^conversores/ieee/$', views.ieee, name='ieee'),
    #evaluador
    url(r'^evaluador/$', views.evaluador, name='evaluador'),
    #graficador
    url(r'^graficador/$', views.graficador, name='graficador'),
    #/derivador
    url(r'^derivador/$', views.derivador, name='derivador'),
    #/biseccion
    url(r'^biseccion/$', views.biseccion, name='biseccion'),
    #/reglafalsa
    url(r'^reglafalsa/$', views.reglafalsa, name='reglafalsa'),
    #/newtonraphson
    url(r'^newtonraphson/$', views.newtonraphson, name='newtonraphson'),
    #secante
    url(r'^secante/$', views.secante, name='secante'),
    #/raices
    url(r'^raices/$', views.raices, name='raices'),
    #rectangulos
    url(r'^rectangulos/$', views.rectangulosview, name='rectangulosview'),
    #trapecio
    url(r'^trapecio/', views.trapecioview, name='trapecioview'),
    #simpson13
    url(r'^simpson13/$', views.simpson13view, name='simpson13view'),
    #simpson38
    url(r'^simpson38/$', views.simpson38, name='simpson38'),
    #montecarlo
    url(r'^montecarlo/$', views.montecarlo, name='montecarlo'),
    #conocenos
    url(r'^conocenos/$', views.conocenos, name='conocenos'),

    #CALCULOS

    #//
    url(r'^$', views.index, name='index'),
    #/braiture/conversores/bases
    url(r'^conversores/bases/calcular$', views.basescalc),
    #//conversores/ieee
    url(r'^conversores/ieee/calcular$', views.ieeecalc),
    #//evaluador
    url(r'^evaluador/calcular$', views.evaluadorcalc),
    #//graficador
    url(r'^graficador/calcular$', views.graficadorcalc),
    #//derivador
    url(r'^derivador/calcular$', views.derivadorcalc),
    #//biseccion
    url(r'^biseccion/calcular$', views.biseccioncalc),
    #//reglafalsa
    url(r'^reglafalsa/calcular$', views.reglafalsacalc),
    #//newtonraphson
    url(r'^newtonraphson/calcular$', views.newtonraphsoncalc),
    #//secante
    url(r'^secante/calcular$', views.secantecalc),
    #//raices
    url(r'^raices/calcular$', views.raicescalc),
    #//rectangulos
    #//simpson13
    #//simpson
    url(r'^simpson38/calcular$', views.simpson38calc),
    #//montecarlo
    url(r'^montecarlo/calcular$', views.montecarlocalc),
]
