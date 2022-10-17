import { writable } from 'svelte/store';

export const STATE = {
    DEFAULT : 'DEFAULT',
    LOADING: 'LOADING',
    IS_BAKLAVA: 'IS_BAKLAVA',
    IS_NOT_BAKLAVA: 'IS_NOT_BAKLAVA',
    ERROR: 'ERROR'
};

export const state = writable(STATE.DEFAULT);