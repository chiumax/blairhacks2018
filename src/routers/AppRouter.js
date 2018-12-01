import React from "react";
import { Router, Route, Switch, Link, NavLink } from "react-router-dom";
import createHistory from "history/createBrowserHistory";

import HomePage from "../components/App"
// import MapPage from "../components/MapPage"

const history = createHistory();

const AppRouter = () => (
  <Router history={history}>
    <div>
      <Switch>
        <Route path="/" component={HomePage} exact={true} />
        
      </Switch>
    </div>
  </Router>
);

export default AppRouter;