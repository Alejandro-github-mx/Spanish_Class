import streamlit as st

# Título
st.title("Cuestionario de Español: Unidad 6 - Día a Día")
st.write("Selecciona la respuesta correcta para cada pregunta.")

# Preguntas (puedes ampliar después)
questions = [
    {"q": "¿Qué haces por la mañana?", "options": ["Desayuno", "Ceno", "Me acuesto"], "a": "Desayuno"},
    {"q": "¿Con qué frecuencia estudias español?", "options": ["Siempre", "Nunca", "A veces"], "a": "A veces"},
    {"q": "¿Qué día viene después del martes?", "options": ["Lunes", "Miércoles", "Viernes"], "a": "Miércoles"},
    {"q": "¿Qué parte del día es 'la tarde'?", "options": ["De 1 p.m. a 8 p.m.", "De 6 a.m. a 12 p.m.", "De 8 p.m. a 12 a.m."], "a": "De 1 p.m. a 8 p.m."},
    {"q": "¿Cuál es la forma correcta del verbo 'ir' en 'yo ___ al trabajo'?", "options": ["voy", "va", "vas"], "a": "voy"},
]

# Estado de sesión
if "score" not in st.session_state:
    st.session_state.score = 0
    st.session_state.q_index = 0
    st.session_state.finished = False

# Mostrar pregunta actual
if not st.session_state.finished:
    q = questions[st.session_state.q_index]
    st.subheader(f"Pregunta {st.session_state.q_index + 1} de {len(questions)}")
    st.write(q["q"])

    for opt in q["options"]:
        if st.button(opt, key=opt + str(st.session_state.q_index)):
            if opt == q["a"]:
                st.success("¡Correcto!")
                st.session_state.score += 1
            else:
                st.error(f"Incorrecto. La respuesta correcta era: {q['a']}")

            if st.session_state.q_index + 1 < len(questions):
                st.session_state.q_index += 1
            else:
                st.session_state.finished = True
            st.experimental_rerun()

else:
    st.success(f"Juego terminado. Puntaje: {st.session_state.score} de {len(questions)}")
    if st.button("Reiniciar juego"):
        st.session_state.score = 0
        st.session_state.q_index = 0
        st.session_state.finished = False
        st.experimental_rerun()
