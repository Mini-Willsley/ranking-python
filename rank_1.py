import random, pygame

def inp():
    while True:
        events = pygame.event.get()
        for i in range(len(events)):
            if events[i].type == pygame.MOUSEBUTTONDOWN:
                eventx = events[i].pos[0]
                return eventx

def display(one, two):
    text = pygame.Surface((250, 500))
    drawtextcentre("freesansbold.ttf", 20, str(one), (255, 255, 255), text, [2, 2])
    screen.blit(text, (0, 0))
    text = pygame.Surface((250, 500))
    drawtextcentre("freesansbold.ttf", 20, str(two), (255, 255, 255), text, [2, 2])
    screen.blit(text, (250, 0))
    pygame.display.update()

def drawtextcentre(font, fontsize, displaytext, colour, blitsurf, positionscalers):
    words = pygame.font.Font(font, fontsize).render(displaytext, True, colour) 
    wordsrect = words.get_rect()
    blitsurfrect = blitsurf.get_rect()
    blitsurf.blit(words, (((blitsurfrect.width // 4) * positionscalers[0]) - wordsrect.centerx, ((blitsurfrect.height // 4) * positionscalers[1]) - wordsrect.centery))

def insertSong(lis, song):
    high, low = len(lis), 0
    while high > low:
        mid = (high + low) // 2
        display(song, lis[mid])
        x = inp()
        if x >= 250:
            high = mid
        else:
            low = mid + 1
    lis.insert(high, song)
    return lis

lis = ["a", "b", "c", "d", "e", "f"]

pygame.init()
screen = pygame.display.set_mode((500, 500))
screen.fill((255, 0, 0))

random.shuffle(lis)
sort = [lis[0]]
for i in range(1, len(lis)):
    sort = insertSong(sort, lis[i])
sort = reversed(sort)

for item in sort:
    print(item)
