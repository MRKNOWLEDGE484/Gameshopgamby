import streamlit as slt

### CONFIGURATION DE LA PAGE
slt.set_page_config(page_title="Niagadougame.com")

# Contenu principal de l'application
slt.markdown("""
    <h1 style='text-align: center; font-size: 50px; color: #FF4500; 
    font-family: "Courier New", Courier, monospace;'>Bienvenue sur NIANGADOU GAMESHOP</h1>
    """, unsafe_allow_html=True)

# Afficher le numéro de téléphone en bas de la page
slt.markdown("""
    <p style='text-align: center; font-size: 20px; color: #32CD32;'>Téléphone : +223 75357017</p>
    """, unsafe_allow_html=True)

# Présentation du site
slt.markdown("""
    <div style='text-align: center; font-family: "Courier New", Courier, monospace; color: #FF4500;'>
        <h1>Bienvenue sur NIANGADOU GAMESHOP</h1>
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
    slt.image('playstation5.jpg', caption="PlayStation 5", width=300)
    slt.markdown("**Prix :** 300 000 FCFA")
    slt.image('playstation4.jpg', caption="PlayStation 4", width=300)
    slt.markdown("**Prix :** 150 000 FCFA")

with col2:
    slt.image('playstation2.jpg', caption="PlayStation 2", width=300)
    slt.markdown("**Prix :** 80 000 FCFA")
    slt.markdown("**Prix :** 50 000 FCFA")

# Section pour Xbox
slt.markdown("## **Nos Consoles Xbox**")
col3, col4 = slt.columns(2)

with col3:
    slt.image('xboxserie s_n.jpg', caption="Xbox Series N", width=300)
    slt.markdown("**Prix :** 400 000 FCFA")
    slt.image('xboxserie s.jpg', caption="Xbox Series", width=300)
    slt.markdown("**Prix :** 350 000 FCFA")

with col4:
    slt.image('xboxone.jpg', caption="Xbox One", width=300)
    slt.markdown("**Prix :** 200 000 FCFA")
    slt.image('xbox360.jpg', caption="Xbox 360", width=300)
    slt.markdown("**Prix :** 70 000 FCFA")

# Section pour Nintendo
slt.markdown("## **Nos Consoles Nintendo**")
col5, col6 = slt.columns(2)

with col5:
    slt.image('ns.jpg', caption="Nintendo Switch", width=300)
    slt.markdown("**Prix :** 250 000 FCFA")

with col6:
    slt.image('nsl.jpg', caption="Nintendo Switch Lite", width=300)
    slt.markdown("**Prix :** 150 000 FCFA")

# Numéro de téléphone en bas de page
slt.markdown("""
    <p style='text-align: center; font-size: 20px; color: #32CD32;'>Téléphone : +223 75357017</p>
    """, unsafe_allow_html=True)
