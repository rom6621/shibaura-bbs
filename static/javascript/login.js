(function(d) {
    var config = {
        kitId: 'rnp8urf',
        scriptTimeout: 3000,
        async: true
    },
    h=d.documentElement,t=setTimeout(function(){h.className=h.className.replace(/\bwf-loading\b/g,"")+" wf-inactive";},config.scriptTimeout),tk=d.createElement("script"),f=false,s=d.getElementsByTagName("script")[0],a;h.className+=" wf-loading";tk.src='https://use.typekit.net/'+config.kitId+'.js';tk.async=true;tk.onload=tk.onreadystatechange=function(){a=this.readyState;if(f||a&&a!="complete"&&a!="loaded")return;f=true;clearTimeout(t);try{Typekit.load(config)}catch(e){}};s.parentNode.insertBefore(tk,s)
})(document);

// ログイン
function onSignIn(token) {
    const form = document.createElement('form');
    form.method = 'POST';
    form.action = "/login";
    const input = document.createElement('input');
    input.name = 'token';
    input.value = JSON.stringify(token);
    form.appendChild(input);
    document.body.appendChild(form);
    form.submit();
    var auth2 = gapi.auth2.getAuthInstance();
    auth2.signOut();
}