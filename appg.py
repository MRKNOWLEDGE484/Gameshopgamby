from PIL import Image
import streamlit as slt
import Home  # Contient la page d'accueil
import Manettes et CD  # Contient la page 'Manettes et CD'

# Créer une barre de navigation
menu = slt.sidebar.selectbox(
    "Navigation",
    ["Accueil", "Manettes et CD"]
)

# Afficher le contenu de la page selon le choix dans le menu
if menu == "Accueil":
    Home.show_page()  # Affiche la page d'accueil
elif menu == "Manettes et CD":
    Manette et CD.show_page()  # Affiche la page 'Manettes et CD'
    header_image = Image.open("headimage2.png")
slt.image(header_image, use_column_width=True)
import streamlit as st

# Titre personnalisé
st.markdown(
    """
    <h1 style='text-align: center; color: #3498db; font-size: 50px; font-weight: bold; text-decoration: underline;'>
        Bienvenue chez Gamby Games
    </h1>
    """,
    unsafe_allow_html=True
)
slt.markdown("Bienvenue sur notre site de vente de consoles et manettes !")
slt.markdown("Numéro 1 : +223 7537017")
slt.markdown("Numero 2 : +223 84555583")
import streamlit as st

# Texte personnalisé
st.markdown(
    """
    <p style='text-align: center; color: #2ecc71; font-size: 24px; font-weight: bold;'>
        Cliquez sur Accueil ou Manettes et CD
    </p>
    """,
    unsafe_allow_html=True
)

