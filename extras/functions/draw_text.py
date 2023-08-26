def draw_text(screen, text, font, color, x, y, shadow=False, shadow_color=(0, 0, 0)):
    if shadow:
        
        text_obj = font.render(text, True, shadow_color)
        screen.blit(text_obj, (x + 2, y + 2))
    text_obj = font.render(text, True, color)
    screen.blit(text_obj, (x, y))