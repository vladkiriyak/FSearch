import React, {Component} from 'react';
import "bootstrap/dist/css/bootstrap.css"


class LoginPanel extends Component {

    render() {

        return (
            <div className="card">
                <h2 className="card-header">FSearch</h2>
                <div className="card-body">
                    User name <input id={'username'} className="input-group-text"/>
                    <br/>
                    Password <input id={'password'} type="password" className="input-group-text"/>
                    <br/>
                    <button onClick={this.authentication} className="btn btn-success">log in</button>
                </div>

            </div>

        )
    }


    authentication = function () {

        let username = document.getElementById('username').value;
        let password = document.getElementById('password').value;


        fetch('http://localhost:8000/searcher/authentication', {
            method: 'POST',
            headers: {
                Accept: 'application/json',
                'Content-Type': 'application/json',
            },
            credentials: 'include',
            body: JSON.stringify({
                username: username,
                password: password,
            }),
        }).then(res => {

            for (let [key, value] of res.headers) {
                console.log(`${key} = ${value}`);
            }



        });


    }
}

export default LoginPanel