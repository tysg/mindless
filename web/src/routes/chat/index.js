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

  const requestGibberish = () => {
    axios.get(backendEndpoint).then((value) => {
      console.log(value);
      setSpeech(value.data);
    });
  };

  const requestMoreGibberish = () => {
    axios.post(backendEndpoint, text).then((value) => {
      console.log(value);
      setSpeech(value.data);
    });
  };

  return (
    <div class={style.container}>
      <nav>
        <Link activeClassName={style.active} href="/">
          Back
        </Link>
      </nav>
      <div class={style.bubble}>{speech}</div>
      <div class={style.container}>
        {avatar !== null && (
          <img class={style.avatar} src={avatar} onClick={requestGibberish}></img>
        )}
        <input onInput={(e) => setText(e.target.value)}>{text}</input>
        <button class={style.button} onClick={requestMoreGibberish}>Send</button>
      </div>
    </div>
  );
};

export default Chat;
