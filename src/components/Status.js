import React, { Component } from "react";
fetch('/api/getTweetsFromCity/')
class Tweet extends React.Component {
  state = {
    tweets: []
  }
  componentDidMount() {
    fetch('/api/getTweetsFromCity').then(results => {
      return results.json();

    }).then(data=> {
      let cards = data.map((tweet)=> {
        return(
        
          

              <div className={"card"}>
              <div className={"blueBar"}>
                <h1>Brian Xiang</h1>
                
                <p>
                Tweet stuff
                </p>

              
              </div>
            </div>)
      });
      this.setState({tweets:cards});
      console.log(cards);
    })
  }
  render() {
    return (
      <div className={"tweet"} >
      <h1 className={"techUsed"}>
          Tweets
          </h1>
          <div className={"cardWrap"}>
        {this.state.cards}
        </div>
        </div>

    );
  }
}

export default Tweet;
