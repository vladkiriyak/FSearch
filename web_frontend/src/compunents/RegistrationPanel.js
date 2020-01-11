import React, {Component} from 'react';
import "bootstrap/dist/css/bootstrap.css"

class RegistrationPanel extends Component {

    render() {

        return (
            <div className="card">
                <h2 className="card-header">FSearch Registration</h2>
                <div className="card-body">
                    User name <input id='username' className="input-group-text"/>
                    <br/>
                    Password <input id='password' type="password" className="input-group-text"/>
                    <br/>
                    <button onClick={this.registration} className="btn btn-success">registration</button>
                </div>

            </div>

        )
    }


    registration = function () {

        let username = document.getElementById('username').value;
        let password = document.getElementById('password').value;


        let xhr = new XMLHttpRequest();
        xhr.open('POST', 'http://localhost:8000/searcher/registration', true,);
        xhr.send(
            JSON.stringify(

                {
                    username: username,
                    password: password
                }
            )
        );


    }


}

export default RegistrationPanel