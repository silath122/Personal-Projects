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
    selectGameText = Text(Point(5.0, 8.0), 'Lets play Rock, Paper, Scissors, you\'re Player 1! \n Click anywhere to start!')
    selectGameText.draw(win)

    # draw quit button
    quit_button = Button(Rectangle(Point(7.0, 8.5), Point(9.0, 9.5)), 'Quit')
    quit_button.draw(win)

    # win and lose text box
    winsText = Text(Point(1.0, 9.25), 'wins')
    winsText.draw(win)
    winsBox = Rectangle(Point(0.5, 8.5), Point(1.5, 9.0))
    winsBox.draw(win)

    losesText = Text(Point(2.0, 9.25), 'loses')
    losesText.draw(win)
    losesBox = Rectangle(Point(1.5, 8.5), Point(2.5, 9.0))
    losesBox.draw(win)

    # accumulator for loops wins and loses
    wins = 0
    loses = 0
    winsText = Text(Point(1.0, 8.75), wins)
    winsText.draw(win)
    losesText = Text(Point(2.0, 8.75), loses)
    losesText.draw(win)

    mousePt = win.getMouse()

    while not quit_button.is_clicked(mousePt):
        # 0 = rock, 1 = paper, 2 = scissors
        computerInput = randint(0, 2)  # used to select rock paper scissors randomly for the computer
        userOutputText.setText('Select an object below')  # tells the player to select rock, paper, or scissors
        mousePt = win.getMouse()

        # computer equal to rock then checks if the player clicked rock, paper, or scissors
        # accumulate the loses/wins and change the visible texts on the score board
        if computerInput == 0:
            if rock.is_clicked(mousePt):
                userOutputText.setText('Player 1 chose rock')
                selectGameText.setText('Tie! Click anywhere to play again or press quit to end the game!')
            elif paper.is_clicked(mousePt):
                userOutputText.setText('Player 1 chose paper')
                selectGameText.setText('Player 1 won! Click anywhere to play again or press quit to end the game!')
                wins += 1
                winsText.setText(wins)
            elif scissors.is_clicked(mousePt):
                userOutputText.setText('Player 1 chose scissors')
                selectGameText.setText('NPC won! Click anywhere to play again or press quit to end the game!')
                loses += 1
                losesText.setText(loses)
            cpOutputText.setText('NPC chose rock')
            win.getMouse()
            cpOutputText.setText('NPC')

        # computer equal to paper then checks if the player clicked rock, paper, or scissors
        # accumulate the loses/wins and change the visible texts on the score board
        elif computerInput == 1:
            if rock.is_clicked(mousePt):
                userOutputText.setText('Player 1 chose rock!')
                selectGameText.setText('NPC won! Click anywhere to play again or press quit to end the game!')
                loses += 1
                losesText.setText(loses)
            elif paper.is_clicked(mousePt):
                userOutputText.setText('Player 1 chose paper')
                selectGameText.setText('Tie! Click anywhere to play again or press quit to end the game!')
            elif scissors.is_clicked(mousePt):
                userOutputText.setText('Player 1 chose scissors')
                selectGameText.setText('Player 1 won! Click anywhere to play again or press quit to end the game!')
                wins += 1
                winsText.setText(wins)
            cpOutputText.setText('NPC chose paper')
            win.getMouse()
            cpOutputText.setText('NPC')

        # computer equal to paper then checks if the player clicked rock, paper, or scissors
        # accumulate the loses/wins and change the visible texts on the score board
        elif computerInput == 2:
            if rock.is_clicked(mousePt):
                userOutputText.setText('Player 1 chose rock!')
                selectGameText.setText('Player 1 won! Click anywhere to play again or press quit to end the game!')
                wins += 1
                winsText.setText(wins)
            elif paper.is_clicked(mousePt):
                userOutputText.setText('Player 1 chose paper')
                selectGameText.setText('NPC won! Click anywhere to play again or press quit to end the game!')
                loses += 1
                losesText.setText(loses)
            elif scissors.is_clicked(mousePt):
                userOutputText.setText('Player 1 chose scissors')
                selectGameText.setText('Tie! Click anywhere to play again or press quit to end the game!')
            cpOutputText.setText('NPC chose scissors')
            win.getMouse()
            cpOutputText.setText('NPC')

    mousePt = win.getMouse()
    # if the player clicks the quit button, then exit the game
    if quit_button.is_clicked(mousePt):
        win.close()

main()