import pygame
import time

# Inicialização do Pygame
pygame.init()

# Definir cores
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
CINZA = (169, 169, 169)

# Definir o tamanho da tela
LARGURA = 800
ALTURA = 600
screen = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption('Galinha Atravessando a Rua')

# Definir o relógio
clock = pygame.time.Clock()

# Definir a classe para a Galinha
class Galinha(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Substitua pelo caminho da sua imagem
        self.image = pygame.image.load("galinha.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 50))  # Redimensionar a imagem
        self.rect = self.image.get_rect()
        self.rect.center = (LARGURA // 2, ALTURA - 50)
        self.velocidade = 5

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.velocidade
        if keys[pygame.K_RIGHT] and self.rect.right < LARGURA:
            self.rect.x += self.velocidade
        if keys[pygame.K_UP] and self.rect.top > 0:
            self.rect.y -= self.velocidade
        if keys[pygame.K_DOWN] and self.rect.bottom < ALTURA:
            self.rect.y += self.velocidade

# Função para exibir o tempo restante
def exibir_tempo(tempo):
    fonte = pygame.font.SysFont(None, 48)
    texto = fonte.render(f'Tempo: {tempo:.1f}s', True, BRANCO)
    screen.blit(texto, (10, 10))

# Função principal do jogo
def game():
    # Criar a galinha
    galinha = Galinha()
    todos_sprites = pygame.sprite.Group()
    todos_sprites.add(galinha)

    # Timer
    tempo_inicial = time.time()

    # Loop principal do jogo
    rodando = True
    while rodando:
        screen.fill(CINZA)

        # Calcular o tempo restante
        tempo_passado = time.time() - tempo_inicial
        tempo_restante = 10 - tempo_passado

        # Verificar se o tempo acabou ou a galinha atingiu o outro lado
        if tempo_restante <= 0:
            rodando = False
            resultado = 'Perdeu! Tempo esgotado!'
        elif galinha.rect.top <= 0:
            rodando = False
            resultado = 'Venceu! A galinha atravessou!'

        # Desenhar a estrada (simples)
        pygame.draw.rect(screen, CINZA, (0, 0, LARGURA, ALTURA))
        pygame.draw.rect(screen, PRETO, (0, ALTURA // 2, LARGURA, 10))

        # Atualizar todos os sprites
        todos_sprites.update()

        # Exibir o tempo
        exibir_tempo(tempo_restante)

        # Exibir a galinha
        todos_sprites.draw(screen)

        # Atualizar a tela
        pygame.display.update()

        # Checar eventos (ex. pressionamento de teclas)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False

        # Limitar os quadros por segundo
        clock.tick(60)

    # Exibir o resultado
    screen.fill(CINZA)
    fonte = pygame.font.SysFont(None, 72)
    texto = fonte.render(resultado, True, BRANCO)
    screen.blit(texto, (LARGURA // 4, ALTURA // 3))
    pygame.display.update()
    pygame.time.wait(3000)

# Iniciar o jogo
game()

# Finalizar o Pygame
pygame.quit()
