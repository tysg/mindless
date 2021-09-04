import { h } from "preact";
import { Link } from "preact-router";
import { useContext, useState } from "preact/hooks";
import { AvatarContext } from "../../components/app";
import style from "./style.css";

const Home = ({ updateBlob }) => {
  const avatar = useContext(AvatarContext);
  const onUpload = ({ target }) => {
    const blobUrl = window.URL
      ? window.URL.createObjectURL(target.files[0])
      : window.webkitURL.createObjectURL(target.files[0]);
    updateBlob(blobUrl);
  };

  return (
    <div class={style.home}>
      <h1>Struggling?</h1>
      <p>Watch our AI struggle more</p>
      <h2>Choose an avatar</h2>
      <input type="file" onInput={onUpload}>
        Upload
      </input>
      {!!avatar && <img src={avatar} />}
      <Link activeClassName={style.active} href="/chat">
        Next
      </Link>
    </div>
  );
};

export default Home;
