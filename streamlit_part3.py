import streamlit as st
# Importation du module
from streamlit_option_menu import option_menu
from streamlit_authenticator import Authenticate

# Nos données utilisateurs doivent respecter ce format
account_data = {
    'usernames': {
        'Thomas': {
            'name': 'Thomas',
            'password': '123TOTO321',
            'email': 'admin@gmail.com',
            'failed_login_attemps': 0,  # Sera géré automatiquement
            'logged_in': False,          # Sera géré automatiquement
            'role': 'administrateur'
        }
    }
}

authenticator = Authenticate(
    account_data,  # Les données des comptes
    "cookie name",         # Le nom du cookie, un str quelconque
    "cookie key",          # La clé du cookie, un str quelconque
    30,                    # Le nombre de jours avant que le cookie expire
)

authenticator.login()

def accueil():
    account_data = {
    'usernames': {
        'Thomas': {
            'name': 'Thomas',
            'password': '123TOTO321',
            'email': 'admin@gmail.com',
            'failed_login_attemps': 0,  # Sera géré automatiquement
            'logged_in': False,          # Sera géré automatiquement
            'role': 'administrateur'
        }
    }
    }
    st.title(f"Salut {account_data['usernames']['Thomas']['name']} !")

  
  # On affiche un menu déroulant (selectbox) DANS la barre latérale (sidebar)
# L'utilisateur peut choisir son moyen de contact préféré parmi trois options

with st.sidebar:
    if st.session_state["authentication_status"]:
        accueil()
        # Le bouton de déconnexion
        authenticator.logout("Déconnexion")
        selection = option_menu(menu_title=None, options = ["Accueil", "Photos"])

  # On indique au programme quoi faire en fonction du choix
if selection == "Accueil":
    st.title(":clown_face: Bienvenue sur ma page")
    st.image("https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse2.mm.bing.net%2Fth%2Fid%2FOIP.OOX0hHEmwYrjVQSOQIYF3gHaHV%3Fpid%3DApi&f=1&ipt=7122fb1b5a2db63190962a83b2d16930ec4fad0f89cff72d729a8f5ba94ae3a9&ipo=images")
elif selection == "Photos":
    st.title(":smiley_cat: Les photos de mon chat")
     # Création de 3 colonnes 
    col1, col2, col3 = st.columns(3)

# Contenu de la première colonne : 
    with col1:
        st.header("Smart")
        st.image("https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse4.mm.bing.net%2Fth%2Fid%2FOIP.DL8Y0WUWzy991cw0rJbgHwHaJz%3Fpid%3DApi&f=1&ipt=74cfd190afb66cabbec796ea0a11596ab2fd5924236ddd22f0dec0cf82e3881d&ipo=images")

# Contenu de la deuxième colonne :
    with col2:
        st.header("Wild...")
        st.image("https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse3.mm.bing.net%2Fth%2Fid%2FOIP.WEJ6Qy6S1FZ9WSqUaVZxKQHaFW%3Fpid%3DApi&f=1&ipt=376cbd246a3694849926c475c5b2f8b3dd41c571aeafd4eb1599312c91d2fcee&ipo=images")

# Contenu de la troisième colonne : 
    with col3:
        st.header("Angry")
            st.image("https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse3.mm.bing.net%2Fth%2Fid%2FOIP.o92DjkjzT2Oe42-UbndRugHaEK%3Fr%3D0%26pid%3DApi&f=1&ipt=13dc838a616746e907864236a8d4da9ae6177c0a1388f5cf6658c4a2df933285&ipo=images")


    elif st.session_state["authentication_status"] is False:
        st.error("L'username ou le password est/sont incorrect")
    elif st.session_state["authentication_status"] is None:
        st.warning('Les champs username et mot de passe doivent être remplie')
