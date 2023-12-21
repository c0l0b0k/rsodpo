document.addEventListener("DOMContentLoaded", (function() {
    var t = new ClipboardJS("#copy-button");
    function e(t) {
        return t = t.replace(/</g, "&lt;").replace(/>/g, "&gt;"),
        document.createTextNode(t)
    };
    var o = null;

    n = document.getElementById("chat-container");
    function c() {
         var t =document.getElementById("recommend_text").value;
                            var r = u( t, "bot-message");

                            r.innerHTML = r.textContent.replace(/```python([^`]+)```/g, (function(t, o) {
                                var i = "copyButton" + Math.random().toString(36).substr(2, 9);
                                return '<div style="position: relative; display: inline-block; width: 100%;"><div style="margin-left: -0.1px; position: absolute; width: 100.1%; height: 30px; background-color: rgba(78, 93, 108, 0.8); text-align: left; padding-left: 10px; border-radius: 10px 10px 0 0; z-index: 1;">python</div><button class="copy-button" data-clipboard-target="#' + i + '" style="position: absolute; top: 40px; right: 10px;"></button><pre id="' + i + '" style="background-color: black; color: white; padding-left: 15px; border-radius: 10px; width: 100%; z-index: 2; padding-top: 45px; padding-bottom: 15px;">' + e(o).textContent + "</pre></div>"
                            }
                            )).replace(/```py([^`]+)```/g, (function(t, o) {
                                var i = "copyButton" + Math.random().toString(36).substr(2, 9);
                                return '<div style="position: relative; display: inline-block; width: 100%;"><div style="margin-left: -0.1px; position: absolute; width: 100.1%; height: 30px; background-color: rgba(78, 93, 108, 0.8); text-align: left; padding-left: 10px; border-radius: 10px 10px 0 0; z-index: 1;">python</div><button class="copy-button" data-clipboard-target="#' + i + '" style="position: absolute; top: 40px; right: 10px;"></button><pre id="' + i + '" style="background-color: black; color: white; padding-left: 15px; border-radius: 10px; width: 100%; z-index: 2; padding-top: 45px; padding-bottom: 15px;">' + e(o).textContent + "</pre></div>"
                            }
                            )).replace(/####\s*(.*?$)/gm, (function(t, e) {
                                return '<strong style="font-weight: 750; color: white;">' + e + "</strong>"
                            }
                            )).replace(/```shell([^`]+)```/g, (function(t, o) {
                                var i = "copyButton" + Math.random().toString(36).substr(2, 9);
                                return '<div style="position: relative; display: inline-block; width: 100%;"><div style="margin-left: -0.1px; position: absolute; width: 100.1%; height: 30px; background-color: rgba(78, 93, 108, 0.8); text-align: left; padding-left: 10px; border-radius: 10px 10px 0 0; z-index: 1;">shell</div><button class="copy-button" data-clipboard-target="#' + i + '" style="position: absolute; top: 40px; right: 10px;"></button><pre id="' + i + '" style="background-color: black; color: white; padding-left: 15px; border-radius: 10px; width: 100%; z-index: 2; padding-top: 45px; padding-bottom: 15px;">' + e(o).textContent + "</pre></div>"
                            }
                            )).replace(/```javascript([^`]+)```/g, (function(t, o) {
                                var i = "copyButton" + Math.random().toString(36).substr(2, 9);
                                return '<div style="position: relative; display: inline-block; width: 100%;"><div style="margin-left: -0.1px; position: absolute; width: 100.1%; height: 30px; background-color: rgba(78, 93, 108, 0.8); text-align: left; padding-left: 10px; border-radius: 10px 10px 0 0; z-index: 1;">javascript</div><button class="copy-button" data-clipboard-target="#' + i + '" style="position: absolute; top: 40px; right: 10px;"></button><pre id="' + i + '" style="background-color: black; color: white; padding-left: 15px; border-radius: 10px; width: 100%; z-index: 2; padding-top: 45px; padding-bottom: 15px;">' + e(o).textContent + "</pre></div>"
                            }
                            )).replace(/```js([^`]+)```/g, (function(t, o) {
                                var i = "copyButton" + Math.random().toString(36).substr(2, 9);
                                return '<div style="position: relative; display: inline-block; width: 100%;"><div style="margin-left: -0.1px; position: absolute; width: 100.1%; height: 30px; background-color: rgba(78, 93, 108, 0.8); text-align: left; padding-left: 10px; border-radius: 10px 10px 0 0; z-index: 1;">javascript</div><button class="copy-button" data-clipboard-target="#' + i + '" style="position: absolute; top: 40px; right: 10px;"></button><pre id="' + i + '" style="background-color: black; color: white; padding-left: 15px; border-radius: 10px; width: 100%; z-index: 2; padding-top: 45px; padding-bottom: 15px;">' + e(o).textContent + "</pre></div>"
                            }
                            )).replace(/```html([^`]+)```/g, (function(t, o) {
                                var i = "copyButton" + Math.random().toString(36).substr(2, 9);
                                return '<div style="position: relative; display: inline-block; width: 100%;"><div style="margin-left: -0.1px; position: absolute; width: 100.1%; height: 30px; background-color: rgba(78, 93, 108, 0.8); text-align: left; padding-left: 10px; border-radius: 10px 10px 0 0; z-index: 1;">html</div><button class="copy-button" data-clipboard-target="#' + i + '" style="position: absolute; top: 40px; right: 10px;"></button><pre id="' + i + '" style="background-color: black; color: white; padding-left: 15px; border-radius: 10px; width: 100%; z-index: 2; padding-top: 45px; padding-bottom: 15px;">' + e(o).textContent + "</pre></div>"
                            }
                            )).replace(/```css([^`]+)```/g, (function(t, o) {
                                var i = "copyButton" + Math.random().toString(36).substr(2, 9);
                                return '<div style="position: relative; display: inline-block; width: 100%;"><div style="margin-left: -0.1px; position: absolute; width: 100.1%; height: 30px; background-color: rgba(78, 93, 108, 0.8); text-align: left; padding-left: 10px; border-radius: 10px 10px 0 0; z-index: 1;">css</div><button class="copy-button" data-clipboard-target="#' + i + '" style="position: absolute; top: 40px; right: 10px;"></button><pre id="' + i + '" style="background-color: black; color: white; padding-left: 15px; border-radius: 10px; width: 100%; z-index: 2; padding-top: 45px; padding-bottom: 15px;">' + e(o).textContent + "</pre></div>"
                            }
                            )).replace(/```csharp([^`]+)```/g, (function(t, o) {
                                var i = "copyButton" + Math.random().toString(36).substr(2, 9);
                                return '<div style="position: relative; display: inline-block; width: 100%;"><div style="margin-left: -0.1px; position: absolute; width: 100.1%; height: 30px; background-color: rgba(78, 93, 108, 0.8); text-align: left; padding-left: 10px; border-radius: 10px 10px 0 0; z-index: 1;">csharp</div><button class="copy-button" data-clipboard-target="#' + i + '" style="position: absolute; top: 40px; right: 10px;"></button><pre id="' + i + '" style="background-color: black; color: white; padding-left: 15px; border-radius: 10px; width: 100%; z-index: 2; padding-top: 45px; padding-bottom: 15px;">' + e(o).textContent + "</pre></div>"
                            }
                            )).replace(/```bash([^`]+)```/g, (function(t, o) {
                                var i = "copyButton" + Math.random().toString(36).substr(2, 9);
                                return '<div style="position: relative; display: inline-block; width: 100%;"><div style="margin-left: -0.1px; position: absolute; width: 100.1%; height: 30px; background-color: rgba(78, 93, 108, 0.8); text-align: left; padding-left: 10px; border-radius: 10px 10px 0 0; z-index: 1;">bash</div><button class="copy-button" data-clipboard-target="#' + i + '" style="position: absolute; top: 40px; right: 10px;"></button><pre id="' + i + '" style="background-color: black; color: white; padding-left: 15px; border-radius: 10px; width: 100%; z-index: 2; padding-top: 45px; padding-bottom: 15px;">' + e(o).textContent + "</pre></div>"
                            }
                            )).replace(/```php([^`]+)```/g, (function(t, o) {
                                var i = "copyButton" + Math.random().toString(36).substr(2, 9);
                                return '<div style="position: relative; display: inline-block; width: 100%;"><div style="margin-left: -0.1px; position: absolute; width: 100.1%; height: 30px; background-color: rgba(78, 93, 108, 0.8); text-align: left; padding-left: 10px; border-radius: 10px 10px 0 0; z-index: 1;">php</div><button class="copy-button" data-clipboard-target="#' + i + '" style="position: absolute; top: 40px; right: 10px;"></button><pre id="' + i + '" style="background-color: black; color: white; padding-left: 15px; border-radius: 10px; width: 100%; z-index: 2; padding-top: 45px; padding-bottom: 15px;">' + e(o).textContent + "</pre></div>"
                            }
                                    //выделяет белым заключенное между **
//                            )).replace(/\*\*\*\*(.*?)\*\*\*\*/g, (function(t, e) {
//                                return '<strong style="font-weight: 750; color: white;">' + e + "</strong>"
//                            }
//                            )).replace(/\*\*(.*?)\*\*/g, (function(t, e) {
//                                return '<strong style="font-weight: 750; color: white;">' + e + "</strong>"
//                            }
//                            )).replace(/\*(.*?)\*/g, (function(t, e) {
//                                return '<strong style="font-weight: 750; color: white;">' + e + "</strong>"
//                            }
                            )).replace(/```([^`]+)```/g, (function(t, o) {
                                var i = "copyButton" + Math.random().toString(36).substr(2, 9);
                                return '<div style="position: relative; display: inline-block; width: 100%;"><div style="margin-left: -0.1px; position: absolute; width: 100.1%; height: 30px; background-color: rgba(78, 93, 108, 0.8); text-align: left; padding-left: 10px; border-radius: 10px 10px 0 0; z-index: 1;">python</div><button class="copy-button" data-clipboard-target="#' + i + '" style="position: absolute; top: 40px; right: 10px;"></button><pre id="' + i + '" style="background-color: black; color: white; padding-left: 15px; border-radius: 10px; width: 100%; z-index: 2; padding-top: 45px; padding-bottom: 15px;">' + e(o).textContent + "</pre></div>"
                            }
                            )).replace(/``([^`]+)``/g, (function(t, e) {
                                return "<mark>" + e + "</mark>"
                            }
                            )).replace(/`([^`]+)`/g, (function(t, e) {
                                return "<mark>" + e + "</mark>"
                            }
                            )),
                            g(r),
                            n.scrollTop = n.scrollHeight
                    }

    function u(t, e) {
        var o = document.createElement("div");
        o.className = e,
        o.style.whiteSpace = "pre-line";

        var i = /(https?:\/\/[^\s]+)/g;
        return t.split(i).forEach((function(t) {
            if (t.match(i)) {
                var e = document.createElement("span");
                e.textContent = t,
                e.classList.add("message-link"),
                e.addEventListener("click", (function() {
                    window.open(t, "_blank")
                }
                )),
                o.appendChild(e)
            } else {
                var n = document.createTextNode(t);
                o.appendChild(n)
            }
        }
        )),
        o
    }
    function g(t) {
        n.appendChild(t)
    }
    c()
}
));