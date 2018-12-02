import React, { Component } from 'react';
import logo from '../images/logo.svg';
import stockGIF from "../images/stocc.gif"
import stockIMG from "../images/stock.png"
import magnify from "../images/mag.svg"
import user from "../images/user.svg"
import lock from "../images/lock.svg"
import ReactChartkick, { LineChart } from 'react-chartkick'
import Chart from 'chart.js'


import Radium, { StyleRoot } from "radium";
import {
  headShake,
  fadeOutUp,
  fadeInUp,
  fadeOutDown,
  fadeInDown,
  fadeIn
} from "react-animations";



ReactChartkick.addAdapter(Chart)
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

		stage: 'login',
    symbol: null,
    register: undefined,
    post: undefined,
    tag: "",
    headShake: {headShaker},
    input: {},
    load: { display: "none" },
    warn: { display: "none" },
    status: { display: "none" },
    logo: { display: "default" },
    warnDisplay: false,
    password: "",
    username: "",
    wrongLog:false,
    table: null,
    doneAnima:false,
    data: null,
    showTable: false,
    interval: "minute"
  };
  myRef = React.createRef();
  checkRegex = event => {
    event.preventDefault();
    let regexCheck = /[!@#$%^&*(),.//;+-/'[\\\]\=~`?":{}|<>]/g.test(
      this.state.tag
    );
    let str = this.state.tag.replace(/\s/g, "");
    regexCheck = !str || regexCheck;
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
                	fetch("http://127.0.0.1:5000/search", {
  		method: 'POST',
  		headers: {
    		'Accept': 'application/json',
    	'Content-Type': 'application/json',
  		},
  		body:JSON.stringify({query:this.state.tag})
	}).then(response => response.text()).then(data => { console.log(data)
		this.setState({table:data})
	}).then(()=> {
		this.setState({ load: fadeOutUpr }, () => {
                    setTimeout(() => {

                      this.setState({ load: defaultM }, () => {
                        setTimeout(() => {
                          this.setState({ logo: fadeOutUpr }, () => {
                            setTimeout(() => {
                              this.setState({
                                status: fadeInUpr,
                                defaultS,
                                logo: defaultM,
                                doneAnima: true
                              });
                            }, 1000);
                          });
                        }, 1000);
                      });
                    }, 1000);
                  });
                }, 3000);
	})
        
                  
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
        	table: null,
          status: defaultM,
          logo: fadeInUpr,
          defaultS,
          input: fadeInUpr,
          doneAnima: false,
          showTable:false
        });
      }, 1000);
    });
  };
  scrollDown = event => {
    window.scrollTo({ behavior: "smooth" });
    window.scrollTo(0, this.myRef.current.offsetTop);
};
handleLog = (button) => {
	let str = button.replace(/\s/g, "").toLowerCase();
	this.setState({register:button, stage:"loginForm",post: str}) 

}
handleLogin = (event) => {
	event.preventDefault();
	fetch("http://127.0.0.1:5000/"+this.state.post, {
  		method: 'POST',
  		headers: {
    		'Accept': 'application/json',
    	'Content-Type': 'application/json',
  		},
  		body:JSON.stringify({uname:this.state.username,pw:this.state.password})
	}).then(response => response.text()).then(data=> {
		if(!(data == "")){
		this.setState({stage: "logged", wrongLog: false})
	}else{
		this.setState({wrongLog:true})
	}})
}
handleUserChange = (event) => {
	this.setState({username: event.target.value})
}
handlePassChange = (event) => {
	this.setState({password: event.target.value})
}

showCompany = () => {
	let rend = [];
	let htm;
	console.log(this.state.table)
	if (!(this.state.table==null)){
		let data = JSON.parse(this.state.table)
		Object.keys(data).forEach((key)=> { 
		rend.push(<div className={"tableData"} key={key} onClick={() => {this.showStock(data[key].toUpperCase())}}><svg viewBox="0 0 20 20" className="Icon">
          <path d="M0 0 L10 10 L0 20"></path>
        </svg><div >{key}</div><div>{data[key]}</div></div>) });
			console.log(this.state.table);
		return rend;
	}

}	
showStock = (key) => {
	console.log(key)
	fetch("http://127.0.0.1:5000/stock/"+key+"/"+this.state.interval).then(response => response.text()).then(data => {console.log(data);this.setState({
		data: data, showTable: true
	})})
}
	
changeInt = (event) => {
	this.setState({interval:event.target.value})
}
switchStatement = () => {
	switch(this.state.stage) {
  		case 'login':
  		return(<div><div className="title" >Stock Prophet</div>
  			<div className={"logHome"}>
  			 <img src={stockGIF} alt={"loading"} className={"HomeGif"} style={this.state.input}/ >
  			<button
              className={"HomeButton ReturnButt LoginButt"}
              onClick={() => {this.handleLog("Register")}}

            >
              Register
            </button>
            <button
              className={"HomeButton ReturnButt LoginButt"}
              
              onClick={() => {this.handleLog("Log in")}}
            >
              Login
            </button>
            </div>
  			</div>);
  		case 'loginForm':
  		return(<div><div className="title">{this.state.register}</div>
  			<form onSubmit={this.handleLogin} className="HomeForm">
              <div className={"FormFlex"}>
                <div style={this.state.input}>
                  <img src={user} alt="" className={"SearchIco"} />
                  <input

					onChange={this.handleUserChange}
                    value={this.state.username}
                    type="text"
                    name="user"
                    placeholder="username"
                    className={"HomeInput"}
                  
                  />
                  
                </div>
                <div><img src={lock} alt="" className={"SearchIco"} />
                  <input
                  	style={this.state.headShake}
					onChange={this.handlePassChange}
                    value={this.state.password}
                    type="password"
                    name=" pass"
                    placeholder="password"
                    className={"HomeInput"}
                  
                  /></div>
                <div>
                  {this.state.wrongLog && <label className={"WarnText"} >
                    Incorrect Password/Username
                  </label>}
                </div>
                <div style={this.state.input}>
                  <input type="submit" value="Submit" className="HomeButton" />
                </div>
              </div>
</form></div>);
  		case 'logged':
  		return(	
      <div>
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
<div style={this.state.status} >
<div className="rectangle"></div>
{!!this.state.doneAnima && <div className={"tableWrap"}>{this.showCompany()}</div>}
{!!this.state.showTable && <LineChart data={JSON.parse(this.state.data)} />}
</div>
      <img src={stockGIF} alt={"loading"} className={"HomeGif"} style={this.state.input}/ >
        <div className="title title-2" style={this.state.input}>Welcome to Stock Prophet</div>


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
                <div style={this.state.input}>
                <div className={"stockInt"}>Stock Interval</div>
                 <select name="interval" onChange={this.changeInt} value={this.state.interval} className={"select"}>
  <option value="minute">minute</option>
  <option value="day">day</option>
  <option value="week">week</option>
  <option value="month">month</option>
</select> </div>
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
      );
  		default:
  		return null;
  	}

}
  render() {
  	return(
  		<StyleRoot>
      <div className="App">
      {this.switchStatement()}
  		</div>
      </StyleRoot>
)
  
}}

export default App;
