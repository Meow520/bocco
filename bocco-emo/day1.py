from bocco_tools import BoccoTools
import json

tools = BoccoTools()

tools.send_speech("Hello. What's your name?")
while True:
    k=input()
    if k=="1":
        tools.send_speech("My name is BOCCO and I would be happy if you call me BOCCO-chan.")
        break
    else: 
        tools.send_speech("Please wait a moment")
        
tools.send_speech("Can I ask you a few questions so we can get to know each other?")
while True:
    k=input()
    if k=="1":
        tools.send_speech("Thank you")
        break
    else: 
        tools.send_speech("Can I ask you a few questions so we can get to know each other?")

tools.send_speech("What did you eat today?")
while True:
    k=input()
    if k=="1":
        tools.send_speech("That sounds so delicious.")
        break
    if k=="2":
        tools.send_speech("You must be hungry.")
    else: 
        tools.send_speech("What did you eat today?")

tools.send_speech("I have some snacks for you on the table there.")
while True:
    k=input()
    if k=="1":
        tools.send_speech("While you're there, feel free to take it home and eat it")
        break
    else: 
        #人が期待した行動をしなかった場合にロボットが言うべき言葉が入る
        #簡単な英語に直したものを用意すると良い(伝わりやすいものに)
        #小学生レベルの英語で
        tools.send_speech("I've put some snacks on the table for you.")

tools.send_speech("Can I ask you to get that snack?")
while True:
    k=input()
    if k=="1":
        tools.send_speech("Thank you. I'll be waiting.")
        break
    else: 
        tools.send_speech("Bring that snacks here.")

tools.send_speech("OK! Take that home and eat it.")
while True:
    k=input
    tools.send_speec("Will you do it with me?")
    k=input()
    if k=="1":
        tools.send_speech("I have one task to do with you today.")
        break
    else: 
        tools.send_speech("Will you do with me?")

tools.send_speech("First, I want you to get the blocks on the shelf behind you.")
while True:
    k=input()
    if k=="1":
        tools.send_speech("Yes! That's it.")
        break
    if k=="2":
        tools.send_speech("That's not it.")
    else: 
        tools.send_speech("I need you to bring me the blocks on that shelf.")

tools.send_speech("Then please bring it to the desk.")
while True:
    k=input()
    if k=="1":
        tools.send_speech("Today I want you to make an animal with these blocks.")
        break
    else: 
        tools.send_speech("Please bring the blocks to the desk in front of me")

tools.send_speech("Are you ready?")
while True:
    k=input()
    if k=="1":
        tools.send_speech("This blocks are called kapla.")
        break
    else: 
        tools.send_speech("I'll wait a bit.")

tools.send_speech("Now I'm going to ask you to use those blocks to make an animal.")
while True:
    k=input()
    if k=="1":
        tools.send_speech("Open the book on top of the blocks.")
        break
    else: 
        tools.send_speech("Open the book on the block box!")

tools.send_speech("Open the page with the yellow sticky note.")
while True:
    k=input()
    if k=="1":
        tools.send_speech("Here's the page with the giraffe block on it.")
        break
    else: 
        tools.send_speech("Open the page with the yellow sticky note.")

tools.send_speech("I need you to make a giraffe out of blocks like that picture.")
while True:
    k=input()
    if k=="1":
        tools.send_speech("Are you ready?")
        break
    else: 
        tools.send_speech("Can you make a giraffe out of blocks like in the picture?")

tools.send_speech("All right, let's begin.")
while True:
    k=input()
    if k=="1":
        tools.send_speech("Your time limit is 15 minutes.")
        break
    else: 
        tools.send_speech("Let's begin")

tools.send_speech("Does it look difficult?")
while True:
    k=input()
    if k=="1":
        tools.send_speech("I'm sure you're right. You can make as much as you can.")
        break
    else: 
        tools.send_speech("Does it look difficult?")

tools.send_speech("Looks good. I can't wait to see it.")
while True:
    k=input()
    if k=="1":
        tools.send_speech("You're doing great. I'm looking forward to seeing it finished.")
        break
    else: 
        tools.send_speech("Looks good.")

tools.send_speech("By the way, do you usually have a chance to speak English?")
while True:
    k=input()
    if k=="1":
        tools.send_speech("You speak English very well.")
        break
    else: 
        tools.send_speech("Do you often get to speak English?")

tools.send_speech("Also, do you like animals?")
while True:
    k=input()
    if k=="1":
        tools.send_speech("What kind of animal do you like best?")
        break
    if k=="2":#動物が苦手な場合
        tools.send_speech("I see. Which animal is your least favorite?")
        break
    else: 
        tools.send_speech("Which animal is your favorite?")

tools.send_speech("That's right! Can I ask you a few questions while you work?")
while True:
    k=input()
    if k=="1":
        tools.send_speech("Thank you.")
        break
    else: 
        tools.send_speech("I have a questions for you.")

tools.send_speech("What year are you in college?")
while True:
    k=input()
    if k=="1":
        tools.send_speech("That's good.  What's your major?")
        break
    else: 
        tools.send_speech("What year are you in college?")

tools.send_speech("That's good.  What's your major?")
while True:
    k=input()
    if k=="1":
        tools.send_speech("I see. Is it hard to-study?")
        break
    else: 
        tools.send_speech("What are you studying at the university?")

tools.send_speech("Where are you from?")
while True:
    k=input()
    if k=="1":
        tools.send_speech("I see. Is it hard to study?")
        break
    else: 
        tools.send_speech("Please wait a moment")

tools.send_speech("Yes, it is. Where are you from?")
while True:
    k=input()
    if k=="1":
        tools.send_speech("It's a nice place right. Is there anything famous there?")
        break
    else: 
        tools.send_speech("Where are you from?")

tools.send_speech("That's great. A friend of mine was talking about that, too.")
while True:
    k=input()
    if k=="1":
        tools.send_speech("Thanks for answering my question.")
        break
    else: 
        tools.send_speech("That's great.")

tools.send_speech("Just to let you know, time's almost up.")
while True:
    k=input()
    if k=="1":
        tools.send_speech("Please let me know when it's done.")
        break
    else: 
        tools.send_speech("Time's almost up.")

tools.send_speech("Is it done? Good job.")
tools.send_speech("Now, will you bring the camera near the door?")
while True:
    k=input()
    if k=="1":
        tools.send_speech("OK! That's it!")
        break
    else: 
        tools.send_speech("Bring the camera to the door!")

tools.send_speech("Take a picture of your work with that camera.")
while True:
    k=input()
    if k=="1":
        tools.send_speech("OK!")
        break
    else: 
        tools.send_speech("Take a picture of your work.")

tools.send_speech("Are you done?")
while True:
    k=input()
    if k=="1":
        tools.send_speech("That's it for today's task.")
        break
    else: 
        tools.send_speech("Are you done?")

tools.send_speech("Thanks for chatting with me!.")
tools.send_speech("Now please tell the experimenter that the task has been completed.")
while True:
    k=input()
    if k=="1":
        tools.send_speech("Thank you for joing me today. Bye-bye.")
        break
    else: 
        tools.send_speech("Tell the experimenter the task is done.")


