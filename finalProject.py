from flask import Flask
app = Flask(__name__)

#Initial
@app.route('/')
@app.route('/restaurants/<int:restaurant_id>')
def showRestaurants():
    restaurant_id = "This page will show all my restaurants"
    return restaurant_id

#Create a new restaurant
@app.route('/restaurant/new')
@app.route('/restaurant/<int:restaurant_id>/menu/new')
def newRestaurant():
    restaurant_id = "This page will be for making new restaurants"
    return restaurant_id


#Edit a restaurant
@app.route('/restaurant/<int:restaurant_id>/edit')
@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/edit')
def editRestaurant():
    restaurant_id = "restaurant_id"
    menu_id = "menu_id"
    return restaurant_id

#Delete a restaurant
@app.route('/restaurant/<int:restaurant_id>/delete')
def deleteRestaurant():
    restaurant_id = "This page will be for deleting restaurant"
    return restaurant_id

#Show menu
@app.route('/restaurant/restaurant_id')
@app.route('/restaurant/restaurant_id/menu')
def showMenu():
    restaurant_id = "This page is for making a new menu for a restaurant"
    return restaurant_id

#New Menu Item
@app.route('/restaurant_id/menu/new')
def newMenuItem():
    return "This page is for making new menu"

#Edit Menu Item
@app.route('/restaurant/restaurant_id/menu/menu_id/edit/')
def editMenuItem():
    return "This page is to edit menu"

#Delete Menu Item
@app.route('/restaurant_id/menu/menu_id/delete')
def deleteMenuItem():
    return "This page deletes the menu"



if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0', port=5000)
