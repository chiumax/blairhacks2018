import React from "react";
import { Link } from "react-router-dom";

const NotFoundPage = () => (
  <div className="notf">
    <div className="notfound">
      <div className="notfound-404">
        <h1>Oops!</h1>
      </div>
      <h2>404 - Page not found</h2>
      <p>The server could not find the URL you requested.</p>
      <Link to="/">Return To Home Page</Link>
    </div>
  </div>
);

export default NotFoundPage;