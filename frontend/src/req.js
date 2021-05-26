const axios = require("axios");



export const resp = async () => await axios.get("http://127.0.0.1:8000/api/testes/");

export const post = async (list) => await axios.post("http://127.0.0.1:8000/api/testes/", list);

export const delet = async () => await axios.post("http://127.0.0.1:8000/api/testes/", []);

