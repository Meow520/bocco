from bocco_tools import BoccoTools
import json

tools = BoccoTools()

tools.send_speech("Hello.This is the second time we have met today. ")
tools.send_speech("My name is BOCCO.I would be happy if you call me BOCCO like before. Can I ask you a few more questions today?")
while True:
    k=input()
    if k=="1":
        tools.send_speech("OK, thank you!")
        break
    else: 
        tools.send_speech("Can I ask you a few more questions?")
        
tools.send_speech("How is the weather today?")
while True:
    k=input()
    if k=="1":
        tools.send_speech("I see. It's getting colder these days, so take care of yourself.")
        break
    else: 
        tools.send_speech("How is the weather today?")

tools.send_speech("Which seasons do you like the best?")
while True:
    k=input()
    if k=="1":
        tools.send_speech("I like it too! There are so many fun events.")
        break
    else":
        tools.send_speech("Which seasons do you like the best?")

tools.send_speech("I have tasks I need to do today, too. Will you do with me?")
while True:
    k=input()
    if k=="1":
        tools.send_speech("First, I want you to get the block on the shelf.")
        break
    else: 
        tools.send_speech("I have tasks I need to do today.")

tools.send_speech("This brock is the same as before.Open the page with the sticky note as you did last time.")
while True:
    k=input()
    if k=="1":
        tools.send_speech("I need you to build this bridge today.")
        break
    else: 
        tools.send_speech("Open the page with the sticky note like last time.")

tools.send_speech("OK! Let's start!")
while True:
    k=input
    tools.send_speec("I think tiday will be more difficult than last time.")
    k=input()
    if k=="1":
        tools.send_speech("Let' start.")
        break
    else: 
        tools.send_speech("Will you do with me?")

tools.send_speech("Time is the same as before, 15 minitues.")
while True:
    k=input()
    if k=="1":
        tools.send_speech("As much as you can do.")
        break
    else: 
        tools.send_speech("Time is less than 15 minitues.")

tools.send_speech("If it's difficult, you can change it to make it easier to make.")
while True:
    k=input()
    if k=="1":
        tools.send_speech("Answer questions as you work.")
        break
    else: 
        tools.send_speech("If it's hard, you can change it to make it easier.")

tools.send_speech("Have you had a chance to speak English since you last spoke to me?")
while True:
    k=input()
    if k=="1":
        tools.send_speech("I see. I think you speak English more fluently than before.")
        break
    else: 
        tools.send_speech("Have you spoken English since we last talked?")

tools.send_speech("Studying English is difficult, isn't it?")
while True:
    k=input()
    if k=="1":
        tools.send_speech("I have some recommendations for you to study!")
        break
    else: 
        tools.send_speech("Studying English is difficult, isn't it?")

tools.send_speech("That means watching foreign dramas and movies.")
while True:
    k=input()
    if k=="1":
        tools.send_speech("It's important to be exposed to English on a regular basis.")
        break
    else: 
        tools.send_speech("That means watching foreign dramas and movies.")

tools.send_speech("Do you have the opportunity to watch English-language dramas and movies?")
while True:
    k=input()
    if k=="1":#英語をはなしていると言ったら
        tools.send_speech("That's a good thing.")
        break
    if k=="2":#英語を話す機会が少なかったら
        tools.send_speech("Well, I hope we'll have more opportunities in the future.")
        break
    else: 
        tools.send_speech("Can you watch English-language dramas and movies?")

tools.send_speech("I recommend that you live a life in which you are exposed to English on a regular basis, as this will naturally improve your English.")
tools.send_speech("Also, listen to English songs!")
tools.send_speech("What kind of artists do you like?")
while True:
    k=input()
    if k=="1":
        tools.send_speech("That's great. I love their music, too")
        break
    else: 
        tools.send_speech("What kind of artists do you like?")

tools.send_speech("Do you have favorite movie?")
while True:
    k=input()
    if k=="1":
        tools.send_speech("I see. My friend I recently talked to said he liked Titanic.")
        break
    else: 
        tools.send_speech("Do you have favorite movie?")

tools.send_speech("Have you seen it?")
while True:
    k=input()
    if k=="1":#見たことあったら
        tools.send_speech("It's a wonderful story.")
        break
    if k=="2":#見てなかったら
        tools.send_speech("I recommend this work. You should definitely take a look.")
        break
    else: 
        tools.send_speech("Have you seen it?")

tools.send_speech("If you rewatch the movie a few times, you'll get the English phrases in your head and be able to use them in your daily life!")
while True:
    k=input()
    if k=="1":
        tools.send_speech("okay.")
        break
    else: 
        tools.send_speech("If you rewatch the movie a few times, you'll learn to speak English better.")

tools.send_speech("Will the work be finished soon?")
while True:
    k=input()
    if k=="1":#もうすぐ終わる場合
        tools.send_speech("Looks good")
        break
    k=="2":#まだ時間がかかる場合
        tools.send_speech("Then I'll wait a little while longer.")
        break
    else: 
        tools.send_speech("Will the work be finished soon?")

tools.send_speech("Let me know when you finish it.")
while True:
    k=input()
    if k=="1":
        tools.send_speech("OK! Thank you.")
        break
    else: 
        tools.send_speech("Let me know when you finish it.")

tools.send_speech("You're doing very well today")
while True:
    k=input()
    if k=="1":
        tools.send_speech("Okay/")
        break
    else: 
        tools.send_speech("You're doing very well today")

tools.send_speech("Can you do the same as before, and bring the camera near the entrance door?")
while True:
    k=input()
    if k=="1":
        tools.send_speech("Yes, that's it!")
        break
    else: 
        tools.send_speech("bring the camera!")

tools.send_speech("Take a picture of your work with that camera.")
while True:
    k=input()
    if k=="1":
        tools.send_speech("That looks good!")
        break
    else: 
        tools.send_speech("Take a picture of your work with that camera.")

tools.send_speech("Tell the experimenter that the task has been completed.")
while True:
    k=input()
    if k=="1":
        tools.send_speech("Thank you for joing me today. Bye-bye.")
        break
    else: 
        tools.send_speech("Tell the experimenter that the task has been completed.")

