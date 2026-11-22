# Sistema HiperSolar — Buraco Negro 4D & Simulação Astronômica

Simulador espacial interativo de alta fidelidade visual e física, centralizado em um buraco negro de quatro dimensões espaciais (Métrica de Schwarzschild-Tangherlini).

## 🌌 Conceito Principal

O sistema modela um ambiente astronômico fictício onde o Sol é substituído por uma singularidade quadridimensional rodeada por um disco de acreção em espiral e oito planetas orbitantes inspirados no Sistema Solar.

## 📐 Física e Interpretação Dimensional

- **Espaço-tempo 5D (4 espaciais + 1 temporal):**
  - Raio do horizonte de eventos ($r_h$): $r_h^2 = \frac{8 G_5 M}{3 \pi c^2}$
  - Temperatura de Hawking ($T_H$): $T_H = \frac{(D - 3) \hbar c}{4 \pi k_B r_h}$ com $D = 5$.
- **Modos de Simulação:**
  - **Modo Visual (Kepleriano Estável):** Órbitas estáveis e harmoniosas com projeção de coordenadas $W$ via rotações nos planos $XW$ e $YW$.
  - **Modo Físico ($1/r^3$):** Aproximação gravitacional em quatro dimensões espaciais onde a força cai com o cubo da distância.

## ✨ Funcionalidades

- Buraco negro central com disco de acreção dinâmico e anel de fótons.
- 8 planetas com tamanhos, cores, velocidades e distâncias orbitais proporcionais.
- Controles interativos em tempo real para rotações 4D ($XW$, $YW$), velocidade do tempo e alternância de modos físicos.
- Painel informativo de seleção de planetas e foco de câmera.
- Hospedagem nativa e compatível com **GitHub Pages**.

## 🚀 Instalação e Execução Local

1. Clone o repositório:
   ```bash
   git clone https://github.com/Mateus0790/buraco-negro-4d.git
   cd buraco-negro-4d
   ```
2. Abra o arquivo `index.html` diretamente em qualquer navegador moderno ou sirva com um servidor local (ex: Live Server / Python HTTP Server):
   ```bash
   python3 -m http.server 8000
   ```
   Acesse `http://localhost:8000`.

## 🌐 Publicação no GitHub Pages

O projeto está configurado para publicação automática no GitHub Pages através do branch `main` na raiz do repositório.
