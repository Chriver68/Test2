import streamlit as st
#from enquete import antwoorden, vragen

st.title("Overzicht")

Totaal_score = 0

for i in st.session_state.antwoorden:
    niet_beantwoord = 0
    if st.session_state.antwoorden[i] == "":
        niet_beantwoord +=1
        #st.write("Vraag ", str(i), "is niet beantwoord!")

if niet_beantwoord > 0:
    st.write("Niet alle vragen zijn beantwoord, eerst alle vragen beantwoorden!")
else:
    #Antwoorden ophalen en op grond van positie van het antwoord de punten ophalen
    for key, value in st.session_state.antwoorden.items():
        index = st.session_state.vragen[key]["Opties"].index(value)
        Totaal_score += st.session_state.vragen[key]["Punten"][index]
        st.write('Vraag', str(key),": ", st.session_state.vragen[key]["Vraag"], '\n Antwoord:  ',
                 value) #, ' . Score = ', str(st.session_state.vragen[key]["Punten"][index] ))

    if Totaal_score < 40:
        st.subheader("De uitslag is: Je bent een lief geil sletje")
    elif Totaal_score < 70:
        st.subheader("De uitslag is: Je bent een lief geil en ondeugend sletje")
    elif Totaal_score <= 100:
        st.subheader("De uitslag is: Je bent een lief en ontzettend geile slet! ;-)")


# ---- CONTACT ----
with st.container():
    st.write("---")
    st.subheader("Kopieer de vragen en antwoorden en de uitslag en plak deze in onderstaand formulier. Bij verzenden krijg je de uitslag in je mailbox")
    st.write("##")

    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/CHR.VERDOOLD@GMAIL.COM" method="POST">
        <input type="text" name="name" placeholder="Uw naam" required>
        <input type="email" name="email" placeholder="Uw email adres" required>
        <input type="hidden" name="_autoresponse" value="Uitslag test">
        <textarea name="message" placeholder="Plaats uw bericht hier" required></textarea>
        <button type="submit">Verzend</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()