import React, { Component } from "react";

import Toolbar from "./components/Toolbar/Toolbar";

class App extends Component {
  render() {
    return (
      <div className="App">
        <Toolbar />
        {/*The purpose of the double braces is as said here. First braces, is a dynamic value. Inner is a jsx object.*/}
        <main style={{ marginTop: "64px" }}>
          <p>This is the content.</p>
        </main>
      </div>
    );
  }
}

export default App;
