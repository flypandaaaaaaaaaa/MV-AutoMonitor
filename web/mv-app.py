#-*-coding:utf-8-*-
from flask import render_template
from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,FileField,TextAreaField
from wtforms.validators import DataRequired
from flask_bootstrap import Bootstrap
from web.Command_Gen import My_Command
from Server.DB.DB_Access import DBSession
from Server.DB.MySQLModel import python_script
app = Flask(__name__)
app.config['SECRET_KEY']='aaaaa'
bootstrap=Bootstrap(app)

class AllFunc(FlaskForm):
    String=StringField('动作',validators=[DataRequired()])
    File=FileField('文件')
    Submit=SubmitField('提交')

class ScriptForm(FlaskForm):
    ScriptName=StringField()
    Arg=TextAreaField()
    Context=TextAreaField()
    Submit=SubmitField()




@app.route('/manage/<id>',methods=['GET','POST'])
def manage(id):
    form=AllFunc()
    my_id=id
    if form.validate_on_submit():
        command_string=form.string.data
        file=form.File.data
        my_command=My_Command(my_id)
        my_command.my_command(command_string,file)

    return render_template('manage.html',form=form)

@app.route('/new/',methods=['GET','POST'])
def new():
    scriptform=ScriptForm()
    if scriptform.validate_on_submit():
        session=DBSession()
        script_name=scriptform.ScriptName.data
        argument=scriptform.Arg.data
        script_context=scriptform.Context.data
        new_script=python_script(script_name=script_name,argument=argument,script_context=script_context)
        session.add(new_script)
        session.commit()
        session.close()
        scriptform.ScriptName.data=''
        scriptform.Arg.data=''
        scriptform.Context.data=''
        return render_template('editscript.html',scriptform=scriptform)
    return render_template('editscript.html',scriptform=scriptform)


@app.route('/edit/<script_id>',methods=['GET','POST'])
def edit(script_id):
    scriptform=ScriptForm()
    my_scriptid=script_id
    session=DBSession()
    script = session.query(python_script).filter_by(id=my_scriptid).first()
    if scriptform.validate_on_submit():
        script.script_name=scriptform.ScriptName.data
        script.argument=scriptform.Arg.data
        script.script_context=scriptform.Context.data
        session.commit()
        session.close()
        return render_template('editscript.html',scriptform=scriptform)
    scriptform.ScriptName.data=script.script_name
    scriptform.Arg.data=script.argument
    scriptform.Context.data=script.script_context

    session.close()
    return render_template('editscript.html',scriptform=scriptform)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=80,threaded=True)