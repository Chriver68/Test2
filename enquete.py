import streamlit as st
#
#"""
#Volgende komt erin:
#1. sidebar voor het kiezen van verschillende opties:
#    1. enquete:
#        1. enquete heeft alleen multiple choice vragen
#        2. op grond van de verschillende vragen kunnen er punten worden gescoord
#        3. op grond van het aantal punten per categorie wordt een uitslag getoond
#        4. wordt getoond in 1x over verschillende kolommen
#        5. de vragen hebben; de vraag, 4 mogelijke antwoorden, per antwoord een bepaald punten aantal.
#        Waarschijnlijk een dictionary anders kijken naar classes
#        6. als alle vragen zijn beantwoord moeten de punten worden verwerkt en een uitslag aan gekoppeld
#        7. uitslag is 1 zin waarbij de uitkomsten van de categorien zijn opgenomen
#    2. overzicht wat is ingevuld ter controle. Alleen te benaderen als alles is ingevuld
#    3. formulier/knop om uitslag naar invuller te sturen
#"""

st.session_state.vragen = \
        {1:{"Vraag":"Hoe vaak heb je sexuele fantasietjes? ", "Opties":  ['','Nooit','Soms','Vaak','Altijd'], "Punten":(0,0,3,6,10)},
            2:{"Vraag":"Hoe vaak kijk je porno? ", "Opties":['','Nooit','Soms','Vaak','Heel veel'], "Punten":(0,0,3,6,10)},
            3:{"Vraag":"Hoe vaak masturbeer je? ", "Opties":['','Nooit','Soms','Vaak','Heel veel'], "Punten":(0,0,3,6,10)},
            4:{"Vraag":"Hoe vaak heb je sex? ", "Opties":['','Nooit','Soms','Vaak','Heel veel'], "Punten":(0,0,3,6,10)},
            5:{"Vraag":"Hoe vaak zou je sex willen hebben? ", "Opties":['','Nooit','Soms','Vaak','Heel veel'], "Punten":(0,0,3,6,10)},
            6:{"Vraag":"Wat vind je het lekkerst om te doen bij een man? ", "Opties":
                ['','Vastbinden en blinddoeken en teasen','Lekker op zijn pik zitten en langzaam op en neer gaan', 'Pijpen', 'Sterretje likken en vingeren'], "Punten":(0,0,3,6,10)},
            7:{"Vraag":"Wat vind je het lekkerst als dat wordt gedaan bij jou? ", "Opties":
                ['','Gebeft worden','In mijn poesje worden genomen','In mijn kontje genomen worden', 'Vastgebonden worden en dan verkracht'], "Punten":(0,0,3,6,10)},
            8:{"Vraag":"Word je geil van versturen van geile foto's van jezelf? ", "Opties":
                ['','Nee','Klein beetje','Best wel','Heel geil!'], "Punten":(0,0,3,6,10)},
            9:{"Vraag": "Ben je dominant of onderdanig? ","Opties":
                ['','Geen van beide','Allebei een beetje','Overwegend onderdanig','Overwegend dominant'], "Punten": (0,0, 3, 6, 10)},
            10:{"Vraag":"Wat zou je wel eens willen gebruiken?","Opties":
                ['','Draadloos vibrerend ei','Tepelklemmen','Zweep','Voorbinddildo'], "Punten": (0,0, 3, 6, 10)},
          }

st.session_state.antwoorden = {1: '', 2: '', 3: '', 4: '',5: '', 6: '',7: '', 8: '', 9: '', 10: ''}

st.title("TEST")
st.subheader("Hieronder svp de vragen invullen. Daarna kan je via 'Overzicht' aan de linkerkant naar de resultaten;")

aantal_vragen = len(st.session_state.vragen)
kolom_verdeling = aantal_vragen/2

col1, col2 = st.columns(2,gap="large")
#Vragen op pagina plaatsen
for i in range(aantal_vragen):
    i += 1
    if i <=kolom_verdeling:
        st.session_state.antwoorden[i] = col1.selectbox(st.session_state.vragen[i]["Vraag"], st.session_state.vragen[i]["Opties"])
    else:
        st.session_state.antwoorden[i] = col2.selectbox(st.session_state.vragen[i]["Vraag"],
                                                      st.session_state.vragen[i]["Opties"])


