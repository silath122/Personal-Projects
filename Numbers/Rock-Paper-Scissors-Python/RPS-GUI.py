from button import Button
from graphics import *
from random import *

# Rock Paper Scissors GUI
# About: Outputs a game of Rock Paper Scissors between the user and computer.
#
# Author: Siah Thomas
# Data: 12/14/2022

def main():
    win = GraphWin('Rock Paper Scissors Shoe', 1000, 750)
    win.setCoords(0.0, 0.0, 10.0, 10.0)
    win.setBackground('LightBlue1')

    # draw rock option
    rock = Button(Rectangle(Point(1.0, 1.0), Point(2.0, 2.0)), 'Rock')
    rock.color_button('white')
    rock.draw(win)

    # draw paper option
    paper = Button(Rectangle(Point(2.25, 1.0), Point(3.25, 2.0)), 'Paper')
    paper.color_button('white')
    paper.draw(win)

    # draw scissors option
    scissors = Button(Rectangle(Point(3.5, 1.0), Point(4.5, 2.0)), 'Scissors')
    scissors.color_button('white')
    scissors.draw(win)

    # output box for user
    userOutputBox = Rectangle(Point(1.25, 3.0), Point(4.25, 6.0))
    userOutputBox.draw(win)
    userOutputBox.setFill('white')
    userOutputText = Text(Point(2.75, 4.5), 'Player 1')
    userOutputText.draw(win)

    # output box for computer
    cpOutputBox = Rectangle(Point(6.25, 3.0), Point(9.25, 6.0))
    cpOutputBox.draw(win)
    cpOutputBox.setFill('white')
    cpOutputText = Text(Point(7.75, 4.5), 'NPC')
    cpOutputText.draw(win)

    # game selection
    selectGameText = Text(Point(5.0, 8.5), 'Lets play Rock, Paper, Scissors! You\'re Player 1!')
    selectGameText.draw(win)

    # draw quit button
    quit_button = Button(Rectangle(Point(7.0, 8.5), Point(9.0, 9.5)), 'Quit')
    quit_button.draw(win)

    # win and lose text box
    wins_text = Text(Point(1.0, 9.25), 'wins')
    wins_text.draw(win)
    wins_box = Rectangle(Point(0.5, 8.5), Point(1.5, 9.0))
    wins_box.draw(win)

    loses_text = Text(Point(2.0, 9.25), 'loses')
    loses_text.draw(win)
    loses_box = Rectangle(Point(1.5, 8.5), Point(2.5, 9.0))
    loses_box.draw(win)

    # accumulator for loops wins and loses
    wins = 0
    loses = 0
    wins_text = Text(Point(1.0, 8.75), wins)
    wins_text.draw(win)
    loses_text = Text(Point(2.0, 8.75), loses)
    loses_text.draw(win)

    numOfGames = 2

    mousePt = win.getMouse()
    while not quit_button.is_clicked(mousePt):
        objects = [rock, paper, scissors]
        currentGame = 0
        while currentGame <= numOfGames:
            userOutputText.setText('Select an object below')

    mousePt = win.getMouse()
    if quit_button.is_clicked(mousePt):
        win.close()

main()