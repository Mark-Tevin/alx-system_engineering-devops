# 0x1A. Application server
Got it! So, here's a detailed task breakdown for setting up the application server:

### **Task 1: Setting Up the Development Environment**
1. **Install Python 3.8**: Ensure Python 3.8 is installed.
   - Use `pyenv` or `apt` for installation.
2. **Create and Activate Virtual Environment**: 
   - Run `python3.8 -m venv env` to create.
   - Activate with `source env/bin/activate`.
3. **Install Dependencies**:
   - Install Flask and other necessary packages with `pip install -r requirements.txt`.
4. **Run the Development Server**:
   - Start the Flask app with `flask run`.

### **Task 2: Configuring a Production Environment with Gunicorn**
1. **Install Gunicorn**:
   - Run `pip install gunicorn`.
2. **Create Gunicorn Config**:
   - Write a configuration file (`gunicorn_config.py`) with necessary settings like `workers`, `bind`, etc.
3. **Test the Gunicorn Server**:
   - Run `gunicorn -c gunicorn_config.py wsgi:app` to test.

### **Task 3: Serving Pages with Nginx**
1. **Install Nginx**:
   - Use `sudo apt-get install nginx`.
2. **Configure Nginx**:
   - Create a config file in `/etc/nginx/sites-available/airbnb_clone`.
   - Set `server_name`, `location` for static files, and reverse proxy to Gunicorn.
3. **Enable the Site and Restart Nginx**:
   - Run `sudo ln -s /etc/nginx/sites-available/airbnb_clone /etc/nginx/sites-enabled/`.
   - Restart Nginx with `sudo systemctl restart nginx`.

### **Task 4: Adding Routes with Query Parameters**
1. **Update Flask Routes**:
   - Add new routes in `app.py` with query parameters.
   - Example: `@app.route('/search')` with `request.args.get()`.
2. **Test Routes Locally**:
   - Use Postman or curl to test new routes.
   - Ensure query parameters work as expected.

### **Task 5: Serving an API**
1. **Create API Endpoints**:
   - Add routes in `app.py` to serve JSON responses.
   - Example: `@app.route('/api/v1/listings')`.
2. **Test API Endpoints**:
   - Test using Postman or curl.
   - Ensure correct data is returned.

### **Task 6: Setting Up Logging and Monitoring**
1. **Configure Logging**:
   - Set up logging in `gunicorn_config.py` and `app.py`.
   - Use rotating file handlers.
2. **Monitor Server Performance**:
   - Install and configure tools like `htop`, `top`, or `newrelic`.
