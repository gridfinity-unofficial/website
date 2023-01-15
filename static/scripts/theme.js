const urlParams = new URLSearchParams(window.location.search);
const urlTheme = urlParams.get("theme");
const cookieTheme = getCookieValue("theme");
if (urlTheme){
    if (urlTheme === "light"){
        document.body.setAttribute("data-bs-theme", "light");
    }if (urlTheme === "dark"){
        document.body.setAttribute("data-bs-theme", "dark");
    }
}else{
    if (cookieTheme === "light"){
        document.body.setAttribute("data-bs-theme", "light");
        document.cookie = "theme=light; max-age=600000 ; path=/ ; SameSite=Strict";
    }if (cookieTheme === "dark"){
        document.body.setAttribute("data-bs-theme", "dark");
        document.cookie = "theme=dark; max-age=600000 ; path=/ ; SameSite=Strict";
    }
}

function getCookieValue(a) {
    const b = document.cookie.match('(^|;)\\s*' + a + '\\s*=\\s*([^;]+)');
    return b ? b.pop() : '';
}

function switchLight(){
    document.body.setAttribute("data-bs-theme", "light");
    document.cookie = "theme=light; max-age=600000 ; path=/ ; SameSite=Strict";
}
function switchDark(){
    document.body.setAttribute("data-bs-theme", "dark");
    document.cookie = "theme=dark; max-age=600000 ; path=/ ; SameSite=Strict";
}