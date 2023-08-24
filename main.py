from tkinter import *
import random
import time

class Ball:
    def __init__(self, canvas, paddle):
        self.canvas = canvas
        self.p = paddle
        self.x = random.randint(0, self.canvas.winfo_width())
        self.y = random.randint(0, 10)
        self.ball = self.canvas.create_oval(self.x, self.y, self.x + 15, self.y + 15, fill='#B500DA')
        self.start_x = random.randint(1, 3)
        self.start_y = random.randint(1, 2)
        self.points = 0

    def bounce(self):
        self.canvas.move(self.ball, self.start_x, self.start_y)
        coords = self.canvas.coords(self.ball)
        if -3 <= coords[0] <= 1:
            self.start_x = random.randint(1, 3)
        elif -3 <= coords[1] <= 1:
            self.start_y = random.randint(1, 3)
        elif 499 <= coords[2] <= 503:
            self.start_x = -(random.randint(1, 3))
        elif 499 <= coords[3] <= 503:
            self.start_y = -(random.randint(1, 3))
        elif self.hit_paddle() == True:
            self.start_y = -(random.randint(1, 3))
            self.points += 1

    def hit_bottom(self):
        coords = self.canvas.coords(self.ball)
        if coords[3] >= 480:
            return True
        else:
            return False

    def hit_paddle(self):
        paddle_coords = self.canvas.coords(self.p.paddle)
        coords = self.canvas.coords(self.ball)
        if paddle_coords[0] <= coords[0] <= paddle_coords[2] and paddle_coords[0] <= coords[2] <= paddle_coords[2]:
            if paddle_coords[1] + 2 <= coords[3] <= paddle_coords[3] - 2:
                return True
        return False


class Paddle:
    def __init__(self, canvas):
        self.canvas = canvas
        self.paddle = self.canvas.create_rectangle(10, 370, 80, 380, fill='green')
        self.x = 0
        self.canvas.bind('<Key>', self.control)

    def move(self):
        self.canvas.move(self.paddle, self.x, 0)
        coords = self.canvas.coords(self.paddle)
        if 499 <= coords[2] <= 503:
            self.x = -2
        elif -3 <= coords[0] <= 1:
            self.x = 2

    def control(self, event):
        if event.keysym == 'Left':
            self.x = -2
        elif event.keysym == 'Right':
            self.x = 2




tk = Tk()
tk.title('Game')
tk.resizable(False, False)
tk.wm_attributes('-topmost', 1)
tk.config(bg='#EEE5B1')

canvas = Canvas(tk, width=500, height=500, bg='#EEE5B1')
canvas.focus_set()
canvas.pack()
canvas.update()

tk.update()

paddle = Paddle(canvas)
ball = Ball(canvas, paddle)

while True:
    def start(event):
        point = canvas.create_text(490, 20, text=f'{ball.points}', fill='green', font=('Helvetica 15 bold'))
        while True:
            if not ball.hit_bottom():
                ball.bounce()
                paddle.move()
                canvas.itemconfig(point, text=f'{ball.points}')
            else:
                time.sleep(1)
                text = canvas.create_text(255, 150, text='You lost!', fill='green', font=('Helvetica 20 bold'))
            tk.update_idletasks()
            tk.update()
            time.sleep(0.01)


    canvas.bind('<space>', start)
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)

# canvas.create_text(250, 25, text='Welcome to the game!', fill='green', font=('Helvetica 15 bold'))
# canvas.create_text(250, 55, text='Choose the level', fill='green', font=('Helvetica 15 bold'))
# b1 = Button(text='Easy level', command=easy)
# b1.pack()
# b2 = Button(text='Medium level')
# b2.pack()
# b3 = Button(text='Hard level')
# b3.pack()
# tk.mainloop()
