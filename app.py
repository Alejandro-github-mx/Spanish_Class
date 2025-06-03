import streamlit as st
import random

# Título
st.title("Cuestionario de Español: Unidad 6 - Día a Día")
st.write("Selecciona la respuesta correcta para cada pregunta.")

# Preguntas
questions = [
    {"q": "¿Qué haces por la mañana?", "options": ["Desayuno", "Ceno", "Me acuesto"], "a": "Desayuno"},
    {"q": "¿Con qué frecuencia estudias español (pista: similar a 'sometimes' en inglés?", "options": ["Siempre", "Nunca", "A veces"], "a": "A veces"},
    {"q": "¿Qué día de la semana es después del martes?", "options": ["Lunes", "Miércoles", "Viernes"], "a": "Miércoles"},
    {"q": "¿Qué parte del día es 'la tarde'?", "options": ["De 12 p.m. a 8 p.m.", "De 6 a.m. a 12 p.m.", "De 8 p.m. a 12 a.m."], "a": "De 12 p.m. a 8 p.m."},
    {"q": "¿Cuál es la forma correcta del verbo 'ir' en 'yo ___ al trabajo'?", "options": ["voy", "va", "vas"], "a": "voy"},
    {"q": "Yo estudio por la noche. ¿Y tú?", "options": ["Yo también", "Yo sí", "Yo no"], "a": "Yo también"},
    {"q": "Completa: Primero me levanto, ______ desayuno, y luego voy al trabajo.", "options": ["después", "también", "siempre"], "a": "después"},
    {"q": "¿Qué verbo es irregular?", "options": ["ir", "vivir", "comer"], "a": "ir"},
    {"q": "¿Qué haces normalmente por la noche?", "options": ["Me ducho", "Desayuno", "Voy al trabajo"], "a": "Me ducho"},
    {"q": "¿Con qué frecuencia haces ejercicio?", "options": ["Nunca", "Cada lunes", "Casi siempre"], "a": "Casi siempre"},
    {"q": "¿Cuál es el presente del verbo 'tener' en 'yo ___'?", "options": ["tengo", "tiene", "tenes"], "a": "tengo"},
    {"q": "¿Qué día viene antes del viernes?", "options": ["Jueves", "Miércoles", "Sábado"], "a": "Jueves"},
    {"q": "¿Cuál es una parte del día?", "options": ["La semana", "La tarde", "El año"], "a": "La tarde"},
    {"q": "Yo no estudio los domingos. ¿Y tú?", "options": ["Yo tampoco", "Yo sí", "Yo también"], "a": "Yo tampoco"},
    {"q": "¿Qué actividad es típica en la mañana?", "options": ["Despertarse", "Dormir", "Cenar"], "a": "Despertarse"},
    {"q": "Completa: Me levanto, me ducho y ______ desayuno.", "options": ["luego", "nunca", "también"], "a": "luego"},
    {"q": "¿Qué verbo es irregular en presente?", "options": ["ser", "leer", "beber"], "a": "ser"},
    {"q": "¿Cuál es la hora adecuada para decir 'Buenas noches'?", "options": ["9 p.m.", "11 a.m.", "3 p.m."], "a": "9 p.m."},
    {"q": "¿Qué día de la semana es Wednesday en el calendario español?", "options": ["Miércoles", "Domingo", "Sábado"], "a": "Miércoles"},
    {"q": "¿Qué parte del día corresponde a 'la mañana'?", "options": ["De 6 a.m. a 12 p.m.", "De 1 p.m. a 7 p.m.", "De 8 p.m. a 12 a.m."], "a": "De 6 a.m. a 12 p.m."}
]

# Estado de sesión
if "score" not in st.session_state:
    st.session_state.score = 0
    st.session_state.q_index = 0
    st.session_state.finished = False
    st.session_state.feedback = ""
    st.session_state.previous = []
    st.session_state.shuffled = {}

# Mostrar pregunta actual
if not st.session_state.finished:
    q = questions[st.session_state.q_index]
    st.subheader(f"Pregunta {st.session_state.q_index + 1} de {len(questions)}")
    st.write(q["q"])

    # Mezclar opciones una sola vez por pregunta
    if st.session_state.q_index not in st.session_state.shuffled:
        opts = q["options"].copy()
        random.shuffle(opts)
        st.session_state.shuffled[st.session_state.q_index] = opts

    shuffled_options = st.session_state.shuffled[st.session_state.q_index]
    selected = st.radio("Selecciona una respuesta:", shuffled_options, key=st.session_state.q_index)

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Confirmar respuesta"):
            if selected == q["a"]:
                st.session_state.feedback = "✅ ¡Correcto!"
                st.session_state.score += 1
            else:
                st.session_state.feedback = f"❌ Incorrecto. La respuesta correcta era: {q['a']}"

            st.session_state.previous.append({"index": st.session_state.q_index, "answer": selected})

            if st.session_state.q_index + 1 < len(questions):
                st.session_state.q_index += 1
            else:
                st.session_state.finished = True
            st.rerun()

    with col2:
        if st.button("Volver a la anterior") and st.session_state.q_index > 0:
            st.session_state.q_index -= 1
            st.session_state.feedback = ""
            if st.session_state.previous:
                st.session_state.previous.pop()
            st.rerun()

    if st.session_state.feedback:
        st.info(st.session_state.feedback)

else:
    st.success(f"Juego terminado. Puntaje: {st.session_state.score} de {len(questions)}")

    total = len(questions)
    percent = st.session_state.score / total

    if percent == 1:
        st.balloons()
        st.info("🚀 ¡Perfecto! Respondiste todo correctamente. ¡Excelente trabajo!")
    elif percent >= 0.8:
        st.info("🙂 Muy bien hecho. Solo unas pocas incorrectas. ¡Sigue así!")
    elif percent >= 0.5:
        st.info("⚠️ Estás en buen camino, pero puedes mejorar. Repasa un poco más.")
    else:
        st.info("❌ Intenta de nuevo. Te recomiendo repasar la Unidad 6.")

    if st.button("Reiniciar juego"):
        st.session_state.score = 0
        st.session_state.q_index = 0
        st.session_state.finished = False
        st.session_state.feedback = ""
        st.session_state.previous = []
        st.session_state.shuffled = {}
        st.rerun()
