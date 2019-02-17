from Shapes.logic import run_prog
from Shapes.Randomizer import *

if __name__ == "__main__":
    NUMBER_OF_SHAPES = run_prog()
    randomizer = RandoMizer()
    figures = randomizer.generate_figures(NUMBER_OF_SHAPES)
    randomizer.define_fig(figures)
