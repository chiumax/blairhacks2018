import React, { Component } from 'react';
import logo from '../images/logo.svg';
import stockGIF from "../images/stocc.gif"
import magnify from "../images/mag.svg"
import Radium, { StyleRoot } from "radium";
import {
  headShake,
  fadeOutUp,
  fadeInUp,
  fadeOutDown,
  fadeInDown,
  fadeIn
} from "react-animations";

const headShaker = {
  animation: "x 1s",
  animationName: Radium.keyframes(headShake, "headShake")
};

const fadeInr = {
  animation: "x 1s",
  animationName: Radium.keyframes(fadeIn, "fadeIn")
};
const fadeOutUpr = {
  animation: "x 1s",
  animationName: Radium.keyframes(fadeOutUp, "fadeOutUp")
};

const fadeOutDownr = {
  animation: "x 1s",
  animationName: Radium.keyframes(fadeOutDown, "fadeOutDown")
};

const fadeInUpr = {
  animation: "x 1s",
  animationName: Radium.keyframes(fadeInUp, "fadeInUp")
};

const fadeInDownr = {
  animation: "x 1s",
  animationName: Radium.keyframes(fadeInDown, "fadeInDown")
};
const defaultS = {
  display: "block",
  overflow: "none"
};
const defaultM = {
  display: "none",
  overflow: "none"
};
const defaultD = {
  display: "default"
};

class App extends Component {

	state = {
		val: "yote",
    symbol: null,
    tag: "",
    headShake: {headShaker},
    input: {},
    load: { display: "none" },
    warn: { display: "none" },
    status: { display: "none" },
    logo: { display: "default" },
    warnDisplay: false
  };
  myRef = React.createRef();
  checkRegex = event => {
    event.preventDefault();
    let regexCheck = /[!@#$%^&*(),.//;+-/'[\\\]\=~`?":{}|<>]/g.test(
      this.state.tag
    );
    let str = this.state.tag.replace(/\s/g, "");
    regexCheck = !str || regexCheck;
    console.log(!str || regexCheck);
    this.setState({ symbol: regexCheck });
    if (regexCheck) {
      this.setState({ headShake: {}, warn: { display: "none" } }, () => {
        setTimeout(() => {
          this.setState({
            headShake: headShaker,
            warnDisplay: true,
            warn: Object.assign({}, fadeInUpr, defaultS)
          });
        }, 1);
      });
    } else {
      if (this.state.warnDisplay) {
        this.setState({ warn: fadeOutUpr, warnDisplay: false }, () => {
          setTimeout(() => {
            this.setState({ warn: defaultM });
          }, 1000);
        });
      }
      this.setState({ input: fadeOutUpr, tag: str }, () => {
        setTimeout(() => {
          this.setState({ input: defaultM }, () => {
            setTimeout(() => {
              this.setState({ load: fadeInUpr, defaultS }, () => {
                setTimeout(() => {
                  this.setState({ load: fadeOutUpr }, () => {
                    setTimeout(() => {
                      this.setState({ load: defaultM }, () => {
                        setTimeout(() => {
                          this.setState({ logo: fadeOutUpr }, () => {
                            setTimeout(() => {
                              this.setState({
                                status: fadeInUpr,
                                defaultS,
                                logo: defaultM
                              });
                            }, 1000);
                          });
                        }, 1000);
                      });
                    }, 1000);
                  });
                }, 3000);
              });
            }, 1000);
          });
        }, 1000);
      });
    }
  };
  handleChange = event => {
    if (this.state.warnDisplay) {
      this.setState({ warn: fadeOutUpr, warnDisplay: false }, () => {
        setTimeout(() => {
          this.setState({ warn: defaultM });
        }, 1000);
      });
    }
    this.setState({ tag: event.target.value, headShake: {} });
  };
  handleReturn = event => {
    event.preventDefault();
    this.setState({ status: fadeOutUpr }, () => {
      setTimeout(() => {
        this.setState({
          status: defaultM,
          logo: fadeInUpr,
          defaultS,
          input: fadeInUpr,
          defaultS
        });
      }, 1000);
    });
  };
  scrollDown = event => {
    window.scrollTo({ behavior: "smooth" });
    window.scrollTo(0, this.myRef.current.offsetTop);
};
  render() {
    return (
    	<StyleRoot>
      <div className="App">
       <button
              className={"HomeButton ReturnButt"}
              style={this.state.status}
              onClick={this.handleReturn}
            >
              Search Again
            </button>
            <div>
              <label
                className={"HomeText ReturnText"}
                style={this.state.status}
              >
                Showing stock results for {this.state.tag}
              </label>
</div>
      <img src={stockGIF} alt={"loading"} className={"HomeGif"} style={this.state.input}/ >
        <div className="title" style={this.state.input}>Stock Prophet</div>


 <form onSubmit={this.checkRegex} className="HomeForm">
              <div className={"FormFlex"}>
                <div>
                  <label className={"HomeText"} style={this.state.load}>
                    Just a moment...
                  </label>
                </div>

                <div style={this.state.input}>
                  <img src={magnify} alt="" className={"SearchIco"} />
                  <input
                  	style={this.state.headShake}
					onChange={this.handleChange}
                    value={this.state.tag}
                    type="text"
                    name=" tag"
                    placeholder="company"
                    className={"HomeInput"}
                  
                  />
                </div>
                <div>
                  <label className={"WarnText"} style={this.state.warn}>
                    Not Valid
                  </label>
                </div>
                <div style={this.state.input}>
                  <input type="submit" value="Submit" className="HomeButton" />
                </div>
              </div>
</form>
      </div>
      </StyleRoot>
    );
  }
}

export default App;
