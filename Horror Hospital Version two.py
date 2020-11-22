#map modeled after Brookhaven Hospital Map(1F) from Silent Hill 2



import sys
import random
import math
#import keyboard
import turtle

import winsound
# Blood message: Icons made by <a href="https://www.flaticon.com/free-icon/blood_2068417" title="Good Ware">Good Ware</a> from <a href="https://www.flaticon.com/" title="Flaticon"> www.flaticon.com</a>


# Hole in wall: https://www.flaticon.com/free-icon/filled-circle_60765?term=circle&page=1&position=72

#Fence Icon: https://www.flaticon.com/free-icon/fence_1515295?term=gate&page=1&position=31

#Person Icon: <div>Icons made by <a href="https://www.flaticon.com/authors/freepik" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>
# Blob monster Icon: <div>Icons made by <a href="http://www.freepik.com/" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>
#Spider Monster Icon:  <a href="https://www.flaticon.com/authors/freepik" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon"> www.flaticon.com</a>
#Hospital Bed Icon: <a href="https://www.flaticon.com/authors/monkik" title="monkik">monkik</a> from <a href="https://www.flaticon.com/" title="Flaticon"> www.flaticon.com</a>

#Flashlight Icon: <a href="https://www.flaticon.com/free-icon/flashlight_3222128?term=flashlights&page=1&position=28" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon"> www.flaticon.com</a>
#Spider Icon: https://www.flaticon.com/free-icon/spider-web_12330?term=spider%20webs&page=1&position=2

#Hand Icon: https://www.flaticon.com/free-icon/zombie_275942?term=zombie&page=3&position=54


#Body Bag: https://www.flaticon.com/free-icon/rectangular-object-silhouette_28800?term=rectangle&page=2&position=89


#Key: https://www.flaticon.com/free-icon/door-key_63432


#Pool: https://www.flaticon.com/free-icon/swimming-pool_1144353?term=pool&page=3&position=54


# Piece of paper: https://www.flaticon.com/free-icon/paper_1010773

#Dead body: <div>Icons made by <a href="http://www.freepik.com/" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>


#Icons made by <a href="https://www.flaticon.com/free-icon/stars_1185701?term=sparkles&page=3&position=96&related_item_id=1185701" title="Vitaly Gorbachev">Vitaly Gorbachev</a> from <a href="https://www.flaticon.com/" title="Flaticon"> www.flaticon.com</a>



wn = turtle.Screen()
wn.setup(935,650)
wn.title("Horror Hospital")
wn.bgpic("brookhavenmap.gif")
wn.bgcolor("black")
wn.update()
wn.tracer(0)







def toggle_pause():
    global is_paused
    if is_paused == True:
        is_paused = False
    else:
        is_paused = True


wn.listen()
wn.onkeypress(toggle_pause, "p")


# winsound.PlaySound("Dreaming.wav", winsound.SND_LOOP|winsound.SND_ASYNC)



turtle.register_shape("standing-up-man-24.gif")
turtle.register_shape("monster-with-big-mouth-1.gif")
turtle.register_shape("hospital-bed-32.gif")
turtle.register_shape("flashlight-24.gif")
turtle.register_shape("spiderweb-64.gif")
turtle.register_shape("eye-flurry-monster-24.gif")
turtle.register_shape("zombie-hand-24.gif")
turtle.register_shape("body-bag-24.gif")
turtle.register_shape("door-key-16.gif")
turtle.register_shape("moving-body-bag-monster-24.gif")
turtle.register_shape("swimming-pool.gif")
turtle.register_shape("hand-monster-hallway.gif")
turtle.register_shape("fence.gif")



turtle.register_shape("textboxone.gif")


turtle.register_shape("C4_text_bed_with_flashlight-1.gif")
turtle.register_shape("C4_text_exit.gif")
turtle.register_shape("C4_text_flashlight.gif")
turtle.register_shape("C4_text_hole_five.gif")
turtle.register_shape("C4_text_hole_four.gif")
turtle.register_shape("C4_text_hole_one.gif")
turtle.register_shape("C4_text_hole_three.gif")
turtle.register_shape("C4_text_hole_two.gif")
turtle.register_shape("C4_text_look_at_bed-1.gif")
turtle.register_shape("C4_text_see_door_without_flashlight_one-1.gif")
turtle.register_shape("C4_text_see_door_without_flashlight_two.gif")
turtle.register_shape("C4_text_threatening_message.gif")
turtle.register_shape("C4_text_three.gif")
turtle.register_shape("C4_text_two.gif")
turtle.register_shape("C4_text_one.gif")
turtle.register_shape("C4_reenter_text.gif")
turtle.register_shape("filled-circle.gif")
turtle.register_shape("blood.gif")
turtle.register_shape("C4_exit_text_two.gif")
turtle.register_shape("C3_entrance_text.gif")
turtle.register_shape("C3_game_over_one.gif")
turtle.register_shape("C3_game_over_two.gif")
turtle.register_shape("C3_game_over_three.gif")
turtle.register_shape("C3_game_over_four.gif")
turtle.register_shape("C3_game_over_five.gif")
turtle.register_shape("C3_game_over_six.gif")
turtle.register_shape("C3_final_game_over.gif")
turtle.register_shape("C3_exit_text.gif")
turtle.register_shape("C3_game_over_seven.gif")
turtle.register_shape("Hall1_warning_zero.gif")
turtle.register_shape("Hall1_warning_one.gif")
turtle.register_shape("Hall1_warning_two.gif")
turtle.register_shape("Hall1_monster_game_over_zero.gif")
turtle.register_shape("Hall1_monster_game_over_one.gif")
turtle.register_shape("Hall1_monster_game_over_two.gif")
turtle.register_shape("Hall1_monster_game_over_three.gif")
turtle.register_shape("Hall1_monster_game_over_four.gif")
turtle.register_shape("Hall1_bathroom_entrance.gif")
turtle.register_shape("C2_locked.gif")
turtle.register_shape("Blob_monster_game_over_final.gif")
turtle.register_shape("dead_body.gif")
turtle.register_shape("blob_monster_warning_one.gif")
turtle.register_shape("blob_monster_warning_two.gif")
turtle.register_shape("exam_room_entrance_text_one.gif")
turtle.register_shape("exam_room_entrance_text_two.gif")
turtle.register_shape("exam_room_entrance_text_three.gif")
turtle.register_shape("exam_room_entrance_text_four.gif")
turtle.register_shape("exam_room_entrance_text_five.gif")
turtle.register_shape("exam_room_entrance_text_six.gif")
turtle.register_shape("broken_glass_hall_one.gif")
turtle.register_shape("exam_room_hand_trigger_one.gif")
turtle.register_shape("exam_room_hand_trigger_two.gif")
turtle.register_shape("exam_room_hand_trigger_three.gif")
turtle.register_shape("exam_room_hand_trigger_four.gif")
turtle.register_shape("exam_room_hand_trigger_five.gif")
turtle.register_shape("exam_room_hand_trigger_six.gif")
turtle.register_shape("exam_room_hand_trigger_seven.gif")
turtle.register_shape("exam_room_hand_trigger_eight.gif")
turtle.register_shape("exam_room_hand_trigger_nine.gif")
turtle.register_shape("exam_room_hand_trigger_ten.gif")
turtle.register_shape("exam_room_hand_trigger_eleven.gif")
turtle.register_shape("exam_room_hand_trigger_twelve.gif")
turtle.register_shape("exam_room_hand_trigger_thirteen.gif")





class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)



class Firsttextbox(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("textboxone.gif")
        self.color("black")
        self.penup()
        self.speed(0)
        self.goto(x, y)

    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()



class Dead_Body(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("dead_body.gif")
        self.color("")
        self.penup()
        self.speed(0)
        self.goto(x, y)

    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()



class Broken_Glass(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("broken_glass_hall_one.gif")
        self.color("")
        self.penup()
        self.speed(0)
        self.goto(x, y)

    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()



class Blob_Monster_Death_Zero(Firsttextbox):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("Hall1_monster_game_over_zero.gif")
        self.color("black")
        self.penup()
        self.speed(0)
        self.goto(x, y)

    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()





class Blob_Monster_Death_One(Firsttextbox):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("Hall1_monster_game_over_one.gif")
        self.color("black")
        self.penup()
        self.speed(0)
        self.goto(x, y)

    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()





class Blob_Monster_Death_Two(Firsttextbox):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("Hall1_monster_game_over_two.gif")
        self.color("black")
        self.penup()
        self.speed(0)
        self.goto(x, y)

    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()



class Blob_Monster_Death_Three(Firsttextbox):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("Hall1_monster_game_over_three.gif")
        self.color("black")
        self.penup()
        self.speed(0)
        self.goto(x, y)

    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()






class Blob_Monster_Death_Four(Firsttextbox):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("Hall1_monster_game_over_four.gif")
        self.color("black")
        self.penup()
        self.speed(0)
        self.goto(x, y)

    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()



class Blob_Monster_Death_Final(Firsttextbox):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("Blob_monster_game_over_final.gif")
        self.color("black")
        self.penup()
        self.speed(0)
        self.goto(x, y)

    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()


class Blob_Monster_Warning_One(Firsttextbox):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("blob_monster_warning_one.gif")
        self.color("black")
        self.penup()
        self.speed(0)
        self.goto(x, y)

    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()




class Blob_Monster_Warning_Two(Firsttextbox):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("blob_monster_warning_two.gif")
        self.color("black")
        self.penup()
        self.speed(0)
        self.goto(x, y)

    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()





class C4_Text_One(Firsttextbox):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("C4_text_one.gif")
        self.penup()


    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()


class C4_Text_Two(Firsttextbox):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("C4_text_two.gif")
        self.penup()



    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()


class C4_Text_Three(Firsttextbox):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("C4_text_three.gif")
        self.penup()


    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()

class C4_Text_Look_At_Bed(Firsttextbox):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("C4_text_look_at_bed-1.gif")
        self.color("black")
        self.penup()
        self.speed(0)
        self.goto(x, y)

    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()


class C4_Text_No_Flashlight_One(Firsttextbox):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("C4_text_see_door_without_flashlight_one-1.gif")
        self.color("black")
        self.penup()
        self.speed(0)
        self.goto(x, y)

    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()



class C4_Text_No_Flashlight_Two(Firsttextbox):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("C4_text_see_door_without_flashlight_two.gif")
        self.color("black")
        self.penup()
        self.speed(0)
        self.goto(x, y)

    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()

class C4_Text_Find_Flashlight(Firsttextbox):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("C4_text_flashlight.gif")
        self.color("black")
        self.penup()
        self.speed(0)
        self.goto(x, y)

    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()



class C4_threatening_message(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("blood.gif")
        self.color("black")
        self.penup()
        self.speed(0)
        self.goto(x, y)

    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()



class C4_Text_Threatening_Message(Firsttextbox):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("C4_text_threatening_message.gif")
        self.color("black")
        self.penup()
        self.speed(0)
        self.goto(x, y)

    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()


class C4_Text_Bed_With_Flashlight(Firsttextbox):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("C4_text_bed_with_flashlight-1.gif")
        self.color("black")
        self.penup()
        self.speed(0)
        self.goto(x, y)

    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()


class C4_Text_Hole(Firsttextbox):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("filled-circle.gif")
        self.color("black")
        self.penup()
        self.speed(0)
        self.goto(x, y)

    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()




class C4_Text_hole_One(Firsttextbox):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("C4_text_hole_one.gif")
        self.color("black")
        self.penup()
        self.speed(0)
        self.goto(x, y)

    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()


class C4_Text_hole_Two(Firsttextbox):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("C4_text_hole_two.gif")
        self.color("black")
        self.penup()
        self.speed(0)
        self.goto(x, y)

    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()


class C4_Text_hole_Three(Firsttextbox):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("C4_text_hole_three.gif")
        self.color("black")
        self.penup()
        self.speed(0)
        self.goto(x, y)

    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()


class C4_Text_hole_Four(Firsttextbox):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("C4_text_hole_four.gif")
        self.color("black")
        self.penup()
        self.speed(0)
        self.goto(x, y)

    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()


class C4_Text_hole_Five(Firsttextbox):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("C4_text_hole_five.gif")
        self.color("black")
        self.penup()
        self.speed(0)
        self.goto(x, y)

    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()


class C4_Text_Exit(Firsttextbox):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("C4_text_exit.gif")
        self.color("black")
        self.penup()
        self.speed(0)
        self.goto(x, y)

    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()



class C4_Exit_End_Door_Two(Firsttextbox):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("C4_exit_text_two.gif")
        self.color("black")
        self.penup()
        self.speed(0)
        self.goto(x, y)

    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()



class C4_Reenter_Text(Firsttextbox):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("C4_reenter_text.gif")
        self.color("black")
        self.penup()
        self.speed(0)
        self.goto(x, y)

    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()



class Bathroom_Text(Firsttextbox):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("Hall1_bathroom_entrance.gif")
        self.color("black")
        self.penup()
        self.speed(0)
        self.goto(x, y)

    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()




class C2_Locked(Firsttextbox):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("C2_locked.gif")
        self.color("black")
        self.penup()
        self.speed(0)
        self.goto(x, y)

    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()



class Door_to_Exit_Text_Box(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("black")
        self.penup()
        self.speed(0)
        self.goto(x, y)

    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()




class Door_To_Second_C4_Textbox(Door_to_Exit_Text_Box):

    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("black")
        self.penup()
        self.speed(0)
        self.goto(x, y)

    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()


class Door_To_Start_Game(Door_to_Exit_Text_Box):

    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("black")
        self.penup()
        self.speed(0)
        self.goto(x, y)

    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()



class C4_Blocked_Door(Door_to_Exit_Text_Box):

    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("black")
        self.penup()
        self.speed(0)
        self.goto(x, y)

    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()







class C4_Door_Reenter(Door_to_Exit_Text_Box):

    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("black")
        self.penup()
        self.speed(0)
        self.goto(x, y)

    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()








class C4_Blocked_Second_Door(Door_to_Exit_Text_Box):

    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("black")
        self.penup()
        self.speed(0)
        self.goto(x, y)

    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()




class C4_Blocked_Return_To_Game(Door_to_Exit_Text_Box):

    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("black")
        self.penup()
        self.speed(0)
        self.goto(x, y)

    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()



class C4_Door_Text_Bed_No_Flashlight(Door_to_Exit_Text_Box):

    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("hospital-bed-32.gif")
        self.color("black")
        self.penup()
        self.speed(0)
        self.goto(x, y)

    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()



class C4_Door_Text_Exit_No_Flashlight_Bed(Door_to_Exit_Text_Box):

    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("hospital-bed-32.gif")
        self.color("black")
        self.penup()
        self.speed(0)
        self.goto(x, y)

    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()



class C3_Entrance_Text(Door_to_Exit_Text_Box):

    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("C3_entrance_text.gif")
        self.color("black")
        self.penup()
        self.speed(0)
        self.goto(x, y)

    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()




class C3_Exit_Text(Door_to_Exit_Text_Box):

    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("C3_exit_text.gif")
        self.color("black")
        self.penup()
        self.speed(0)
        self.goto(x, y)

    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()





class C1_Entry_Text(Door_to_Exit_Text_Box):

    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("Hall1_bathroom_entrance.gif")
        self.color("black")
        self.penup()
        self.speed(0)
        self.goto(x, y)

    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()





class C3_Game_Over_One(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("C3_game_over_one.gif")
        self.color("black")
        self.penup()
        self.speed(0)
        self.goto(x, y)

    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()




class C3_Game_Over_Two(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("C3_game_over_two.gif")
        self.color("black")
        self.penup()
        self.speed(0)
        self.goto(x, y)

    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()




class C3_Game_Over_Three(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("C3_game_over_three.gif")
        self.color("black")
        self.penup()
        self.speed(0)
        self.goto(x, y)

    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()





class C3_Game_Over_Four(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("C3_game_over_four.gif")
        self.color("black")
        self.penup()
        self.speed(0)
        self.goto(x, y)

    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()





class C3_Game_Over_Five(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("C3_game_over_five.gif")
        self.color("black")
        self.penup()
        self.speed(0)
        self.goto(x, y)

    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()



class C3_Game_Over_Six(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("C3_game_over_six.gif")
        self.color("black")
        self.penup()
        self.speed(0)
        self.goto(x, y)

    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()




class C3_Game_Over_Seven(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("C3_game_over_seven.gif")
        self.color("black")
        self.penup()
        self.speed(0)
        self.goto(x, y)

    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()



class C3_Game_Over_Final(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("C3_final_game_over.gif")
        self.color("black")
        self.penup()
        self.speed(0)
        self.goto(x, y)

    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()



class C4_Door_Text_Exit_Flashlight(Door_to_Exit_Text_Box):

    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("black")
        self.penup()
        self.speed(0)
        self.goto(x, y)





class C4_Exit_Blood_Text(Door_to_Exit_Text_Box):

    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("black")
        self.penup()
        self.speed(0)
        self.goto(x, y)



class C4_Exit_To_Hole_Two(Door_to_Exit_Text_Box):

    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("black")
        self.penup()
        self.speed(0)
        self.goto(x, y)


class C4_Exit_To_Hole_Three(Door_to_Exit_Text_Box):

    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("black")
        self.penup()
        self.speed(0)
        self.goto(x, y)


class C4_Exit_To_Hole_Four(Door_to_Exit_Text_Box):

    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("black")
        self.penup()
        self.speed(0)
        self.goto(x, y)


class C4_Exit_To_Hole_Five(Door_to_Exit_Text_Box):

    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("black")
        self.penup()
        self.speed(0)
        self.goto(x, y)


class C4_Exit_Hole_Text(Door_to_Exit_Text_Box):

    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("black")
        self.penup()
        self.speed(0)
        self.goto(x, y)


class C4_Exit_Second_Bed_Text(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("black")
        self.penup()
        self.speed(0)
        self.goto(x, y)

    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()


class C4_Exit_End_Door (turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("black")
        self.penup()
        self.speed(0)
        self.goto(x, y)

    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()




class Door(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("black")
        self.penup()
        self.speed(0)
        self.goto(x, y)

    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()


class Door_2(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("black")
        self.penup()
        self.speed(0)
        self.goto(x, y)

    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()





class DoortoenterC3(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("")
        self.penup()
        self.speed(0)
        self.goto(x, y)


class DoortoexitC3(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("")
        self.penup()
        self.speed(0)
        self.goto(x, y)




class Door_to_enter_examination_room(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("")
        self.penup()
        self.speed(0)
        self.goto(x, y)


class Door_to_exit_examination_room(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("")
        self.penup()
        self.speed(0)
        self.goto(x, y)


class Door_to_Enter_C2(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("")
        self.penup()
        self.speed(0)
        self.goto(x, y)


class Door_to_Exit_C2(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("")
        self.penup()
        self.speed(0)
        self.goto(x, y)

class Door_to_Exit_C2_with_key(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("")
        self.penup()
        self.speed(0)
        self.goto(x, y)



class Door_to_Exit_Hallway(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("black")
        self.penup()
        self.speed(0)
        self.goto(x, y)


class Door_to_Exit_to_Pool_Area(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("")
        self.penup()
        self.speed(0)
        self.goto(x, y)


class Door_to_exit_game(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("fence.gif")
        self.color("")
        self.penup()
        self.speed(0)
        self.goto(x, y)



class Trigger_Hand_Monster(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("black")
        self.penup()
        self.speed(0)
        self.goto(x, y)

    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()


class Hospital_Bed(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("hospital-bed-32.gif")
        self.color("black")
        self.penup()
        self.speed(0)
        self.goto(x, y)

    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()



class Pool(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("swimming-pool.gif")
        self.color("black")
        self.penup()
        self.speed(0)
        self.goto(x, y)

    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()

class Flashlight(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("flashlight-24.gif")
        self.color("black")
        self.penup()
        self.speed(0)
        self.goto(x, y)

    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()


class Key(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("door-key-16.gif")
        self.color("black")
        self.penup()
        self.speed(0)
        self.goto(x, y)

    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()


class Spiderwebs(turtle.Turtle):
 def __init__(self, x, y):
    turtle.Turtle.__init__(self)
    self.shape("spiderweb-64.gif")
    self.color("black")
    self.penup()
    self.speed(0)
    self.goto(x, y)

 def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()










class Blobmonster(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("monster-with-big-mouth-1.gif")
        self.color("black")
        self.penup()
        self.speed(0)
        self.goto(x, y)
        self.direction = random.choice(["up", "down"])

    def move(self):
        dx = 0

        dy = 0

        if self.direction == "up":

            dx = 0

            dy = 24



        elif self.direction == "down":

            dx = 0

            dy = -24



        elif self.direction == "left":

            dx = -24

            dy = 0



        elif self.direction == "right":

            dx = 24

            dy = 0

        else:

          self.goto(0, 0)

        # check if player is close
        # If so, go that direction

        if self.is_close(player):
            if player.xcor() < self.xcor():
                self.direction = "left"
            elif player.xcor() < self.xcor():
                self.direction = "right"
            elif player.ycor() < self.ycor():
                self.direction = "up"
            elif player.ycor() < self.ycor():
                self.direction = "down"



        #calculate the spot to move to
        move_to_x = self.xcor() + dx
        move_to_y = self.ycor() + dy
        #check if a space has a wall
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)
        else:
            #choose a different direction
            self.direction = random.choice(["up", "down"])

        #set timer to move next time
        wn.ontimer(self.move, t=random.randint(100, 300))

    def is_close(self, other):

        a= self.xcor()-other.xcor()
        b= self.ycor()-other.ycor()
        distance = math.sqrt((a**2) + (b**2))

        if distance < 75:
            return True
        else:
            return False

    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()





class Spidermonster(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("eye-flurry-monster-24.gif")
        self.color("")
        self.penup()
        self.speed(0)
        self.goto(x, y)
        self.direction = random.choice(["left", "right"])

    def move(self):
        if self.direction == "left":
            dx = -24
            dy = 0
        elif self.direction == "right":
            dx = 24
            dy = 0
        elif self.direction == "up":
            dx = 0
            dy = 24
        elif self.direction == "down":
            dx = 0
            dy = -24
        else:
            dx = 0
            dy = 0

        # check if player is close
        # If so, go that direction

        if self.is_close(player):
            if player.xcor() < self.xcor():
                self.direction = "left"
            elif player.xcor() < self.xcor():
                self.direction = "right"
            elif player.ycor() < self.ycor():
                self.direction = "up"
            elif player.ycor() < self.ycor():
                self.direction = "down"



        #calculate the spot to move to
        move_to_x = self.xcor() + dx
        move_to_y = self.ycor() + dy
        #check if a space has a wall
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)
        else:
            #choose a different direction
            self.direction = random.choice(["left", "right", "up", "down"])

        #set timer to move next time
        wn.ontimer(self.move, t=random.randint(100, 300))

    def is_close(self, other):

        a= self.xcor()-other.xcor()
        b= self.ycor()-other.ycor()
        distance = math.sqrt((a**2) + (b**2))

        if distance < 75:
            return True
        else:
            return False

    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()







class Hand_Monster_Hallway(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("hand-monster-hallway.gif")
        self.color("")
        self.penup()
        self.speed(0)
        self.goto(x, y)
        self.direction = random.choice(["left", "right"])

    def move(self):
        if self.direction == "left":
            dx = -24
            dy = 0
        elif self.direction == "right":
            dx = 24
            dy = 0
        elif self.direction == "up":
            dx = 0
            dy = 24
        elif self.direction == "down":
            dx = 0
            dy = -24
        else:
            dx = 0
            dy = 0

        # check if player is close
        # If so, go that direction

        if self.is_close(player):
            if player.xcor() < self.xcor():
                self.direction = "left"
            elif player.xcor() < self.xcor():
                self.direction = "right"
            elif player.ycor() < self.ycor():
                self.direction = "up"
            elif player.ycor() < self.ycor():
                self.direction = "down"



        #calculate the spot to move to
        move_to_x = self.xcor() + dx
        move_to_y = self.ycor() + dy

        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)
        else:
            #choose a different direction
            self.direction = random.choice(["left", "right", "up", "down"])

        #set timer to move next time
        wn.ontimer(self.move, t=random.randint(100, 300))

    def is_close(self, other):

        a= self.xcor()-other.xcor()
        b= self.ycor()-other.ycor()
        distance = math.sqrt((a**2) + (b**2))

        if distance < 75:
            return True
        else:
            return False

    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()










class Handmonster(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("zombie-hand-24.gif")
        self.color("")
        self.penup()
        self.speed(0)
        self.goto(x, y)
        self.direction = random.choice(["left", "right"])

    def move(self):
        if self.direction == "left":
            dx = -24
            dy = 0
        elif self.direction == "right":
            dx = 24
            dy = 0
        elif self.direction == "up":
            dx = 0
            dy = 24
        elif self.direction == "down":
            dx = 0
            dy = -24
        else:
            dx = 0
            dy = 0

        # check if player is close
        # If so, go that direction

        if self.is_close(player):
            if player.xcor() < self.xcor():
                self.direction = "left"
            elif player.xcor() < self.xcor():
                self.direction = "right"
            elif player.ycor() < self.ycor():
                self.direction = "up"
            elif player.ycor() < self.ycor():
                self.direction = "down"



        #calculate the spot to move to
        move_to_x = self.xcor() + dx
        move_to_y = self.ycor() + dy
        #check if a space has a wall
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)
        else:
            #choose a different direction
            self.direction = random.choice(["left", "right", "up", "down"])

        #set timer to move next time
        wn.ontimer(self.move, t=random.randint(100, 300))

    def is_close(self, other):

        a= self.xcor()-other.xcor()
        b= self.ycor()-other.ycor()
        distance = math.sqrt((a**2) + (b**2))

        if distance < 75:
            return True
        else:
            return False

    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()




class Body_Bag_monster(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("body-bag-24.gif")
        self.color("")
        self.penup()
        self.speed(0)
        self.goto(x, y)
        self.direction = random.choice(["left", "right"])

    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()


class Body_Bag_monster_moving(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("moving-body-bag-monster-24.gif")
        self.color("")
        self.penup()
        self.speed(0)
        self.goto(x, y)
        self.direction = random.choice(["left", "right"])

    def move(self):
        if self.direction == "left":
            dx = -24
            dy = 0
        elif self.direction == "right":
            dx = 24
            dy = 0
        elif self.direction == "up":
            dx = 0
            dy = 24
        elif self.direction == "down":
            dx = 0
            dy = -24
        else:
            dx = 0
            dy = 0

        # check if player is close
        # If so, go that direction

        if self.is_close(player):
            if player.xcor() < self.xcor():
                self.direction = "left"
            elif player.xcor() < self.xcor():
                self.direction = "right"
            elif player.ycor() < self.ycor():
                self.direction = "up"
            elif player.ycor() < self.ycor():
                self.direction = "down"





        #calculate the spot to move to
        move_to_x = self.xcor() + dx
        move_to_y = self.ycor() + dy
        #check if a space has a wall
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)
        else:
            #choose a different direction
            self.direction = random.choice(["left", "right", "up", "down"])

        #set timer to move next time
        wn.ontimer(self.move, t=random.randint(100, 300))

    def is_close(self, other):

        a= self.xcor()-other.xcor()
        b= self.ycor()-other.ycor()
        distance = math.sqrt((a**2) + (b**2))

        if distance < 75:
            return True
        else:
            return False


    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()





class Hospital_Bed_Two(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("hospital-bed-32.gif")
        self.color("black")
        self.penup()
        self.speed(0)
        self.goto(x, y)

    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()





class Hallway_Blood_Message(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("Hall1_warning_zero.gif")
        self.color("black")
        self.penup()
        self.speed(0)
        self.goto(x, y)

    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()



class Hallway_Blood_Message_One(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("Hall1_warning_one.gif")
        self.color("black")
        self.penup()
        self.speed(0)
        self.goto(x, y)

    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()




class Hallway_Blood_Message_Two(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("Hall1_warning_two.gif")
        self.color("black")
        self.penup()
        self.speed(0)
        self.goto(x, y)

    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()





class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("standing-up-man-24.gif")
        self.color("blue")
        self.penup()
        self.speed(0)

    def go_up(self):

        move_to_x = player.xcor()
        move_to_y = player.ycor() + 24



        #Check if the space has a wall
        if (move_to_x, move_to_y) not in walls:
             self.goto(move_to_x, move_to_y)


    def go_down(self):

        move_to_x = player.xcor()
        move_to_y = player.ycor() - 24

        # Check if the space has a wall
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def go_left(self):
        move_to_x = player.xcor() - 24
        move_to_y = player.ycor()

        # Check if the space has a wall
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def go_right(self):

        move_to_x = player.xcor() + 24
        move_to_y = player.ycor()

        # Check if the space has a wall
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def close_text(self):

        move_to_x = player.xcor() + 504
        move_to_y = player.ycor()

        # Check if the space has a wall
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def toggle_pause(self):
        global is_paused
        if is_paused == True:
            is_paused = False
        else:
            is_paused = True

    def is_collision(self, other):
        a= self.xcor()-other.xcor()
        b= self.ycor()-other.ycor()
        distance = math.sqrt((a**2) + (b**2))

        if distance < 5:
            return True
        else:
            return False





class Exam_Entrance_Text_One(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("exam_room_entrance_text_one.gif")
        self.color("black")
        self.penup()
        self.speed(0)
        self.goto(x, y)

    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()



class Exam_Entrance_Text_Two(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("exam_room_entrance_text_two.gif")
        self.color("black")
        self.penup()
        self.speed(0)
        self.goto(x, y)

    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()


class Exam_Entrance_Text_Three(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("exam_room_entrance_text_three.gif")
        self.color("black")
        self.penup()
        self.speed(0)
        self.goto(x, y)

    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()



class Exam_Entrance_Text_Four(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("exam_room_entrance_text_four.gif")
        self.color("black")
        self.penup()
        self.speed(0)
        self.goto(x, y)

    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()



class Exam_Entrance_Text_Five(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("exam_room_entrance_text_five.gif")
        self.color("black")
        self.penup()
        self.speed(0)
        self.goto(x, y)

    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()



class Exam_Entrance_Text_Six(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("exam_room_entrance_text_six.gif")
        self.color("black")
        self.penup()
        self.speed(0)
        self.goto(x, y)

    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()






levels=[""]

#Level when player doesn't have flashlight
level_1 = [


     "XXXX4XXXX",
     "XX     XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
     "XX  F  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
     "XX     XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
     "XX     XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
     "XX     XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
     "XX  P  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
     "XX  H  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
     "XXXXXXXXX"

]

level_failed_exit_C4 = [


     "XXXXEXXXXX",
     "XX  P  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
     "XX  F  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
     "XX     XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
     "XX     XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
     "XX     XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
     "XX     XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
     "XX  H  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
     "XXXXXXXXX"

]




#Level where player has flashlight and can leave the room
level_2 = [
     "XXXXEXXX",
     "XX     XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
     "XX  P  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
     "XX     XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
     "XXY   ZXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
     "XX     XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
     "XX     XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
     "XX  V  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
     "XXXXXXXXX"

]



level_exit_message = [
     "XXXXEXXX",
     "XX     XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
     "XX     XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
     "XX     XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
     "XXYP  ZXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
     "XX     XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
     "XX     XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
     "XX  V  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
     "XXXXXXXXX"

]


level_3 = [
     "XXXCCCXX",
     "XX     XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
     "XX  P  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
     "XX     XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
     "XX     XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
     "XX     XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
     "XX  S  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
     "XX W  1XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
     "XXXXXXXXX"

]


level_examinationroom = [
     "XXXXXXXX",
     "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
     "XX  C  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
     "XX  Y  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
     "XX     XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
     "XX     XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
     "XX     XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
     "XX     XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
     "XX     XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
     "XX  P  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
     "XXXXXXXXX"

]


level_examination_room_with_monster = [
     "XXZ1234X",
     "XX56789X",
     "XX  C  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
     "XX  P  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
     "XX     XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
     "XX     XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
     "XX     XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
     "XX     XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
     "XX     XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
     "XX  A  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
     "XXXXXXXXX"

]









level_C2 = [
     "XXXIIIXXX",
     "XX  P  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
     "XX     XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
     "XX     XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
     "XX   V XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
     "XX     XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
     "XX     XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
     "XX  K  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
     "XXXXXXXXX"

]


level_C2_with_moving_monster = [

     "XXXXXXXXX",
     "XX  J  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
     "XX     XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
     "XX     XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
     "XX   U XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
     "XX     XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
     "XX     XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
     "XX  P  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx",
     "XXXXXXXXX"

]



level_pool_area = [

     "XXXXXXXXXXXXXX",
     "XXXX      P  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
     "XXXX         XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
     "XXXX  XXXXX  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
     "    9 X 3 X  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
     "XXXX  XXXXX  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
     "XXXX         XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
     "XXXXXXXXXXXXXX",
     "XXXXXXXXXXXXXX"

]



level_with_text = [
    "  X                               X       ",
    "  X                             X       ",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXPX                       RXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXX  XXXXXXXXXXXXXXXXXXXXX",
    "X                     X            ",
    "X                     X             ",
    "X                1      X             ",
    "XXXXXXXXXXXXX   XXX  XXXX    XXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"






]



level_with_text_C4_text_one = [
    "  X                               X       ",
    "  X                                                                                                                                X       ",
    "XXXXXXXX                                                                                                                          XPX                   RXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXX  XXXXXXXXXXXXXXXXXXXXX",
    "X                     X            ",
    "X                     X             ",
    "X                A      X             ",
    "XXXXXXXXXXXXX   XXX  XXXX    XXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"






]


level_with_text_C4_text_two = [
    "  X                                                                                                                                      X       ",
    "  X    XX                                                                                                                               XPX                   2XXXXXXXXXXXXXXXXXXXXXXXXXXXx                         X       ",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXX  XXXXXXXXXXXXXXXXXXXXX",
    "X                     X            ",
    "X                     X             ",
    "X                B      X             ",
    "XXXXXXXXXXXXX   XXX  XXXX    XXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"






]


level_with_text_C4_text_three = [

    "                                                                                                                           X",
    "  X     XXXXXXXXX                                                                                                         XPX                   3                      X       ",
    "  X     XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX                                                                            X       ",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXX  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx",
    "XXXXXXXXXXX XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXX  XXXXXXXXXXXXXXXXXXXXX",
    "X                     X            ",
    "X                     X             ",
    "X                C      X             ",
    "XXXXXXXXXXXXX   XXX  XXXX    XXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"






]



level_with_text_C4_see_door_without_flashlight_one = [
    "  X                                                      X       ",
    "  X                             X       ",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXX  XXXXXXXXXXXXXXXXXXXXX",
    "X                     X            ",
    "X                     X             ",
    "X                D      X             ",
    "XXXXXXXXXXXXX   XXX  XXXX    XXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
"  X                                                                                                                      XPX                   4",
"                                                                                                                          X",
    "                    X"






]

level_with_text_C4_see_door_without_flashlight_two = [
    "  X                               X       ",
    "  X                             X       ",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXX  XXXXXXXXXXXXXXXXXXXXX",
    "X                     X            ",
    "X                     X             ",
    "X                E      X             ",
    "XXXXXXXXXXXXX   XXX  XXXX    XXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "        X                                                                                                                X",
    "XXXXXXX                                                                                                                 XPX                   5XXXXX",
    "X                                                                                                                        X"





]





level_with_text_C4_look_at_the_bed = [
    "  X                               X       ",
    "  X                             X       ",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXX  XXXXXXXXXXXXXXXXXXXXX",
    "X                     X            ",
    "X                     X             ",
    "X                H      X             ",
    "XXXXXXXXXXXXX   XXX  XXXX    XXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "X                                     X",
    "                                                                       X",
    "                                                                      XPX                   6XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx                     ",
    "                                                                       X "






]



level_with_text_C4_text_flashlight = [
    "  X                               X       ",
    "  X                             X       ",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXX  XXXXXXXXXXXXXXXXXXXXX",
    "X                     X            ",
    "X                     X             ",
    "X                I      X             ",
    "XXXXXXXXXXXX   XXX  XXXX    XXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX                                                                                      X",
    "                                                                                                                           XPX                   7XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx",
    "                                                                                                                            X"






]





level_with_text_C4_text_bed_with_flashlight = [
    "  X                               X       ",
    "  X                             X       ",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXX  XXXXXXXXXXXXXXXXXXXXX",
    "X                     X            ",
    "X                     X             ",
    "X                ?      X             ",
    "XXXXXXXXXXXXX   XXX  XXXX    XXXXXXXXXXXXX",
    "                                                                XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "                                                                        XPX                   WXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx",
    "                                                                         X"






]




level_with_text_C4_hole_one = [
    "  X                               X       ",
    "  X                             X       ",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXX  XXXXXXXXXXXXXXXXXXXXX",
    "X                     X            ",
    "X                    X             ",
    "X               K       X           ",
    "XXXXXXXXXXXX   XXX  XXXX    XXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "                                      ",
    "                                      ",
    "                                      ",
    "                                      ",
    "                                      ",
    "                                      ",
    "                                      ",
    "                                      ",
    "                                      ",
    "                                                                                                          X                                ",
"                                                                                                         XPX                   9XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx                        ",
    "                                                                                                          X                          "








]


level_with_text_C4_hole_two = [
    "  X                               X       ",
    "  X                             X       ",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXX  XXXXXXXXXXXXXXXXXXXXX",
    "X                     X            ",
    "X                     X             ",
    "X                L      X             ",
    "XXXXXXXXXXXXX   XXX  XXXX    XXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "                                     ",
    "                                     ",
    "                                     ",
    "                                     ",
    "                                      ",
    "                                      ",
    "                                      ",
    "                                      ",
    "                                     X",
    "                                    XPX                   0XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx",
    "                                     X"






]


level_with_text_C4_hole_three = [
    "  X                               X       ",
    "  X                             X       ",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXX  XXXXXXXXXXXXXXXXXXXXX",
    "X                     X            ",
    "X                     X             ",
    "X                M      X             ",
    "XXXXXXXXXXXXX   XXX  XXXX    XXXXXXXXXXXXX",
    "                                           ",
    "                                            ",
    "                                             ",
    "                                              ",
    "                                              ",
    "                                               ",
    "                                               ",
    "                                         XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
"                                             XPX                   QXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx",
    "                                          X"







]


level_with_text_C4_hole_four = [
    "  X                               X       ",
    "  X                             X       ",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXX  XXXXXXXXXXXXXXXXXXXXX",
    "X                     X            ",
    "X                     X             ",
    "X                N      X             ",
    "XXXXXXXXXXXXX   XXX  XXXX    XXXXXXXXXXXXX",
    "                                           ",
    "                                            ",
    "                                                               XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
"                                                                            XPX                   SXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "                                                                             X"







]


level_with_text_C4_hole_five = [
    "  X                               X       ",
    "  X                             X       ",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXX  XXXXXXXXXXXXXXXXXXXXX",
    "X                     X            ",
    "X                     X             ",
    "X                O      X             ",
    "XXXXXXXXXXXXX   XXX  XXXX    XXXXXXXXXXXXX",
    "                                           ",
    "                                            ",
    "                                             ",
    "                                             ",
    "                                             ",
    "                                            ",
    "                                           ",
    "                                            ",
    "                                             ",
    "                                             ",
    "                                             ",
    "                                            ",
    "                                      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
"                                                                           XPX                   TXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx",
    "                                                                            X"







]







level_with_text_C4_exit = [
    "                                          ",
    "  X                               X       ",
    "  X                             X       ",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXX  XXXXXXXXXXXXXXXXXXXXX",
    "X                     X            ",
    "X                     X             ",
    "X                !      X             ",
    "XXXXXXXXXXXXX   XXX  XXXXX   XXXXXXXXXXXXX",
    "                                           ",
    "                                            ",
    "                                            ",
    "                                            ",
    "                                                        X",
            "                                                       XPX                   @ ",
    "         X                                              X"

]




level_with_text_C4_exit_two = [
    "                                          ",
    "  X                               X       ",
    "  X                             X       ",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXX  XXXXXXXXXXXXXXXXXXXXX",
    "X                     X            ",
    "X                     X             ",
    "X                #      X             ",
    "XXXXXXXXXXXXX   XXX  XXXXX   XXXXXXXXXXXXX",
    "                                           ",
    "                                            ",
    "                                            ",
    "                                            ",
    "                                                        X",
            "                                                       XPX                   $ ",
    "         X                                              X"

]



level_C4_near_hospital_bed_with_light = [
     "XXXXEXXXX",
     "XX     XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
     "XX     XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
     "XX     XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
     "XXY   ZXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
     "XX     XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
     "XX  P  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
     "XX  V  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
     "XXXXXXXXX"

]






level_with_text_C4_threatening_message = [
    "  X                               X       ",
    "  X                             X       ",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXX  XXXXXXXXXXXXXXXXXXXXX",
    "X                     X            ",
    "X                     X             ",
    "X                J      X             ",
    "XXXXXXXXXXX   XXX  XXXX    XXXXXXXXXXXXX",
    "                                         ",
    "                                         ",
    "                                         ",
    "                                         ",
    "                                         ",
"XXXXXXXXXXXXXXXXXXXX                          XX",
    "                                          XPX                   8",
    "                                           X"


]











level_C4_reenter = [
    "  X                               X       ",
    "  X                            X       ",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXX  XXXXXXXXXXXXXXXXXXXXX",
    "X                     X            ",
    "X                     X             ",
    "X                /      X             ",
    "XXXXXXXXXXX   XXX  XXXX    XXXXXXXXXXXXX",
    "                                         ",
    "                                         ",
    "                                         ",
    "                                         ",
    "                                         ",
"XXXXXXXXXXXXXXXXXXXX                          XX",
    "                                             ",
    "                                             ",
    "                                             ",
    "                                             ",
    "                                             ",
    "                                           X",
    "                                           X",
    "                                          XPX                   } ",
    "                                           X"


]





level_C3_entrance_text = [
    "  X                               X       ",
    "  X                            X       ",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXX  XXXXXXXXXXXXXXXXXXXXX",
    "X                     X            ",
    "X                     X             ",
    "X                C      X             ",
    "XXXXXXXXXXX   XXX  XXXX    XXXXXXXXXXXXX",
    "                                         ",
    "                                         ",
    "                                         ",
    "                                         ",
    "                                         ",
"XXXXXXXXXXXXXXXXXXXX                          XX",
    "                                             ",
    "                                             ",
    "                                             ",
    "                                             ",
    "                                             ",
    "                                           X",
    "                                           X",
    "                                          XPX                   1 ",
    "                                           X"


]





level_hallway_one_blood_message = [
    "  X                               X       ",
    "  X                            X       ",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXX  XXXXXXXXXXXXXXXXXXXXX",
    "X                     X            ",
    "X                     X             ",
    "X                D      X             ",
    "XXXXXXXXXXX   XXX  XXXX    XXXXXXXXXXXXX",
    "                                         ",
    "                                         ",
    "                                         ",
    "                                         ",
    "                                         ",
"XXXXXXXXXXXXXXXXXXXX                          XX",
    "                                             ",
    "                                             ",
    "                                             ",
    "                                             ",
    "                                             ",
    "                                           X",
    "                                           X",
    "                                          XPX                   2 ",
    "                                           X"


]




level_hallway_two_blood_message = [
    "  X                               X       ",
    "  X                            X       ",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXX  XXXXXXXXXXXXXXXXXXXXX",
    "X                     X            ",
    "X                     X             ",
    "X                E      X             ",
    "XXXXXXXXXXX   XXX  XXXX    XXXXXXXXXXXXX",
    "                                         ",
    "                                         ",
    "                                         ",
    "                                         ",
    "                                         ",
"XXXXXXXXXXXXXXXXXXXX                          XX",
    "                                             ",
    "                                             ",
    "                                             ",
    "                                             ",
    "                                             ",
    "                                           X",
    "                                           X",
    "                                          XPX                   3 ",
    "                                           X"


]







level_hallway_three_blood_message = [
    "  X                               X       ",
    "  X                            X       ",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXX  XXXXXXXXXXXXXXXXXXXXX",
    "X                     X            ",
    "X                     X             ",
    "X                F      X             ",
    "XXXXXXXXXXX   XXX  XXXX    XXXXXXXXXXXXX",
    "                                         ",
    "                                         ",
    "                                         ",
    "                                         ",
    "                                         ",
"XXXXXXXXXXXXXXXXXXXX                          XX",
    "                                             ",
    "                                             ",
    "                                             ",
    "                                             ",
    "                                             ",
    "                                           X",
    "                                           X",
    "                                          XPX                   4 ",
    "                                           X"


]






level_bathroom_entrance = [
    "  X                               X       ",
    "  X                            X       ",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXX  XXXXXXXXXXXXXXXXXXXXX",
    "X                     X            ",
    "X                     X             ",
    "X                I      X             ",
    "XXXXXXXXXXX   XXX  XXXX    XXXXXXXXXXXXX",
    "                                         ",
    "                                         ",
    "                                         ",
    "                                         ",
    "                                         ",
"XXXXXXXXXXXXXXXXXXXX                          XX",
    "                                             ",
    "                                             ",
    "                                             ",
    "                                             ",
    "                                             ",
    "                                           X",
    "                                           X",
    "                                          XPX                   6 ",
    "                                           X"


]




level_C3_enter_text = [
    "  X                               X       ",
    "  X                            X       ",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXX  XXXXXXXXXXXXXXXXXXXXX",
    "X                     X            ",
    "X                     X             ",
    "X                J      X             ",
    "XXXXXXXXXXX   XXX  XXXX    XXXXXXXXXXXXX",
    "                                         ",
    "                                         ",
    "                                         ",
    "                                         ",
    "                                         ",
"XXXXXXXXXXXXXXXXXXXX                          XX",
    "                                             ",
    "                                             ",
    "                                             ",
    "                                             ",
    "                                             ",
    "                                           X",
    "                                           X",
    "                                          XPX                   7 ",
    "                                           X"


]



level_C3_game_over_one_text = [
    "  X                               X       ",
    "  X                            X       ",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXX  XXXXXXXXXXXXXXXXXXXXX",
    "X                     X            ",
    "X                     X             ",
    "X                K      X             ",
    "XXXXXXXXXXX   XXX  XXXX    XXXXXXXXXXXXX",
    "                                         ",
    "                                         ",
    "                                         ",
    "                                         ",
    "                                         ",
"XXXXXXXXXXXXXXXXXXXX                          XX",
    "                                             ",
    "                                             ",
    "                                             ",
    "                                             ",
    "                                             ",
    "                                           X",
    "                                           X",
    "                                          XPX                   8 ",
    "                                           X"


]


level_C3_game_over_two_text = [
    "  X                               X       ",
    "  X                            X       ",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXX  XXXXXXXXXXXXXXXXXXXXX",
    "X                     X            ",
    "X                     X             ",
    "X                L      X             ",
    "XXXXXXXXXXX   XXX  XXXX    XXXXXXXXXXXXX",
    "                                         ",
    "                                         ",
    "                                         ",
    "                                         ",
    "                                         ",
"XXXXXXXXXXXXXXXXXXXX                          XX",
    "                                             ",
    "                                             ",
    "                                             ",
    "                                             ",
    "                                             ",
    "                                           X",
    "                                           X",
    "                                          XPX                   9 ",
    "                                           X"


]


level_C3_game_over_three_text = [
    "  X                               X       ",
    "  X                            X       ",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXX  XXXXXXXXXXXXXXXXXXXXX",
    "X                     X            ",
    "X                     X             ",
    "X                N      X             ",
    "XXXXXXXXXXX   XXX  XXXX    XXXXXXXXXXXXX",
    "                                         ",
    "                                         ",
    "                                         ",
    "                                         ",
    "                                         ",
"XXXXXXXXXXXXXXXXXXXX                          XX",
    "                                             ",
    "                                             ",
    "                                             ",
    "                                             ",
    "                                             ",
    "                                           X",
    "                                           X",
    "                                          XPX                   ! ",
    "                                           X"


]




level_C3_game_over_four_text = [
    "  X                               X       ",
    "  X                            X       ",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXX  XXXXXXXXXXXXXXXXXXXXX",
    "X                     X            ",
    "X                     X             ",
    "X                O      X             ",
    "XXXXXXXXXXX   XXX  XXXX    XXXXXXXXXXXXX",
    "                                         ",
    "                                         ",
    "                                         ",
    "                                         ",
    "                                         ",
"XXXXXXXXXXXXXXXXXXXX                          XX",
    "                                             ",
    "                                             ",
    "                                             ",
    "                                             ",
    "                                             ",
    "                                           X",
    "                                           X",
    "                                          XPX                   @ ",
    "                                           X"


]



level_C3_game_over_five_text = [
    "  X                               X       ",
    "  X                            X       ",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXX  XXXXXXXXXXXXXXXXXXXXX",
    "X                     X            ",
    "X                     X             ",
    "X                R      X             ",
    "XXXXXXXXXXX   XXX  XXXX    XXXXXXXXXXXXX",
    "                                         ",
    "                                         ",
    "                                         ",
    "                                         ",
    "                                         ",
"XXXXXXXXXXXXXXXXXXXX                          XX",
    "                                             ",
    "                                             ",
    "                                             ",
    "                                             ",
    "                                             ",
    "                                           X",
    "                                           X",
    "                                          XPX                   # ",
    "                                           X"


]



level_C3_game_over_six_text = [
    "  X                               X       ",
    "  X                            X       ",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXX  XXXXXXXXXXXXXXXXXXXXX",
    "X                     X            ",
    "X                     X             ",
    "X                S      X             ",
    "XXXXXXXXXXX   XXX  XXXX    XXXXXXXXXXXXX",
    "                                         ",
    "                                         ",
    "                                         ",
    "                                         ",
    "                                         ",
"XXXXXXXXXXXXXXXXXXXX                          XX",
    "                                             ",
    "                                             ",
    "                                             ",
    "                                             ",
    "                                             ",
    "                                           X",
    "                                           X",
    "                                          XPX                   ^ ",
    "                                           X"


]



level_C3_game_over_seven_text = [
    "  X                               X       ",
    "  X                            X       ",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXX  XXXXXXXXXXXXXXXXXXXXX",
    "X                     X            ",
    "X                     X             ",
    "X                T      X             ",
    "XXXXXXXXXXX   XXX  XXXX    XXXXXXXXXXXXX",
    "                                         ",
    "                                         ",
    "                                         ",
    "                                         ",
    "                                         ",
"XXXXXXXXXXXXXXXXXXXX                          XX",
    "                                             ",
    "                                             ",
    "                                             ",
    "                                             ",
    "                                             ",
    "                                           X",
    "                                           X",
    "                                          XPX                   * ",
    "                                           X"


]




level_C3_game_over_final = [
    "  X                               X       ",
    "  X                            X       ",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXX  XXXXXXXXXXXXXXXXXXXXX",
    "X                     X            ",
    "X                     X             ",
    "X                U      X             ",
    "XXXXXXXXXXX   XXX  XXXX    XXXXXXXXXXXXX",
    "                                         ",
    "                                         ",
    "                                         ",
    "                                         ",
    "                                         ",
"XXXXXXXXXXXXXXXXXXXX                          XX",
    "                                             ",
    "                                             ",
    "                                             ",
    "                                             ",
    "                                             ",
    "                                           X",
    "                                           X",
    "                                          XPX                   ( ",
    "                                           X"


]





level_C1_entry = [
    "  X                               X       ",
    "  X                            X       ",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXX  XXXXXXXXXXXXXXXXXXXXX",
    "X                     X            ",
    "X                     X             ",
    "X                Q      X             ",
    "XXXXXXXXXXX   XXX  XXXX    XXXXXXXXXXXXX",
    "                                         ",
    "                                         ",
    "                                         ",
    "                                         ",
    "                                         ",
"XXXXXXXXXXXXXXXXXXXX                          XX",
    "                                             ",
    "                                             ",
    "                                             ",
    "                                             ",
    "                                             ",
    "                                           X",
    "                                           X",
    "                                          XPX                   $ ",
    "                                           X"


]





level_blob_monster_warning = [
    "  X                               X       ",
    "  X                            X       ",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXX  XXXXXXXXXXXXXXXXXXXXX",
    "X                     X            ",
    "X                     X             ",
    "X                Q      X             ",
    "XXXXXXXXXXX   XXX  XXXX    XXXXXXXXXXXXX",
    "                                         ",
    "                                         ",
    "                                         ",
    "                                         ",
    "                                         ",
"XXXXXXXXXXXXXXXXXXXX                          XX",
    "                                             ",
    "                                             ",
    "                                             ",
    "                                             ",
    "                                             ",
    "                                           X",
    "                                           X",
    "                                          XPX                   $ ",
    "                                           X"


]




level_C2_locked_door = [
    "  X                               X       ",
    "  X                            X       ",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXX  XXXXXXXXXXXXXXXXXXXXX",
    "X                     X            ",
    "X                     X             ",
    "X                -      X             ",
    "XXXXXXXXXXX   XXX  XXXX    XXXXXXXXXXXXX",
    "                                         ",
    "                                         ",
    "                                         ",
    "                                         ",
    "                                         ",
"XXXXXXXXXXXXXXXXXXXX                          XX",
    "                                             ",
    "                                             ",
    "                                             ",
    "                                             ",
    "                                             ",
    "                                           X",
    "                                           X",
    "                                          XPX                   = ",
    "                                           X"


]




level_blob_monster_death_zero = [
    "  X                               X       ",
    "  X                            X       ",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXX  XXXXXXXXXXXXXXXXXXXXX",
    "X                     X            ",
    "X                     X             ",
    "X                A      X             ",
    "XXXXXXXXXXX   XXX  XXXX    XXXXXXXXXXXXX",
    "                                         ",
    "                                         ",
    "                                         ",
    "                                         ",
    "                                         ",
"XXXXXXXXXXXXXXXXXXXX                          XX",
    "                                             ",
    "                                             ",
    "                                             ",
    "                                             ",
    "                                             ",
    "                                           X",
    "                                           X",
    "                                          XPX                   1 ",
    "                                           X"


]




level_blob_monster_death_one = [
    "  X                               X       ",
    "  X                            X       ",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXX  XXXXXXXXXXXXXXXXXXXXX",
    "X                     X            ",
    "X                     X             ",
    "X                B      X             ",
    "XXXXXXXXXXX   XXX  XXXX    XXXXXXXXXXXXX",
    "                                         ",
    "                                         ",
    "                                         ",
    "                                         ",
    "                                         ",
"XXXXXXXXXXXXXXXXXXXX                          XX",
    "                                             ",
    "                                             ",
    "                                             ",
    "                                             ",
    "                                             ",
    "                                           X",
    "                                           X",
    "                                          XPX                   2 ",
    "                                           X"


]



level_blob_monster_death_two = [
    "  X                               X       ",
    "  X                            X       ",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXX  XXXXXXXXXXXXXXXXXXXXX",
    "X                     X            ",
    "X                     X             ",
    "X                C      X             ",
    "XXXXXXXXXXX   XXX  XXXX    XXXXXXXXXXXXX",
    "                                         ",
    "                                         ",
    "                                         ",
    "                                         ",
    "                                         ",
"XXXXXXXXXXXXXXXXXXXX                          XX",
    "                                             ",
    "                                             ",
    "                                             ",
    "                                             ",
    "                                             ",
    "                                           X",
    "                                           X",
    "                                          XPX                   3 ",
    "                                           X"


]




level_blob_monster_death_three = [
    "  X                               X       ",
    "  X                            X       ",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXX  XXXXXXXXXXXXXXXXXXXXX",
    "X                     X            ",
    "X                     X             ",
    "X                D      X             ",
    "XXXXXXXXXXX   XXX  XXXX    XXXXXXXXXXXXX",
    "                                         ",
    "                                         ",
    "                                         ",
    "                                         ",
    "                                         ",
"XXXXXXXXXXXXXXXXXXXX                          XX",
    "                                             ",
    "                                             ",
    "                                             ",
    "                                             ",
    "                                             ",
    "                                           X",
    "                                           X",
    "                                          XPX                   4 ",
    "                                           X"


]




level_blob_monster_death_four = [
    "  X                               X       ",
    "  X                            X       ",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXX  XXXXXXXXXXXXXXXXXXXXX",
    "X                     X            ",
    "X                     X             ",
    "X                E      X             ",
    "XXXXXXXXXXX   XXX  XXXX    XXXXXXXXXXXXX",
    "                                         ",
    "                                         ",
    "                                         ",
    "                                         ",
    "                                         ",
"XXXXXXXXXXXXXXXXXXXX                          XX",
    "                                             ",
    "                                             ",
    "                                             ",
    "                                             ",
    "                                             ",
    "                                           X",
    "                                           X",
    "                                          XPX                   5 ",
    "                                           X"


]




level_blob_monster_death_final = [
    "  X                               X       ",
    "  X                            X       ",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXX  XXXXXXXXXXXXXXXXXXXXX",
    "X                     X            ",
    "X                     X             ",
    "X                F      X             ",
    "XXXXXXXXXXX   XXX  XXXX    XXXXXXXXXXXXX",
    "                                         ",
    "                                         ",
    "                                         ",
    "                                         ",
    "                                         ",
"XXXXXXXXXXXXXXXXXXXX                          XX",
    "                                             ",
    "                                             ",
    "                                             ",
    "                                             ",
    "                                             ",
    "                                           X",
    "                                           X",
    "                                          XPX                   6 ",
    "                                           X"


]






level_blob_monster_warning_one = [
    "  X                               X       ",
    "  X                            X       ",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXX  XXXXXXXXXXXXXXXXXXXXX",
    "X                     X            ",
    "X                     X             ",
    "X                U      X             ",
    "XXXXXXXXXXX   XXX  XXXX    XXXXXXXXXXXXX",
    "                                         ",
    "                                         ",
    "                                         ",
    "                                         ",
    "                                         ",
"XXXXXXXXXXXXXXXXXXXX                          XX",
    "                                             ",
    "                                             ",
    "                                             ",
    "                                             ",
    "                                             ",
    "                                           X",
    "                                           X",
    "                                          XPX                   $ ",
    "                                           X"


]




level_blob_monster_warning_two = [
    "  X                               X       ",
    "  X                            X       ",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXX  XXXXXXXXXXXXXXXXXXXXX",
    "X                     X            ",
    "X                     X             ",
    "X                V      X             ",
    "XXXXXXXXXXX   XXX  XXXX    XXXXXXXXXXXXX",
    "                                         ",
    "                                         ",
    "                                         ",
    "                                         ",
    "                                         ",
"XXXXXXXXXXXXXXXXXXXX                          XX",
    "                                             ",
    "                                             ",
    "                                             ",
    "                                             ",
    "                                             ",
    "                                           X",
    "                                           X",
    "                                          XPX                   8 ",
    "                                           X"


]


level_exam_entrance_one = [
    "  X                               X       ",
    "  X                            X       ",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXX  XXXXXXXXXXXXXXXXXXXXX",
    "X                     X            ",
    "X                     X             ",
    "X                A      X             ",
    "XXXXXXXXXXX   XXX  XXXX    XXXXXXXXXXXXX",
    "                                         ",
    "                                         ",
    "                                         ",
    "                                         ",
    "                                         ",
"XXXXXXXXXXXXXXXXXXXX                          XX",
    "                                             ",
    "                                             ",
    "                                             ",
    "                                             ",
    "                                             ",
    "                                           X",
    "                                           X",
    "                                          XPX                   1 ",
    "                                           X"


]



level_exam_entrance_two = [
    "  X                               X       ",
    "  X                            X       ",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXX  XXXXXXXXXXXXXXXXXXXXX",
    "X                     X            ",
    "X                     X             ",
    "X                B      X             ",
    "XXXXXXXXXXX   XXX  XXXX    XXXXXXXXXXXXX",
    "                                         ",
    "                                         ",
    "                                         ",
    "                                         ",
    "                                         ",
"XXXXXXXXXXXXXXXXXXXX                          XX",
    "                                             ",
    "                                             ",
    "                                             ",
    "                                             ",
    "                                             ",
    "                                           X",
    "                                           X",
    "                                          XPX                   2 ",
    "                                           X"


]


level_exam_entrance_three = [
    "  X                               X       ",
    "  X                            X       ",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXX  XXXXXXXXXXXXXXXXXXXXX",
    "X                     X            ",
    "X                     X             ",
    "X                C      X             ",
    "XXXXXXXXXXX   XXX  XXXX    XXXXXXXXXXXXX",
    "                                         ",
    "                                         ",
    "                                         ",
    "                                         ",
    "                                         ",
"XXXXXXXXXXXXXXXXXXXX                          XX",
    "                                             ",
    "                                             ",
    "                                             ",
    "                                             ",
    "                                             ",
    "                                           X",
    "                                           X",
    "                                          XPX                   3 ",
    "                                           X"


]




level_exam_entrance_four = [
    "  X                               X       ",
    "  X                            X       ",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXX  XXXXXXXXXXXXXXXXXXXXX",
    "X                     X            ",
    "X                     X             ",
    "X                D      X             ",
    "XXXXXXXXXXX   XXX  XXXX    XXXXXXXXXXXXX",
    "                                         ",
    "                                         ",
    "                                         ",
    "                                         ",
    "                                         ",
"XXXXXXXXXXXXXXXXXXXX                          XX",
    "                                             ",
    "                                             ",
    "                                             ",
    "                                             ",
    "                                             ",
    "                                           X",
    "                                           X",
    "                                          XPX                   4 ",
    "                                           X"


]




level_exam_entrance_five = [
    "  X                               X       ",
    "  X                            X       ",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXX  XXXXXXXXXXXXXXXXXXXXX",
    "X                     X            ",
    "X                     X             ",
    "X                E      X             ",
    "XXXXXXXXXXX   XXX  XXXX    XXXXXXXXXXXXX",
    "                                         ",
    "                                         ",
    "                                         ",
    "                                         ",
    "                                         ",
"XXXXXXXXXXXXXXXXXXXX                          XX",
    "                                             ",
    "                                             ",
    "                                             ",
    "                                             ",
    "                                             ",
    "                                           X",
    "                                           X",
    "                                          XPX                   5 ",
    "                                           X"


]



level_exam_entrance_six = [
    "  X                               X       ",
    "  X                            X       ",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXX  XXXXXXXXXXXXXXXXXXXXX",
    "X                     X            ",
    "X                     X             ",
    "X                F      X             ",
    "XXXXXXXXXXX   XXX  XXXX    XXXXXXXXXXXXX",
    "                                         ",
    "                                         ",
    "                                         ",
    "                                         ",
    "                                         ",
"XXXXXXXXXXXXXXXXXXXX                          XX",
    "                                             ",
    "                                             ",
    "                                             ",
    "                                             ",
    "                                             ",
    "                                           X",
    "                                           X",
    "                                          XPX                   6 ",
    "                                           X"


]



level_exam_hand_monster_trigger_one = [
    "  X                               X       ",
    "  X                            X       ",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXX  XXXXXXXXXXXXXXXXXXXXX",
    "X                     X            ",
    "X                     X             ",
    "X                G      X             ",
    "XXXXXXXXXXX   XXX  XXXX    XXXXXXXXXXXXX",
    "                                         ",
    "                                         ",
    "                                         ",
    "                                         ",
    "                                         ",
"XXXXXXXXXXXXXXXXXXXX                          XX",
    "                                             ",
    "                                             ",
    "                                             ",
    "                                             ",
    "                                             ",
    "                                           X",
    "                                           X",
    "                                          XPX                   7 ",
    "                                           X"


]










level_C4_near_hole = [
           "XXXXEXXXX",
           "XX     XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
           "XX     XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
           "XX     XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
           "XXY  PZXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
           "XX     XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
           "XX     XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
           "XX  V  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
           "XXXXXXXXX"


]

#First Version of hallway

level_0 = [
    "  X                               X       "
    "  X                             X       ",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XYXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XBXXXXXXXXXXXXXHHXXLLXXXXXXXXXXXXXXXXX",
    "XU       C  S         XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX            ",
    "X           S         XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX             ",
    "X  P        S         XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX             ",
    "XXEEXXXTTTXXXX)XXXXZZXXXX    XXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

]




level_after_blob_monster_warning = [
    "  X                               X       "
    "  X                             X       ",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XYXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XBXXXXXXXXXXXXXHHXXLLXXXXXXXXXXXXXXXXX",
    "XP       C  S        XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX            ",
    "X           S        XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX             ",
    "X           S        XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX             ",
    "XXEEXXXTTTXXXX)XXXXZZXXXX    XXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

]


level_outside_C2 = [
    "  X                               X       "
    "  X                             X       ",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XYXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XBXXXXXXXXXXXXXHHXXLLXXXXXXXXXXXXXXXXX",
    "X        C  S         XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX            ",
    "X           S         XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX             ",
    "X           S P       XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX             ",
    "XXEEXXXTTTXXXX)XXXXZZXXXX    XXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

]




level_outside_C1 = [
    "  X                               X       "
    "  X                             X       ",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XYXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XBXXXXXXXXXXXXXHHXXLLXXXXXXXXXXXXXXXXX",
    "X        C  S         XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX            ",
    "X           S         XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX             ",
    "X           S       P XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX             ",
    "XXEEXXXTTTXXXX)XXXXZZXXXX    XXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

]


level_outside_bathroom = [
    "  X                               X       "
    "  X                             X       ",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XYXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XBXXXXXXXXXXXXXHHXXLLXXXXXXXXXXXXXXXXX",
    "X        C  S  P      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX            ",
    "X           S         XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX             ",
    "X           S         XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX             ",
    "XXEEXXXTTTXXXX)XXXXZZXXXX    XXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

]




level_exit_blood_message_hallway = [
    "  X                               X       "
    "  X                             X       ",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XYXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XBXXXXXXXXXXXXXHHXXLLXXXXXXXXXXXXXXXXX",
    "X        C  S         XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX            ",
    "X        P  S         XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX             ",
    "X           S         XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX             ",
    "XXEEXXXTTTXXXX)XXXXZZXXXX    XXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

]


level_player_coming_out_of_C3 = [
    "  X                               X       "
    "  X                             X       ",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XYXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XBXXXXXXXXXXXXXHHXXLLXXXXXXXXXXXXXXX",
    "X        C  S         XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX            ",
    "X           S         XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "X        P  S         XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX             ",
    "XXEEXXXTTTXXXX)XXXXZZXXXX    XXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

]




level_hallway_version_2 = [
    "  X                               X       "
    "  X                           XXX  X       ",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XYXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXX  XXLLXXXXXXXXXXXXXXX",
    "X                   P XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX            ",
    "X                     XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX             ",
    "X       B             XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX             ",
    "XXEEXXXXXXXXXGGGXXXZZXXXX    XXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

]


level_player_coming_out_of_C2_without_key = [
    "  X                               X       "
    "  X                             X       ",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XYXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXX  XXLLXXXXXXXXXXXXXXX",
    "X                     XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX            ",
    "X                     XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX             ",
    "X       B      P      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX             ",
    "XXEEXXXXXXXXXGGGXXXZZXXXX    XXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

]




level_hallway_version_3 = [
    "  X                               X       ",
    "  X                             X       ",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XYXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XR                   2XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX            ",
    "XR                   4XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX             ",
    "XR             P     5XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX             ",
    "XXXXXXXXXXXXXXXXXXXXXXXXX    XXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
     "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
      "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

]


level_hallway_exit = [

    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXXWSXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXX67XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXX  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXX  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXXX  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "    X                XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "    X  B            PXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXOXXXXXXX",

]

hospital_bed_with_lights = []
monsters=[]
doors = []
other = []
items = []
spiders = []
spiderwebs = []
spiderwebs2 = []
decorations = []
exam_entrances = []
exam_exits = []
C2_entrances = []
C2_exits = []
exit_hallways = []
exit_to_pools = []
pools = []
door_to_exit_games = []
hand_monster_hallways = []
hand_monster_hallways2 = []
hand_monster_hallways3 = []
spider_monster_hallways2 = []
spider_monster_hallways3 = []
door_bed_no_flashlights = []
C4_hole_triggers = []
blood_messages = []

textone = []

levels.append(level_0)
levels.append(level_1)
levels.append(level_2)
levels.append(level_3)
levels.append(level_player_coming_out_of_C3)
levels.append(level_examinationroom)
levels.append(level_examination_room_with_monster)
levels.append(level_hallway_version_2)
levels.append(level_C2)
levels.append(level_C2_with_moving_monster)
levels.append(level_player_coming_out_of_C2_without_key)
levels.append(level_hallway_version_3)
levels.append(level_hallway_exit)
levels.append(level_pool_area)






levels.append(level_with_text) #15
levels.append(level_with_text_C4_text_one) #16
levels.append(level_with_text_C4_text_two)#17
levels.append(level_with_text_C4_text_three)#18
levels.append(level_with_text_C4_see_door_without_flashlight_one)#19
levels.append(level_with_text_C4_see_door_without_flashlight_two)#20
levels.append(level_failed_exit_C4)#21
levels.append(level_with_text_C4_look_at_the_bed)#22
levels.append(level_with_text_C4_text_flashlight)#23

levels.append(level_with_text_C4_text_bed_with_flashlight)#24
levels.append(level_with_text_C4_threatening_message)#25
levels.append(level_with_text_C4_hole_one)#26
levels.append(level_with_text_C4_hole_two)#27
levels.append(level_with_text_C4_hole_three)#28
levels.append(level_with_text_C4_hole_four)#29
levels.append(level_with_text_C4_hole_five)#30
levels.append(level_with_text_C4_exit)#31
levels.append(level_C4_near_hole)#32
levels.append(level_C4_near_hospital_bed_with_light)#33
levels.append(level_exit_message)#34
levels.append(level_with_text_C4_exit)#35
levels.append(level_C4_reenter)#36
levels.append(level_with_text_C4_exit_two)#37
levels.append(level_C3_entrance_text)#38
levels.append(level_hallway_one_blood_message)#39
levels.append(level_hallway_two_blood_message)#40
levels.append(level_hallway_three_blood_message)#41
levels.append(level_exit_blood_message_hallway)#42
levels.append(level_bathroom_entrance)#43
levels.append(level_outside_bathroom)#44
levels.append(level_C3_enter_text)#45
levels.append(level_C1_entry)#46
levels.append(level_outside_C1)#47
levels.append(level_C3_game_over_one_text)#48
levels.append(level_C3_game_over_two_text)
levels.append(level_C3_game_over_three_text)
levels.append(level_C3_game_over_four_text)
levels.append(level_C3_game_over_five_text)
levels.append(level_C3_game_over_six_text)
levels.append(level_C3_game_over_seven_text)
levels.append(level_C3_game_over_final)
levels.append(level_C2_locked_door)
levels.append(level_outside_C2)
levels.append(level_blob_monster_death_zero)
levels.append(level_blob_monster_death_one)
levels.append(level_blob_monster_death_two)
levels.append(level_blob_monster_death_three)
levels.append(level_blob_monster_death_four)
levels.append(level_blob_monster_death_final)
levels.append(level_blob_monster_warning)
levels.append(level_blob_monster_warning_one)
levels.append(level_blob_monster_warning_two)
levels.append(level_after_blob_monster_warning)
levels.append(level_exam_entrance_one)
levels.append(level_exam_entrance_two)
levels.append(level_exam_entrance_three)
levels.append(level_exam_entrance_four)
levels.append(level_exam_entrance_five)
levels.append(level_exam_entrance_six)
levels.append(level_exam_hand_monster_trigger_one)









blood_messages_twos = []
C1_doors = []
dead_bodies = []
blob_monster_warnings = []
blob_monster_warning_doors = []
broken_glasses = []





#first hallway with blob monster
def setup_maze_0(level):



    for y in range (len(level)):
        for x in range (len(level[y])):
            character = level[y][x]

            screen_x= -60 + (x*24)
            screen_y= 45 - (y*24)


            if character == "X":
                pen.goto(screen_x, screen_y)
                pen.stamp()
                walls.append((screen_x, screen_y))

            if character == "P":
                player.goto(screen_x, screen_y)



            if character == "B":
                monsters.append(Blobmonster(screen_x, screen_y))
                # walls.append((screen_x, screen_y))


            if character == "Y":
                dead_bodies.append(Dead_Body(screen_x, screen_y))



            if character == "U":
                blob_monster_warning_doors.append(Door_2(screen_x, screen_y))


            if character == "D":

                doors.append(Door(screen_x, screen_y))


            if character == "E":
                other.append(Door_2(screen_x, screen_y))

            if character == "T":
                secondroomentrances.append(DoortoenterC3(screen_x, screen_y))

            if character == "L":
                exam_entrances.append(Door_to_enter_examination_room(screen_x, screen_y))

            if character == "S":
                broken_glasses.append(Broken_Glass(screen_x, screen_y))

            if character == "G":
                C2_entrances.append(Door_to_Enter_C2(screen_x, screen_y))

            if character == "H":
                bathroom_entrances.append(Door_2(screen_x, screen_y))

            if character == "C":
                blood_messages_triggers.append(C4_threatening_message(screen_x, screen_y))

            if character == "Z":
                C1_doors.append(Door_2(screen_x, screen_y))

            if character == ")":
                C2_password_lockeds.append(Door_2(screen_x, screen_y))


def setup_maze_without_flashlight(level):



    for y in range (len(level)):
        for x in range (len(level[y])):
            character = level[y][x]

            screen_x= -60 + (x*24)
            screen_y= -545 - (y*24)


            if character == "X":
                pen.goto(screen_x, screen_y)
                pen.stamp()
                walls.append((screen_x, screen_y))

            if character == "P":
                player.goto(screen_x, screen_y)

            if character == "B":
                monsters.append(Blobmonster(screen_x, screen_y))


            if character == "D":

                doors.append(Door(screen_x, screen_y))

            if character == "E":
                other.append(Door_2(screen_x, screen_y))

            if character == "H":
                hospitalbeds.append(Hospital_Bed(screen_x, screen_y))



















#first room where player wakes up

def setup_maze(level):

    for y in range (len(level)):
        for x in range (len(level[y])):
            character = level[y][x]

            screen_x= -92 + (x*24)
            screen_y= -130 - (y*24)


            if character == "X":
                pen.goto(screen_x, screen_y)
                pen.stamp()
                walls.append((screen_x, screen_y))

            if character == "P":
                player.goto(screen_x, screen_y)



            if character == "D":

                doors.append(Door(screen_x, screen_y))

            if character == "E":
                C4_returns.append(Door_2(screen_x, screen_y))

            if character == "H":
                hospitalbeds.append(Hospital_Bed(screen_x, screen_y))

            if character == "F":
                items.append(Flashlight(screen_x, screen_y))


            if character == "G":
                door_bed_no_flashlights.append(C4_Door_Text_Bed_No_Flashlight(screen_x, screen_y))


            if character == "Y":
                blood_messages.append(C4_threatening_message(screen_x, screen_y))


            if character == "V":
                second_hospital_beds.append(Hospital_Bed_Two(screen_x, screen_y))


            if character == "Z":
                C4_hole_triggers.append(C4_Text_Hole(screen_x, screen_y))




            if character == "4":
                C4_blocked_exits.append(C4_Blocked_Door(screen_x, screen_y))




#last maze of the game
def setup_maze_1(level):

    for y in range (len(level)):
        for x in range (len(level[y])):
            character = level[y][x]

            screen_x= -62 + (x*24)
            screen_y= 70 - (y*24)


            if character == "X":
                pen.goto(screen_x, screen_y)
                pen.stamp()
                walls.append((screen_x, screen_y))

            if character == "P":
                player.goto(screen_x, screen_y)

            if character == "B":
                monsters.append(Blobmonster(screen_x, screen_y))
                walls.append((screen_x, screen_y))

            if character == "D":

                doors.append(Door(screen_x, screen_y))

            if character == "E":
                doors.append(Door_2(screen_x, screen_y))

            if character == "F":
                items.append(Flashlight(screen_x, screen_y))

            if character == "R":
                exit_hallways.append(Door_to_Exit_Hallway(screen_x, screen_y))

            if character == "Z":
                handmonsters.append(Handmonster(screen_x, screen_y))

            if character == "2":
                hand_monster_hallways.append(Hand_Monster_Hallway(screen_x, screen_y))

            if character == "4":
                hand_monster_hallways2.append(Hand_Monster_Hallway(screen_x, screen_y))

            if character == "5":
                hand_monster_hallways3.append(Hand_Monster_Hallway(screen_x, screen_y))


def setup_maze_exit(level):

    for y in range (len(level)):
        for x in range (len(level[y])):
            character = level[y][x]

            screen_x= -580 + (x*24)
            screen_y= 60 - (y*24)


            if character == "X":
                pen.goto(screen_x, screen_y)
                pen.stamp()
                walls.append((screen_x, screen_y))

            if character == "P":
                player.goto(screen_x, screen_y)


            if character == "H":
                 hospitalbeds.append(Hospital_Bed(screen_x, screen_y))

            if character == "S":
                spiders.append(Spidermonster(screen_x, screen_y))

            if character == "6":
                spider_monster_hallways2.append(Spidermonster(screen_x, screen_y))

            if character == "7":
                spider_monster_hallways3.append(Spidermonster(screen_x, screen_y))

            if character == "W":
                spiderwebs.append(Spiderwebs(screen_x, screen_y))

            if character == "B":
                monsters.append(Blobmonster(screen_x, screen_y))


            if character == "O":
                exit_to_pools.append(Door_to_Exit_to_Pool_Area(screen_x, screen_y))






def setup_maze_pool_area(level):

    for y in range (len(level)):
        for x in range (len(level[y])):
            character = level[y][x]

            screen_x= -540 + (x*24)
            screen_y= -150 - (y*24)


            if character == "X":
                pen.goto(screen_x, screen_y)
                pen.stamp()
                walls.append((screen_x, screen_y))

            if character == "P":
                player.goto(screen_x, screen_y)

            if character == "3":
                pools.append(Pool(screen_x, screen_y))

            if character == "9":
                door_to_exit_games.append(Door_to_exit_game(screen_x, screen_y))



















def setup_maze_C3(level):

    for y in range (len(level)):
        for x in range (len(level[y])):
            character = level[y][x]

            screen_x= 36 + (x*24)
            screen_y= -130 - (y*24)


            if character == "X":
                pen.goto(screen_x, screen_y)
                pen.stamp()
                walls.append((screen_x, screen_y))

            if character == "P":
                player.goto(screen_x, screen_y)



            if character == "E":
                doors.append(Door_2(screen_x, screen_y))

            if character == "W":
                spiderwebs.append(Spiderwebs(screen_x, screen_y))

            if character == "1":
                spiderwebs2.append(Spiderwebs(screen_x, screen_y))

            if character == "C":
                secondroomexits.append(DoortoexitC3(screen_x, screen_y))

            if character == "S":
                spiders.append(Spidermonster(screen_x, screen_y))



def setup_maze_C2(level):

    for y in range (len(level)):
        for x in range (len(level[y])):
            character = level[y][x]

            screen_x= 176 + (x*24)
            screen_y= -130 - (y*24)


            if character == "X":
                pen.goto(screen_x, screen_y)
                pen.stamp()
                walls.append((screen_x, screen_y))

            if character == "P":
                player.goto(screen_x, screen_y)

            if character == "I":
                C2_exits.append(Door_to_Exit_C2(screen_x, screen_y))

            if character == "V":
                bodybagmonsters.append(Body_Bag_monster(screen_x, screen_y))

            if character == "K":
                keys.append(Key(screen_x, screen_y))

            if character == "U":
                bodybagmonstermovings.append(Body_Bag_monster_moving(screen_x, screen_y))
            if character == "J":
                C2_exit_with_keys.append(Door_to_Exit_C2_with_key(screen_x, screen_y))
















def setup_maze_Examination_room(level):

    for y in range (len(level)):
        for x in range (len(level[y])):
            character = level[y][x]

            screen_x= 300 + (x*24)
            screen_y= 180 - (y*24)


            if character == "X":
                pen.goto(screen_x, screen_y)
                pen.stamp()
                walls.append((screen_x, screen_y))

            if character == "P":
                player.goto(screen_x, screen_y)

            if character == "C":
                hospitalbeds2.append(Hospital_Bed(screen_x, screen_y))

            if character == "Y":
                triggerhandmonsters.append(Trigger_Hand_Monster(screen_x, screen_y))

            if character == "Z":
                handmonsters.append(Handmonster(screen_x, screen_y))

            if character == "8":
                handmonsters2.append(Handmonster(screen_x, screen_y))

            if character == "9":
                handmonsters3.append(Handmonster(screen_x, screen_y))

            if character == "1":
                handmonsters4.append(Handmonster(screen_x, screen_y))

            if character == "2":
                handmonsters5.append(Handmonster(screen_x, screen_y))

            if character == "3":
                handmonsters6.append(Handmonster(screen_x, screen_y))

            if character == "4":
                handmonsters7.append(Handmonster(screen_x, screen_y))

            if character == "5":
                handmonsters8.append(Handmonster(screen_x, screen_y))

            if character == "6":
                handmonsters9.append(Handmonster(screen_x, screen_y))

            if character == "7":
                handmonsters10.append(Handmonster(screen_x, screen_y))

            if character == "A":
                exam_exits.append(Door_to_exit_examination_room(screen_x, screen_y))

            



C4_texts = []
C4_text_twos = []
C4_text_threes = []
C4_text_fours = []
C4_text_fives = []
C4_door_second_boxes = []
C4_text_no_flashlight_ones = []
C4_text_no_flashlight_twos = []

start_games = []
C4_blocked_exits = []
C4_blocked_second_exits = []
C4_blocked_exit_return_to_games = []
C4_bed_without_flashlights = []
C4_exit_door_beds = []
C4_find_flashlight_texts = []
C4_exit_flashlights = []
C4_text_threatening_messages = []
C4_text_hole_ones = []
C4_exit_to_hole_twos = []
C4_exit_to_hole_threes = []
C4_exit_to_hole_fours = []
C4_exit_to_hole_fives = []
C4_exit_hole_texts = []
C4_exit_blood_messages = []
C4_bed_with_flashlights = []
second_hospital_beds = []
C4_exit_second_bed_texts = []
C4_exits = []
C4_exit_door_end_texts = []
C4_returns = []
C4_reenter_texts = []
C4_reenter_exit_texts = []
C4_exit_text_twos = []
C4_door_to_exit_text_twos = []

def text_level(level):
    for y in range(len(level)):
        for x in range(len(level[y])):
            character = level[y][x]

            screen_x = -350 + (x * 24)
            screen_y = 205 - (y * 24)

            if character == "X":
                pen.goto(screen_x, screen_y)
                pen.stamp()
                walls.append((screen_x, screen_y))

            if character == "P":
                player.goto(screen_x, screen_y)


            if character == "1":
                textone.append(Firsttextbox(screen_x, screen_y))

            if character == "A":
                C4_texts.append(C4_Text_One(screen_x, screen_y))

            if character == "B":
                C4_text_twos.append(C4_Text_Two(screen_x, screen_y))

            if character == "C":
                C4_text_threes.append(C4_Text_Three(screen_x, screen_y))

            if character == "D":
                C4_text_no_flashlight_ones.append(C4_Text_No_Flashlight_One(screen_x, screen_y))

            if character == "E":
                C4_text_no_flashlight_twos.append(C4_Text_No_Flashlight_Two(screen_x, screen_y))


            if character == "K":
                C4_texts.append(C4_Text_hole_One(screen_x, screen_y))

            if character == "L":
                C4_text_twos.append(C4_Text_hole_Two(screen_x, screen_y))

            if character == "M":
                C4_text_threes.append(C4_Text_hole_Three(screen_x, screen_y))

            if character == "N":
                C4_text_fours.append(C4_Text_hole_Four(screen_x, screen_y))

            if character == "O":
                C4_text_fives.append(C4_Text_hole_Five(screen_x, screen_y))



            if character == "?":
                C4_bed_with_flashlights.append(C4_Text_Bed_With_Flashlight(screen_x, screen_y))

            if character == "!":
                C4_exits.append(C4_Text_Exit(screen_x, screen_y))


            if character == "/":
                C4_reenter_texts.append(C4_Reenter_Text(screen_x, screen_y))


            if character == "}":
                C4_reenter_exit_texts.append(C4_Door_Reenter(screen_x, screen_y))


            if character == "G":
                no_flashlight_beds.append(C4_Text_Look_At_Bed(screen_x, screen_y))

            if character == "H":
                C4_bed_without_flashlights.append(C4_Text_Look_At_Bed(screen_x, screen_y))

            if character == "I":
                C4_find_flashlight_texts.append(C4_Text_Find_Flashlight(screen_x, screen_y))

            if character == "J":
                C4_text_threatening_messages.append(C4_Text_Threatening_Message(screen_x, screen_y))

            if character == "#":
                C4_exit_text_twos.append(C4_Exit_End_Door_Two(screen_x, screen_y))


            if character == "$":
                C4_door_to_exit_text_twos.append(Door_2(screen_x, screen_y))

            if character == "R":
                exit_text.append(Door_to_Exit_Text_Box(screen_x, screen_y))

            if character == "2":
                C4_door_second_boxes.append(Door_To_Second_C4_Textbox(screen_x, screen_y))

            if character == "3":
                start_games.append(Door_To_Start_Game(screen_x, screen_y))

            if character == "4":
                C4_blocked_second_exits.append(C4_Blocked_Second_Door(screen_x, screen_y))

            if character == "5":
                C4_blocked_exit_return_to_games.append(C4_Blocked_Return_To_Game(screen_x, screen_y))

            if character == "6":
                C4_exit_door_beds.append(C4_Door_Text_Exit_No_Flashlight_Bed(screen_x, screen_y))

            if character == "7":
                C4_exit_flashlights.append(C4_Door_Text_Exit_Flashlight(screen_x, screen_y))

            if character == "8":
                C4_exit_blood_messages.append(C4_Exit_Blood_Text(screen_x, screen_y))

            if character == "9":
                C4_exit_to_hole_twos.append(C4_Exit_To_Hole_Two(screen_x, screen_y))

            if character == "0":
                C4_exit_to_hole_threes.append(C4_Exit_To_Hole_Three(screen_x, screen_y))

            if character == "Q":
                C4_exit_to_hole_fours.append(C4_Exit_To_Hole_Four(screen_x, screen_y))

            if character == "S":
                C4_exit_to_hole_fives.append(C4_Exit_To_Hole_Five(screen_x, screen_y))

            if character == "T":
                C4_exit_hole_texts.append(C4_Exit_Hole_Text(screen_x, screen_y))

            if character == "W":
                C4_exit_second_bed_texts.append(C4_Exit_Second_Bed_Text(screen_x, screen_y))

            if character == "@":
                C4_exit_door_end_texts.append(C4_Exit_End_Door(screen_x, screen_y))





bathroom_entrances = []
blood_messages_triggers = []
C3_entrance_texts = []
C3_exit_entrance_texts = []
hallway_blood_messages_triggers = []
hallway_blood_messages_ones = []
hallway_blood_messages_twos = []
hallway_exit_blood_message_texts = []
hallway_exit_blood_message_texts_ones = []
hallway_exit_blood_message_texts_twos = []
hallway_exit_blood_message_texts_ends = []
bathroom_locked_texts = []
hallway_exit_bathroom_entrances = []
C3_exit_to_hallways = []
C3_exit_text_ends = []
C1_entry_texts = []
C1_exit_entry_texts = []
C3_game_over_ones = []
C3_game_over_twos = []
C3_game_over_threes = []
C3_game_over_fours = []
C3_game_over_fives = []
C3_game_over_sixes = []
C3_game_over_sevens = []
C3_exit_door_ones = []
C3_exit_door_twos = []
C3_exit_door_threes = []
C3_exit_door_fours = []
C3_exit_door_fives = []
C3_exit_door_sixes = []
C3_exit_door_sevens = []
C3_final_game_overs = []
C3_final_door_game_overs = []
C2_password_lockeds = []
C2_door_text_exits = []
C2_locked_texts = []


def hallway_one_text_level(level):
    for y in range(len(level)):
        for x in range(len(level[y])):
            character = level[y][x]

            screen_x = -350 + (x * 24)
            screen_y = 205 - (y * 24)

            if character == "X":
                pen.goto(screen_x, screen_y)
                pen.stamp()
                walls.append((screen_x, screen_y))

            if character == "P":
                player.goto(screen_x, screen_y)

            if character == "A":
                bathroom_entrances.append(Door_2(screen_x, screen_y))

            if character == "C":
                C3_entrance_texts.append(C3_Entrance_Text(screen_x, screen_y))

            if character == "D":
                hallway_blood_messages_triggers.append(Hallway_Blood_Message(screen_x, screen_y))

            if character == "E":
                hallway_blood_messages_ones.append(Hallway_Blood_Message_One(screen_x, screen_y))

            if character == "F":
                hallway_blood_messages_twos.append(Hallway_Blood_Message_Two(screen_x, screen_y))

            if character == "I":
                bathroom_locked_texts.append(Bathroom_Text(screen_x, screen_y))

            if character == "J":
                C3_exit_text_ends.append(C3_Exit_Text(screen_x, screen_y))

            if character == "K":
                C3_game_over_ones.append(C3_Game_Over_One(screen_x, screen_y))

            if character == "L":
                C3_game_over_twos.append(C3_Game_Over_Two(screen_x, screen_y))

            if character == "N":
                C3_game_over_threes.append(C3_Game_Over_Three(screen_x, screen_y))

            if character == "O":
                C3_game_over_fours.append(C3_Game_Over_Four(screen_x, screen_y))

            if character == "R":
                C3_game_over_fives.append(C3_Game_Over_Five(screen_x, screen_y))

            if character == "S":
                C3_game_over_sixes.append(C3_Game_Over_Six(screen_x, screen_y))

            if character == "T":
                C3_game_over_sevens.append(C3_Game_Over_Seven(screen_x, screen_y))

            if character == "U":
                C3_final_game_overs.append(C3_Game_Over_Final(screen_x, screen_y))

            if character == "Q":
                C1_entry_texts.append(C1_Entry_Text(screen_x, screen_y))

            if character == "-":
                C2_locked_texts.append(C2_Locked(screen_x, screen_y))

            if character == "1":
                C3_exit_entrance_texts.append(Door_2(screen_x, screen_y))

            if character == "2":
                hallway_exit_blood_message_texts.append(Door_2(screen_x, screen_y))

            if character == "3":
                hallway_exit_blood_message_texts_ones.append(Door_2(screen_x, screen_y))

            if character == "4":
                hallway_exit_blood_message_texts_twos.append(Door_2(screen_x, screen_y))

            if character == "5":
                hallway_exit_blood_message_texts_ends.append(Door_2(screen_x, screen_y))

            if character == "6":
                hallway_exit_bathroom_entrances.append(Door_2(screen_x, screen_y))

            if character == "7":
                C3_exit_to_hallways.append(Door_2(screen_x, screen_y))

            if character == "$":
                C1_exit_entry_texts.append(Door_2(screen_x, screen_y))

            if character == "8":
                C3_exit_door_ones.append(Door_2(screen_x, screen_y))

            if character == "9":
                C3_exit_door_twos.append(Door_2(screen_x, screen_y))

            if character == "!":
                C3_exit_door_threes.append(Door_2(screen_x, screen_y))

            if character == "@":
                C3_exit_door_fours.append(Door_2(screen_x, screen_y))

            if character == "#":
                C3_exit_door_fives.append(Door_2(screen_x, screen_y))

            if character == "^":
                C3_exit_door_sixes.append(Door_2(screen_x, screen_y))

            if character == "*":
                C3_exit_door_sevens.append(Door_2(screen_x, screen_y))

            if character == "(":
                C3_final_door_game_overs.append(Door_2(screen_x, screen_y))


            if character == "=":
                C2_door_text_exits.append(Door_2(screen_x, screen_y))






blob_monster_death_zeros = []
blob_monster_death_ones = []
blob_monster_death_twos = []
blob_monster_death_threes = []
blob_monster_death_fours = []
blob_monster_text_exit_zeros = []
blob_monster_text_exit_ones = []
blob_monster_text_exit_twos = []
blob_monster_text_exit_threes = []
blob_monster_text_exit_fours = []
blob_monster_death_finals = []
blob_monster_text_exit_finals = []
blob_monster_warnings = []
blob_monster_warnings_texts = []
blob_monster_warning_text_exits = []
blob_monster_warning_two_doors = []
blob_monster_two_warnings = []





def blob_monster_one_text_level(level):
    for y in range(len(level)):
        for x in range(len(level[y])):
            character = level[y][x]

            screen_x = -350 + (x * 24)
            screen_y = 205 - (y * 24)

            if character == "X":
                pen.goto(screen_x, screen_y)
                pen.stamp()
                walls.append((screen_x, screen_y))

            if character == "P":
                player.goto(screen_x, screen_y)


            if character == "A":
                blob_monster_death_zeros.append(Blob_Monster_Death_Zero(screen_x, screen_y))

            if character == "B":
                blob_monster_death_ones.append(Blob_Monster_Death_One(screen_x, screen_y))

            if character == "C":
                blob_monster_death_twos.append(Blob_Monster_Death_Two(screen_x, screen_y))

            if character == "D":
                blob_monster_death_threes.append(Blob_Monster_Death_Three(screen_x, screen_y))

            if character == "E":
                blob_monster_death_fours.append(Blob_Monster_Death_Four(screen_x, screen_y))

            if character == "F":
                blob_monster_death_finals.append(Blob_Monster_Death_Final(screen_x, screen_y))

            if character == "Q":
                blob_monster_warnings_texts.append((screen_x, screen_y))


            if character == "U":
                blob_monster_warnings.append(Blob_Monster_Warning_One(screen_x, screen_y))

            if character == "V":
                blob_monster_two_warnings.append(Blob_Monster_Warning_Two(screen_x, screen_y))

            if character == "8":
                blob_monster_warning_two_doors.append(Door_2(screen_x, screen_y))


            if character == "1":
                blob_monster_text_exit_zeros.append(Door_2(screen_x, screen_y))

            if character == "2":
                blob_monster_text_exit_ones.append(Door_2(screen_x, screen_y))

            if character == "3":
                blob_monster_text_exit_twos.append(Door_2(screen_x, screen_y))

            if character == "4":
                blob_monster_text_exit_threes.append(Door_2(screen_x, screen_y))

            if character == "5":
                blob_monster_text_exit_fours.append(Door_2(screen_x, screen_y))

            if character == "6":
                blob_monster_text_exit_finals.append(Door_2(screen_x, screen_y))

            if character == "$":
                blob_monster_warning_text_exits.append(Door_2(screen_x, screen_y))






exam_room_enter_text_ones = []
exam_room_enter_text_twos = []
exam_room_enter_text_threes = []
exam_room_enter_text_fours = []
exam_room_enter_text_fives = []
exam_room_enter_text_sixes = []
exam_room_exit_text_ones = []
exam_room_exit_text_twos = []
exam_room_exit_text_threes = []
exam_room_exit_text_fours = []
exam_room_exit_text_fives = []
exam_room_exit_text_sixes = []


def exam_room_text_level(level):
    for y in range(len(level)):
        for x in range(len(level[y])):
            character = level[y][x]

            screen_x = -350 + (x * 24)
            screen_y = 205 - (y * 24)

            if character == "X":
                pen.goto(screen_x, screen_y)
                pen.stamp()
                walls.append((screen_x, screen_y))

            if character == "P":
                player.goto(screen_x, screen_y)


            if character == "A":
                exam_room_enter_text_ones.append(Exam_Entrance_Text_One(screen_x, screen_y))

            if character == "B":
                exam_room_enter_text_twos.append(Exam_Entrance_Text_Two(screen_x, screen_y))

            if character == "C":
                exam_room_enter_text_threes.append(Exam_Entrance_Text_Three(screen_x, screen_y))

            if character == "D":
                exam_room_enter_text_fours.append(Exam_Entrance_Text_Four(screen_x, screen_y))

            if character == "E":
                exam_room_enter_text_fives.append(Exam_Entrance_Text_Five(screen_x, screen_y))

            if character == "F":
                exam_room_enter_text_sixes.append(Exam_Entrance_Text_Six(screen_x, screen_y))


            if character == "1":
                exam_room_exit_text_ones.append(Door_2(screen_x, screen_y))


            if character == "2":
                exam_room_exit_text_twos.append(Door_2(screen_x, screen_y))

            if character == "3":
                exam_room_exit_text_threes.append(Door_2(screen_x, screen_y))


            if character == "4":
                exam_room_exit_text_fours.append(Door_2(screen_x, screen_y))


            if character == "5":
                exam_room_exit_text_fives.append(Door_2(screen_x, screen_y))


            if character == "6":
                exam_room_exit_text_sixes.append(Door_2(screen_x, screen_y))


















items=[]
hospitalbeds = []
hospitalbeds2 = []
secondroomentrances = []
secondroomexits = []
handmonsters = []
handmonsters2 = []
handmonsters3 = []
handmonsters4 = []
handmonsters5 = []
handmonsters6 = []
handmonsters7 = []
handmonsters8 = []
handmonsters9 = []
handmonsters10 = []
triggerhandmonsters = []
bodybagmonsters = []
bodybagmonstermovings = []
keys = []
C2_exit_with_keys = []
exit_text = []
no_flashlight_beds = []




#Create class instances
pen=Pen()
player = Player()


#Create wall coordinate list
walls=[]

length = len(handmonsters)

# Iterating the index
# same as 'for i in range(len(list))'


#setupthelevel


text_level(levels[16])



#Keyboard binding

turtle.listen()

turtle.onkey(player.go_left, "a")
turtle.onkey(player.go_right, "d")
turtle.onkey(player.go_up, "w")
turtle.onkey(player.close_text, "i")
turtle.onkey(player.go_down, "s")
turtle.onkey(player.toggle_pause, "p")

for monster in monsters:
    wn.ontimer(monster.move, t=250)

for spider in spiders:
    wn.ontimer(spider.move, t=250)

for handmonster in handmonsters:
    wn.ontimer(handmonster.move, t=250)

for hand_monster_hallway in hand_monster_hallways:
    wn.ontimer(hand_monster_hallway.move, t=250)

print(handmonsters)
print(hospitalbeds)





is_paused = True






while True:


    #iterate through enemy list to see if player collided






    for door_exit, C4_text in zip(exit_text, C4_texts):
        if player.is_collision(door_exit):
            C4_text.destroy()
            C4_texts.remove(C4_text)

            pen.clear()
            text_level(levels[17])

    wn.update()




    for C4_second_box, C4_text_two in zip(C4_door_second_boxes, C4_text_twos):

        if player.is_collision(C4_second_box):
            C4_text_two.destroy()
            C4_text_twos.remove(C4_text_two)


            pen.clear()
            text_level(levels[18])

    wn.update()


    for start_game, C4_text_three in zip(start_games, C4_text_threes):
        if player.is_collision(start_game):
            C4_text_three.destroy()
            C4_text_threes.remove(C4_text_three)

            pen.clear()



            setup_maze(levels[2])

    wn.update()



    for hospitalbed in hospitalbeds:
        if player.is_collision(hospitalbed):
            pen.clear()
            text_level(levels[22])

    for blocked_exit in C4_blocked_exits:
        if player.is_collision(blocked_exit):

            pen.clear()
            text_level(levels[19])

    wn.update()

    for blocked_second_exit, C4_text_no_flashlight_one in zip(C4_blocked_second_exits, C4_text_no_flashlight_ones):
        if player.is_collision(blocked_second_exit):
            C4_text_no_flashlight_one.destroy()
            C4_text_no_flashlight_ones.remove(C4_text_no_flashlight_one)

            pen.clear()
            text_level(levels[20])

    wn.update()


    for C4_blocked_exit_return_to_game, C4_text_no_flashlight_two in zip(C4_blocked_exit_return_to_games, C4_text_no_flashlight_twos):
        if player.is_collision(C4_blocked_exit_return_to_game):
            C4_text_no_flashlight_two.destroy()
            C4_text_no_flashlight_twos.remove(C4_text_no_flashlight_two)

            pen.clear()
            setup_maze(levels[21])

    wn.update()


    for door_bed_no_flashlight in door_bed_no_flashlights:
        if player.is_collision(door_bed_no_flashlight):
            pen.clear()
            text_level(levels[22])



    for C4_exit_bed_without_flashlight, C4_exit_door_bed in zip(C4_bed_without_flashlights, C4_exit_door_beds):
        if player.is_collision(C4_exit_door_bed):
            C4_exit_bed_without_flashlight.destroy()
            C4_bed_without_flashlights.remove(C4_exit_bed_without_flashlight)
            pen.clear()
            setup_maze(levels[2])


    for item, door, C4_blocked_exit in zip(items, hospitalbeds, C4_blocked_exits):
        if player.is_collision(item):
            item.destroy()
            items.remove(item)
            hospitalbed.destroy()
            hospitalbeds.remove(hospitalbed)
            C4_blocked_exit.destroy()
            C4_blocked_exits.remove(C4_blocked_exit)

            pen.clear()
            text_level(levels[23])
    wn.update()






    for C4_exit_flashlight, C4_find_flashlight_text in zip(C4_exit_flashlights, C4_find_flashlight_texts):
        if player.is_collision(C4_exit_flashlight):
            C4_find_flashlight_text.destroy()
            C4_find_flashlight_texts.remove(C4_find_flashlight_text)
            pen.clear()
            setup_maze(levels[3])


    for blood_message in blood_messages:
        if player.is_collision(blood_message):
            pen.clear()
            text_level(levels[25])

    for C4_exit_blood_message, C4_text_threatening_message in zip(C4_exit_blood_messages, C4_text_threatening_messages):
        if player.is_collision(C4_exit_blood_message):
            C4_text_threatening_message.destroy()
            C4_text_threatening_messages.remove(C4_text_threatening_message)
            pen.clear()
            setup_maze(levels[34])



    for C4_hole_trigger in C4_hole_triggers:
        if player.is_collision(C4_hole_trigger):
            pen.clear()
            text_level(levels[26])

    for C4_hole_two, C4_text in zip(C4_exit_to_hole_twos, C4_texts):
        if player.is_collision(C4_hole_two):
            C4_text.destroy()
            C4_texts.remove(C4_text)
            pen.clear()
            text_level(levels[27])

    for C4_hole_three, C4_text_two in zip(C4_exit_to_hole_threes, C4_text_twos):
        if player.is_collision(C4_hole_three):
            C4_text_two.destroy()
            C4_text_twos.remove(C4_text_two)
            pen.clear()
            text_level(levels[28])


    for C4_hole_four, C4_text_three in zip(C4_exit_to_hole_fours, C4_text_threes):
        if player.is_collision(C4_hole_four):
            C4_text_three.destroy()
            C4_text_threes.remove(C4_text_three)
            pen.clear()
            text_level(levels[29])


    for C4_hole_five, C4_text_four in zip(C4_exit_to_hole_fives, C4_text_fours):
        if player.is_collision(C4_hole_five):
            C4_text_four.destroy()
            C4_text_fours.remove(C4_text_four)
            pen.clear()
            text_level(levels[30])


    for C4_hole_exit, C4_text_five in zip(C4_exit_hole_texts, C4_text_fives):
        if player.is_collision(C4_hole_exit):
            C4_text_five.destroy()
            C4_text_fives.remove(C4_text_five)
            pen.clear()
            setup_maze(levels[32])


    for C4_bed_with_flashlight in hospital_bed_with_lights:
        if player.is_collision(C4_bed_with_flashlight):
            C4_bed_with_flashlight.destroy()
            hospital_bed_with_lights.remove(C4_bed_with_flashlight)
            pen.clear()
            setup_maze(levels[33])


    for hospital_bed_two in second_hospital_beds:
        if player.is_collision(hospital_bed_two):
            hospital_bed_two.destroy()
            second_hospital_beds.remove(hospital_bed_two)
            pen.clear()
            text_level(levels[24])

    for C4_exit_second_bed,  C4_bed_with_flashlight in zip(C4_exit_second_bed_texts, C4_bed_with_flashlights):
        if player.is_collision(C4_exit_second_bed):
            C4_bed_with_flashlight.destroy()
            C4_bed_with_flashlights.remove(C4_bed_with_flashlight)
            pen.clear()
            setup_maze(levels[33])


    for door, hospital_bed_two, C4_hole_trigger in zip(doors, second_hospital_beds, C4_hole_triggers):
        if player.is_collision(door):
            door.destroy()
            doors.remove(door)
            hospital_bed_two.destroy()
            second_hospital_beds.remove(hospital_bed_two)
            C4_hole_trigger.destroy()
            C4_hole_triggers.remove(C4_hole_trigger)
            blood_message.destroy()
            blood_messages.remove(blood_message)
            pen.clear()
            text_level(levels[35])


    for C4_end_exit, C4_exit, hospital_bed_two, blood_message, C4_hole_trigger in zip(C4_exit_door_end_texts, C4_exits,  second_hospital_beds, blood_messages, C4_hole_triggers):
        if player.is_collision(C4_end_exit):
             C4_exit.destroy()
             C4_exits.remove(C4_exit)
             hospital_bed_two.destroy()
             second_hospital_beds.remove(hospital_bed_two)
             blood_message.destroy()
             blood_messages.remove(blood_message)
             C4_hole_trigger.destroy()
             C4_hole_triggers.remove(C4_hole_trigger)
             pen.clear()
             text_level(levels[37])


    for C4_exit_text_two, C4_door_to_exit_text_two in zip(C4_exit_text_twos, C4_door_to_exit_text_twos ):
        if player.is_collision(C4_door_to_exit_text_two):
            C4_exit_text_two.destroy()
            C4_exit_text_twos.remove(C4_exit_text_two)
            pen.clear()
            setup_maze_0(levels[1])


    for C4_return in C4_returns:
        if player.is_collision(C4_return):
            C4_return.destroy()
            C4_returns.remove(C4_return)
            pen.clear()
            text_level(levels[35])

    for C4_reenter_text, C4_reenter_door in zip(C4_reenter_texts, C4_reenter_exit_texts):
        if player.is_collision(C4_reenter_door):

            C4_reenter_text.destroy()
            C4_reenter_texts.remove(C4_reenter_text)
            pen.clear()
            setup_maze(levels[3])


    for bathroom_entrance in bathroom_entrances:
        if player.is_collision(bathroom_entrance):
            bathroom_entrance.destroy()
            bathroom_entrances.remove(bathroom_entrance)
            pen.clear()
            hallway_one_text_level(levels[43])


    for  hallway_exit_bathroom_entrance, bathroom_locked_text in  zip(hallway_exit_bathroom_entrances, bathroom_locked_texts):
        if player.is_collision(hallway_exit_bathroom_entrance):
            bathroom_locked_text.destroy()
            bathroom_locked_texts.remove(bathroom_locked_text)
            pen.clear()
            setup_maze_0(levels[44])


    for   blob_monster_warning_door in blob_monster_warning_doors:
        if player.is_collision(blob_monster_warning_door):
            blob_monster_warning_door.destroy()
            blob_monster_warning_doors.remove(blob_monster_warning_door)
            pen.clear()
            blob_monster_one_text_level(levels[65])

    for blob_monster_warning, blob_monster_warning_text_exit in zip(blob_monster_warnings, blob_monster_warning_text_exits):
        if player.is_collision(blob_monster_warning_text_exit):
            blob_monster_warning.destroy()
            blob_monster_warnings.remove(blob_monster_warning)
            pen.clear()
            blob_monster_one_text_level(levels[66])



    for blob_monster_warning_two_door, blob_monster_two_warning in zip(blob_monster_warning_two_doors, blob_monster_two_warnings):
        if player.is_collision(blob_monster_warning_two_door):
            blob_monster_two_warning.destroy()
            blob_monster_two_warnings.remove(blob_monster_two_warning)
            pen.clear()
            setup_maze_0(levels[67])






                                        






    for monster, blood_messages_trigger in zip(monsters, blood_messages_triggers):
        if player.is_collision(monster):
            monster.destroy()
            monsters.remove(monster)
            blood_messages_trigger.destroy()
            blood_messages_triggers.remove(blood_messages_trigger)
            pen.clear()
            blob_monster_one_text_level(levels[58])
    wn.update()


    for blob_monster_death_zero, blob_monster_text_exit_zero in zip(blob_monster_death_zeros, blob_monster_text_exit_zeros):
        if player.is_collision(blob_monster_text_exit_zero):
            blob_monster_death_zero.destroy()
            blob_monster_death_zeros.remove(blob_monster_death_zero)
            pen.clear()
            blob_monster_one_text_level(levels[59])


    for blob_monster_death_one, blob_monster_text_exit_one in zip(blob_monster_death_ones, blob_monster_text_exit_ones):
        if player.is_collision(blob_monster_text_exit_one):
            blob_monster_death_one.destroy()
            blob_monster_death_ones.remove(blob_monster_death_one)
            pen.clear()
            blob_monster_one_text_level(levels[60])

    for blob_monster_death_two, blob_monster_text_exit_two in zip(blob_monster_death_twos, blob_monster_text_exit_twos):
        if player.is_collision(blob_monster_text_exit_two):
            blob_monster_death_two.destroy()
            blob_monster_death_twos.remove(blob_monster_death_two)
            pen.clear()
            blob_monster_one_text_level(levels[61])


    for blob_monster_death_three, blob_monster_text_exit_three in zip(blob_monster_death_threes, blob_monster_text_exit_threes):
        if player.is_collision(blob_monster_text_exit_three):
            blob_monster_death_three.destroy()
            blob_monster_death_threes.remove(blob_monster_death_three)
            pen.clear()
            blob_monster_one_text_level(levels[62])


    for blob_monster_death_four, blob_monster_text_exit_four in zip(blob_monster_death_fours, blob_monster_text_exit_fours):
        if player.is_collision(blob_monster_text_exit_four):
            blob_monster_death_four.destroy()
            blob_monster_death_fours.remove(blob_monster_death_four)
            pen.clear()
            blob_monster_one_text_level(levels[63])



    for blob_monster_death_final, blob_monster_text_exit_final in zip(blob_monster_death_finals, blob_monster_text_exit_finals):
        if player.is_collision(blob_monster_text_exit_final):
            blob_monster_death_final.destroy()
            blob_monster_death_finals.remove(blob_monster_death_final)
            pen.clear()
            setup_maze_0(levels[1])







    for others in other:
        for monster in monsters:
         if player.is_collision(others):
            monster.destroy()
            monsters.remove(monster)
            pen.clear()
            text_level(levels[36])







    for key in keys:
        for bodybagmonster in bodybagmonsters:

         if player.is_collision(key):
            key.destroy()
            keys.remove(key)
            bodybagmonster.destroy()
            bodybagmonsters.remove(bodybagmonster)
            pen.clear()
            setup_maze_C2(levels[10])
    wn.update()



    for secondroomentrance in secondroomentrances:

        for monster in monsters:
          if player.is_collision(secondroomentrance):
            monster.destroy()
            monsters.remove(monster)
            pen.clear()
            hallway_one_text_level(levels[38])



    for blood_messages_trigger, monster in zip(blood_messages_triggers, monsters):
        if player.is_collision(blood_messages_trigger):
            monster.destroy()
            monsters.remove(monster)
            pen.clear()
            hallway_one_text_level(levels[39])


    for hallway_exit_blood_message_text, hallway_blood_messages_trigger in zip(hallway_exit_blood_message_texts, hallway_blood_messages_triggers):
        if player.is_collision(hallway_exit_blood_message_text):
            hallway_blood_messages_trigger.destroy()
            hallway_blood_messages_triggers.remove(hallway_blood_messages_trigger)
            pen.clear()
            hallway_one_text_level(levels[40])

    for hallway_blood_messages_one,  hallway_exit_blood_message_texts_one in zip(hallway_blood_messages_ones,  hallway_exit_blood_message_texts_ones):
        if player.is_collision( hallway_exit_blood_message_texts_one):
            hallway_blood_messages_one.destroy()
            hallway_blood_messages_ones.remove(hallway_blood_messages_one)
            pen.clear()
            hallway_one_text_level(levels[41])

    for hallway_blood_messages_two,  hallway_exit_blood_message_texts_two in zip(hallway_blood_messages_twos,  hallway_exit_blood_message_texts_twos):

        if player.is_collision( hallway_exit_blood_message_texts_two):
            hallway_blood_messages_two.destroy()
            hallway_blood_messages_twos.remove(hallway_blood_messages_two)
            pen.clear()
            setup_maze_0(levels[42])











    for  C3_exit_entrance_text, C3_entrance_text in  zip(C3_exit_entrance_texts,  C3_entrance_texts):
        if player.is_collision(C3_exit_entrance_text):
          C3_exit_entrance_text.destroy()
          C3_exit_entrance_texts.remove(C3_exit_entrance_text)
          C3_entrance_text.destroy()
          C3_entrance_texts.remove(C3_entrance_text)
          pen.clear()
          setup_maze_C3(levels[4])


    for spider, spiderweb, spiderweb2 in zip(spiders, spiderwebs, spiderwebs2):
        if player.is_collision(spider):
            spider.destroy()
            spiders.remove(spider)
            spiderweb.destroy()
            spiderwebs.remove(spiderweb)
            spiderweb2.destroy()
            spiderwebs2.remove(spiderweb2)
            pen.clear()
            hallway_one_text_level(levels[48])


    for spider, spiderweb, spiderweb2 in zip(spiders, spiderwebs, spiderwebs2):
        if player.is_collision(spiderweb):
            spider.destroy()
            spiders.remove(spider)
            spiderweb.destroy()
            spiderwebs.remove(spiderweb)
            spiderweb2.destroy()
            spiderwebs2.remove(spiderweb2)
            pen.clear()
            hallway_one_text_level(levels[48])


    for spider, spiderweb, spiderweb2 in zip(spiders, spiderwebs, spiderwebs2):
        if player.is_collision(spiderweb2):
            spider.destroy()
            spiders.remove(spider)
            spiderweb.destroy()
            spiderwebs.remove(spiderweb)
            spiderweb2.destroy()
            spiderwebs2.remove(spiderweb2)
            pen.clear()
            hallway_one_text_level(levels[48])

    for secondroomexit in secondroomexits:


        for spider, spiderweb, spiderweb2 in zip(spiders, spiderwebs, spiderwebs2):

           if player.is_collision(secondroomexit):
            spider.destroy()
            spiders.remove(spider)
            spiderweb.destroy()
            spiderwebs.remove(spiderweb)
            spiderweb2.destroy()
            spiderwebs2.remove(spiderweb2)
            pen.clear()
            hallway_one_text_level(levels[45])


    for C3_exit_door_one, C3_game_over_one in zip(C3_exit_door_ones, C3_game_over_ones):
        if player.is_collision(C3_exit_door_one):
            C3_game_over_one.destroy()
            C3_game_over_ones.remove(C3_game_over_one)
            pen.clear()
            hallway_one_text_level(levels[49])


    for C3_exit_door_two, C3_game_over_two in zip(C3_exit_door_twos, C3_game_over_twos):
        if player.is_collision(C3_exit_door_two):
            C3_game_over_two.destroy()
            C3_game_over_twos.remove(C3_game_over_two)
            pen.clear()
            hallway_one_text_level(levels[50])

    for C3_exit_door_three, C3_game_over_three in zip(C3_exit_door_threes, C3_game_over_threes):
        if player.is_collision(C3_exit_door_three):
            C3_game_over_three.destroy()
            C3_game_over_threes.remove(C3_game_over_three)
            pen.clear()
            hallway_one_text_level(levels[51])

    for C3_exit_door_four, C3_game_over_four in zip(C3_exit_door_fours, C3_game_over_fours):
        if player.is_collision(C3_exit_door_four):
            C3_game_over_four.destroy()
            C3_game_over_fours.remove(C3_game_over_four)
            pen.clear()
            hallway_one_text_level(levels[52])

    for C3_exit_door_five, C3_game_over_five in zip(C3_exit_door_fives, C3_game_over_fives):
        if player.is_collision(C3_exit_door_five):
            C3_game_over_five.destroy()
            C3_game_over_fives.remove(C3_game_over_five)
            pen.clear()
            hallway_one_text_level(levels[53])


    for C3_exit_door_six, C3_game_over_six in zip(C3_exit_door_sixes, C3_game_over_sixes):
        if player.is_collision(C3_exit_door_six):
            C3_game_over_six.destroy()
            C3_game_over_sixes.remove(C3_game_over_six)
            pen.clear()
            hallway_one_text_level(levels[54])

    for C3_exit_door_seven, C3_game_over_seven in zip(C3_exit_door_sevens, C3_game_over_sevens):
        if player.is_collision(C3_exit_door_seven):
            C3_game_over_seven.destroy()
            C3_game_over_sevens.remove(C3_game_over_seven)
            pen.clear()
            hallway_one_text_level(levels[55])

    for C3_final_door_game_over,  C3_final_game_over in  zip(C3_final_door_game_overs,  C3_final_game_overs):
        if player.is_collision(C3_final_door_game_over):
            C3_final_game_over.destroy()
            C3_final_game_overs.remove( C3_final_game_over)
            pen.clear()
            setup_maze_0(levels[5])

    for C3_exit_text_end, C3_exit_to_hallway in zip(C3_exit_text_ends, C3_exit_to_hallways):
        if player.is_collision(C3_exit_to_hallway):
            C3_exit_to_hallway.destroy()
            C3_exit_to_hallways.remove(C3_exit_to_hallway)
            C3_exit_text_end.destroy()
            C3_exit_text_ends.remove(C3_exit_text_end)
            pen.clear()
            setup_maze_0(levels[5])

    for C1_door in C1_doors:
        if player.is_collision(C1_door):
            pen.clear()
            hallway_one_text_level(levels[46])

    for C1_entry_text, C1_exit_entry_text in zip(C1_entry_texts, C1_exit_entry_texts):
        if player.is_collision(C1_exit_entry_text):
            C1_entry_text.destroy()
            C1_entry_texts.remove(C1_entry_text)
            pen.clear()
            setup_maze_0(levels[47])

    for C2_password_locked, hallway_blood_messages_trigger in zip(C2_password_lockeds, hallway_blood_messages_triggers):
        if player.is_collision(C2_password_locked):
            hallway_blood_messages_trigger.destroy()
            hallway_blood_messages_triggers.remove(hallway_blood_messages_trigger)
            pen.clear()
            hallway_one_text_level(levels[56])


    for C2_password_locked, monster in zip(C2_password_lockeds, monsters):
        if player.is_collision(C2_password_locked):
            monster.destroy()
            monsters.remove(monster)
            pen.clear()
            hallway_one_text_level(levels[56])

    for C2_locked_text, C2_door_text_exit in zip(C2_locked_texts, C2_door_text_exits):
        if player.is_collision(C2_door_text_exit):
            C2_locked_text.destroy()
            C2_locked_texts.remove(C2_locked_text)
            pen.clear()
            setup_maze_0(levels[57])




    #
    # for blob_monster_warning_door in  blob_monster_warning_doors:
    #     if player.is_collision(blob_monster_warning_door):
    #         blob_monster_warning_door.destroy()
    #         blob_monster_warning_doors.remove(blob_monster_warning_door)
    #         pen.clear()
    #         blob_monster_one_text_level(levels[65])
    #
    # for blob_monster_warning_two_door in blob_monster_warning_two_doors:
    #     if player.is_collision(blob_monster_warning_two_door):
    #         blob_monster_warning_two_door.destroy()
    #         blob_monster_warning_two_doors.remove(blob_monster_warning_two_door)
    #         pen.clear()
    #         blob_monster_one_text_level(levels[66])

    for exam_entrance in exam_entrances:
        for monster, blood_messages_trigger, blob_monster_warning_door in zip(monsters, blood_messages_triggers, blob_monster_warning_doors):
         if player.is_collision(exam_entrance):
            blood_messages_trigger.destroy()
            blood_messages_triggers.remove(blood_messages_trigger)
            monster.destroy()
            monsters.remove(monster)
            blob_monster_warning_door.destroy()
            blob_monster_warning_doors.remove(blob_monster_warning_door)
            pen.clear()
            exam_room_text_level(levels[68])


    for exam_room_exit_text_one, exam_room_enter_text_one in zip(exam_room_exit_text_ones, exam_room_enter_text_ones):
        if player.is_collision(exam_room_exit_text_one):
            exam_room_enter_text_one.destroy()
            exam_room_enter_text_ones.remove(exam_room_enter_text_one)
            pen.clear()
            exam_room_text_level(levels[69])

    for exam_room_exit_text_two, exam_room_enter_text_two in zip(exam_room_exit_text_twos, exam_room_enter_text_twos):
        if player.is_collision(exam_room_exit_text_two):
            exam_room_enter_text_two.destroy()
            exam_room_enter_text_twos.remove(exam_room_enter_text_two)
            pen.clear()
            exam_room_text_level(levels[70])

    for exam_room_exit_text_three, exam_room_enter_text_three in zip(exam_room_exit_text_threes, exam_room_enter_text_threes):
        if player.is_collision(exam_room_exit_text_three):
            exam_room_enter_text_three.destroy()
            exam_room_enter_text_threes.remove(exam_room_enter_text_three)
            pen.clear()
            exam_room_text_level(levels[71])

    for exam_room_exit_text_four, exam_room_enter_text_four in zip(exam_room_exit_text_fours, exam_room_enter_text_fours):
        if player.is_collision(exam_room_exit_text_four):
            exam_room_enter_text_four.destroy()
            exam_room_enter_text_fours.remove(exam_room_enter_text_four)
            pen.clear()
            exam_room_text_level(levels[72])

    for exam_room_exit_text_five, exam_room_enter_text_five in zip(exam_room_exit_text_fives, exam_room_enter_text_fives):
        if player.is_collision(exam_room_exit_text_five):
            exam_room_enter_text_five.destroy()
            exam_room_enter_text_fives.remove(exam_room_enter_text_five)
            pen.clear()
            exam_room_text_level(levels[73])

    for exam_room_exit_text_six, exam_room_enter_text_six in zip(exam_room_exit_text_sixes, exam_room_enter_text_sixes):
        if player.is_collision(exam_room_exit_text_six):
            exam_room_enter_text_six.destroy()
            exam_room_enter_text_sixes.remove(exam_room_enter_text_six)
            pen.clear()
            setup_maze_Examination_room(levels[6])

    for triggerhandmonster in triggerhandmonsters:
        if player.is_collision(triggerhandmonster):
            triggerhandmonster.destroy()
            triggerhandmonsters.remove(triggerhandmonster)
            pen.clear()
            exam_room_text_level(levels[74])





            #setup_maze_Examination_room(levels[7])

    for exam_exit in exam_exits:

        for handmonster, handmonster2, handmonster3, handmonster4, handmonster5, handmonster6, handmonster7, handmonster8, handmonster9, handmonster10, hospitalbed2 in zip(handmonsters, handmonsters2, handmonsters3, handmonsters4, handmonsters5, handmonsters6, handmonsters7, handmonsters8, handmonsters9, handmonsters10, hospitalbeds2):
          if player.is_collision(exam_exit):

             handmonster.destroy()
             handmonsters.remove(handmonster)

             handmonster2.destroy()
             handmonsters2.remove(handmonster2)

             handmonster3.destroy()
             handmonsters3.remove(handmonster3)

             handmonster4.destroy()
             handmonsters4.remove(handmonster4)

             handmonster5.destroy()
             handmonsters5.remove(handmonster5)

             handmonster6.destroy()
             handmonsters6.remove(handmonster6)

             handmonster7.destroy()
             handmonsters7.remove(handmonster7)

             handmonster8.destroy()
             handmonsters8.remove(handmonster8)

             handmonster9.destroy()
             handmonsters9.remove(handmonster9)

             handmonster10.destroy()
             handmonsters10.remove(handmonster10)

             hospitalbed2.destroy()
             hospitalbeds2.remove(hospitalbed2)

             pen.clear()
             setup_maze_0(levels[8])

    for C2_entrance in C2_entrances:

        if player.is_collision(C2_entrance):
            monster.destroy()
            monsters.remove(monster)
            pen.clear()
            setup_maze_C2(levels[9])

    for C2_exit in C2_exits:
        if player.is_collision(C2_exit):
            pen.clear()
            setup_maze_0(levels[11])

    for bodybagmonstermoving in bodybagmonstermovings:
        if player.is_collision(bodybagmonstermoving):
            print("You died!")

    for C2_exit_with_key in C2_exit_with_keys:
      for bodybagmonstermoving in bodybagmonstermovings:
        if player.is_collision(C2_exit_with_key):
            bodybagmonstermoving.destroy()
            bodybagmonstermovings.remove(bodybagmonstermoving)
            pen.clear()
            setup_maze_1(levels[12])

    for exit_hallway in exit_hallways:
      for hand_monster_hallway, hand_monster_hallway2, hand_monster_hallway3 in zip(hand_monster_hallways, hand_monster_hallways2, hand_monster_hallways3):
        if player.is_collision(exit_hallway):
              hand_monster_hallway.destroy()
              hand_monster_hallways.remove(hand_monster_hallway)
              hand_monster_hallway2.destroy()
              hand_monster_hallways2.remove(hand_monster_hallway2)
              hand_monster_hallway3.destroy()
              hand_monster_hallways3.remove(hand_monster_hallway3)
              pen.clear()
              setup_maze_exit(levels[13])

    for exit_to_pool in exit_to_pools:
      for spiderweb, monster, spider, spider_monster_hallway2, spider_monster_hallway3 in zip(spiderwebs, monsters, spiders, spider_monster_hallways2, spider_monster_hallways3):
        if player.is_collision(exit_to_pool):
            spiderweb.destroy()
            spiderwebs.remove(spiderweb)
            monster.destroy()
            monsters.remove(monster)
            spider.destroy()
            spiders.remove(spider)
            spider_monster_hallway2.destroy()
            spider_monster_hallways2.remove(spider_monster_hallway2)
            spider_monster_hallway3.destroy()
            spider_monster_hallways3.remove(spider_monster_hallway3)
            pen.clear()
            setup_maze_pool_area(levels[14])

    for door_to_exit_game in door_to_exit_games:
      for pool in pools:
        if player.is_collision(door_to_exit_game):
            pool.destroy()
            pools.remove(pool)
            pen.clear()
            print("You win!")







    wn.update()





















def title_screen():
 input("\nWelcome to Hospital Horrors! Press any key to continue.")
 input("\nmove left: a\nmove right:d\nmove up:w\nmove down:s\npick up object:p\nopen doors:i")
 input("\nLet's begin!")
 wake_up()


def wake_up():
    input("\nYou wake up in your hospital bed to the sound of a blood curdling scream down the hallway. There is darkness all around you.")
    input("\nThe dead silence that follows makes your heart beat quicker.")
    input("\nYou don't know how you ended up in this dark hospital all alone. All you know is that you need to escape!")
    input("\nYou get up from the bed, still not being able to see a thing.")
    input("\nPress 'w,a,s,d' to explore room and 'p' to pick up objects.")
    explore=""
    while explore!=("a","s","d","w","g","h","p"):
        explore=input("\nPress w-forward,a-left,s-turn around,d-right to explore the room. Press i to open doors.\n")
        if explore=="s":
            print("\nYou look at the bed. Although it looks comfy, now is probably not the best time for a nap.")
        if explore=="a":
            flash=input("\nYou see a black cylinder-like object on the grimy hospital floor.\nPress p to pick it up?")
            if flash=="p":
                print("\nYou pick up the object and discover that it is a flash light. You turn it on.")
                flash_light()
            else:
                print("\nYou chose to not pick up the object.")
        if explore=="d":
            print("\nYou see a blank wall in front of you.")
        if explore=="w":
            print("\nYou see the vague outlines of a door in front of you. Although you want to get out as soon as you can,\nit's probably better "
                  "not to stumble blindly down a dark hallway where something threatening might be lurking.")


def flash_light():
    input("\nThe flash light illuminates the tiny hospital room.")
    light_explore=""
    while light_explore!=("a","s","d","w","g","h","p"):
        light_explore=input("\nPress w-forward,a-left,s-turn around,d-right to explore the room. Press i to open doors.\n")
        if light_explore=="s":
            print("\nYou look at the bed. There is a thin layer of dirt on the white sheets.")
        elif light_explore=="a":
            input("\nSomeone has written a threatening message in blood on the wall:'Don't bother, it's too late.'")
        elif light_explore=="d":
            hole=input("\nYou see tacky wallpaper with bouquets of roses printed all over it. There is a small hole in the wall.\nWould you like to look through it? Press i to look.")
            if hole=="i":
                input("\nYou look through the hole.")
                input("\nAt first, you see nothing, but then you see what looks like a large, unraveled spiderweb strewn all around the room from floor to ceiling.")
                input("\nLarge cotton cocoons hang from the ceiling.")
                input("\nLong spindly legs jut out from something sitting in the corner of the room.")
                input("\nYou can't see what it is from the tiny hole.")
            else:
                print("\nYou decide not to look through the hole. Who knows what horrible thing you'd see?")
        elif light_explore=="w":
            exit=input("\nWould you like to exit into the hallway? Press w again to confirm.")
            if exit=="w":
                input("\nYou open the door, stepping out into the dark corridor.")
                explore_hallway()
            else:
                print("\nYou decide to stay in the room for a bit. Probably safer in here anyways.")


def explore_hallway():
    input("\nYou turn and face the long, dark hallway.")
    input("\nYou listen for any noise, and hear a heart-stopping crunching sound to your left.")
    corridor_explore = ""
    while corridor_explore != ("a", "s", "d", "w", "g", "h", "p"):
        corridor_explore=input("\nPress w-forward,a-left,s-turn around,d-right to explore hallway. Press i to open doors.\n")
        if corridor_explore=="w":
            input("\nYou walk down the hallway. Stopping to examine your surroundings, you notice a door to your right that says 'C3' on it.")
            input("\nYou can still hear something chewing on flesh behind you. It doesn't seem to have noticed you yet.")
            hallway_second_block()
        if corridor_explore=="a":
            input("\nYou look to your left and see what looks like a giant blob-shaped monster with human arms for legs chewing on some unfortunate victim in a hospital gown.")
            first_game_over=input("\nWould you like to get a closer look? Press a again to go left.")
            if first_game_over=="a":
                input("\nA twisted fascination draws you closer to the creature.")
                input("\nYou see four tendril like appendages sticking out from the creature's body, each with its own human-like mouth tearing into the victim's flesh.")
                input("\nYou hear a loud crunch under your foot. Looking down, you see the now broken syringe on the ground.")
                input("\nThe creature stops eating, turning toward you with it's four mouths.")
                input("\nThe monster lets out an ear-piercing scream as it rushes at you.")
                input("\nThe last thing you hear is the creature's scream as it tears your flesh from your bones.")
                you_died_blob_monster_one()
            else:
                input("\nYou decide it's best not to get any closer. The monster seems preoccupied with its meal. As long as you are quiet, it will not notice you.")
                input("\nYou face the never-ending darkness of the hallway ahead again.")

        if corridor_explore=="d":
            input("\nYou look at the door to the room you just came out of, the label 'C4' printed on a tiny plaque.")
            go_back=input("\nDo you want to go back inside? Press i for yes and any other key for no.")
            if go_back=="i":
                input("\nYou step inside the small hospital room again, closing the door behind you.")
                flash_light()
            else:
                print("\nYou decide to not go back into the room. You face the long hallway again.")
                continue
        if corridor_explore == "s":
            input("\nYou turn around and notice a door labeled 'Outdoor Pool Area.' To your right, there is a blob-like monster with human arms for legs feasting on a corpse.")
            down_the_hallway_one()


def down_the_hallway_one():
    corridor_explore = ""
    open_again = ""
    open_once_more=""
    while corridor_explore != ("a", "s", "d", "w", "g", "h", "p"):
        corridor_explore=input("\nPress w-forward,a-left,s-turn around,d-right to explore hallway. Press i to open doors.\n")
        if corridor_explore == "w":
            input("\nThere is a door in front of you labeled 'Outdoor Pool Area.'")
            down_the_hallway_one()
        if corridor_explore=="s":
            explore_hallway()
        if corridor_explore=="d":
            input("\nYou look to your right and see what looks like a giant blob-shaped monster with human arms for legs chewing on some unfortunate victim in a hospital gown.")
            first_game_over = input("\nWould you like to get a closer look? Press d again to go right.")
            if first_game_over == "d":
                input("\nA twisted fascination draws you closer to the creature.")
                input("\nYou see four tendril like appendages sticking out from the creature's body, each with its own human-like mouth tearing into the victim's flesh.")
                input("\nYou hear a loud crunch under your foot. Looking down, you see the now broken syringe on the ground.")
                input("\nThe creature stops eating, turning toward you with it's four mouths.")
                input("\nThe monster lets out an ear-piercing scream as it rushes at you.")
                input("\nThe last thing you hear is the creature's scream as it tears your flesh from your bones.")
                you_died_blob_monster_one()
            else:
                input("\nYou decide it's best not to get any closer. The monster seems preoccupied with its meal. As long as you are quiet, it will not notice you.")
                input("\nYou face the door leading to the pool area again.")
                continue
        if corridor_explore=="a":
            input("\nYou look at the door to the room you just came out of, the label 'C4' printed on a tiny plaque.")
            go_back_two = input("\nDo you want to go back inside? Press i for yes and any other key for no.")
            if go_back_two == "i":
                input("\nYou step inside the small hospital room again, closing the door behind you.")
                flash_light()
            else:
                print("\nYou decide not go back into the room. You face the 'outdoor pool area' door again.")
                continue

        if corridor_explore=="i":
          input("\nYou try opening the door but it is locked. The door makes a loud creaking sound as you try to open it.")
          input("\nThe creature doesn't seem to notice, but it's probably best not to push your luck by trying to open it again.")
        while open_again != ("a", "s", "d", "w", "g", "h", "p"):
          open_again = input("\nPress i to keep trying to open the door and any other key to quit.\n")
          if open_again == "i":
            open_again = input("\nYou try to open the door again. A much louder creak echoes in the hallway. The creature stops eating, listening for any noise.")
            open_once_more = input("\nPress i to keep trying to open the door and any other key to quit.\n")
          if open_once_more=="i":
                input("\nYou try one more time to open the door despite already knowing that it's locked.")
                input("\nThe four-mouthed creature screams as it hears you, rushing at you.")
                input("\nThe last thing you hear is its horrid scream as it rips out your entrails.")
                you_died_blob_monster_one()
          else:
            input("\nYou decide to not open the door.")
            down_the_hallway_one()


def hallway_second_block():
    corridor_explore=""
    while corridor_explore != ("a", "s", "d", "w", "g", "h", "p"):
        corridor_explore=input("\nPress w-forward,a-left,s-turn around,d-right to explore hallway. Press i to open doors.\n")
        if corridor_explore=="a":
            input("\nYou shine your flashlight against the dirty,blood-stained wall to your left.")
            input("\nThere is a message on the wall written in blood: ")
            input("\n'You can't escape from its web. Don't go in there.'")
            continue
        if corridor_explore=="d":
            input("\nThe door knob on the door to your right is sticky to the touch.")
            input("\nYou feel something sticky underneath your feet.")
            input("\nYou shine your flashlight down and notice a sticky substance coming out from this room.")
            spider_game_over=input("\nWould you like to enter this room? Press i for yes and any other key for no.")
            if spider_game_over=="i":
                input("\nYou enter the room, accidentally dropping your flashlight as you walk right into a thick string of web.")
                input("\nYou kneel to pick it up, only to find that your knees are now stuck to the floor.")
                input("\nYou struggle in vain until you hear something stir behind you.")
                input("\nYou turn around and see an eight-legged creature.")
                input("\nIts entire body is made up of human faces, each one contorted in a unique expression of pain.")
                input("\nThe creature pushes the door shut, killing your last hope of freedom.")
                input("\nOnly darkness now.")
                you_died_spider_monster_one()
            else:
                input("\nYou decide not to go into the room. Seems like a pretty bad idea.")
                continue
        if corridor_explore=="s":
            walk_back=input("\nWould you like to turn back around and walk towards the 'Outdoor Pool Area' door? Press s again to confirm.")
            if walk_back=="s":
                input("\nYou turn around and walk back towards the 'Outdoor Pool Area' door. The blob monster is still chewing happily on its meal to your right.")
                down_the_hallway_one()
            else:
                input("\nYou decide to keep facing forward.")
                continue
        if corridor_explore=="w":
            hallway_third_block_one()


def hallway_third_block_one():
    input("\nYou walk further down the hallway until you find yourself accidentally stepping on broken glass.")
    input("\nYou stop hearing the blob monster's loud chewing. It's only a matter of seconds before it turns the corner and sees you.")
    corridor_explore = ""
    while corridor_explore != ("a", "s", "d", "w", "g", "h", "p"):
     corridor_explore = input("\nPress w-forward,a-left,s-turn around,d-right to explore hallway. Press i to open doors.\n")
     if corridor_explore=="w":
         input("\nNot even looking back, you run as fast as you can until you see two doors, one to your left and one to your right.")
         hallway_fourth_block_one()
     if corridor_explore=="d":
            input("\nThere is a door to your right labeled 'C2.'")
            input("\nYou need a number code to open it.")
     if corridor_explore=="a":
         input("\nThere is a blank wall to your left. Nothing important.")
     if corridor_explore=="s":
         hallway_third_block_backwards_one()


def hallway_third_block_backwards_one():
         input("\nYou turn around and see a monster now looking at you with it's two big, antennae eyes.")
         input("\nWith blood still dripping from its four mouths, the creature screams as it runs at you.")
         input("\nDo you want to press s to turn back around and run for your life or do you want to stay where you are?")
         corridor_explore=""
         while corridor_explore != ("a", "s", "d", "w", "g", "h", "p"):
          corridor_explore = input("\nPress w-forward,a-left,s-turn around,d-right to explore hallway. Press i to open doors.\n")
          if corridor_explore=="s":
                input("\nYou turn around and run as fast as you can until you see two doors, one to your left and one to your right.")
                hallway_fourth_block_one()
          if corridor_explore=="a":
                input("\nYou look at the door labeled 'C2.'")
                input("\nIt requires a number code to open.")
                input("\nThe monster continues to stumble towards you.")
                input("\nYou could try opening it with 'i' using brute force, but that's probably not a great idea.")
                open_again=input("\nPress w-forward,a-left,s-turn around,d-right to explore hallway. Press i to open doors.\n")
                if open_again=="i":
                    input("\nYou try opening the door with all of your strength, but it doesn't budge.")
                    input("\nYou don't have much time to feel sad about this though, as the monster uses its brute force to knock you down and tear your flesh.")
                    you_died_blob_monster_two()
                else:
                    input("\nYou decide to not try and open the door.")
                    continue
          if corridor_explore=="w":
              input("\nInstead of running, you think that maybe charging at the monster is the most logical choice.")
              input("\nDespite having no weapons or anyway to defend yourself, maybe you can beat it through will power alone!")
              are_you_kidding=input("\nWould you like to charge at the monster? Press 'w' to confirm and any other key for no.")
              if are_you_kidding=="w":
                     input("\nYou run heroically towards the terrible screaming monstrosity.")
                     input("\nDespite being a strong candidate for the Darwin award, no one can say you didn't die an honorable, gruesome death.")
                     you_died_blob_monster_two()
              else:
                     input("\nYou realize that this would basically be suicide, and decide to turn around and run anyway from this monster.")
                     input("\nYou run as fast as you can until you see two doors, one to your left and one to your right.")
                     hallway_fourth_block_one()
          if corridor_explore=="d":
                input("\nInstead of running, you decide to examine the blank wall to your right.")
                input("\nThe monster is getting closer.")
                see_again=""
                while see_again!=("a","s","d","w"):
                    see_again = input("\nPress w-forward,a-left,s-turn around,d-right to explore hallway. Press i to open doors.\n")
                    if see_again=="d":
                      see_again=input("\nIt looks terribly dirty, someone should clean it.")
                      input("\nProbably won't be you though considering that the monster has just caught up to you.")
                      input("\nThe last thing you see is your blood spattered all over the wall.")
                      you_died_blob_monster_two()
                    else:
                     input("You decide to stop looking at the wall. Probably for the best considering the blood-thirsty monster in front of you.")
                     hallway_third_block_backwards_one()



def hallway_fourth_block_one():
    corridor_explore=""
    input("\nYou feel yourself sweat as you look back and forth between each door.")
    while corridor_explore != ("a", "s", "d", "w", "g", "h", "p"):
        corridor_explore = input("\nPress w-forward,a-left,s-turn around,d-right to explore hallway. Press i to open doors.\n")
        if corridor_explore=="w":
            input("\nThere seems to be a makeshift barricade up ahead made up mostly of chairs and over turn hospital beds.")
            input("\nAre you sure that you want to run to this dead end?")
            dead_end=input("\nPress w to run to the end of the hallway and any other key for no.")
            if dead_end=="w":
                input("\nYou run to the end of the hallway.")
                input("\nDespite looking hastily thrown together, the barricade is too strong for you to move.")
                input("\nYou see your blood splatter all over the barricade as the monster catches up to you, screaming with two of its mouths while feasting on your flesh with the other two.")
                you_died_blob_monster_three()
            else:
                input("\nYou decide not to run towards the barricade.")
                continue
        if corridor_explore == "a":
            input("\nThere is a door to your left.")
            save_yourself=input("\nWould you like to press i to open it?")
            if save_yourself=="i":
              input("\nTo your relief, it opens!")
              input("\nYou rush inside, slamming the door behind you.")
              input("\nThe monster continues to scream in the hallway as you shine your flashlight on the dark room.")
              examination_room()
            else:
                input("\nYou decide not to open the door.")
                continue
        if corridor_explore=="s":
            input("\nThe monster is almost right behind you. Are you sure you want to turn around?")
            turn_around=input("\nPress s to turn around and any other key for no.")
            if turn_around=="s":
                input("\nYou decide to turn around.")
                input("\nThe monster raises four of its twelve human arm legs, pushing you down to the ground.")
                input("\nIts four mouths rip you to pieces as the world goes dark.")
                you_died_blob_monster_three()
            else:
                input("\nYou decide not to turn around. Probably a smart move.")
                continue
        if corridor_explore=="d":
            input("\nThere is a door to your right.")
            does_not_open=input("\nWould you like to press i to open it?")
            if does_not_open=="i":
              input("\nUnfortunately, the door does not budge.")
              input("\nDo you want to try and open the door again?")
              still_locked = input("\nPress i for yes and any other key for no.")
              if still_locked == "i":
                    input("\nYou try opening the locked door again but it is still locked.")
                    input("\nThe monster's ear-piercing scream is the last thing you hear as it tears at your flesh.")
                    you_died_blob_monster_three()
              else:
                    input("\nYou decide to not try and open the door again. What would be the point?")
                    continue
            else:
                input("\nYou decide to not try and open the door.")
                continue





def examination_room():
    input("\nThe room seems to have been stripped bare, except for one hospital bed in front of you.")
    input("\nBlack mold is growing out of every corner.")
    input("\nYou shine your flashlight all around the tiny room.")
    input("\nAlthough you don't see anything, you swear you hear something breathing to your right.")
    input("\nThe blob monster outside has stopped screaming, though you can still hear its monstrous footsteps stomping back and forth in the hallway.")
    exam_explore=""
    while exam_explore != ("a", "s", "d", "w", "g", "h", "p"):
        exam_explore = input("\nPress w-forward,a-left,s-turn around,d-right to explore examination room. Press i to open doors.\n")
        if exam_explore=="s":
            input("\nYou can still hear the footsteps of the blob monster pacing right outside the door.")
            get_killed=input("\nWould you like to go outside anyways? Press i to go out into the hallway and any other key not to.")
            if get_killed=="i":
                input("\nYou go out into the hallway.")
                input("\nAfter just five minutes, the horrendous creature is enjoying the easiest meal it has ever had to catch.")
                you_died_blob_monster_four()
            else:
                input("\nYou decide not to head into the hallway. Why risk getting eaten?")
                input("\nYou face the hospital room again.")
                continue
        if exam_explore=="a":
            input("\nYou look to the left of the room.")
            input("\nThere is a message written on the wall:")
            input("\n'It wants to add you to its collection.'")
        if exam_explore=="d":
            input("\nYou look to the right of the room.")
            input("\nThe blank wall before you seems normal at first.")
            input("\nBut as you continue to look at it, the wall seems to be pulsing, each pulse perfectly timed with the mysterious sound of breathing reverberating in the room.")
        if exam_explore=="w":
            input("\nThere is a hospital bed right in front of you with a particularly bad odor.")
            remove_sheets=input("\nPress p to move aside the sheets and any other key not to.")
            if remove_sheets=="p":
                input("\nYou toss aside the sheets and see a large puddle of water in the center of the bed.")
                input("\nIn the middle of the water, there is a sheet of paper on top of what looks like a pile of tar.")
                pick_up=input("\nWould you like to pick up the sheet of paper? Press p for yes and any other key for no.")
                if pick_up=="p":
                    input("\nYou try to tug the piece of paper off of the tar-covered hill.")
                    input("\nIt doesn't give. The breathing in the right corner grows more labored and loud.")
                    once_more=input("\nOne more pull might do the trick. Press p to try again and any other key to give up.")
                    if once_more=="p":
                        input("\nWith one more gentle tug, you are able to pull the sheet of paper free.")
                        input("\nYou hear a sharp inhale reverberate around the room as the ground shakes under your feet.")
                        input("\nA dark ooze drips out of the top right corner of the room.")
                        input("\nThen, what looks like a pale hand protrudes from the slime.")
                        input("\nMore arms join it, until there is a giant cluster of hands coming out of the corner of the room.")
                        input("\nThey all reach out for you with their elongated arms.")
                        slime_monster()
                    else:
                        input("\nYou decide not to try again. You put the sheet back on the bed, hoping to mitigate the odor.")
                        continue

                else:
                    input("\nYou decide not to pick up the piece of paper. You put the sheet back on the bed to mitigate the odor.")
                    continue
            else:
                input("\nYou decide not to tug at the foul smelling sheets. Something probably died under there.")
                continue


def slime_monster():
    input("\nThe hands continue to move towards you, some grabbing at the air, some the ceiling, and others at the floor.")
    input("\nIt's only a matter of time before they grab you.")
    slime_explore = ""
    while slime_explore != ("a", "s", "d", "w", "g", "h", "i","p"):
        slime_explore = input("\nPress w-forward,a-left,s-turn around,d-right to explore examination room. Press i to open doors.\n")
        if slime_explore == "s":
            input("\nYou turn around and see the door leading out to the hallway.")
            input("\nIt might be safer out there than it is in here.")
            escape_slime=input("\nWould you like to escape from this room? Press i to open the door and any other key to stay in the room.")
            if escape_slime=="i":
                input("\nYou push open the door, slamming it behind you as you step out into the dark hallway.")
                hallway_fourth_block_two()
            else:
                input("\nYou decide to stay in the room for some reason.")
                input("\nThe monster grabs your ankles, dragging you to its disgusting, slime-filled corner.")
                input("\nYour desperate, outstretched hands are the last part of you to disappear into the black goo.")
                you_died_slime_monster()
        if slime_explore=="a":
            input("\nYou look to your left and see a message written on the wall: ")
            input("\nIt wants to add you to its collection.")
            input("\nNow knowing what 'it' is, maybe it's best if you try to get out of this room.")
            input("\nYou remember that there is a door behind you.")
            okay_fine=input("\nWould you like to keep staring at the wall though? Press a for yes and any other key for no.")
            if okay_fine=="a":
                input("\nYou continue to stare at the wall.")
                input("\nThe monster grabs your ankles, dragging you to its disgusting, slime-filled corner.")
                input("\nYour desperate, outstretched hands are the last part of you to disappear into the black goo.")
                you_died_slime_monster()
            else:
                input("\nYou decide to stop staring at the wall.")
                continue
        if slime_explore=="d":
            input("\nYou shine your flashlight to your right.")
            input("\nA large grey, human-like eye stares back at you, its black pupil shrinking under your flashlight's harsh light.")
            input("\nThe creature sharply inhales as the hands continue to feel around every inch of the room.")
            input("\nYou remember that there is a door behind you.")
            why_though=input("\nWould you like to keep staring at the weird eye in front of you instead of escaping? Press d for yes and any other key for no.")
            if why_though=="d":
                input("\nThe monster lets out a long exhale as you feel the hands grip your ankles.")
                input("\nYour desperate, outstretched hands are the last part of you to disappear into the black goo.")
                you_died_slime_monster()
            else:
                input("\nYou decide to stop staring at the giant eye.")
                continue
        if slime_explore=="w":
            input("\nThe monster's hands continue to emerge from the corner of the room.")
            input("\nAre you sure that you want to walk towards the monster?")
            kill_yourself=input("\nPress w to end it all and any other key to keep going.")
            if kill_yourself=="w":
                input("\nYou walk towards the monster, figuring what's the point?")
                input("\nOpening the door right behind you is just too much effort.")
                input("\nThe monster grabs your ankles, dragging you to its disgusting, slime-filled corner.")
                input("\nYour desperate, outstretched hands are the last part of you to disappear into the black goo.")
                you_died_slime_monster()
            else:
                input("\nYou decide to keep braving this nightmare.")
                input("\nGood for you!")
                input("\nEscaping shouldn't be too hard. After all, there is an unlocked door right behind you.")
                continue



def hallway_fourth_block_two():
    input("\nYou face the barricade, made up of hospital beds and wheel chairs, at the end of the hallway.")
    input("\nYou hear a loud scratching sound behind you.")
    explore=""
    while explore != ("a", "s", "d", "w", "g", "h", "i","p"):
        explore = input("\nPress w-forward,a-left,s-turn around,d-right to explore hallway. Press i to open doors.\n")
        if explore == "s":
            input("\nYou turn around and see the blob monster scratching at a door towards the end of the hallway.")
            input("\nIt seems completely preoccupied with whatever is behind that door.")
            input("\nWould you like to walk further down the hallway?")
            keep_going=input("\nPress s again for yes and any other key for no.")
            if keep_going=="s":
                input("\nYou walk further down the hallway.")
                hallway_third_block_backwards_two()
            else:
                input("\nYou decide to stay where you are, facing the barricade again.")
                continue
        if explore=="w":
            input("\nThe barricade in front of you is insurmountable.")
            input("\nYou hear the faint sound of pain-filled moaning mixed with choked laughter coming from the other side.")
            input("\nAlthough there seems to be nothing there, you feel this new creature's presence.")
            input("\nIt's probably for the best that you'll never know what horrid thing is making that sound.")
        if explore=="a":
            input("\nYou look at the door to the examination room.")
            input("\nBlack tar oozes out the bottom of the door.")
            meh=input("\nWould you like to go back into the room with the tar monster? Press i for yes and any other key for no.")
            if meh=="i":
                input("\nYou open the door.")
                input("\nBefore you can even take one step inside, the monster grabs you, shutting the door behind you.")
                you_died_slime_monster_two()
            else:
                input("\nYou decide not to open the door with the terrifying monster you just escaped from behind it.")
                continue
        if explore=="d":
            input("\nYou look to your right and see a door.")
            input("\nThere is a small message written on the door.")
            input("\n'Some guy died in here. It should have been you.'")
            it_wont_open=input("\nDo you want to try and open it? Press i for yes and any other key for no.")
            if it_wont_open=="i":
                input("\nYou try opening the door.")
                input("\nIt doesn't budge.")
            else:
                input("\nYou decide to not open the door.")


def hallway_third_block_backwards_two():
    input("\nYou accidentally step on the same glass as before, but the monster doesn't seem to notice.")
    input("\nWhatever is behind that door has its complete attention as it scrapes at the door with five of its human-like hands.")
    explore_third=""
    while explore_third != ("a", "s", "d", "w", "g", "h", "i","p"):
        explore_third = input("\nPress w-forward,a-left,s-turn around,d-right to explore hallway. Press i to open doors.\n")
        if explore_third=="s":
            input("\nWould you like to turn back around and walk back towards the barricade?")
            walk_back=input("\nPress s again for yes and any other key for no.")
            if walk_back=="s":
                input("\nYou decide to turn around and walk back.")
                hallway_fourth_block_two()
            else:
                input("\nYou decide to not head back towards the barricade.")
                continue
        if explore_third=="w":
            input("\nThe blob monster is blocking off the rest of the hallway.")
            input("\nYou could try to slip past it, but then it would probably notice you.")
            input("\nWould you like to try and sneak past the blob monster?")
            keep_going=input("\nPress w again for yes and any other key for no.")
            if keep_going=="w":
                input("\nYou try to side-step past the monster.")
                input("\nYou accidentally brush by one of its twelve arms.")
                input("\nThe monster turns to face you with its four, tendril-like mouths.")
                input("\nThe last thing you hear is its horrible, high-pitched scream.")
                you_died_blob_monster_five()
            else:
                input("\nYou decide to not slip past the monster.")
                continue
        if explore_third=="a":
            input("\nYou notice a door to your left with the label 'C2' on it.")
            input("\nIt requires a number code to open.")
            input("\nRemembering the piece of paper you got from the other room, you take it out of your pocket.")
            input("\nThere is a number code written on it that may open this door.")
            input("\nThe blob monster lets out a frustrated groan as it continues to scratch at the door.")
            key_door=input("\nWould you like to open the door? Press i for yes and any other key for no.")
            if key_door=="i":
                input("\nYou punch the code into the key pad.")
                input("\nThe door unlocks with a loud beep that makes your heart stop.")
                input("\nThe blob monster stops pawing at the door, raising two of its tendril mouths in the air.")
                input("\nLuckily, you manage to open the door and slip into the next room right as it opens one of its mouth to scream.")
                c2_room()
            else:
                input("\nYou decide to not open the door.")
                continue
        if explore_third=="d":
            input("\nThere is a blank wall to your left.")
            input("\nLooking down, you also notice a black marker on the floor.")
            input("\nMaybe you should write your own creepy message to be read by the next unlucky sap to end up here.")
            own_message=input("\nPlease enter your own creepy message or press q not to: ")
            if own_message=="q":
                input("\nYou decide to not write a message.")
                continue
            else:
                input("\nThe next time someone is forced to wander these cursed hospice halls, they may turn and shine their flash light on your chilling message: "+own_message+" How blood-curdling!")
                continue

def c2_room():
    input("\nYou shine your flashlight on a single wooden table in the center of the room.")
    explore_c2 = ""
    while explore_c2 != ("a", "s", "d", "w", "g", "h", "i", "p"):
     explore_c2 = input("\nPress w-forward,a-left,s-turn around,d-right to explore room C2. Press i to open doors.\n")
     if explore_c2=="s":
        input("\nYou face the door you just came in through.")
        input("\nWould you like to go back out into the hallway?")
        go_back=input("\nPress i to go back out and any other key to stay in the room.")
        if go_back=="i":
            input("\nYou go back out into the hallway.")
            hallway_third_block_backwards_two()
        else:
            input("\nYou decide to stay in the room.")
            continue
     if explore_c2=="w":
         input("\nYou look down at the table and see a single metal key.")
         input("\nThere is a tag attached to it that reads 'key to outdoor pool area.'")
         input("\nWould you like to pick up the key?")
         get_key=input("\nPress p to pick up the key and any other key not to.")
         if get_key=="p":
            input("\nYou pick up the key.")
            writing_on_wall_c2_room()
         else:
            input("\nYou decide not to pick up the key.")
            continue
     if explore_c2=="a":
        input("\nYou look to your left and see nothing but a turned over wheel chair and a bottle of spilled pills.")
     if explore_c2=="d":
        input("\nYou look to your right and see what looks like a body bag on the floor.")
        input("\nIt writhes and twists on the floor like a worm.")
        input("\nYou hear what sounds like a man groaning inside but there is something off about it, inhuman.")
        input("\nWould you like to open the body bag?")
        open_bag=input("\nPress i for yes and any other key for no.")
        if open_bag=="i":
            input("\nYou unzip the black body bag.")
            input("\nA mixture of of what smells like moldy cheese and sour milk hits your nostrils as some mysterious, slimy substance spills out of the bag.")
            input("\nIt spills over your hands, and before you know it, both of them have melted into a pile of liquid on the ground.")
            input("\nThe substance has a mind of its own as it travels up your arms.")
            input("\nYou scream in agony until the foul substance covers your head, dissolving your mind into an opaque liquid.")
            you_died_body_bag_monster()
        else:
            input("\nYou decide to not open the weird, groaning bag.")


def writing_on_wall_c2_room():
    input("\nYour flashlight dies as you pocket the key.")
    input("\nYou can't see a thing as you try flicking the flashlight's switch on and off.")
    input("\nIn the dark, you can hear strange groaning to your right and the vague outline of something trying to prop itself up.")
    input("\nA sudden inhuman, high-pitched scream sounds from down the hall, followed by the sound of a slamming door.")
    input("\nThe thing to your right is now standing upright and hopping towards you.")
    input("\nIt's clumsy movements would be funny if not for its pain-filled groan which seems to grow louder the closer it gets.")
    escape_c2=""
    while escape_c2 != ("a", "s", "d", "w", "g", "h", "i", "p"):
     escape_c2 = input("\nPress w-forward,a-left,s-turn around,d-right to explore room C2. Press i to open doors.\n")
     if escape_c2=="s":
         input("\nWould you like to exit from room C2?")
         leave_room=input("\nPress i to go back into the hallway and any other key to stay in the room.")
         if leave_room=="i":
            input("\nYou leave the room, slamming the door behind you.")
            hallway_block_three_three()
         else:
            input("\nYou decide not to leave the room.")
     if escape_c2=="w":
         input("\nAre you sure that you want to walk further into the room away from the only other door? You aren't alone in here.")
         why_not=input("\nPress w again to walk to the other end of the room or any other key to stay where you are.")
         if why_not=="w":
             input("\nYou walk to the end of the room.")
             input("\nThere is nothing past the wooden table but a blank wall.")
             input("\nBefore you can think of turning back around, you feel a horrifying slimy substance drip down your shoulder as the strange, body bag monster stands right behind you.")
             input("\nThe substance seems to liquefy everything it touches, a revelation you come to shortly before your entire head melts into a puddle.")
             you_died_body_bag_monster_two()
         else:
             input("\nYou decide to stay where you are.")
             continue
     if escape_c2=="a":
         input("\nYou look to your left and see a wheelchair and a bottle of spilled pills.")
         input("\nYou can feel the strange bag-like monster getting closer and closer to you.")
         input("\nWould you like to walk over to the wheelchair on your left?")
         input("\nRemember, you're not alone in here.")
         keep_looking=input("\nPress a again to walk to your left and any other key to stay where you are.")
         if keep_looking=="a":
             input("\nYou walk over to the wheelchair.")
             input("\nIt seems pretty ordinary, nothing unusual about it.")
             input("\nAs you think more about how average this wheelchair is, you hear a loud groan right behind you.")
             input("\nYou turn around and see the body-bag-like creature towering over you.")
             input("\nIt release a foul-smelling, substance that turns even your bones to liquid.")
             input("\nPainful as it is, at least it's a quick way to go.")
             you_died_body_bag_monster_two()
         else:
             input("\nYou decide to stay where you are near the door.")
     if escape_c2=="d":
        input("\nYou look to your right and see the body bag monster hopping towards you.")
        input("\nPathetic as it looks, there's no telling what it might do to you if it catches up to you.")
        input("\nYour flashlight feels cold and heavy in your hands, each flick of its switch reminding you how pointless it is to keep holding onto it.")
        input("\nWould you like to throw your useless flashlight at the body bag monster?")
        curiosity_kills=input("\nPress i to throw your flashlight at the monster and any other key not to.")
        if curiosity_kills=="i":
            input("\nFed up with all of these stupid monsters, you throw your flashlight at it, hitting it with a satisfying squish.")
            input("\nThe monster groans one more time, before releasing a strange liquid which starts to spread all over the room.")
            input("\nYou watch the substance dissolve your flashlight into a pile of liquid.")
            get_out=input("\nWould you like to escape from room C2 before the mysterious substance touches you? Press i to escape through the door and any other key to stay where you are.")
            if get_out=="i":
                input("\nYou open the door and escape into the hallway, not even looking back once.")
                hallway_block_three_three()
            else:
                input("\nYou decide to stay where you are, paralyzed with fear.")
                input("\nThe liquid drenches through your shoes, dissolving them and your feet into a puddle.")
                input("\nWithin seconds, there is nothing left of you but a pile of fluid on the floor.")
                you_died_body_bag_monster_two()
        else:
            input("\nYou decide not to throw your flashlight at the monster. Who knows what might happen?")


def hallway_block_three_three():
    input("\nYou face the blockade at the end of the hallway.")
    input("\nSuddenly, the door to the examination room bursts open in front of you.")
    input("\nThousands of hands, all intertwined and woven together, emerge from the room.")
    input("\nThey grab at the walls, the ceiling, the floor, pulling themselves down the hallway towards you.")
    escape_hallway = ""
    while escape_hallway != ("a", "s", "d", "w", "g", "h", "i", "p"):
        escape_hallway = input("\nPress s to run for your life!!...or press w to stay where you are.\n")
        if escape_hallway=="s":
           hallway_block_two_three_backwards()
        elif escape_hallway=="w":
            input("\nYou stay where you are, watching the strange creature get closer and closer.")
            input("\nIt grabs your arms and pulls you down the hallway at a frightening speed.")
            input("\nYou make one last vain attempt to hold onto the examination room's door frame before being dragged inside, the door slamming behind you.")
            you_died_hallway_monster()
        else:
            continue


def hallway_block_two_three_backwards():
    input("\nYou run as fast as you can, not wanting to look at the hideous thing chasing you.")
    input("\nAs you run, you notice that the blob-shaped monster is no longer in the hallway.")
    input("\nYou stop to catch a glimpse of the door it was clawing at, and notice one of the creature's disembodied arms is jamming the door, keeping it from closing.")
    input("\nYou see what look like strings of silk from a spiderweb on the other side of the door.")
    input("\nWould you like to try and hide from the monster in this room, or do you want to keep running down the hallway?")
    keep_going=""
    while keep_going != ("w","i"):
        keep_going = input("\nPress i to enter the room or w to keep going.\n")
        if keep_going=="w":
          hallway_block_one_three_backwards()
        if keep_going=="i":
          input("\nYou kick the monster's arm aside and shut the door behind you.")
          input("\nThe room is pitch black.")
          input("\nYou step further into the room, until you find yourself stuck in place.")
          input("\nYou panic as one of your arms gets stuck in a thick strand of web.")
          input("\nLooking up, you now see the blob monster from the hallway wrapped up in some kind of strange, white cocoon.")
          input("\nTwo of its arms stick out, hanging limp.")
          input("\nA strange, eight-legged creature moves towards you as you continue to struggle.")
          input("\nThe spider-like creature's body is covered with human faces, each one twisted in a unique expression of agony.")
          input("\nThey all seem to look at you, as the spider begins to wrap you in its webbing.")
          you_died_hallway_monster_spider()
        else:
          input("\nYou can't decide on whether to hide or run.")
          input("\nThe many armed monster grabs your ankles, dragging you down the hallway.")
          input("\nYou scream as the door to the examination room slams shut.")
          you_died_hallway_monster_two()


def hallway_block_one_three_backwards():
    input("\nYou run to the end of the hallway.")
    input("\nYou see a door labeled 'Outdoor Pool Area.'")
    input("\nYou take out the key and unlock the door.")
    input("\nThe monster is getting closer and closer, grabbing at the air, trying to find you.")
    almost_there = ""
    while almost_there != ("s", "i",):
        almost_there = input("\nPress i to open the door or s to stay where you are.")
        if almost_there=="i":
            input("\nYou open the door, shutting it behind you right before the monster is able to grab you.")
            input("\nYou manage to lock the door before the monster can open it again.")
            pool_corridor()
        if almost_there=="s":
            input("\nYou turn around to face the monster.")
            input("\nIt grabs your legs, pulling you down the hallway and back to the examination room.")
            input("\nYou try to grab at anything to save yourself but its too late.")
            input("\nThe monster has you now.")
            you_died_hallway_monster_three()

def pool_corridor():
    input("\nYou run down the corridor as the monster bangs at the closed door.")
    input("\nIt's only a matter of time before it busts through.")
    input("\nTo your right you catch a glimpse of a giant web down a short hallway.")
    input("\nIt is filled with spider-looking creatures, with eight legs, human skin, and various human faces on them, all of them with agonized expressions.")
    input("\nYou keep running until you see a door to your left with light coming in through a small window.")
    input("\nThe door at the end of the hallway opens as the monster pushes its way through.")
    input("\nWould you like to exit through this door or keep running to the end of the hallway?")
    almost_there=""
    while almost_there != ("a", "s", "d", "w", "g", "h", "i", "p"):
        almost_there = input("\nPress i to go through the door or w to keep running down the hall.")
        if almost_there=="i":
          pool_function()
        if almost_there=="w":
          input("\nYou panic and decide to keep running down the hallway.")
          input("\nAnother blob monster with four-tentacle mouths waits for you at the end of the corridor.")
          input("\nIt manages to charge at you and end your life before the monster behind you can grab you.")
          you_died_blob_monster_pool_corridor()

def pool_function():
    input("\nCold, fresh air breezes past your face as you step through the door.")
    input("\nOnce you close it, all of the monstrous creatures seem to disappear like a bad dream.")
    input("\nA thick fog covers everything, making it impossible to see past the fence surrounding the pool.")
    input("\nThere is an empty pool in front of you.")
    input("\nLooking down, you see a large black hole at the bottom of the pool.")
    input("\nIt seems to go on forever.")
    input("\nThe fence surrounds the entire pool area.")
    input("\nHowever, there is a small gap in the part of the fence to your left.")
    input("\nWould you like to go through the gap in the fence into the unknown?")
    finally_done=""
    while finally_done != ("a", "s", "d", "w", "g", "h", "i", "p"):
        finally_done=input("\nPress i to go through the fence and any other key not to.")
        if finally_done=="i":
          input("\nYou slide through the gap in the fence.")
          input("\nNone of the immediate surrounding buildings look familiar to you.")
          input("\nIn the distance, you swear you hear someone screaming, but its too far away to tell.")
          input("\nFighting the urge to turn back, you walk into the fog, braving whatever horrors await you.")
          you_win()
        else:
         input("\nYou decide to stay by the pool for a bit, needing a break from facing yet more awful nightmarish monstrosities.")


def you_win():
    input("\nThank you for playing my game!")
    input("\nThis plot was heavily inspired by Silent Hill 2, with the basic layout of the map having been modeled from the 1st floor of Brookhaven Hospital from said game.")
    input("\nThis was my first big coding project using Python.")
    input("\nThank you so much for taking the time to play through it!")
    input("\nA smiley face for you: \n:)")
    input("\nGoodbye!")
    sys.exit()

















def you_died_blob_monster_one():
    keep_playing=""
    while keep_playing!="Y" or "N":
        keep_playing = input("\nYou have just been killed by a monstrous blob. Would you like to keep playing? Y or N?")
        if keep_playing=="Y":
            print("\nYay!:)")
            explore_hallway()
        elif keep_playing=="N":
            input("\nThanks for playing!")
            sys.exit()
        else:
            continue

def you_died_blob_monster_two():
    keep_playing=""
    while keep_playing!="Y" or "N":
        keep_playing = input("\nYou have just been killed by a monstrous blob. Would you like to keep playing? Y or N?")
        if keep_playing=="Y":
            print("\nYay!:)")
            hallway_third_block_one()
        elif keep_playing=="N":
            input("\nThanks for playing!")
            sys.exit()
        else:
            continue

def you_died_blob_monster_three():
    keep_playing = ""
    while keep_playing != "Y" or "N":
        keep_playing = input("\nYou have just been killed by a monstrous blob. Would you like to keep playing? Y or N?")
        if keep_playing == "Y":
            print("\nYay!:)")
            hallway_fourth_block_one()
        elif keep_playing == "N":
            input("\nThanks for playing!")
            sys.exit()
        else:
            continue

def you_died_blob_monster_four():
    keep_playing = ""
    while keep_playing != "Y" or "N":
        keep_playing = input("\nYou have just been killed by a monstrous blob. Would you like to keep playing? Y or N?")
        if keep_playing == "Y":
            print("\nYay!:)")
            examination_room()
        elif keep_playing == "N":
            input("\nThanks for playing!")
            sys.exit()
        else:
            continue

def you_died_blob_monster_five():
    keep_playing = ""
    while keep_playing != "Y" or "N":
        keep_playing = input("\nYou have just been killed by a monstrous blob. Would you like to keep playing? Y or N?")
        if keep_playing == "Y":
            print("\nYay!:)")
            hallway_third_block_backwards_two()
        elif keep_playing == "N":
            input("\nThanks for playing!")
            sys.exit()
        else:
            continue


def you_died_spider_monster_one():
    keep_playing=""
    while keep_playing!="Y" or "N":
        keep_playing = input("\nYou have just been killed by a spider monster. Would you like to keep playing? Y or N?")
        if keep_playing=="Y":
            print("\nYay!:)")
            input("\nYou walk down the hallway. Stopping to examine your surroundings, you notice a door to your right that says 'C3' on it.")
            input("\nThe blob-monster can still be heard chewing on flesh behind you. It doesn't seem to have noticed you yet.")
            hallway_second_block()
        elif keep_playing=="N":
            input("\nThanks for playing!")
            sys.exit()
        else:
            continue

def you_died_slime_monster():
    keep_playing = ""
    while keep_playing != "Y" or "N":
      keep_playing = input("\nYou have just been killed by a slime monster. Would you like to keep playing? Y or N?")
      if keep_playing == "Y":
         print("\nYay!:)")
         slime_monster()
      elif keep_playing == "N":
             input("\nThanks for playing!")
             sys.exit()
      else:
            continue

def you_died_slime_monster_two():
    keep_playing = ""
    while keep_playing != "Y" or "N":
     keep_playing = input("\nYou have just been killed by a slime monster. Would you like to keep playing? Y or N?")
     if keep_playing == "Y":
         print("\nYay!:)")
         hallway_fourth_block_two()
     elif keep_playing == "N":
         input("\nThanks for playing!")
         sys.exit()
     else:
         continue

def you_died_body_bag_monster():
    keep_playing = ""
    while keep_playing != "Y" or "N":
     keep_playing = input("\nYou have just been killed by a body bag monster. Would you like to keep playing? Y or N?")
     if keep_playing == "Y":
         print("\nYay!:)")
         c2_room()
     elif keep_playing == "N":
         input("\nThanks for playing!")
         sys.exit()
     else:
         continue

def you_died_body_bag_monster_two():
    keep_playing = ""
    while keep_playing != "Y" or "N":
     keep_playing = input("\nYou have just been killed by a body bag monster. Would you like to keep playing? Y or N?")
     if keep_playing == "Y":
         print("\nYay!:)")
         writing_on_wall_c2_room()
     elif keep_playing == "N":
         input("\nThanks for playing!")
         sys.exit()
     else:
         continue

def you_died_hallway_monster():
    keep_playing = ""
    while keep_playing != "Y" or "N":
     keep_playing = input("\nYou have just been killed by a monster with many hands. Would you like to keep playing? Y or N?")
     if keep_playing == "Y":
        print("\nYay!:)")
        hallway_block_three_three()
     elif keep_playing == "N":
        input("\nThanks for playing!")
        sys.exit()
     else:
         continue

def you_died_hallway_monster_spider():
    keep_playing = ""
    while keep_playing != "Y" or "N":
     keep_playing = input("\nYou have just been killed by a monster spider. Would you like to keep playing? Y or N?")
     if keep_playing == "Y":
        print("\nYay!:)")
        hallway_block_two_three_backwards()
     elif keep_playing == "N":
        input("\nThanks for playing!")
        sys.exit()
     else:
         continue


def you_died_hallway_monster_two():
    keep_playing = ""
    while keep_playing != "Y" or "N":
     keep_playing = input("\nYou have just been killed by a monster with many hands. Would you like to keep playing? Y or N?")
     if keep_playing == "Y":
        print("\nYay!:)")
        hallway_block_two_three_backwards()
     elif keep_playing == "N":
        input("\nThanks for playing!")
        sys.exit()
     else:
         continue

def you_died_hallway_monster_three():
    keep_playing = ""
    while keep_playing != "Y" or "N":
     keep_playing = input("\nYou have just been killed by a monster with many hands. Would you like to keep playing? Y or N?")
     if keep_playing == "Y":
        print("\nYay!:)")
        hallway_block_one_three_backwards()
     elif keep_playing == "N":
        input("\nThanks for playing!")
        sys.exit()
     else:
         continue

def you_died_blob_monster_pool_corridor():
    keep_playing = ""
    while keep_playing != "Y" or "N":
        keep_playing = input("\nYou have just been killed by a blob monster. Would you like to keep playing? Y or N?")
        if keep_playing == "Y":
            print("\nYay!:)")
            pool_corridor()
        elif keep_playing == "N":
            input("\nThanks for playing!")
            sys.exit()
        else:
         continue





#title_screen()
#wake_up()
#flash_light()
#hallway_one()
#explore_hallway()
#down_the_hallway_one()
#hallway_second_block()
#hallway_third_block_one()
#hallway_third_block_backwards_one()
#hallway_fourth_block_one()
#examination_room()
#slime_monster()
#hallway_fourth_block_two()
#c2_room()
#writing_on_wall_c2_room()
#hallway_block_two_three_backwards()
#pool_corridor()

