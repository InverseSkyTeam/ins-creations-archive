from CEF4pygame import CEFpygame,pygame
browser=CEFpygame(
    URL='https://code.xueersi.com/',
    VIEWPORT_SIZE=(800,500)
)


pygame.init()
display_width = 900
display_height = 600
display = pygame.display.set_mode((display_width,display_height))
run=1
clock = pygame.time.Clock()
while run:
    FPS = str(round(clock.get_fps()))
    pygame.display.set_caption('fps:' + FPS)
    events=pygame.event.get()
    pygame.key.set_repeat(500,100)
    keys=pygame.key.get_pressed()
    alt_pressed=keys[1073742050]
    ctrl_pressed=keys[1073742048]
    shift_pressed=keys[pygame.K_LSHIFT]
    for event in events:
        if event.type == pygame.QUIT:
            run=0
        if event.type == pygame.MOUSEMOTION:
            browser.motion_at(event.pos[0]-50,event.pos[1]-70,alt=alt_pressed,shift=shift_pressed,control=ctrl_pressed)
        if event.type == pygame.MOUSEBUTTONDOWN:
            browser.mousedown_at(event.pos[0]-50,event.pos[1]-70,event.button,alt=alt_pressed,shift=shift_pressed,control=ctrl_pressed)
        if event.type == pygame.MOUSEBUTTONUP:
            browser.mouseup_at(event.pos[0]-50,event.pos[1]-70,event.button,alt=alt_pressed,shift=shift_pressed,control=ctrl_pressed)
        if event.type == pygame.KEYDOWN:
            browser.keydown(event.key,alt=alt_pressed,shift=shift_pressed,control=ctrl_pressed)
        if event.type == pygame.KEYUP:
            browser.keyup(event.key,alt=alt_pressed,shift=shift_pressed,control=ctrl_pressed)
    display.blit(browser.image, (50,70))
    pygame.display.update()
    clock.tick(114514)
    
