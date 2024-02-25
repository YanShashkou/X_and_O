import pygame

pygame.init()
screen = pygame.display.set_mode((360,360))
screen.fill('White')
pygame.display.set_caption("X and O")
X= pygame.image.load("X-removebg-preview.png")
O = pygame.image.load("O-removebg-preview.png")
bg = pygame.image.load("png-transparent-tic-tac-toe-bitmap-computer-icons-bmp-file-format-others-angle-furniture-symmetry-thumbnail-removebg-preview.png")
running=True
last_player = 'O'
field = {
    1: None,
    2: None,
    3: None,
    4: None,
    5: None,
    6: None,
    7: None,
    8: None,
    9: None
}



while running:
    pygame.display.update()
    screen.blit(bg,(0,0))


    def select(cord):
        if cord[0] < 120:
            if cord[1] < 120:
                return (15, 20)
            elif 240 > cord[1] > 120:
                return (15, 135)
            elif cord[1] > 240:
                return (15, 250)
        elif 240 > cord[0] > 120:
            if cord[1] < 120:
                return (130, 20)
            elif 240 > cord[1] > 120:
                return (130, 135)
            elif cord[1] > 240:
                return (130, 250)
        else:
            if cord[1] < 120:
                return (250, 20)
            elif 240 > cord[1] > 120:
                return (250, 135)
            elif cord[1] > 240:
                return (250, 250)

        #     return (15,20)
        # elif cord[0] > 120 < 240 and cord[1] < 120:
        #     return (130,20)
    def add(player, cord):
        if cord[0] < 120:
            if cord[1] < 120:
                if field[1] != None:
                    raise 'Field is already filled'
                field[1] = player
            elif 240 > cord[1] > 120:
                if field[4] != None:
                    raise 'Field is already filled'
                field[4] = player
            elif cord[1] > 240:
                if field[7] != None:
                    raise 'Field is already filled'
                field[7] = player
        elif 240 > cord[0] > 120:
            if cord[1] < 120:
                if field[2] != None:
                    raise 'Field is already filled'
                field[2] = player
            elif 240 > cord[1] > 120:
                if field[5] != None:
                    raise 'Field is already filled'
                field[5] = player
            elif cord[1] > 240:
                if field[8] != None:
                    raise 'Field is already filled'
                field[8] = player
        else:
            if cord[1] < 120:
                if field[3] != None:
                    raise 'Field is already filled'
                field[3] = player
            elif 240 > cord[1] > 120:
                if field[6] != None:
                    raise 'Field is already filled'
                field[6] = player
            elif cord[1] > 240:
                if field[9] != None:
                    raise 'Field is already filled'
                field[9] = player
    def check():
        global running
        if field[1] and field[2] and field[3] and field[1] == field[1] and field[2] == field[1] and field[3] == field[
            1]:
            print(f'Win {last_player}1')
            pygame.draw.line(bg, 'Red', (20, 50), (330, 50), 20)
        elif field[4] and field[5] and field[6] and field[4] == field[4] and field[5] == field[4] and field[6] == field[
            4]:
            print(f'Win {last_player}2')
            pygame.draw.line(bg, 'Red', (20, 170), (330, 170), 20)
        elif field[7] and field[8] and field[9] and field[7] == field[7] and field[8] == field[7] and field[9] == field[
            7]:
            print(f'Win {last_player}3')
            pygame.draw.line(bg, 'Red', (20, 290), (330, 290), 20)
        elif field[1] and field[4] and field[7] and field[1] == field[1] and field[4] == field[1] and field[7] == field[
            1]:
            print(f'Win {last_player}4')
            pygame.draw.line(bg, 'Red', (70, 20), (70, 330), 20)
        elif field[2] and field[5] and field[8] and field[2] == field[2] and field[5] == field[2] and field[8] == field[2]:
            print(f'Win {last_player}5')
            pygame.draw.line(bg, 'Red', (180, 20), (180, 330), 20)
        elif field[3] and field[6] and field[9] and field[3] == field[3] and field[6] == field[3] and field[9] == field[
            3]:
            print(f'Win {last_player}6')
            pygame.draw.line(bg, 'Red', (300, 20), (300, 330), 20)
        elif field[1] and field[5] and field[9] and field[1] == field[1] and field[5] == field[1] and field[9] == field[
            1]:
            print(f'Win {last_player}7')
            pygame.draw.line(bg, 'Red', (50, 50), (300, 300), 20)
        elif field[3] and field[5] and field[7] and field[3] == field[3] and field[5] == field[3] and field[7] == field[
            3]:
            pygame.draw.line(bg, 'Red', (330, 40), (50, 320), 20)


    def draw(cord):
        global last_player
        if last_player == "O":
            last_player = "X"
            try:
                add(last_player, cord)
                screen.blit(X, cord)
            except:
                print("select another one")
        else:
            last_player = "O"
            try:
                add(last_player, cord)
                screen.blit(O, cord)
            except:
                print("select another one")

    for event in pygame.event.get():

        if event.type == pygame.MOUSEBUTTONDOWN:
            draw(select(event.pos))
            print(field)
            check()
        if event.type == pygame.QUIT:
            pygame.quit()
            running=False