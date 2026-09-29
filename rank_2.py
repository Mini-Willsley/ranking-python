import random, pygame, sys

# gather user input when sorting
def inp():
    while True:
        events = pygame.event.get()
        for i in range(len(events)):
            # terminate sorting if window closed
            if events[i].type == pygame.QUIT:
                print("Sorting Terminated.")
                pygame.display.quit()
                pygame.quit()
                sys.exit()

            # only return x coord as program only needs left or right
            if events[i].type == pygame.MOUSEBUTTONDOWN:
                eventx = events[i].pos[0]
                return eventx

# display items on screen
def display(left, right):
    text = pygame.Surface((250, 500))

    for val in ((left, 0), (right, 250)):
        text.fill((200, 200, 200))
        drawtextcentre(str(val[0]), text, [2, 2])
        screen.blit(text, (val[1], 0))
    
    pygame.display.update()

# draw text onto surface
def drawtextcentre(displaytext, blitsurf, positionscalars):
    font = "freesansbold.ttf"
    fontsize = 20
    colour = (40, 40, 40)

    # create rendered text for each individual word
    words = displaytext.split()
    for i in range(len(words)):
        words[i] = pygame.font.Font(font, fontsize).render(" " + words[i] + " ", True, colour)

    line = []
    lines = []
    linetotal = 0
    linetotals = []
    lineheight = words[0].height
    blitsurfrect = blitsurf.get_rect()

    # create lines of words based on length of each word
    for word in words:
        if linetotal + word.get_rect().width < (blitsurfrect.width // 2):
            linetotal += word.get_rect().width
            line.append(word)
        else:
            linetotals.append(linetotal)
            linetotal = word.get_rect().width
            lines.append(line)
            line = [word]

    # cleanup single words and ending lines from above loop
    if not lines:
        linetotals.append(linetotal)
        lines.append(line)
    elif line != lines[-1]:
        linetotals.append(linetotal)
        lines.append(line)

    textsurf = pygame.Surface((max(linetotals), lineheight * len(lines)))
    textsurf.fill((200, 200, 200))

    # add each word to line and add each line to surface
    for i in range(len(lines)):
        offset = 0
        linesurf = pygame.Surface((linetotals[i], lineheight))
        linesurf.fill((200, 200, 200))
        for j in range(len(lines[i])):
            linesurf.blit(lines[i][j], (offset, 0))
            offset += lines[i][j].width
        textsurf.blit(linesurf, (textsurf.get_rect().width // 2 - linesurf.get_rect().centerx, lineheight * i))

    # add text onto surface
    textsurfrect = textsurf.get_rect()
    blitsurf.blit(textsurf, (((blitsurfrect.width // 4) * positionscalars[0]) - textsurfrect.centerx, ((blitsurfrect.height // 4) * positionscalars[1]) - textsurfrect.centery))

# move the items (modified binary search)
def insertitem(lis, item):
    high, low = len(lis), 0
    while high > low:
        mid = (high + low) // 2
        display(item, lis[mid])
        x = inp()
        if x >= 250:
            high = mid
        else:
            low = mid + 1
    lis.insert(high, item)
    return lis

# list to be sorted (insert list here)
lis = ["A", "B", "C", "D", "E", "F"]

# create window
pygame.init()
screen = pygame.display.set_mode((500, 500))

# sort the items 
random.shuffle(lis)
sort = [lis[0]]
for i in range(1, len(lis)):
    sort = insertitem(sort, lis[i])
sort = reversed(sort)

# close window after sort
pygame.display.quit()
pygame.quit()

# output sorted list
print("Sorting Complete.\nOutcome:")
for item in sort:
    print(item)
