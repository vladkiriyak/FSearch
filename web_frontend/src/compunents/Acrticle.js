import React, {Component} from 'react';


class Article extends Component {

    constructor(props) {
        super(props);

        this.state = {

            isOpen: true
        };
    }


    render() {

        const {article} = this.props;


        const body = this.state.isOpen && (
            <section>
                <div className="card-header">
                    {article.title}
                </div>
                <div className="card-body">
                    {article.body}
                </div>
            </section>
        );
        return (
            <div className="card">
                {/*<button className="btn btn-primary" onClick={this.handleClick}>click</button>*/}
                {body}
            </div>


        )
    }

    handleClick = () => {

        this.setState({
            isOpen: !this.state.isOpen

        });

        console.log("Hi");
    }
}

export default Article