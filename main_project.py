from flask import Flask, render_template
from firebase import firebase
firebase = firebase.FirebaseApplication('https://esp8266-4cd3e.firebaseio.com', None)
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def chart():
    result = firebase.get('/ESP8266_Test/Push/Int', None)
    data_get = list(result.values())
    # print(len(data_get))
    # print(data_get[0]['time'])

    time_data = []
    for data in data_get:
        time_loop = datetime.fromtimestamp(data['time'])
        time_data.append(str(time_loop))

    final_data = []
    for time,move_data in zip(time_data,data_get):
        date_dict = {'time_con': str(time)}
        move_data.update(date_dict)
        final_data.append(move_data)
        # print(move_data)

    final = []
    loop_end = 0
    for x in reversed(final_data):
        if loop_end != 10:
            final.append(x)
            loop_end += 1
    loop_end = 0

    # print(final_data)
    return render_template('template.html', values=final)



@app.route('/log')
def log():
    result = firebase.get('/ESP8266_Test/Push/Int', None)
    data_get = list(result.values())

    time_data = []
    for data in data_get:
        time_loop = datetime.fromtimestamp(data['time'])
        time_data.append(str(time_loop))

    # print(time_data)

    final_data = []
    for time,move_data in zip(time_data,data_get):
        date_dict = {'time_con': str(time)}
        move_data.update(date_dict)
        final_data.append(move_data)
        # print(move_data)

    final = []
    for x in reversed(final_data):
        final.append(x)
    # print(final_data)
    return render_template('log.html', values=final)


if __name__ == '__main__':
    app.debug = True
    app.run()