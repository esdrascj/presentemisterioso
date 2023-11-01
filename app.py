import streamlit as st
from PIL import Image



st.set_page_config(page_title="Presente", page_icon="🎁")


with open("./style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# add_page_title(page_icon="🎁")  # Optional method to add title and icon to current page


def exibir_surpresa():
   
    
    st.header(
        """
        Esse site vale uma viagem para comemorar 2 anos de casado 🎉
        """
    )
    st.divider()
    st.write(
        """
            Mesmo com todos os gastos que tivemos esse ano, não poderia deixar de me esforçar um pouco para termos esse tempo de qualidade que é tão valioso.
            E para incrementar as comemorações, nosso 2 anos será comemorado também com o nosso 1º natal como familia.
            Para celebrarmos esse tempo e com pouco dinheiro(ou nenhum dinheiro disponível, apenas um cartão de crédito), fiz a reserva de um airbnb muito aconchegante.
            Mais detalhes na seção abaixo.
        
            """
    )
    st.divider()

    st.markdown(
        f"""
        Informações importantes**
        - Destino: Casoca Casa de Praia - Lot. Jardim Imbassaí 🏖
        - Data de ida: sábado 23 de dezembro a partir das 14h
        - Data de volta: terça 26 de dezembro a partir até as 11h<br><br>Clique no link abaixo para ver todos os detalhes da nossa residência temporaria: 
        <div class="airbnb-embed-frame" data-id="41314204" data-view="home" data-hide-reviews="true" style="width: 600px; height: 100px; margin: auto; align-items: center;">
        <a href="https://www.airbnb.com.br/rooms/41314204?guests=1&amp;adults=1&amp;s=66&amp;source=embed_widget" rel="nofollow">Ver no Airbnb</a>
        <a href="https://www.airbnb.com.br/rooms/41314204?guests=1&amp;adults=1&amp;s=66&amp;source=embed_widget" rel="nofollow">Casa · Mata de São João · ★4,98 · 1 quarto · 1 cama · 1 banheiro</a>
        <script async="" src="https://www.airbnb.com.br/embeddable/airbnb_jssdk"></script></div>

        """,
        unsafe_allow_html=True,
    )

    image = Image.open('images/entrada.webp')
    image2 = Image.open('images/patio.webp')
    image3 = Image.open('images/sala.webp')
    image4 = Image.open('images/sala2.webp')
    image5 = Image.open('images/cozinha.webp')
    image6 = Image.open('images/quarto.webp')

    st.image(image)
    st.image(image2)
    st.image(image3)
    st.image(image4)
    st.image(image5)
    st.image(image6)


    


def main():
    option = st.selectbox(
        "Selecione a opção para mostrar a surpresa",
        ("Não exibir", "Exibir surpresa"),
    )

    if option == ("Exibir surpresa"):
        st.balloons()
        exibir_surpresa()

    else:
        st.write()


def surpresa():
    st.markdown()


if __name__ == "__main__":
    main()
