<script>
    import { state, STATE } from '../stores.js';

    let stateValue;

	state.subscribe(value => {
		stateValue = value;
	});

    let message;

    $: switch(stateValue) {
        case STATE.IS_BAKLAVA:
            message = 'Yay! Baklava!'
            break;
        case STATE.IS_NOT_BAKLAVA:
            message = 'Not my job boss'
            break;
        default:
            message = 'Point your camera at the object';
    }
</script>

<div class="container">
    {#if stateValue === STATE.LOADING}
        <h1>LOADING</h1>
    {:else}
        <p>{message}</p>
    {/if}
</div>


<style>
    .container {
        position: absolute;
        bottom: 0;
        padding: 40px;
        text-align: center;
        background: #000;
        color: #fff;
        width: 100%;
    }
</style>