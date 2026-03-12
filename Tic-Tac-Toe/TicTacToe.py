import tkinter as tk
from tkinter import messagebox

class TicTacToe():
    def __init__(self, master):
        #init the GUI Screen
        self.master = master
        master.title('Tic Tac Toe')

        #Player 1
        self.current_player = 0

        #create the buttons for the game
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        
        for row in range(3):
            for col in range(3):
                btn = tk.Button(master, text="", font=('Arial', 60), height=2, width=5, command=lambda r=row, c=col: self.click(r, c))
                btn.grid(row=row, column=col)
                self.buttons[row][col] = btn


    '''
    handle the clicks on the buttons
    r: row of the button
    c: column of the button
    '''
    def click(self, r, c):
        btn = self.buttons[r][c]
        if btn['text'] == '':
            btn.config(state=tk.DISABLED)
            if self.current_player == 0:
                btn.config(text='X', disabledforeground='blue')
            else:
                btn.config(text = 'O', disabledforeground='red')
            
            is_win_case = self.check_win()
            
            if is_win_case:
                messagebox.showinfo("Game's Over", f"Winner!! player {self.current_player+1} wins")
                self.reset_game()
            elif all(self.buttons[i][j]['text'] != '' for i in range(3) for j in range(3)) :
                messagebox.showinfo("Game's over", "Tie!!, No Winner")
                self.reset_game() 
            else: 
                self.current_player ^= 1 


    '''
    check win cases: the same value in full row/full column / full diagonal
    return true if any win case occurs
    '''
    def check_win(self):
        if (self.buttons[0][0]['text'] == self.buttons[1][1]['text']  == self.buttons[2][2]['text'] != '' or 
            self.buttons[0][2]['text'] == self.buttons[1][1]['text'] == self.buttons[2][0]['text'] != ''):
            return True
        else:
            for i in range(3):
                if(self.buttons[i][0]['text'] == self.buttons[i][1]['text'] == self.buttons[i][2]['text'] != '' or 
                   self.buttons[0][i]['text'] == self.buttons[1][i]['text'] == self.buttons[2][i]['text'] != ''):
                    return True
        return False

    def reset_game(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(state=tk.NORMAL, text='')
        self.current_player = 0