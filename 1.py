from flask import Flask,render_template,request
import os
from abc_1 import characters
app=Flask(__name__)

BASE_PATH=os.getcwd()#get current working directory
UPLOAD_PATH=os.path.join(BASE_PATH,'static/upload/')


@app.route('/',methods=['POST','GET'])
def main():#receiving the file and saving it in a folder, this is called static
    if request.method=='POST':
        upload_file=request.files['imagename']
        filename=upload_file.filename
        path_save=os.path.join(UPLOAD_PATH,filename)
        upload_file.save(path_save)
        text=characters(path_save,filename)
        return render_template('htmla.html',upload=True,upload_image=filename,text=text)
    return render_template('htmla.html',upload=False)






if __name__=="__main__":
    app.run(debug=True)