# Snake Game First Version
* It was an early project made for understanding how the PyGame module worked.
<img src="https://user-images.githubusercontent.com/68196837/223507904-daa8ebe7-54c6-43af-9795-13c0cf3e7054.png" width="400">

>The starting structure of the game.

<img src="https://user-images.githubusercontent.com/68196837/223509270-c3b56175-5d7d-4c35-84f8-93dcc6efee56.png" width="400">

>Ingame screenshot

#### Additional Notes For Future Updates
* Might have been better if there was a high score system
* The snake's head doesn't have a directional movement information such as eyes or a face
* When the body becomes larger the tail gets mixed with the other yellow squares and movement can't be predicted.

# Snake Game Update (15.03.2023)
With small changes in the code the snake's head has a darker color and there is now an indicator for the high score. The general mechanic wasn't changed and the movement of the snake seems laggy even if it isn't. I think it's about the display method I used when I first created the project. The snake is made out of boxes and when the snake moves one box of space, every box moves to where the previous box was (in other words: the end of the tail moves where the previous tail part was and this process is continued until it reaches the head). And after this movement process is done, the snake is displayed as if it is a single frame. I used a single yellow square for every part of the snake, The animation quality can be improvised by adding more than one interconnected circles as a single tail part which whould do the exact same thing as the squares where doing but with more frames.

<img src="https://user-images.githubusercontent.com/68196837/225385557-e8d713a3-91a0-4c22-80a9-e687352576e9.png" width="400">

>Ingame screenshot
