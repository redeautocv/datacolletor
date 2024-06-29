from app.init  import create_app
import datacolletor.app.init
import datacolletor
import datacolletor.app

 




app= datacolletor.app.init.create_app()


if __name__=='__main__':
    app.run(debug=True)