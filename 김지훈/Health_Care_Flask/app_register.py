from flask import Flask, render_template, request, redirect, url_for, g, jsonify
import User

from __main__ import app

@app.route('/register')
def register():
    #이미 로그인 했다면 메인페이지
    if g.user != None:
        return redirect(url_for("hello"))

    return render_template("register.html")


@app.route('/register_process', methods=["POST"])
def register_process():
    userName = request.form.get('userName')
    userPw = request.form.get('userPassword')
    userEmail = request.form.get('userEmail')
    user = User.User(userName, userPw, userEmail)
    if User.select_user_with_name(userName) == None and User.select_user_with_email(userEmail) == None:
        #print("register success!")
        User.insert_user(user)
        return jsonify({'result' : 'success'})
    else:
        #print("register fail..")
        return jsonify({'result' : 'fail'})

    # print(f'비동기 테스트 {userName}')
    # return jsonify({'result' : 'success'})
    
    
    
