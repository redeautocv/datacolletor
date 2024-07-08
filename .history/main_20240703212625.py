from  flask import Flask
import app
import app.initi

app=  app.initi.create_app()
app = create_app()

if __name__=='__main__':
    app.run(debug=True)