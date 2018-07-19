#-*-coding:utf-8-*-
from flask import render_template
from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,FileField
from wtforms.validators import DataRequired
from flask_bootstrap import Bootstrap
from Server.Server_Config import *
from werkzeug import secure_filename
from command_gen_cls import My_Command

app = Flask(__name__)
app.config['SECRET_KEY']='aaaaa'
bootstrap=Bootstrap(app)
class AllFunc(FlaskForm):
    string=StringField('Title',validators=[DataRequired()])
    File=FileField('文件')
    submit=SubmitField('提交')




@app.route('/manage/<id>',methods=['GET','POST'])
def manage(id):
    form=AllFunc()
    my_id=id
    if form.validate_on_submit():
        comand_name = form.string.data
        if comand_name in ['reboot','shutdown']:
            my_command=My_Command(my_id)
            my_command.control_command(comand_name)
        elif comand_name in ['sendfile']:
            my_filename= secure_filename(form.File.data.filename)
            my_command=My_Command(my_id)
            my_command.send_file()
            my_uuid=My_Command.uuid
            form.File.data.save(command_path+my_uuid+my_filename)
    return render_template('manage.html',form=form)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=80,threaded=True)