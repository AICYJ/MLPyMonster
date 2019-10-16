//frontend/src/app.js
import React, { Component } from 'react';

class App extends Component {
    state = {
        posts: []
    };

    async componentDidMount() {
        try {
            const res = await fetch('http://localhost:8000/Porker/');
            const posts = await res.json();
            this.setState({
                posts
            });
        } catch (e) {
            console.log(e);
        }
    }

    render() {
        return (
            <div>
                {this.state.posts.map(item => (
                    <div key={item.serial}>
                        <h1>{item.shape}</h1>
                        <span>{item.number}</span>
                    </div>
                ))}
            </div>
        );
    }
}

export default App;
