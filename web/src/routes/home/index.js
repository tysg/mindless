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
      <input type="file" onInput={onUpload} style="margin-left:80px;"></input>
      {!!avatar && <img class={style.avatar} src={avatar} />}
      <Link activeClassName={style.active} href="/chat" style="text-decoration: none; font-weight: bolder;">
        Next
      </Link>
    </div>
  );
};

export default Home;
