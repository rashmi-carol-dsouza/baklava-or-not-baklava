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
        if (stateValue === STATE.IS_BAKLAVA) return "BAKLAVA";
        if (stateValue === STATE.IS_NOT_BAKLAVA) return "NOT BAKLAVA";
        return "BAKLAVA OR NOT BAKLAVA";
    };
</script>

<header class="header {getHeaderClass()}">
    <h1>{getHeaderText()}</h1>
</header>

<style>
    header {
        padding: 20px;
        text-align: center;
        font-size: 2.441rem;
        font-weight: 700;
        color: #fff;
        text-transform: uppercase;
        z-index: 1;
        position: absolute;
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
