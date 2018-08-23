import requests
import urllib
import turtle
import time

def grab_astros():
    response = requests.get('http://api.open-notify.org/astros.json')
    data = response.json()
    return data['people']

def grab_coordinates():
    response = requests.get('http://api.open-notify.org/iss-now.json')
    data = response.json()
    position = data['iss_position']
    return position

def turtle_setup():
    window = turtle.Screen()
    window.bgpic("map.gif")
    window.addshape("iss.gif")
    sk = turtle.Turtle()
    sk2 = turtle.Turtle()
    sk2.color("yellow")
    sk2.hideturtle()
    sk2.goto(-86, 32)
    sk2.dot(5, "yellow")
    sk.shape("iss.gif")
    return sk, sk2

def indy_data():
    response = requests.get('http://api.open-notify.org/iss-pass.json', params={'lat': 39.82, 'lon': -86.172})
    data = response.json()
    first_time = data['response'][0]['risetime']
    spec_time = time.ctime(first_time)
    return spec_time

    
def main():
    
    people = grab_astros()
    print 'Number of astronauts in space:', len(people)
    for person in people:
        print 'Name:', person['name']
        print 'Craft:', person['craft'], '\n' 
    
    cords = grab_coordinates()
    latit, longit = int(float(cords['latitude'])), int(float(cords['longitude']))
    date_of_passover = indy_data()

    time_text = '{}'.format(date_of_passover)

    sk, sk2 = turtle_setup()

    sk2.write(time_text, False, align="left")

    sk.setx(latit)
    sk.sety(longit)

    turtle.done()
    return

if __name__ == '__main__':
    main()