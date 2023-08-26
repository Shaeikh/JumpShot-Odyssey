# Stylish PyGame GUI

![PyGame GUI Image 1](https://github.com/Shaeikh/JumpShot-Odyssey/assets/51645154/a0690710-6199-4d0a-a961-3b2f1cfff5c4)
![PyGame GUI Image 2](https://github.com/Shaeikh/JumpShot-Odyssey/assets/51645154/1e74cab0-5e63-4b03-b77f-928d230a9a32)
![PyGame GUI Image 3](https://github.com/Shaeikh/JumpShot-Odyssey/assets/51645154/975faf8e-31d5-47ee-8ceb-14724cc87fd1)
![PyGame GUI Image 4](https://github.com/Shaeikh/JumpShot-Odyssey/assets/51645154/20fe6ae4-93ba-48b1-9fa0-c8b6da4c21fc)




Enhance your PyGame projects with the Stylish PyGame GUI. This GUI includes buttons, sliders, background soundtracks, smooth screen transitions, and more, all designed to elevate your user's experience.

## Features

- **Handler:** A most common and easy-to-use handler for the code
- **Buttons:** Stylish buttons with animations for seamless user interaction.
- **Sliders:** Dynamic sliders for settings like volume or brightness. > [!NOTE]
> These sliders are modified version of https://github.com/pygame-examples/pygame-examples/blob/main/pgex/examples/horizontal_slider/main.py .
- **Background Soundtrack:** Add ambiance with an integrated background soundtrack.
- **Smooth Transitions:** Effortlessly transition between screens or levels.
- **Interactive:** Engage users with interactive elements and animations.
- **Themes:** Customize themes to match your game's aesthetics.

## Getting Started

1. **Installation:** Ensure Python and PyGame are installed.
```shell
pip install pygame
2. **Download:** Clone or download the the repo.
```shell
git clone https://github.com/Shaeikh/JumpShot-Odyssey
```
3. **Integration:** Import modules and customize elements.
4. **Usage:** Create buttons, sliders, screens, and handle interactions.

# Buttons
```py
# This is a basic button, for all params check the file
button = Button(
    pygame.Rect(x, y, width, height),
    "Button title",
    button_color,
    hover_color,
    text_color,
    font,
    border_radius, # Radius of button border 
    label="Label" # Optional, this will be displayed beside the button
)
```

# Slider
```py
sound_effects_slider = Slider(
        rect,
        step=1, # Value which will be added or removed each time the slider is moved
        callback=lambda val: function(), # This returns the value of the slider 
        slider_color=color,
        color=color,
    )
```


