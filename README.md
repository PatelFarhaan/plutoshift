# _**PLUTOSHIFT**_

## How to run this application:

1. Create a virtual environment using the command: 
    ```
    virtualenv venv
   ```
   
2. Actiavte the virtual environment using the command: 
    ```
    source venv/bin/activate
   ```

3. Install all the requirements: 
    ```
    pip3 install -r requirements.txt
   ```
   
4. Make  migrations: 
    ```
    python3 manage.py makemigrations
   ```
   
5. Migrate Changes: 
    ```
    python3 manage.py migrate
   ```
   
4. Run the application:
    ```
    python3 manage.py runserver
   ```


## API Endpoint:

URL:
    ```
    http://127.0.0.1:8000/ml/
    ```

METHOD:
    ```
    POST
    ```


PAYLOAD:

        {
       "target":{
          "influent_flow":[
             {
                "time": "2007-12-10",
                "value": 9.59076113897809
             },
             {
                "time": "2007-12-11",
                "value": 8.51959031601596
             },
             {
                "time": "2007-12-12",
                "value": 8.18367658262066
             }
          ]
       },
       "forecast_length": "180D"
    }
