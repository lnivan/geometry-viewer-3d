from render3D import *
from vectors import *


window_size = (800, 800)

pygame.init()
window = pygame.display.set_mode((window_size))

render3D = Render3D(window, Vector2(300, 200), Vector2(400, 400))



running = True
while running == True:

    events = pygame.event.get()
    for event in events:

        if event.type == pygame.QUIT:
            running = False

    render3D.update(events)


    window.fill((100, 100, 100))
    render3D.refresh()
    render3D.draw_point(Vector3(10, 10, 5))
    render3D.draw_point(Vector3(20, 10, 5))
    render3D.draw_point(Vector3(10, 10, -5))
    render3D.draw_point(Vector3(20, 10, -5))    
    render3D.draw_point(Vector3(10, -10, 5))
    render3D.draw_point(Vector3(20, -10, 5))
    render3D.draw_point(Vector3(10, -10, -5))
    render3D.draw_point(Vector3(20, -10, -5))
    
    pygame.display.flip()
