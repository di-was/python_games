from tkinter import *
import pygame
import time
from PIL import ImageTk, Image

pygame.init()

# global
withcomputer = False
withperson = False


# main function
def main_tkinter():
    global withcomputer
    global withperson

    screen = Tk()
    # screen Title
    screen.title("Home Page")
    screen.geometry("700x500")

    # Blueprint for class
    class Buttons(Button):
        def __init__(self, screen, **whatever):
            Button.__init__(self, master=screen, **whatever)
            self.defaultFontcolor = self["fg"]
            self.defaultBorwid = self['borderwidth']
            self.defaultFont = self["font"]
            self.bind("<Enter>", self.on_touch)
            self.bind("<Leave>", self.off_touch)

        def on_touch(self, event):
            self['fg'] = 'orange'
            self['font'] = 'Helvetica 25 bold italic'
            self['borderwidth'] = 0

        def off_touch(self, event):
            self['fg'] = self.defaultFontcolor
            self['font'] = 'Helvetica 20 bold italic'
            self['borderwidth'] = self.defaultBorwid

    # Background image, flag
    background_image = ImageTk.PhotoImage(file=r'background.png')
    background_label = Label(screen, image=background_image)
    flag_image = ImageTk.PhotoImage(file=r'frame.png')
    flag_label = Label(screen, image=flag_image)

    flag_label.grid(row=0, column=0)
    background_label.place(relwidth=1.5, relheight=1)

    # Button commands
    def close():
        screen.destroy()

    def with_computer():
        global withcomputer
        withcomputer = True
        screen.destroy()

    def with_person():
        global withperson
        withperson = True
        screen.destroy()

    # Buttons
    Start_computer = Buttons(screen, text='1) Computer', font='Helvetica 20 bold italic', borderwidth=0,
                             command=with_computer)
    Start_Duo = Buttons(screen, text='2) Person', font='Helvetica 20 bold italic', borderwidth=0,
                        command=with_person)
    Source_code = Buttons(screen, text='3) Source Code', font='Helvetica 20 bold italic', borderwidth=0)
    Exit = Buttons(screen, text="4) Exit", font='Helvetica 20 bold italic', borderwidth=0,
                   command=close)

    # show buttons
    Start_computer.grid(row=1, column=0)
    Start_Duo.grid(row=2, column=0)
    Source_code.grid(row=3, column=0)

    Exit.grid(row=4, column=0)

    # mainloop
    screen.mainloop()


if __name__ == "__main__":
    main_tkinter()

font = pygame.font.SysFont(None, 40)


def display_message(mess, color):
    screen_text = font.render(mess, True, color)
    window.blit(screen_text, [250, 640])


def draw_final_line(x_first, x_second, y_first, y_second, width):
    pygame.draw.line(window, (255, 0, 0), (x_first, x_second), (y_first, y_second), width)

# activate person mode

x = pygame.image.load("x.png")
o = pygame.image.load("0.png")
first_letter = x
one = False
two = False
three = False

four = False
five = False
six = False

seven = False
eight = False
nine = False

one_letter = 1
two_letter = 2
three_letter = 3
four_letter = 4
five_letter = 5
six_letter = 6
seven_letter = 7
eight_letter = 8
nine_letter = 9
occupied = []

first_row_win = False
second_row_win = False
third_row_win = False

first_column_win = False
second_column_win = False
third_column_win = False

first_diagonal_win = False
second_diagonal_win = False

if withperson is True:
    window = pygame.display.set_mode((600, 700))
    pygame.display.set_caption("Tic Tac Toe")

    Running = True

    while Running is True:
        window.fill((255, 255, 255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Running = False
            if event.type == pygame.MOUSEBUTTONDOWN:

                if pygame.mouse.get_pressed()[0]:
                    get_position = pygame.mouse.get_pos()
                    position = get_position[0] // 200, get_position[1] // 200

                    # change turn
                    if position not in occupied:
                        if first_letter == x:
                            first_letter = o
                        elif first_letter == o:
                            first_letter = x

                    if one is False:
                        if position == (0, 0):
                            one = True
                            one_letter = first_letter
                            occupied.append((0, 0))

                    if two is False:
                        if position == (1, 0):
                            two = True
                            two_letter = first_letter
                            occupied.append((1, 0))

                    if three is False:
                        if position == (2, 0):
                            three = True
                            three_letter = first_letter
                            occupied.append((2, 0))

                    if four is False:
                        if position == (0, 1):
                            four = True
                            four_letter = first_letter
                            occupied.append((0, 1))

                    if five is False:
                        if position == (1, 1):
                            five = True
                            five_letter = first_letter
                            occupied.append((1, 1))

                    if six is False:
                        if position == (2, 1):
                            six = True
                            six_letter = first_letter
                            occupied.append((2, 1))

                    if seven is False:
                        if position == (0, 2):
                            seven = True
                            seven_letter = first_letter
                            occupied.append((0, 2))

                    if eight is False:
                        if position == (1, 2):
                            eight = True
                            eight_letter = first_letter
                            occupied.append((1, 2))

                    if nine is False:
                        if position == (2, 2):
                            nine = True
                            nine_letter = first_letter
                            occupied.append((2, 2))

                    #  row wins
                    if one_letter == two_letter == three_letter:  # 1
                        first_row_win = True

                    if four_letter == five_letter == six_letter:  # 2
                        second_row_win = True

                    if seven_letter == eight_letter == nine_letter:  # 3
                        third_row_win = True

                    # column wins
                    if one_letter == four_letter == seven_letter:
                        first_column_win = True

                    if two_letter == five_letter == eight_letter:
                        second_column_win = True

                    if three_letter == six_letter == nine_letter:
                        third_column_win = True

                    # diagonal wins
                    if one_letter == five_letter == nine_letter:
                        first_diagonal_win = True

                    if three_letter == five_letter == seven_letter:
                        second_diagonal_win = True

        # design of the board
        pygame.draw.line(window, (0, 0, 0), (200, 0), (200, 600), 7)
        pygame.draw.line(window, (0, 0, 0), (400, 0), (400, 600), 7)

        pygame.draw.line(window, (0, 0, 0), (0, 200), (600, 200), 7)
        pygame.draw.line(window, (0, 0, 0), (0, 400), (600, 400), 7)

        pygame.draw.rect(window, (0, 0, 0), (0, 602, 600, 100))

        if one is True:
            window.blit(one_letter, (25, 25))

        if two is True:
            window.blit(two_letter, (225, 25))

        if three is True:
            window.blit(three_letter, (425, 25))

        if four is True:
            window.blit(four_letter, (25, 225))

        if five is True:
            window.blit(five_letter, (225, 225))

        if six is True:
            window.blit(six_letter, (425, 225))

        if seven is True:
            window.blit(seven_letter, (25, 425))

        if eight is True:
            window.blit(eight_letter, (225, 425))

        if nine is True:
            window.blit(nine_letter, (425, 425))

        if first_letter == x:
            display_message("o's turn", (255, 255, 255))

        elif first_letter == o:
            display_message("x's turn", (255, 255, 255))

        if first_row_win is True:
            draw_final_line(0, 100, 700, 100, 4)
            Running = False

        if second_row_win is True:
            draw_final_line(0, 275, 700, 275, 4)
            Running = False

        if third_row_win is True:
            draw_final_line(0, 475, 700, 475, 4)
            Running = False

        if first_column_win is True:
            draw_final_line(100, 0, 100, 600, 4)
            Running = False

        if second_column_win is True:
            draw_final_line(300, 0, 300, 600, 4)
            Running = False

        if third_column_win is True:
            draw_final_line(500, 0, 500, 600, 4)
            Running = False

        if first_diagonal_win is True:
            draw_final_line(0, 0, 700, 650, 4)
            Running = False

        if second_diagonal_win is True:
            draw_final_line(0, 600, 650, 0, 4)
            Running = False

        if one is True and two is True and three is True and four is True and five is True and six is True and seven is True and eight is True and nine is True:
            Running = False

        pygame.display.update()

time.sleep(1)