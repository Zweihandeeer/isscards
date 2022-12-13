from django.shortcuts import render
from importlib.resources import path
from django.shortcuts import render,redirect
from home.models import Cartas
from home.forms import CartasForm


def home(request):
    return render(request, "index.html")

def login(request):
    submitted = False
    if request.method == 'POST':
        form = contactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
    return render(request, "login.html")

def coach(request):
    return render(request, "coachview.html")

def listarcartas(request):
    cartas = Cartas.objects.all()
    return render(request,"coachview.html", {"cartas": cartas})

""" def listCartas(con):
    miCursor = con.cursor()
    while True:        
        miCursor.execute("select biblio.id_biblioteca as 'ID de Biblioteca', game.nombre_juego as 'Juego',  cset.nombre_set as 'Set', card.id_carta as 'ID de carta', card.nombre as 'Nombre de carta',card.habilidad as 'Habilidad',  kw.keyword_name as 'Keyword', card.costo as 'Costo de mana', card.fuerza as 'Fuerza', card.salud as 'Salud', rare.card_rarity as 'Rareza', ctype.card_type as 'Tipo de carta', reg.region_name as 'Region', speed.type_of_spell as 'Tipo de Hechizo' from cc_carta card inner join connect_juego game on card.cod_juego = game.id_juego inner join connect_biblioteca biblio on biblio.id_biblioteca = card.cod_biblioteca inner join cc_rarity rare on rare.id_rarity = card.cod_rarity inner join cc_cardtype ctype on ctype.id_card_type = card.cod_cardtype inner join cc_sets cset on cset.id_set = card.cod_set inner join cc_region reg on reg.id_region = card.cod_region_1 inner join cc_speed speed on speed.id_speed = card.cod_speed inner join cc_keyword kw on kw.id_keyword = card.cod_keyword_1 order by 4;")
        registros = miCursor.fetchall()
        for listado in registros:
            print("↳ Nombre Carta: ",listado[6],", ID Región: ",listado[4],", Costo: ",listado[8],", Fuerza: ",listado[12],", Puntos de salud: ",listado[13],", Habilidad: ",listado[11])
        print("\nCantidad de cartas encontradas: ", len(registros),"\n") 
        con.commit()  """

def player(request):
    return render(request, "playerview.html")

def cmatchup(request):
    return render(request, "coachmatchup.html")