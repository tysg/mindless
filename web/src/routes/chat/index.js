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
  const [speech, setSpeech] = useState("Click me!");
  const [wobble, setWobble] = useState(0);

  const requestGibberish = () => {
    axios.get(backendEndpoint).then((value) => {
      console.log(value);
      setWobble(1);
      setSpeech(value.data);
    });
  };

  const requestMoreGibberish = () => {
    axios.post(backendEndpoint, text).then((value) => {
      console.log(value);
      setWobble(1);
      setSpeech(value.data);
    });
  };

  return (
    <div class={style.container}>
      <nav>
        <Link activeClassName={style.active} href="/" style="text-decoration: none; font-weight: bolder;">
          Back
        </Link>
      </nav>
      <div class={style.bubble}>{speech}</div>
      <div class={style.container}>
        {avatar !== null && (
          <img class={style.avatar} src={avatar} 
          onClick={requestGibberish}
          onAnimationEnd={() => setWobble(0)}
          wobble={wobble}></img>
        )}
        <input class={style.textinput} onInput={(e) => setText(e.target.value)} placeholder="Type a few words...">{text}</input>
        <button class={style.button} onClick={requestMoreGibberish}>Send</button>
      </div>
    </div>
  );
};

export default Chat;
