$(document).ready(function(){
    var UID = "U34B8602A8"; 
    var KEY = "rppopks6ksa5pooz"; // 并不会隐藏KEY
    var API_NOW = "http://api.seniverse.com/v3/weather/now.json"; // 获取天气实况
    var API_DAILY = "http://api.seniverse.com/v3/weather/daily.json"
    var API_LIFE = "https://api.seniverse.com/v3/life/suggestion.json"
    var LOCATION = "nanjing"; // 除拼音外，还可以使用 v3 id、汉语等形式
    // 获取当前时间戳
    var ts = Math.floor((new Date()).getTime() / 1000);
    // 构造验证参数字符串
    var str = "ts=" + ts + "&uid=" + UID;
    // 使用 HMAC-SHA1 方式，以 API 密钥（key）对上一步生成的参数字符串（raw）进行加密
    // 并将加密结果用 base64 编码，并做一个 urlencode，得到签名 sig
    var sig = CryptoJS.HmacSHA1(str, KEY).toString(CryptoJS.enc.Base64);
    sig = encodeURIComponent(sig);
    str = str + "&sig=" + sig;

    // 构造最终请求的 url
    var url_now = API_NOW + "?location=" + LOCATION + "&" + str + "&callback=jsonpCallbackNow";
    var url_daily = API_DAILY + "?location=" + LOCATION + "&" + str + "&days=3" + "&callback=jsonpCallbackDaily";
    var url_life = API_LIFE + "?location=" + LOCATION + "&" + str + "&callback=jsonpCallbackLife";
    // console.log(url);
    // 向 HTML 中动态插入 script 标签，通过 JSONP 的方式进行调用
    var newScript = document.createElement('script');
    newScript.type = 'text/javascript';
    newScript.src = url_now;
    $('body').append(newScript);

    var newScript = document.createElement('script');
    newScript.type = 'text/javascript';
    newScript.src = url_daily;
    $('body').append(newScript);

    var newScript = document.createElement('script');
    newScript.type = 'text/javascript';
    newScript.src = url_life;
    $('body').append(newScript);
});
