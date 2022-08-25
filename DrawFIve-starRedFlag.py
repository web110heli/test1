import turtle
import DrawStar
turtle.setup(600,400)
turtle.bgcolor("red")
DrawStar.star(150,"yellow",0,-280,100)   #主星
DrawStar.star(50,"yellow",305,-100,180)  #第1小星
DrawStar.star(50,"yellow",30,-50,110)    #第2小星
DrawStar.star(50,"yellow",5,-40,50)      #第3小星
DrawStar.star(50,"yellow",300,-100,10)  #第4小星
turtle.done()
