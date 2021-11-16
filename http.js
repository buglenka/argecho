function jsonParams(r) {
    r.return(200, decodeURIComponent(JSON.stringify(r.args)));
}

export default {jsonParams};
