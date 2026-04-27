import streamlit as st
import random

st.set_page_config(page_title="Trivia Villanas Disney", page_icon="👑")

# Preguntas
preguntas = [
    {
        "pregunta": "¿Cómo se llama la villana de La Sirenita?",
        "opciones": ["Úrsula", "Maléfica", "Cruella", "Jafar"],
        "respuesta": "Úrsula"
    },
    {
        "pregunta": "¿Qué villana quiere matar a Blancanieves?",
        "opciones": ["La Reina Malvada", "Úrsula", "Gothel", "Cruella"],
        "respuesta": "La Reina Malvada"
    },
    {
        "pregunta": "¿Qué villana usa un abrigo de dálmatas?",
        "opciones": ["Cruella de Vil", "Maléfica", "Yzma", "Úrsula"],
        "respuesta": "Cruella de Vil"
    },
    {
        "pregunta": "¿Quién es la villana de La Bella Durmiente?",
        "opciones": ["Maléfica", "Úrsula", "Madre Gothel", "Reina de Corazones"],
        "respuesta": "Maléfica"
    },
    {
        "pregunta": "¿Qué villana secuestra a Rapunzel?",
        "opciones": ["Madre Gothel", "Úrsula", "Cruella", "Maléfica"],
        "respuesta": "Madre Gothel"
    }
]

# Estado de sesión
if "preguntas_mezcladas" not in st.session_state:
    st.session_state.preguntas_mezcladas = random.sample(preguntas, len(preguntas))
    st.session_state.respuestas_usuario = {}

st.title("👑 Trivia de Villanas Disney")
st.write("Responde las 5 preguntas:")

# Mostrar preguntas
for i, p in enumerate(st.session_state.preguntas_mezcladas):
    st.subheader(f"Pregunta {i+1}: {p['pregunta']}")

    opciones_mezcladas = random.sample(p["opciones"], len(p["opciones"]))

    respuesta = st.radio(
        "Selecciona una opción:",
        opciones_mezcladas,
        key=f"pregunta_{i}"
    )

    st.session_state.respuestas_usuario[i] = respuesta

# Botón de verificación
if st.button("Verificar respuestas"):
    puntaje = 0

    for i, p in enumerate(st.session_state.preguntas_mezcladas):
        if st.session_state.respuestas_usuario.get(i) == p["respuesta"]:
            puntaje += 1

    st.write(f"Tu puntaje: {puntaje}/5")

    if puntaje == 5:
        st.balloons()
        st.success("🎉 ¡Perfecto! Conoces muy bien a las villanas Disney")
    else:
        st.warning("Sigue intentando 👀")

# Botón reiniciar
if st.button("Jugar de nuevo"):
    st.session_state.preguntas_mezcladas = random.sample(preguntas, len(preguntas))
    st.session_state.respuestas_usuario = {}
    st.experimental_rerun()

