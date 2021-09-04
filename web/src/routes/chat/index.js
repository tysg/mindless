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
      .post(backendEndpoint, text)
      .then((value) => {
        console.log(value);
        setSpeech(value.data);
      })
      .then(() => setLoading(false));
  };
  return (
    <div>
      <nav>
        <Link activeClassName={style.active} href="/">
          Back
        </Link>
      </nav>
      {avatar !== null && <img class={style.avatar} src={avatar}></img>}
      <p>{speech}</p>
      <textarea onInput={(e) => setText(e.target.value)}>{text}</textarea>
      <button onClick={requestGibberish}>Send</button>
    </div>
  );
};

export default Chat;
