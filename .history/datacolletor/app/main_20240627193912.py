from app.initi  import create_app
import app.initi
import datacolletor.app.initi
import datacolletor

 




app= datacolletor.app.initi.create_app()


if __name__=='__main__':
    app.run(debug=True)