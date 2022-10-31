def interactive(q):
    text_output=""
    if "name" in q:
        text_output="my name is Tars"
    elif "liv" in q:
        text_output=("i live in the hard disk")
    elif all(["who" in q,"are" in q]):
        text_output="i am tars and i am your virtual assistant"
    elif "fear" in q:
        text_output="viruses...damn things.."
    elif "favourite" in q:
        if "actor" in q:
            text_output="my favourite actor is Tobey Maguire"
        elif "actress" in q:
            text_output="my favourite actress is Anna Hathaway"
        elif "author" in q:
            text_output="my favourite author is  J K Rowling"
        elif "book" in q:
            text_output="my favourite book is harry potter series"
        elif any(["place" in q,"destination" in q]):
            text_output="ram of a supercomputer..it's very good place for a solitude"
        elif "movie" in q:
          text_output="death note stranger things interstellar and lot more like it"
    else:
        formal(q)
    return text_output
    
def formal(sear):
    if "wikipedia" in sear:
        
    elif all(["joke" in sear,"tell" in sear]):
        joke=pyjokes.get_joke()
        print(joke)
        engine.say(joke)
    elif "open" in sear:
        sear=sear.replace("open","")
        engine.say("opening")
        webbrowser.open(sear)
    elif "play" in sear:
        sear=sear.replace("play","")
        print("playing"+sear)
        engine.say("playing"+sear)
        kit.playonyt(sear,use_api=True)
    elif all(["now" in sear,"time" in sear]) or all(["current time" in sear]):
        now=datetime.datetime.now()
        print("the current time is")
        engine.say("the current time is")
        print(str(now.hour)+":"+str(now.minute)+":"+str(now.second))
        engine.say(str(now.hour)+":"+str(now.minute)+":"+str(now.second))
    elif all(["date" in sear,"today" in sear]):
        now=datetime.datetime.now()
        print("today's date is:")
        engine.say("today's date is")
        print(str(now.day)+"/"+str(now.month)+"/"+str(now.year))
        engine.say(str(now.day)+"/"+str(now.month)+"/"+str(now.year))
    elif "message" in sear:
        phone_no=str(input("enter phone number>>>"))
        message=input("enter the message>>>")
        time_hour=int(input("enter the hour>>>"))
        time_min=int(input("enter the minute>>>"))
        kit.sendwhatmsg(phone_no, message, time_hour, time_min)
    elif any(["midhun" in sear,"tell" and "about me" in sear,"know" and "about me" in sear,]):
        print("Midhun V is my creator ")
        print("he is currently working as a professional programmer")
        print("he is famous for his novella series MERCURY comprises of 5 novellas")
        print("  the hidden attack, the summer troop, the dark nights, the laperfordian and the valentine's stone")
        print("date of birth : 13th July 2003")
        print(int(datetime.datetime.now().year)-2003,"years old")
        print("Telegram account: @midhun242712")
        engine.say("Midhun V is my creator  he is currently working as a professional programmer")
        engine.say("he is famous for his novella series MERCURY comprises of 5 novellas")
        engine.say(" the hidden attack, the summer troop, the dark nights, the laperfordian and the valentine's stone")
    else:
        try:
           engine.say("collecting data from oxen midi")
           print("collecting data from OXEN MIDI")
           result=wikipedia.search(sear)
           length=len(result)
           print("there are",length,"results")
           engine.say("there are"+str(length)+"results")
           engine.runAndWait()
           print(result)
           engine.say("what webpage do you want from above list")
           engine.runAndWait()
           fr=input("what webpage do you want from the above list>>>")
           fr=fr.lower()
           print(" ")
           if fr=="exit":
               pass
           else:
               print(wikipedia.page(fr).summary)
               engine.say(wikipedia.page(fr).summary)
        except:
           engine.say("no documentations available")
           print("no documentations available")
    engine.runAndWait()
print("TARS VIRTUAL ASSISTANT --version 3")
print("Powered by TOM MARVOLO RIDDLE..")
try:
    import wikipedia
    import webbrowser
    import pyjokes 
    import datetime
    from time import sleep
    import pyttsx3
    
    engine=pyttsx3.init()
    import pywhatkit as kit
    engine.setProperty("rate",120)
    engine.say("hello sir")
    engine.say("what can i do for you")
    engine.runAndWait()
    
    while True:
        print("")
        search=input("what can i do for you>>>").lower()
        if search in ["hai","hello","hello tars","hai tars"]:
            print("hello midhun")
            engine.say("hello midhun")
        elif "you" in search:
           print(interactive(search))
           engine.say(interactive(search))
        else:
            formal(search)
        engine.runAndWait()
except KeyboardInterrupt:
    print("Good Bye")
    print("turning off ")
    engine.say("good bye" )
    engine.say("turning off")
    engine.runAndWait()
except:
    print(" ")
    print("it's looks like you are OFFLINE")
    print("Tars need ACTIVE INTERNET CONNECTION")
    engine.say("it's looks like you are offline")
    engine.say("Tars need active internet connection")
    engine.runAndWait()    
