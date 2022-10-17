<script>
    import { state, STATE } from "../stores.js";
    let stateValue;

    state.subscribe((value) => {
        stateValue = value;
    });

    $: getHeaderClass = () => {
        if (stateValue === STATE.IS_BAKLAVA) return "header-correct";
        if (stateValue === STATE.IS_NOT_BAKLAVA) return "header-incorrect";
        return "header-default";
    };

    $: getHeaderText = () => {
        if (stateValue === STATE.IS_BAKLAVA) return "Baklava";
        if (stateValue === STATE.IS_NOT_BAKLAVA) return "Not Baklava";
        if(stateValue === STATE.LOADING) return "Loading...."
        return "Point at object";
    };
</script>

<header class="header {getHeaderClass()}">
    <h1>{getHeaderText()}</h1>
</header>

<style>
    header {
        padding: 20px;
        text-align: center;
        font-size: 2rem;
        font-weight: 700;
        color: #fff;
        text-transform: uppercase;
        z-index: 0;
        position: absolute;
        bottom: 0;
        width: 100%;
    }

    .header-correct {
        background-color: #4f9d69;
    }

    .header-incorrect {
        background-color: #d84654;
    }

    .header-default {
        background-color: #5b629a;
    }
</style>