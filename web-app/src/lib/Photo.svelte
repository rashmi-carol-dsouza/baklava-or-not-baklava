<script>
  import { onMount } from "svelte";
  import { state, STATE } from "../stores.js";

  import FaCamera from "svelte-icons/fa/FaCamera.svelte";
  import FaCheck from "svelte-icons/fa/FaCheck.svelte";
  import IoMdClose from "svelte-icons/io/IoMdClose.svelte";
  import FaUndo from "svelte-icons/fa/FaUndo.svelte";

  let canvas;
  let imgSrc;
  let canvasContext;
  let videoSource = null;
  let loading = false;

  let stateValue;

  state.subscribe((value) => {
    stateValue = value;
  });

  onMount(() => {
    canvasContext = canvas.getContext("2d");
    canvasContext.canvas.width = window.innerWidth;
    canvasContext.canvas.height = window.innerHeight;
  });

  const activateVideoCamara = async () => {
    try {
      loading = true;
      const stream = await navigator.mediaDevices.getUserMedia({
        video: true,
        audio: false,
      });
      videoSource.srcObject = stream;
      videoSource.play();
      loading = false;
    } catch (error) {
      console.log(error);
    }
  };

  async function postImage(formData) {
    const API_URL = `${import.meta.env.VITE_API_URL}/photo`;
    const response = await fetch(API_URL, { method: "POST", body: formData });
    const { is_baklava } = await response.json();
    return is_baklava;
  }

  $: getButtonClass = () => {
    if (stateValue === STATE.IS_BAKLAVA) return "button-correct";
    if (stateValue === STATE.IS_NOT_BAKLAVA) return "button-incorrect";
    return "button-default";
  };

  const revertToCameraView = () => {
    state.set(STATE.DEFAULT);
    activateVideoCamara();
  };

  const clickCameraButton = (event) => {
    event.preventDefault();
    if (stateValue === STATE.IS_BAKLAVA || stateValue === STATE.IS_NOT_BAKLAVA)
      return;
    state.set(STATE.LOADING);
    canvasContext.drawImage(videoSource, 0, 0, canvas.width, canvas.height);
    canvas.toBlob(async function (blob) {
      imgSrc = canvas.toDataURL("image/jpeg");
      const formData = new FormData();
      formData.append("image", blob, "user-image.png");
      const is_baklava = await postImage(formData);
      state.set(is_baklava ? STATE.IS_BAKLAVA : STATE.IS_NOT_BAKLAVA);
    });
  };

  activateVideoCamara();
</script>

<form>
  <div class="button-container">
    <button
      on:click={clickCameraButton}
      class="button button-camera {getButtonClass()}"
    >
      {#if stateValue === STATE.IS_BAKLAVA}
        <div class="icon icon-correct">
          <FaCheck />
        </div>
      {:else if stateValue === STATE.IS_NOT_BAKLAVA}
        <div class="icon icon-incorrect">
          <IoMdClose />
        </div>
      {:else}
        <div class="icon icon-default">
          <FaCamera />
        </div>
      {/if}
    </button>

    {#if stateValue === STATE.IS_BAKLAVA || stateValue === STATE.IS_NOT_BAKLAVA}
      <button on:click={revertToCameraView} class="button button-reset">
        <div class="icon icon-reset">
          <FaUndo />
        </div>
      </button>
    {/if}
  </div>
</form>

<canvas bind:this={canvas} />

<div class="camera">
  {#if stateValue === STATE.LOADING}
    <h1>LOADING</h1>
  {/if}
  {#if stateValue === STATE.DEFAULT}
    <!-- svelte-ignore a11y-media-has-caption -->
    <video bind:this={videoSource} class="video-stream" />
  {:else}
    <!-- svelte-ignore a11y-missing-attribute -->
    <img src={imgSrc} class="photo" />
  {/if}
</div>

<style>
  h1 {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translateY(-50%) translateX(-50%);
  }

  form {
    position: relative;
  }

  .button-container {
    position: absolute;
    left: 50%;
    top: 100px;
    transform: translateY(-50%) translateX(-50%);
    z-index: 1;
    display: flex;
    justify-content: space-between;
  }

  .button {
    border-radius: 50%;
    border: 0;
    padding: 15px;
  }

  .button-reset {
    background-color: #566886;
    margin-left: 20px;
  }

  .video-stream,
  .photo {
    width: 100vw;
    height: 100vh;
    object-fit: cover;
    position: fixed;
    top: 0;
    left: 0;
  }

  .icon {
    color: white;
    width: 48px;
    height: 48px;
  }

  .button-default {
    background-color: #666ba3;
  }

  .button-correct {
    background-color: #64a67f;
  }

  .button-incorrect {
    background-color: #da5869;
  }

  .button-reset {
    background-color: #566886;
  }
</style>
