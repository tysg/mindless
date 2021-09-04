import axios from "axios";
import { h } from "preact";
import { useContext, useEffect, useState } from "preact/hooks";
import { Link } from "preact-router";
import style from "./style.css";

import { backendEndpoint } from "../../../constants";
import { AvatarContext } from "../../components/app";

const Chat = () => {
  const avatar = useContext(AvatarContext);
  const [text, setText] = useState("");
  const [speech, setSpeech] = useState("");
  const [loading, setLoading] = useState(false);

  const requestGibberish = () => {
    setText("");
    setLoading(true);
    axios
      .get(backendEndpoint)
      .then((value) => setSpeech(value))
      .then(() => setLoading(false));
  };
  return (
    <div>
      <Link href="/">Back</Link>
      {avatar !== null && <img src={window.URL.createObjectURL(avatar)}></img>}
      <h1>Talk</h1>
      <textarea onInput={(e) => setText(e.target.value)}>{text}</textarea>
      <button onClick={requestGibberish}>Send</button>
    </div>
  );
};

export default Chat;
