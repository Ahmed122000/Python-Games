import tkinter as tk
import random

#-----configuration----------
CELL_SIZE=28        #pixel size of one grid cell
GRID_WIDTH=30       #number of cells horizontally
GRID_HEIGHT=20      #number of cells vertically
INITIAL_SPEED=150   #milliseconds between moves(the lower the faster)
SPEED_INCREMENT=5   #decrease in ms per food eaten (speed up)


class SnakeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Snake Game")
        self.width_px = CELL_SIZE*GRID_WIDTH
        self.height_px = CELL_SIZE*GRID_HEIGHT
        self.canvas = tk.Canvas(root, width=self.width_px, height=self.height_px, bg='black')
        self.canvas.pack()

        self.score_var = tk.StringVar()
        self.score_var.set("Score: 0")
        self.score_label = tk.Label(root, textvariable=self.score_var, font=("arial",14))
        self.score_label.pack(anchor='w', padx=6, pady=6)

        self.running = True
        self.game_over = False
        self.after_id = None

        self.reset_game()
        self.bind_keys()
        self.game_loop()


    def reset_game(self):
        self.direction = 'right'                #initial direction for the snake
        self.snake = [(5, 5), (4, 3), (3, 5)]   #snake --> list of cells
        self.spwan_food()                       #create the food for the snake
        self.score=0                            #initial score
        self.speed = INITIAL_SPEED              #initial speed for the snake
        self.game_over = False                  #the game is done
        self.draw_all()                         #draw all the elements for the game

    def bind_keys(self):
        self.root.bind("<Up>",      lambda e:self.change_dir("up"))
        self.root.bind("<Down>",    lambda e:self.change_dir("down"))
        self.root.bind("<Right>",   lambda e:self.change_dir("right"))
        self.root.bind("<Left>",    lambda e:self.change_dir("left"))
        self.root.bind("w",         lambda e:self.change_dir("up"))
        self.root.bind("s",         lambda e:self.change_dir("down"))
        self.root.bind("d",         lambda e:self.change_dir("right"))
        self.root.bind("a",         lambda e:self.change_dir("left"))
        self.root.bind("R",         lambda e:self.restart())
        self.root.bind("r",         lambda e:self.restart())
        self.root.bind("<space>",   lambda e:self.toggle_pause())

    def restart(self):
        if self.game_over:
            self.canvas.delete("all")
            self.reset_game()
            self.running=True
            self.game_loop()
    
    def toggle_pause(self):
        self.running = not self.running
        if self.running and not self.game_over:
            self.game_loop()
        self.draw_all()

    def change_dir(self, new_dir):
        opposites = {"up":'down', 'down':'up', 'right':'left', 'left':'right'}
        if opposites.get(new_dir) == self.direction:
            return
        self.direction = new_dir

    def spwan_food(self):
        while True: 
            x = random.randint(0, GRID_WIDTH-1)
            y = random.randint(0, GRID_HEIGHT-1)
            if(x, y) not in self.snake:
                self.food = (x, y)
                break

    def game_loop(self):
        if not self.running:
            return 
        if self.game_over:
            return  

        self.move_snake()
        self.draw_all()
        self.after_id = self.root.after(self.speed, self.game_loop)

    
    def move_snake(self):
        head_x, head_y = self.snake[0]
        if self.direction == 'up':
            new_head = (head_x, head_y-1)
        elif self.direction == 'down':
            new_head = (head_x, head_y+1)
        elif self.direction == 'right':
            new_head = (head_x+1, head_y)
        else: #left
            new_head = (head_x-1 , head_y)


        x, y = new_head
        if x<0 or x>= GRID_WIDTH or y < 0 or y >= GRID_HEIGHT:
            self.end_game()
            return 

        if new_head in self.snake:
            self.end_game()
            return 
        
        self.snake.insert(0, new_head)

        if new_head == self.food:
            self.score += 1
            self.score_var.set(f"Score: {self.score}")
            if self.speed - SPEED_INCREMENT > 20:
                self.speed-= SPEED_INCREMENT
            self.spwan_food()
        else:
            self.snake.pop() #remove tail

    
    def end_game(self):
        self.game_over = True
        self.running = False
        self.draw_all()
        if self.after_id:
            try: 
                self.root.after_cancel(self.after_id)
            except Exception: 
                pass

    
    def draw_all(self):
        self.canvas.delete('all')
        fx, fy = self.food
        self.draw_cell(fx, fy, fill='red')

        for i, (x, y) in enumerate(self.snake):
            if i == 0: 
                self.draw_cell(x, y, fill='lime', outline='darkgreen')
            else:
                self.draw_cell(x, y, fill="green", outline='darkgreen')

        if not self.running and not self.game_over:
            self.canvas.create_text(self.width_px //2, self.height_px//2, 
                                    text="Game Paused (click space to resume)", 
                                    fill="white", font=("Arial", 20), justify='center')
        
        if self.game_over:
            self.canvas.create_text(self.width_px //2, self.height_px//2-20, 
                                    text="Game Over)", 
                                    fill="white", font=("Arial", 28, 'bold'), justify='center')
            self.canvas.create_text(self.width_px //2, self.height_px//2+20, 
                                    text=f"Score: {self.score}", 
                                    fill="white", font=("Arial", 16), justify='center')
            
    
    def draw_cell(self, grid_x, grid_y, fill='white', outline=""):
        x1 = grid_x * CELL_SIZE
        y1 = grid_y * CELL_SIZE
        x2 = x1 + CELL_SIZE
        y2 = y1 + CELL_SIZE

        self.canvas.create_rectangle(x1, y1, x2, y2, fill=fill, outline=outline)
