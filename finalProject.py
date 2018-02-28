from flask import Flask, render_template, url_for, redirect
app = Flask(__name__)


#fake database of restaurants

restaurant = {'name':'Pib Burgers','id':'1'}

restaurants = [{'name':'KCreeppers','id':1}, {'name':'Mc Shrimpss','id':2}]


#Initial
#the argument restaurant_id = restaurant id allows me to pass the value
#of restaurant_id to the template restarants.html
@app.route('/')
@app.route('/restaurants')
def showRestaurants():
    restaurants_id = restaurants
    return render_template('restaurants.html', restaurants_id = restaurants_id)


#Create a new restaurant
#int will turn into an interger once checked
@app.route('/restaurant/new')
@app.route('/restaurant/<int:restaurant_id>/menu/new')
def newRestaurant(restaurant_id):
    restaurant_id = "This page will be for making new restaurants"
    return render_template('restaurantNew.html',restaurant_id = restaurant_id)

#Edit a restaurant & menu
@app.route('/restaurant/<int:restaurant_id>/edit')
@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/edit')
def editRestaurant(restaurant_id,menu_id):
    return "edit restaurant's menu"

#Delete a restaurant
@app.route('/restaurant/<int:restaurant_id>/delete')
def deleteRestaurant(restaurant_id):
    restaurant_id = "This page will be for deleting restaurant"
    return restaurant_id

#Show menu
@app.route('/restaurant/<int:restaurant_id>')
@app.route('/restaurant/<int:restaurant_id>/menu')
def showMenu(restaurant_id):
    restaurant_id = "This page is for making a new menu for a restaurant"
    return restaurant_id

#New Menu Item
@app.route('/restaurant/<int:restaurant_id>/menu/new')
def newMenuItem(restaurant_id):
    restaurant_id = "This page is for making a new menu"
    return restaurant_id

#Edit Menu Item
@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/edit/')
def editMenuItem(restaurant_id,menu_id):
    return "This page is to edit menu"


#Delete Menu Item
@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/delete')
def deleteMenuItem(restaurant_id,menu_id):
    return "This page is to delete the menu"


if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0', port=5000)
