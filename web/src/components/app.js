import { createContext, h } from "preact";
import { Router } from "preact-router";

// Code-splitting is automated for `routes` directory
import Home from "../routes/home";
import Chat from "../routes/chat";
import { useState } from "preact/hooks";

export const AvatarContext = createContext(null);

const App = () => {
  const [blob, setBlob] = useState(null);
  return (
    <div id="app">
      <AvatarContext.Provider value={blob}>
        <Router>
          <Home path="/" updateBlob={setBlob} />
          <Chat path="/chat" />
        </Router>
      </AvatarContext.Provider>
    </div>
  );
};

export default App;
