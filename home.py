from PIL import Image
import streamlit as slt
# Configuration de la page

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
        <p>Téléphone : <a href="tel:+22375357017">+223 75357017</a></p>
        <a href="https://wa.me/+22375357017" target="_blank">
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
slt.title("GAMBY GAMESHOP")
slt.markdown("Bienvenue sur notre site de vente de consoles et manettes !")
slt.markdown("Numéro 1 : +223 75357017")
slt.markdown("Numero 2 : +223 84555583")

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
    Bienvenue sur GAMBY GAMESHOP
             numéro 1 : +223 75357017
             numéro 2 : +223 84555583
    </h1>
    """, unsafe_allow_html=True)

# Image d'entête sous le titre
header_image = Image.open("headimage.png")
slt.image(header_image, use_column_width=True)

# Présentation du site
slt.markdown(""" 
    <div style='text-align: center; font-family: "Courier New", Courier, monospace; color: #FF4500;'>
        <p style='font-size: 22px;'>
            GAMBY GAMESHOP est votre destination numéro 1 pour tout ce qui concerne les consoles de jeux vidéo, les jeux, 
            les manettes et accessoires. Que vous soyez un fan de PlayStation, Xbox ou Nintendo, nous avons tout ce qu'il vous faut !
        </p>
    </div>
    """, unsafe_allow_html=True)

# Section pour PlayStation
slt.markdown("## **Nos Consoles PlayStation**")
col1, col2 = slt.columns(2)

with col1:
    slt.image(Image.open("playstation5.jpeg"), caption="PlayStation 5", width=300)
    slt.markdown("<div style='border: 2px solid #4B0082; background-color: #FFA500; padding: 10px; border-radius: 10px;'>**Prix :** 350 000 FCFA</div>", unsafe_allow_html=True)
    slt.image(Image.open("Playstation4.jpeg"), caption="PlayStation 4", width=300)
    slt.markdown("<div style='border: 2px solid #4B0082; background-color: #FFA500; padding: 10px; border-radius: 10px;'>**Prix :** 150 000 FCFA</div>", unsafe_allow_html=True)

with col2:
    slt.image(Image.open("Playstation3.jpeg"), caption="PlayStation 3", width=300)
    slt.markdown("<div style='border: 2px solid #4B0082; background-color: #FFA500; padding: 10px; border-radius: 10px;'>**Prix :** 70 000 FCFA</div>", unsafe_allow_html=True)
    slt.image(Image.open("Playstation2.jpeg"), caption="PlayStation 2", width=300)
    slt.markdown("<div style='border: 2px solid #4B0082; background-color: #FFA500; padding: 10px; border-radius: 10px;'>**Prix :** 35 000 FCFA</div>", unsafe_allow_html=True)

# Section pour Xbox
slt.markdown("## **Nos Consoles Xbox**")
col3, col4 = slt.columns(2)

with col3:
    slt.image(Image.open("xboxserie s.jpeg"), caption="Xbox Series S", width=300)
    slt.markdown("<div style='border: 2px solid #4B0082; background-color: #FFA500; padding: 10px; border-radius: 10px;'>**Prix :** 400 000 FCFA</div>", unsafe_allow_html=True)
    slt.image(Image.open("xboxserie x.jpeg"), caption="Xbox Serie X", width=300)
    slt.markdown("<div style='border: 2px solid #4B0082; background-color: #FFA500; padding: 10px; border-radius: 10px;'>**Prix :** 350 000 FCFA</div>", unsafe_allow_html=True)

with col4:
    slt.image(Image.open("xboxone.jpeg"), caption="Xbox One", width=300)
    slt.markdown("<div style='border: 2px solid #4B0082; background-color: #FFA500; padding: 10px; border-radius: 10px;'>**Prix :** 200 000 FCFA</div>", unsafe_allow_html=True)
    slt.image(Image.open("xbox360.jpeg"), caption="Xbox 360", width=300)
    slt.markdown("<div style='border: 2px solid #4B0082; background-color: #FFA500; padding: 10px; border-radius: 10px;'>**Prix :** 70 000 FCFA</div>", unsafe_allow_html=True)

# Section pour Nintendo
slt.markdown("## **Nos Consoles Nintendo**")
col5, col6 = slt.columns(2)

with col5:
    slt.image(Image.open("ns.jpeg"), caption="Nintendo Switch", width=300)
    slt.markdown("<div style='border: 2px solid #4B0082; background-color: #FFA500; padding: 10px; border-radius: 10px;'>**Prix :** 250 000 FCFA</div>", unsafe_allow_html=True)

with col6:
    slt.image(Image.open("nsl.jpeg"), caption="Nintendo Switch Lite", width=300)
    slt.markdown("<div style='border: 2px solid #4B0082; background-color: #FFA500; padding: 10px; border-radius: 10px;'>**Prix :** 150 000 FCFA</div>", unsafe_allow_html=True)

### ime de bas
header_image1 = Image.open("headimage4.png")
slt.image(header_image1, use_column_width=True)
###
header_image1 = Image.open("headimage5.png")
slt.image(header_image1, use_column_width=True)
###
col1m, col2m = slt.columns(2)
with col1m:
    slt.image(Image.open("pearce.jpg") , caption ="READY FOR WAR",width=300)
slt.markdown("<div style='border: 2px solid #4B0082; background-color: #D41E1E; padding: 10px; border-radius: 10px;'>AIDEN PEARCE</div>", unsafe_allow_html=True)
with col2m:
    slt.image(Image.open("kratos.jpg") , caption ="READY FOR ENEMIES",width=300)
slt.markdown("<div style='border: 2px solid #4B0082; background-color: #D41E1E; padding: 10px; border-radius: 10px;'>KRATOS</div>", unsafe_allow_html=True)
# Contact en bas de page
slt.markdown("""
    <div style='text-align: center; font-family: "Courier New", Courier, monospace; color: #32CD32;'>
        <p style='font-size: 20px;'>Contactez-nous sur :</p>
        <a href="https://wa.me/+22375357017" target="_blank">
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
    <p style='text-align: center; font-size: 20px; color: #000000;'>Téléphone : <a href="tel:+22375357017">+223 75357017</a></p>
    """, unsafe_allow_html=True)
###
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
        <p>Téléphone : <a href="tel:+22375357017">+223 75357017</a></p>
        <a href="https://wa.me/+22375357017" target="_blank">
            <img src="https://upload.wikimedia.org/wikipedia/commons/6/6b/WhatsApp.svg" alt="WhatsApp">
        </a>
        <a href="https://www.instagram.com/" target="_blank">
            <img src="https://upload.wikimedia.org/wikipedia/commons/a/a5/Instagram_icon.png" alt="Instagram">
        </a>
    </div>
    """, unsafe_allow_html=True)
# Appliquer une couleur de fond verte néon sur toute l'étendue de la page
slt.markdown("""
    <style>
        body {
            background-color: #39FF14; /* Couleur de fond verte néon */
            color: #000000; /* Couleur du texte */
            height: 100vh; /* Hauteur de la fenêtre */
            margin: 0; /* Supprimer les marges */
            padding: 0; /* Supprimer le padding */
        }
        .stApp {
            background-color: #39FF14; /* Couleur de fond pour l'application Streamlit */
        }
    </style>
""", unsafe_allow_html=True)
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

# Titre centré
slt.markdown(""" 
    <h1 style='text-align: center; font-size: 50px; color: #FF4500; 
    font-family: "Courier New", Courier, monospace; text-decoration: underline;'>
    Les differents manttes
    </h1>
    """, unsafe_allow_html=True)
slt.markdown("Numéro 1 : +223 75357017")
slt.markdown("Numero 2 : +223 84555583")

# Image d'entête sous le titre
header_image = Image.open("headimage2.png")
slt.image(header_image, use_column_width=True)
### Commentaire des manettes
import streamlit as slt

# Publicité pour les manettes avec trame de fond noire
slt.markdown("""
    <div style="text-align: center; font-family: 'Courier New', Courier, monospace; color: #FF4500; background-color: #000000; padding: 20px; border-radius: 10px;">
        <h2 style="font-size: 36px; text-decoration: underline;">Découvrez Nos Manettes de Jeux</h2>
        <p style="font-size: 22px; color: #FFFFFF;">
            Que vous soyez un joueur passionné de PlayStation, Xbox ou Nintendo, nous avons les manettes qu'il vous faut !
            Nos manettes sont conçues pour offrir une expérience de jeu fluide, avec une ergonomie adaptée à chaque style de jeu.
            Profitez de notre large gamme de manettes de haute qualité et améliorez votre gameplay dès maintenant.
        </p>
        <h3 style="color: #FFD700; margin-top: 20px;">Commandez dès maintenant et profitez des meilleures offres !</h3>
        <p style="font-size: 18px; color: #32CD32; font-weight: bold;">GAMBY GAMESHOP - Votre boutique pour toutes vos manettes de jeux vidéo.</p>
    </div>
    """, unsafe_allow_html=True)

# Catégorie Manettes PlayStation
slt.markdown("## Manettes PlayStation")

col1, col2 = slt.columns([1, 1])
with col1:
    ps2_controller = Image.open("ps2.jpeg")
    slt.image(ps2_controller, caption="Manette PlayStation 2", use_column_width=True)
    slt.markdown("""
        <div style='border: 2px solid orange; padding: 10px; background-color: #FFD700; text-align: center;'>
            <strong>Prix :</strong> 12,000 CFA
        </div>
    """, unsafe_allow_html=True)

    ps3_controller = Image.open("ps3.jpeg")
    slt.image(ps3_controller, caption="Manette PlayStation 3", use_column_width=True)
    slt.markdown("""
        <div style='border: 2px solid orange; padding: 10px; background-color: #FFD700; text-align: center;'>
            <strong>Prix :</strong> 15,000 CFA
        </div>
    """, unsafe_allow_html=True)

with col2:
    ps4_controller = Image.open("ps4.jpeg")
    slt.image(ps4_controller, caption="Manette PlayStation 4", use_column_width=True)
    slt.markdown("""
        <div style='border: 2px solid orange; padding: 10px; background-color: #FFD700; text-align: center;'>
            <strong>Prix :</strong> 20,000 CFA
        </div>
    """, unsafe_allow_html=True)

    ps5_controller = Image.open("ps5.jpeg")
    slt.image(ps5_controller, caption="Manette PlayStation 5", use_column_width=True)
    slt.markdown("""
        <div style='border: 2px solid orange; padding: 10px; background-color: #FFD700; text-align: center;'>
            <strong>Prix :</strong> 25,000 CFA
        </div>
    """, unsafe_allow_html=True)
### Manettes
slt.markdown("## Manettes Xbox")

col1, col2, col3 = slt.columns([1, 1, 1])
with col1:
    xbox_one_controller = Image.open("one.jpeg")
    slt.image(xbox_one_controller, caption="Manette Xbox One", use_column_width=True)
    slt.markdown("""
        <div style='border: 2px solid orange; padding: 10px; background-color: #FFD700; text-align: center;'>
            <strong>Prix :</strong> 18,000 CFA
        </div>
    """, unsafe_allow_html=True)

    xbox_series_x_controller = Image.open("x.jpeg")
    slt.image(xbox_series_x_controller, caption="Manette Xbox Series X", use_column_width=True)
    slt.markdown("""
        <div style='border: 2px solid orange; padding: 10px; background-color: #FFD700; text-align: center;'>
            <strong>Prix :</strong> 22,000 CFA
        </div>
    """, unsafe_allow_html=True)

with col2:
    xbox_series_s_controller = Image.open("s.jpeg")
    slt.image(xbox_series_s_controller, caption="Manette Xbox Series S", use_column_width=True)
    slt.markdown("""
        <div style='border: 2px solid orange; padding: 10px; background-color: #FFD700; text-align: center;'>
            <strong>Prix :</strong> 20,000 CFA
        </div>
    """, unsafe_allow_html=True)

with col3:
    xbox_360_controller = Image.open("360.jpeg")
    slt.image(xbox_360_controller, caption="Manette Xbox 360", use_column_width=True)
    slt.markdown("""
        <div style='border: 2px solid orange; padding: 10px; background-color: #FFD700; text-align: center;'>
            <strong>Prix :</strong> 17,000 CFA
        </div>
    """, unsafe_allow_html=True)
### publicité CD
import streamlit as slt

# Publicité pour les CD de consoles avec trame de fond noire
slt.title("Nos CD")
slt.markdown("""
    <div style="text-align: center; font-family: 'Courier New', Courier, monospace; color: #FF4500; background-color: #000000; padding: 20px; border-radius: 10px;">
        <h2 style="font-size: 36px; text-decoration: underline;">Découvrez Nos CD de Jeux Vidéo</h2>
        <p style="font-size: 22px; color: #FFFFFF;">
            Plongez dans l'univers de vos consoles préférées avec nos CD de jeux vidéo. Que ce soit pour PlayStation, Xbox ou Nintendo Switch, nous avons les titres les plus populaires et les nouveautés que vous recherchez.
            Nos CD sont disponibles à des prix compétitifs pour offrir des heures de divertissement intense.
        </p>
        <h3 style="color: #FFD700; margin-top: 20px;">Achetez vos CD de jeux maintenant et vivez l'expérience ultime du gaming !</h3>
        <p style="font-size: 18px; color: #32CD32; font-weight: bold;">GAMBY GAMES - Votre source pour les CD de jeux vidéo de toutes les consoles.</p>
    </div>
    """, unsafe_allow_html=True)
### image de bas
header_imagem1 = Image.open("endm.jpeg")
slt.image(header_imagem1, use_column_width=True)
header_imagem = Image.open("logo.png")
slt.image(header_imagem, use_column_width=True)

# Section contact avec logos sous la présentation
slt.markdown("## Contactez-nous")

col1, col2 = slt.columns([1, 1])
with col1:
    whatsapp_logo = Image.open("wlogo.jpeg")
    slt.image(whatsapp_logo, width=50)
    slt.markdown("""
        <a href="https://wa.me/22375357017" target="_blank">Contactez-nous sur WhatsApp</a>
    """, unsafe_allow_html=True)

with col2:
    instagram_logo = Image.open("ilogo.jpeg")
    slt.image(instagram_logo, width=50)
    slt.markdown("""
        <a href="https://www.instagram.com" target="_blank">Contactez-nous sur Instagram</a>
    """, unsafe_allow_html=True)

# Ajout du filigrane "GAMBY GAMES" dans le style jeu vidéo
slt.markdown("""
    <div style='position: fixed; bottom: 10px; right: 10px; font-size: 20px; color: rgba(255, 255, 255, 0.1); font-family: "Courier New", Courier, monospace;'>
        GAMBY GAMES
    </div>
    """, unsafe_allow_html=True)




   


   
  

    

    
