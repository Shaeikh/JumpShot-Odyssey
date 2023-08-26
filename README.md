# GUI

![image](https://github.com/Shaeikh/JumpShot-Odyssey/assets/51645154/9b848bae-9209-4225-b63b-1c49f3ade26d)

![image](https://github.com/Shaeikh/JumpShot-Odyssey/assets/51645154/bbef607d-5ecc-4530-b22e-032c1239a2bb)

![image](https://github.com/Shaeikh/JumpShot-Odyssey/assets/51645154/c9946ec4-1aa5-4245-a72b-f3570c454a8f)

![image](https://github.com/Shaeikh/JumpShot-Odyssey/assets/51645154/506212da-5490-40e0-808d-ef6ec807f676)


Enhance your PyGame projects with the Stylish PyGame GUI. This GUI includes buttons, sliders, background soundtracks, smooth screen transitions, and more, all designed to elevate your user's experience.

## Features

- **Handler:** A most common and easy-to-use handler for the code
- **Buttons:** Stylish buttons with animations for seamless user interaction.
- **Sliders:** Dynamic sliders for settings like volume or brightness.
> [!NOTE]
> These sliders are modified version of https://github.com/pygame-examples/pygame-examples/blob/main/pgex/examples/horizontal_slider/main.py .

- **Background Soundtrack:** Add ambiance with an integrated background soundtrack.
- **Smooth Transitions:** Effortlessly transition between screens or levels.
- **Interactive:** Engage users with interactive elements and animations.
- **Themes:** Customize themes to match your game's aesthetics.

## Getting Started

1. **Installation:** Ensure Python and PyGame are installed.
```shell
pip install pygame
```
2. **Download:** Clone or download the the repo.
```shell
git clone https://github.com/Shaeikh/JumpShot-Odyssey
```
3. **Integration:** Import modules and customize elements.
4. **Usage:** Create buttons, sliders, screens, and handle interactions.

## Buttons
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

### Slider
```py
slider = Slider(
        rect,
        step=1, # Value which will be added or removed each time the slider is moved
        callback=lambda val: function(), # This returns the value of the slider 
        slider_color=color,
        color=color,
    )
```

## Credits
Created by Shaeikh. Use, modify, and share with or without credit idc.

## License
This project is under the [MIT License](https://github.com/Shaeikh/JumpShot-Odyssey/blob/main/LICENSE).
