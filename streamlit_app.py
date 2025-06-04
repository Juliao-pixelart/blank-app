import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Função para gerar o gráfico do coração
def gerar_coracao(nome):
    t = np.linspace(0, 2 * np.pi, 1000)
    x = 16 * np.sin(t) ** 3
    y = 13 * np.cos(t) - 5 * np.cos(2 * t) - 2 * np.cos(3 * t) - np.cos(4 * t)

    fig, ax = plt.subplots(figsize=(6, 5))
    ax.plot(x, y, color='red')
    ax.fill(x, y, color='red')
    ax.axis('equal')
    ax.text(0, 0, nome, ha='center', va='center', fontsize=12, color='white')
    return fig

# Título do aplicativo
st.title("Um Pedido Especial")

# Texto do pedido
pedido_texto = "Amor, tenho um pedido especial para fazer, em seu aniversário pensei muito bem no que te entregar de presente, e nada melhor que um pedido novo. Você quer namorar comigo por mais 70 anos? [S/N]:"
resposta = st.text_input(pedido_texto).strip().upper()

# Lógica após clicar no botão "Enviar Resposta"
if st.button("Enviar Resposta"):
    if resposta == 'S':
        nome = 'Mariana/TEKPIX <3'
        
        # Exibe o coração
        fig = gerar_coracao(nome)
        st.pyplot(fig)
        
        # Mensagem de agradecimento
        agradecimento = "Obrigado por me escolher como seu parceiro pra vida, será bem divertido o tempo que passaremos junto, eu te amo muito minha TEKPIX, razão da minha felicidade. Espero que curta nossa vida juntos, prometo te dar muitas capivaras ainda. :)"
        st.write(agradecimento)
        
        # --- Adicionar o vídeo aqui ---
        st.markdown("---") # Adiciona uma linha divisória para separar o conteúdo
        st.subheader("Um Presente para Você!")
        
        # URL de exemplo de um vídeo do YouTube (substitua pelo seu vídeo!)
        video_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ" # Este é um Rickroll! :)
        # Para um vídeo mais apropriado, você pode procurar por "coração" ou "amor" no YouTube.
        # Por exemplo, um vídeo de uma música romântica ou um momento especial de vocês.
        
        st.video(video_url)
        # Se fosse um vídeo local: st.video("nome_do_seu_video.mp4")
        
    elif resposta == 'N':
        st.warning("Escolha errada, provavelmente sua visão está na versão Tekpix, tente novamente.")
    elif resposta: # Captura qualquer outra coisa que não seja 'S' ou 'N'
        st.warning("Por favor, responda com S ou N.")
