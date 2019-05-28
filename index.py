import os
from flask import Flask, jsonify, request
from teleflask import Teleflask
import datetime

###

print("oi")

app = Flask(__name__)

bot = Teleflask(os.environ["API_KEY"])
bot.init_app(app)

###

print("ooi")

last_prediction_time = None
last_prediction_decision = False
last_predicition_leave_time = None 


# Register the /start command
@bot.command("start")
def start(update, text):
    return TextMessage("<b>Oi, porra!</b>", parse_mode="html")
# end def

def get_random_timestamp():
    start_date = datetime.datetime.now()   # tomorrow
    start_date = start_date.replace(hour = 11, minute=30, second=0)  # set to 8 AM
    seconds_max = 6*70*60  # 8AM to 3PM is 7 hours                 # 7 hrs in seconds
    time_offset = np.random.randint(0, seconds_max)
    day_offset = np.random.choice(range(5))
    final_date = start_date + datetime.timedelta(seconds=time_offset, days=day_offset)
    return final_date

# Register the /previsao command
@bot.command("previsao")
def previsao(update, text):
    global last_prediction_time
    global last_prediction_decision
    global last_predicition_leave_time

    if last_prediction_time == datetime.today():
        message = random.choice["Você já perguntou isso, poxa :(", "Já respondi isso hoje!", "Olha aí em cima, porra"]
    else: 
        last_prediction_time = datetime.today()
        last_prediction_decision = random.choice([True, True, True, True, False])

        message = "VAI!" if last_prediction_decision else "NÃO VAI!"

        if last_prediction_decision:
            last_predicition_leave_time = get_random_timestamp()
            message += "Ele sairá às " + last_predicition_leave_time.strftime("%H:%M") + " :)"
        else:
            last_predicition_leave_time = None
            message += "Sorry :("
    

    # update is the update object. It is of type pytgbot.api_types.receivable.updates.Update
    # text is the text after the command. Can be empty. Type is str.
    return [TextMessage("O Enzo....", parse_mode="html"), TextMessage(message, parse_mode="html")]
# end def

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)