from PIL import Image
import streamlit as slt

# Configuration de la page
slt.set_page_config(page_title="GAMBYGameshop.com", layout="wide",page_icon=r"C:\Users\Lenovo\Desktop\games shop project\logo.png")
# Créer un conteneur amélioré pour le numéro et les logos en haut à gauche
slt.markdown(""" 
    <style>
        .top-left-container {
            position: fixed;
            top: 10px;  /* Positionnez-le à 10 pixels du haut */
            left: 10px; /* Positionnez-le à 10 pixels de la gauche */
            z-index: 1; /* Assurez-vous qu'il est au-dessus des autres éléments */
            background-color: rgba(0, 0, 0, 0.7); /* Fond semi-transparent */
            padding: 15px 20px; /* Espacement intérieur */
            border-radius: 15px; /* Coins arrondis */
            box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.3); /* Ombre portée */
            display: flex; /* Flexbox pour alignement */
            align-items: center; /* Alignement vertical centré */
        }
        .top-left-container img {
            width: 30px; /* Largeur des logos */
            height: 30px; /* Hauteur des logos */
            margin-right: 15px; /* Espacement à droite des logos */
        }
        .top-left-container a {
            color: #ffffff; /* Couleur du texte */
            font-size: 16px; /* Taille de la police */
            font-weight: bold; /* Texte en gras */
            text-decoration: none; /* Pas de soulignement */
            margin-right: 20px; /* Espacement à droite des liens */
        }
        .top-left-container p {
            color: #32CD32; /* Couleur du texte du numéro */
            font-size: 16px; /* Taille de la police */
            margin-right: 20px; /* Espacement à droite du texte */
        }
    </style>
    <div class="top-left-container">
        <p>Téléphone : <a href="tel:+2237537017">+223 7537017</a></p>
        <a href="https://wa.me/+2237537017" target="_blank">
            <img src="https://upload.wikimedia.org/wikipedia/commons/6/6b/WhatsApp.svg" alt="WhatsApp">
        </a>
        <a href="https://www.instagram.com/" target="_blank">
            <img src="https://upload.wikimedia.org/wikipedia/commons/a/a5/Instagram_icon.png" alt="Instagram">
        </a>
    </div>
    """, unsafe_allow_html=True)
# Styles pour la barre de navigation
slt.markdown("""
<style>
    .sidebar .sidebar-content {
        background-color: #0f4c81; /* Couleur de fond de la barre */
        color: white; /* Couleur du texte */
        border-radius: 10px; /* Arrondir les bords */
        padding: 10px; /* Espacement interne */
    }
    .sidebar .sidebar-content h1 {
        font-size: 1.5em; /* Taille du titre */
        text-align: center; /* Centrer le titre */
        margin-bottom: 20px; /* Marge en bas du titre */
    }
    .sidebar .sidebar-content a {
        color: #f0f0f0; /* Couleur des liens */
        font-size: 1.2em; /* Taille de la police des liens */
        text-decoration: none; /* Supprimer le soulignement */
        display: block; /* Chaque lien sur une nouvelle ligne */
        margin: 10px 0; /* Espacement entre les liens */
    }
    .sidebar .sidebar-content a:hover {
        color: #ffcc00; /* Couleur au survol des liens */
    }
</style>
""", unsafe_allow_html=True)

# Titre du menu
slt.sidebar.markdown("<h1 style='color: white;'>Menu 🎮</h1>", unsafe_allow_html=True)

# Liens de navigation
slt.sidebar.markdown("[🎮 Consoles](#consoles)")
slt.sidebar.markdown("[🕹️ Manettes](#manettes)")

# Appliquer une couleur de fond bleu électrique sur toute l'étendue de la page
slt.markdown("""
    <style>
        body {
            background-color: #00BFFF; /* Couleur de fond bleu électrique */
            color: #FFFFFF; /* Couleur du texte */
            height: 100vh; /* Hauteur de la fenêtre */
            margin: 0; /* Supprimer les marges */
            padding: 0; /* Supprimer le padding */
        }
        .stApp {
            background-color: #00BFFF; /* Couleur de fond pour l'application Streamlit */
        }
        .sidebar .sidebar-content {
            background-color: rgba(255, 255, 255, 0.9); /* Fond de la barre latérale */
            border: 2px solid #007FFF; /* Bordure autour de la barre */
            border-radius: 10px; /* Coins arrondis */
            padding: 10px; /* Espacement intérieur */
            box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.3); /* Ombre */
        }
        .sidebar h1, .sidebar h2 {
            color: #007FFF; /* Couleur des titres */
            font-family: 'Arial', sans-serif; /* Police */
        }
    </style>
""", unsafe_allow_html=True)

# Titre de l'application
slt.title("NIANGADOU GAMESHOP")
slt.markdown("Bienvenue sur notre site de vente de consoles et manettes !")
slt.markdown("Numéro 1 : +223 7537017")
slt.markdown("Numero 2 : +223 84555583")
# Titre du menu
slt.sidebar.markdown("<h2 style='text-align: center;'>🎮 Menu 🎮</h2>", unsafe_allow_html=True)
slt.sidebar.success("Choisissez la page")
slt.sidebar.markdown("## 🎮 Consoles \n Sélectionnez cette section pour découvrir nos consoles.")
slt.sidebar.markdown("## 🎮 Manettes \n Explorez notre collection de manettes.")
slt.sidebar.markdown("## 🎶 CD \n Consultez notre sélection de CD de jeux.")
# Appliquer une couleur de fond bleu électrique sur toute l'étendue de la page
slt.markdown("""
    <style>
        body {
            background-color: #00BFFF; /* Couleur de fond bleu électrique */
            color: #FFFFFF; /* Couleur du texte */
            height: 100vh; /* Hauteur de la fenêtre */
            margin: 0; /* Supprimer les marges */
            padding: 0; /* Supprimer le padding */
        }
        .stApp {
            background-color: #00BFFF; /* Couleur de fond pour l'application Streamlit */
        }
    </style>
""", unsafe_allow_html=True)



# Titre centré
slt.markdown(""" 
    <h1 style='text-align: center; font-size: 50px; color: #FF4500; 
    font-family: "Courier New", Courier, monospace; text-decoration: underline;'>
    Bienvenue sur NIANGADOU GAMESHOP
             numéro 1 : +223 7537017
             numéro 2 : +223 84555583
    </h1>
    """, unsafe_allow_html=True)

# Image d'entête sous le titre
header_image = Image.open(r"C:\Users\Lenovo\Desktop\games shop project\headimage.png")
slt.image(header_image, use_column_width=True)

# Présentation du site
slt.markdown(""" 
    <div style='text-align: center; font-family: "Courier New", Courier, monospace; color: #FF4500;'>
        <p style='font-size: 22px;'>
            NIANGADOU GAMESHOP est votre destination numéro 1 pour tout ce qui concerne les consoles de jeux vidéo, les jeux, 
            les manettes et accessoires. Que vous soyez un fan de PlayStation, Xbox ou Nintendo, nous avons tout ce qu'il vous faut !
        </p>
    </div>
    """, unsafe_allow_html=True)

# Section pour PlayStation
slt.markdown("## **Nos Consoles PlayStation**")
col1, col2 = slt.columns(2)

with col1:
    slt.image(Image.open(r"C:\Users\Lenovo\Desktop\games shop project\playstation5.jpeg"), caption="PlayStation 5", width=300)
    slt.markdown("<div style='border: 2px solid #4B0082; background-color: #FFA500; padding: 10px; border-radius: 10px;'>**Prix :** 350 000 FCFA</div>", unsafe_allow_html=True)
    slt.image(Image.open(r"C:\Users\Lenovo\Desktop\games shop project\playstation4.jpeg"), caption="PlayStation 4", width=300)
    slt.markdown("<div style='border: 2px solid #4B0082; background-color: #FFA500; padding: 10px; border-radius: 10px;'>**Prix :** 150 000 FCFA</div>", unsafe_allow_html=True)

with col2:
    slt.image(Image.open(r"C:\Users\Lenovo\Desktop\games shop project\playstation3.jpeg"), caption="PlayStation 3", width=300)
    slt.markdown("<div style='border: 2px solid #4B0082; background-color: #FFA500; padding: 10px; border-radius: 10px;'>**Prix :** 35 000 FCFA</div>", unsafe_allow_html=True)
    slt.image(Image.open(r"C:\Users\Lenovo\Desktop\games shop project\playstation2.jpeg"), caption="PlayStation 2", width=300)
    slt.markdown("<div style='border: 2px solid #4B0082; background-color: #FFA500; padding: 10px; border-radius: 10px;'>**Prix :** 35 000 FCFA</div>", unsafe_allow_html=True)

# Section pour Xbox
slt.markdown("## **Nos Consoles Xbox**")
col3, col4 = slt.columns(2)

with col3:
    slt.image(Image.open(r"C:\Users\Lenovo\Desktop\games shop project\xboxserie s.jpeg"), caption="Xbox Series N", width=300)
    slt.markdown("<div style='border: 2px solid #4B0082; background-color: #FFA500; padding: 10px; border-radius: 10px;'>**Prix :** 400 000 FCFA</div>", unsafe_allow_html=True)
    slt.image(Image.open(r"C:\Users\Lenovo\Desktop\games shop project\xboxserie x.jpeg"), caption="Xbox Series", width=300)
    slt.markdown("<div style='border: 2px solid #4B0082; background-color: #FFA500; padding: 10px; border-radius: 10px;'>**Prix :** 350 000 FCFA</div>", unsafe_allow_html=True)

with col4:
    slt.image(Image.open(r"C:\Users\Lenovo\Desktop\games shop project\xboxone.jpeg"), caption="Xbox One", width=300)
    slt.markdown("<div style='border: 2px solid #4B0082; background-color: #FFA500; padding: 10px; border-radius: 10px;'>**Prix :** 200 000 FCFA</div>", unsafe_allow_html=True)
    slt.image(Image.open(r"C:\Users\Lenovo\Desktop\games shop project\xbox360.jpeg"), caption="Xbox 360", width=300)
    slt.markdown("<div style='border: 2px solid #4B0082; background-color: #FFA500; padding: 10px; border-radius: 10px;'>**Prix :** 70 000 FCFA</div>", unsafe_allow_html=True)

# Section pour Nintendo
slt.markdown("## **Nos Consoles Nintendo**")
col5, col6 = slt.columns(2)

with col5:
    slt.image(Image.open(r"C:\Users\Lenovo\Desktop\games shop project\ns.jpeg"), caption="Nintendo Switch", width=300)
    slt.markdown("<div style='border: 2px solid #4B0082; background-color: #FFA500; padding: 10px; border-radius: 10px;'>**Prix :** 250 000 FCFA</div>", unsafe_allow_html=True)

with col6:
    slt.image(Image.open(r"C:\Users\Lenovo\Desktop\games shop project\nsl.jpeg"), caption="Nintendo Switch Lite", width=300)
    slt.markdown("<div style='border: 2px solid #4B0082; background-color: #FFA500; padding: 10px; border-radius: 10px;'>**Prix :** 150 000 FCFA</div>", unsafe_allow_html=True)

### ime de bas
header_image1 = Image.open(r"C:\Users\Lenovo\Desktop\games shop project\headimage4.png")
slt.image(header_image1, use_column_width=True)
###
header_image1 = Image.open(r"C:\Users\Lenovo\Desktop\games shop project\headimage5.png")
slt.image(header_image1, use_column_width=True)
###
col1m, col2m = slt.columns(2)
with col1m:
    slt.image(Image.open(r"C:\Users\Lenovo\Desktop\games shop project\pearce.jpg") , caption ="READY FOR WAR",width=300)
slt.markdown("<div style='border: 2px solid #4B0082; background-color: #D41E1E; padding: 10px; border-radius: 10px;'>AIDEN PEARCE</div>", unsafe_allow_html=True)
with col2m:
    slt.image(Image.open(r"C:\Users\Lenovo\Desktop\games shop project\kratos.jpg") , caption ="READY FOR ENEMIES",width=300)
slt.markdown("<div style='border: 2px solid #4B0082; background-color: #D41E1E; padding: 10px; border-radius: 10px;'>KRATOS</div>", unsafe_allow_html=True)
# Contact en bas de page
slt.markdown("""
    <div style='text-align: center; font-family: "Courier New", Courier, monospace; color: #32CD32;'>
        <p style='font-size: 20px;'>Contactez-nous sur :</p>
        <a href="https://wa.me/+2237537017" target="_blank">
            <img src="https://upload.wikimedia.org/wikipedia/commons/6/6b/WhatsApp.svg" alt="WhatsApp" style="width: 30px; height: 30px; vertical-align: middle;"/>
            WhatsApp
        </a>
        <br>
        <a href="https://www.instagram.com/" target="_blank">
            <img src="https://upload.wikimedia.org/wikipedia/commons/a/a5/Instagram_icon.png" alt="Instagram" style="width: 30px; height: 30px; vertical-align: middle;"/>
            Instagram
        </a>
    </div>
    """, unsafe_allow_html=True)
# Numéro de téléphone répété en bas de page
slt.markdown(""" 
    <p style='text-align: center; font-size: 20px; color: #000000;'>Téléphone : <a href="tel:+2237537017">+223 7537017</a></p>
    """, unsafe_allow_html=True)
###
