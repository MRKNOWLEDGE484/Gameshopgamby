from PIL import Image
import streamlit as st

# Configuration de la page
st.set_page_config(page_title="GAMBY GAMESHOP", page_icon="🎮", layout="wide")

# Styles globaux
st.markdown("""
    <style>
        body {
            background-color: #00BFFF; /* Couleur de fond bleu électrique */
            color: #FFFFFF; /* Couleur du texte */
            margin: 0; /* Supprimer les marges */
            padding: 0; /* Supprimer le padding */
            font-family: 'Courier New', Courier, monospace; /* Police */
        }
        .top-left-container {
            position: fixed;
            top: 10px; 
            left: 10px; 
            z-index: 1; 
            background-color: rgba(0, 0, 0, 0.7); 
            padding: 15px 20px; 
            border-radius: 15px; 
            box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.3);
            display: flex; 
            align-items: center; 
        }
        .top-left-container img {
            width: 30px; 
            height: 30px; 
            margin-right: 15px; 
        }
        .top-left-container a {
            color: #ffffff; 
            font-size: 16px; 
            font-weight: bold; 
            text-decoration: none; 
            margin-right: 20px; 
        }
        h1 {
            text-align: center; 
            font-size: 50px; 
            color: #FF4500; 
            text-decoration: underline;
        }
        .product-card {
            border: 2px solid #4B0082; 
            background-color: #FFA500; 
            padding: 10px; 
            border-radius: 10px; 
            margin-bottom: 20px; 
        }
        .section-title {
            text-align: center; 
            font-size: 30px; 
            color: #FF4500; 
            margin-top: 40px;
        }
    </style>
""", unsafe_allow_html=True)

# Créer un conteneur amélioré pour le numéro et les logos en haut à gauche
st.markdown("""
    <div class="top-left-container">
        <p>Téléphone : <a href="tel:+22375357017">+223 75357017</a></p>
        <a href="https://wa.me/+22375357017" target="_blank">
            <img src="https://upload.wikimedia.org/wikipedia/commons/6/6b/WhatsApp.svg" alt="WhatsApp">
        </a>
        <a href="https://www.instagram.com/" target="_blank">
            <img src="https://upload.wikimedia.org/wikipedia/commons/a/a5/Instagram_icon.png" alt="Instagram">
        </a>
    </div>
""", unsafe_allow_html=True)

# Titre de l'application
st.title("GAMBY GAMESHOP")
st.markdown("Bienvenue sur notre site de vente de consoles et manettes !")

# Image d'entête
header_image = Image.open("headimage.png")
st.image(header_image, use_column_width=True)

# Présentation du site
st.markdown("""
    <div style='text-align: center; color: #FF4500;'>
        <p style='font-size: 22px;'>
            GAMBY GAMESHOP est votre destination numéro 1 pour tout ce qui concerne les consoles de jeux vidéo, les jeux, 
            les manettes et accessoires. Que vous soyez un fan de PlayStation, Xbox ou Nintendo, nous avons tout ce qu'il vous faut !
        </p>
    </div>
""", unsafe_allow_html=True)

# Sections pour les consoles
consoles = {
    "PlayStation": [
        ("playstation5.jpeg", "PlayStation 5", "350 000 FCFA"),
        ("Playstation4.jpeg", "PlayStation 4", "150 000 FCFA"),
        ("Playstation3.jpeg", "PlayStation 3", "70 000 FCFA"),
        ("Playstation2.jpeg", "PlayStation 2", "35 000 FCFA"),
    ],
    "Xbox": [
        ("xboxserie s.jpeg", "Xbox Series S", "400 000 FCFA"),
        ("xboxserie x.jpeg", "Xbox Serie X", "350 000 FCFA"),
        ("xboxone.jpeg", "Xbox One", "200 000 FCFA"),
        ("xbox360.jpeg", "Xbox 360", "70 000 FCFA"),
    ],
    "Nintendo": [
        ("ns.jpeg", "Nintendo Switch", "250 000 FCFA"),
        ("nsl.jpeg", "Nintendo Switch Lite", "150 000 FCFA"),
    ]
}

for console, products in consoles.items():
    st.markdown(f"## **Nos Consoles {console}**")
    cols = st.columns(2)
    for i, (img, name, price) in enumerate(products):
        with cols[i % 2]:
            st.image(Image.open(img), caption=name, width=300)
            st.markdown(f"<div class='product-card'><strong>Prix :</strong> {price}</div>", unsafe_allow_html=True)

# Image de bas
header_image_footer = Image.open("headimage4.png")
st.image(header_image_footer, use_column_width=True)

# Section de personnages
st.markdown("## **Personnages Célèbres**")
col1m, col2m = st.columns(2)
with col1m:
    st.image(Image.open("pearce.jpg"), caption="READY FOR WAR", width=300)
    st.markdown("<div class='product-card'>AIDEN PEARCE</div>", unsafe_allow_html=True)
with col2m:
    st.image(Image.open("kratos.jpg"), caption="READY FOR ENEMIES", width=300)
    st.markdown("<div class='product-card'>KRATOS</div>", unsafe_allow_html=True)

# Contact en bas de page
st.markdown("""
    <div style='text-align: center; color: #32CD32;'>
        <p style='font-size: 20px;'>Contactez-nous : <a href="tel:+22375357017">+223 75357017</a> | <a href="tel:+22384555583">+223 84555583</a></p>
    </div>
""", unsafe_allow_html=True)
