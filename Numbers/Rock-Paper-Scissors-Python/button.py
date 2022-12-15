from graphics import *

# button
# About: Entity Button class for RPS-GUI
#
# Author: Siah Thomas
# Date: 12/14/2022

class Button:

    # standard constructor
    def __init__(self, shape, label):
        self.shape = shape
        self.text = Text(shape.getCenter(), label)

    # label getter
    def get_label(self):
        return self.text.getText()

    # label setter
    def set_label(self, label):
        self.text.setText(label)

    # method to draw button into window
    def draw(self, win):
        self.shape.draw(win)
        self.text.draw(win)

    # method to remove button from window
    def undraw(self):
        self.shape.undraw()
        self.text.undraw()

    # check if the item is clicked by user
    def is_clicked(self, point):
        xRange = (self.shape.getP1().getX() <= point.getX() and point.getX() <= self.shape.getP2().getX())
        yRange = (self.shape.getP1().getY() <= point.getY() and point.getY() <= self.shape.getP2().getY())
        return xRange and yRange

    # method to color button
    def color_button(self, color):
        self.shape.setFill(color)
