from flask import Flask, render_template
import MarsInfo

#################################################
# Database Setup
#################################################
mars_info = MarsInfo.MarsInfo()

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################

# create route that renders index.html template
@app.route("/")
def show_index():

    d = mars_info.retrieve()

    return render_template(
        "index.html",
        news_title = d['News']['title'],
        news_abstract = d['News']['abstract'],
        image_url = d['Image']['url'],
        weather_conditions = d['Weather']['conditions'],
        facts_table_html = d['Facts']['table_html'],
        hemisphere0 = d['Hemispheres']['title_and_image_list'][0],
        hemisphere1 = d['Hemispheres']['title_and_image_list'][1],
        hemisphere2 = d['Hemispheres']['title_and_image_list'][2],
        hemisphere3 = d['Hemispheres']['title_and_image_list'][3]
    )

# create route that renders index.html template
@app.route("/scrape")
def update():
    mars_info.update()
    return show_index()

if __name__ == '__main__':
    app.run(debug=True)
