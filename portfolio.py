from flask import Flask, render_template  
                                          
app = Flask(__name__)                     
                                          
@app.route('/my_portfolio')                           
                                          
def my_portfolio():
  return render_template('my_portfolio.html')    


@app.route('/my_projects')                           
                                          
def my_projects():
  return render_template('my_projects.html') 

@app.route('/about_me')                           
                                          
def about_me():
  return render_template('about_me.html') 

app.run(debug=True)