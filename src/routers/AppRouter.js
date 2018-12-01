import React from "react";
import { Router, Route, Switch, Link, NavLink } from "react-router-dom";
import createHistory from "history/createBrowserHistory";

import HomePage from "../components/App"
import NotFound from "../components/404"
// import MapPage from "../components/MapPage"

const history = createHistory();

const AppRouter = () => (
  <Router history={history}>
    <div>
      <Switch>
        <Route path="/" component={HomePage} exact={true} />
        <Route component={NotFound} />
      </Switch>
    </div>
  </Router>
);

export default AppRouter;