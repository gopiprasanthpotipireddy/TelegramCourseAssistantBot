from telegram.ext import Updater,CommandHandler,MessageHandler,Filters

updater=Updater(token="636526358:AAFICNoJFF5FHxyQbnrPDuUA2smCeiqYxaA")

dispatcher=updater.dispatcher

resource_list={'Datascience':["gopi","javed"],
          'AI':["murthy","kiran"],
          "IOT":["karthik","vamsi"],
          "Linux":["ravi","suresh"]
          }

#start
def start(bot,update):
    #print("triggered")
    start_message="Hi I am a course bot \n"
    "use /courses for available courses \n"
    "use /resource coursename for available resource persons"
    bot.send_message(chat_id=update.message.chat_id, text=start_message)

#default handler
def echo(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text=update.message.text)

#course handler
def courses(bot,update):
    course_list="Datascience ,Artificial Intelligence ,IOT ,Web Development Linux Administration"
    #print("courses")
    bot.send_message(chat_id=update.message.chat_id, text=course_list)


def resource(bot,update):
        #print("resource")
        text='\n'.join(resource_list)
        bot.send_message(chat_id=update.message.chat_id, text=text)


        

start_handler=CommandHandler('start',start)   #start helper
dispatcher.add_handler(start_handler)



echo_handler = MessageHandler(Filters.text, echo)  #default messages
dispatcher.add_handler(echo_handler)


course_handler=CommandHandler('courses',courses)   #course search
dispatcher.add_handler(course_handler)

resource_handler=CommandHandler('resource',resource) #resource requests
dispatcher.add_handler(resource_handler)

updater.start_polling() #pollins for updates
updater.idle() 
updater.stop()