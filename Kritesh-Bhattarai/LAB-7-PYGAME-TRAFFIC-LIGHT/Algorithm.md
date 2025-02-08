# Algorithm for Traffic Light Simulation using Pygame

1. **Initialize Pygame:**
    - Import the `pygame` module.
    - Initialize Pygame using `pygame.init()`.

2. **Set up the display:**
    - Create a display window with dimensions 800x800 using `pygame.display.set_mode((800, 800))`.
    - Set the window caption to "Traffic Light" using `pygame.display.set_caption("Traffic Light")`.

3. **Define colors:**
    - Define color constants for GREY, BLACK, RED, GREEN, YELLOW, and WHITE.

4. **Main loop:**
    - Create a `running` variable and set it to `True`.
    - Start a `while` loop that runs as long as `running` is `True`.

5. **Event handling:**
    - Inside the loop, check for events using `pygame.event.get()`.
    - If the event type is `pygame.QUIT`, set `running` to `False` to exit the loop.

6. **Drawing the traffic light:**
    - Fill the screen with the WHITE color using `screen.fill(WHITE)`.
    - Draw the traffic light structure:
      - Draw a grey rectangle for the traffic light pole using `pygame.draw.rect(screen, GREY, (250, 50, 300, 700))`.
      - Draw a black rectangle for the traffic light box using `pygame.draw.rect(screen, BLACK, (300, 100, 200, 600))`.

7. **Traffic light logic:**
    - Get the current time in milliseconds using `pygame.time.get_ticks()`.
    - Use the modulo operator to determine which light to display based on the current time:
      - If `current_time % 3000 < 1000`, draw a red circle using `pygame.draw.circle(screen, RED, (400, 200), 80)`.
      - If `current_time % 3000 < 2000`, draw a yellow circle using `pygame.draw.circle(screen, YELLOW, (400, 400), 80)`.
      - Otherwise, draw a green circle using `pygame.draw.circle(screen, GREEN, (400, 600), 80)`.

8. **Update the display:**
    - Update the display using `pygame.display.update()`.

9. **Quit Pygame:**
    - After exiting the loop, quit Pygame using `pygame.quit()`.
