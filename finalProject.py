from flask import Flask, render_template, url_for, redirect
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem



app = Flask(__name__)


#fake database of restaurants

# restaurant = {'name':'Pib Burgers','id':'1'}
#
restaurants = [{'name':'KCreeppers','id':1}, {'name':'Mc Shrimpss','id':2}]
#
# items = [ {'name':'Cheese Pizza', 'description':'made with fresh cheese', 'price':'$5.99','course' :'Entree', 'id':'1'}, {'name':'Chocolate Cake','description':'made with Dutch Chocolate', 'price':'$3.99', 'course':'Dessert','id':'2'},{'name':'Caesar Salad', 'description':'with fresh organic vegetables','price':'$5.99', 'course':'Entree','id':'3'},{'name':'Iced Tea', 'description':'with lemon','price':'$.99', 'course':'Beverage','id':'4'},{'name':'Spinach Dip', 'description':'creamy dip with fresh spinach','price':'$1.99', 'course':'Appetizer','id':'5'} ]
# item =  {'name':'Cheese Pizza','description':'made with fresh cheese','price':'$5.99','course' :'Entree'}


#Initial
#the argument restaurant_id = restaurant id allows me to pass the value
#of restaurant_id to the template restarants.html
@app.route('/')
@app.route('/restaurant/new/')
def showRestaurants():
    restaurant_id = restaurants
    return render_template('restaurants.html', restaurant_id = restaurant_id)


#Create a new restaurant
#int will turn into an interger once checked
@app.route('/restaurant/new')
@app.route('/restaurant/<int:restaurant_id>/menu/new')
def newRestaurant(restaurant_id):
    restaurant_id = restaurant
    return render_template('newRestaurant.html',restaurant_id = restaurant_id)


#Edit a restaurant & menu
@app.route('/restaurant/<int:restaurant_id>/edit/')
@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/edit/')
def editRestaurant(restaurant_id,menu_id):
    restaurant_id = restaurant
    menu_id = item
    return render_template('editRestaurant.html',restaurant_id = restaurant_id,menu_id = menu_id)

#Delete a restaurant
@app.route('/restaurant/<int:restaurant_id>/delete')
def deleteRestaurant(restaurant_id):
    restaurant_id = restaurant
    # restaurant_id = "This page will be for deleting restaurant"
    return render_template('deleteRestaurant.html',restaurant_id = restaurant_id)

#Show menu
@app.route('/restaurant/<int:restaurant_id>')
@app.route('/restaurant/<int:restaurant_id>/menu')
def showMenu(restaurant_id):
    # restaurant_id = "This page is to show menu for restaurant"
    restaurant_id = restaurant
    return render_template('menu.html',restaurant_id = restaurant_id)

#New Menu Item
@app.route('/restaurant/<int:restaurant_id>/menu/new')
def newMenuItem(restaurant_id):
    # restaurant_id = "This page is for making a new menu"
    restaurant_id = restaurant
    return render_template('newMenuItem.html',restaurant_id = restaurant_id)

#Edit Menu Item
@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/edit')
def editMenuItem(restaurant_id,menu_id):
    menu_id = item
    restaurant_id = restaurant
    return render_template('editMenuItem.html', restaurant_id = restaurant_id, menu_id = menu_id)


#Delete Menu Item
@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/delete')
def deleteMenuItem(restaurant_id,menu_id):
    restaurant_id = restaurant
    menu_id = item
    # return "This page is to delete the menu"
    return render_template('deleteMenuItem.html', restaurant_id = restaurant_id, menu_id = menu_id)


if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0', port=5000)
