import React, {Component} from 'react';
import "bootstrap/dist/css/bootstrap.css"

class Test extends Component {

    render() {

        return (
            // <div className="card">
            //     <h2 className="card-header">FSearch</h2>
            //     <div className="card-body" >
            //     User name <input id={'username'} className="input-group-text"/>
            //     <br/>
            //     Password <input id={'password'} type="password" className="input-group-text"/>
            //     <br/>
            //     <button onClick={this.authentication} className="btn btn-success">log in</button>
            // </div>
            //
            //     </div>

            <div>
                {this.test_func()}
            </div>

        )
    }


    test_func = function () {

        // let username = document.getElementById('username').value;
        // let password = document.getElementById('password').value;


        console.log("hello");

        fetch('http://localhost:8000/searcher/test', {
            method: 'POST',
            headers: {
                Accept: 'application/json',
                'Content-Type': 'application/json',
            },
            credentials: 'include',
            body: JSON.stringify({
                username: 'v',
                password: 'v',
            }),
        }).then(res => {

            for (let [key, value] of res.headers) {
                console.log(`${key} = ${value}`);
            }


            // return res.json();
        });
    }
}


export default Test