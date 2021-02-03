# Snake-Game

A replica of the very famous and interesting Nokia's "SNAKE GAME".

Python's turtle graphics plays the role of both the snake and the food object.

As the file names suggest, snake.py deals with creating snake, extending the length of snake when it swallows food, and snake movements when the player presses the arrow keys on his keyboard.
A screen listener listens to all the keypresses, and responds to the arrow keys to move the snake.

food.py deals with giving random positions to the food object (again a turtle graphics object).

scoreboard.py keeps track of the current player score, increases score when food is swallowed, and also deals with displaying messages like "Score: " and also the "GAME OVER" message.

The basic logic behind the entire code is to create 3 turtle objects in the starting (in the shape of a square), and bind them together to give the impression of a rectangle (depicted as snake in the game). As the snake keeps swallowing food, new turtle objects keep getting created, and get appended to the snake tail.

To keep the animation smooth, turtle.tracer() and turtle.update() were used. The animation of snake moving is not shown in real-time. Instead, the screen is refreshed every 0.1 seconds, and the changes are reflected then.

To make the snake move, the logic incorporated is that "nth square comes at (n-1)th's position, and so on. This way only the first square is moved. 2nd square comes at 1st's place, 3rd comes on 2nd's place and so on. This logic is used in the entire main.py file.
