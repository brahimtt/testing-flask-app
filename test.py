from flask import Flask,render_template,request
import subprocess
import os
import colorama

app=Flask(__name__,template_folder="templates")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/execute', methods=['POST','GET'])
def execute():
    colorama.init()
    file=request.form.get("file_name")
    env=request.form.get("env_folder")
    try:
        env_dir=os.path.join("/home/brahim/test/",env)
        test_dir=os.path.join("/home/brahim/test/",file)
        print(test_dir)
        result_process=subprocess.Popen(f"pip install -r {env_dir}/requirements.txt",shell=True,stdout=subprocess.PIPE)
        result=subprocess.Popen(f"pytest -v --html=templates/report.html --self-contained-html --css=templates/assets/style.css {test_dir}",shell=True,stdout=subprocess.PIPE)
        result_process.wait()
        result.wait()

    except subprocess.CalledProcessError as e :
        return colorama.Fore.RED+"FAILURE:"+colorama.Style.RESET_ALL+result.stderr

    return render_template("report.html")

    
        
if __name__=='__main__':
    app.run(host="0.0.0.0",debug=True)
