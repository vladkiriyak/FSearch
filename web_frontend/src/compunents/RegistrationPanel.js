import React, {Component} from 'react';
import "bootstrap/dist/css/bootstrap.css"

class RegistrationPanel extends Component {

    render() {

        return (
            <div className="card">
                <h2 className="card-header">FSearch Registration</h2>
                <div className="card-body" >
                User name <input className="input-group-text"/>
                <br/>
                Password <input type="password" className="input-group-text"/>
                <br/>
                <button className="btn btn-success">registration</button>
            </div>

                </div>

        )
    }
}

export default RegistrationPanel