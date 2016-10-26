var system = require('system');
var page = new WebPage(),
    address, output, size;
 
if (system.args.length < 2 || system.args.length > 3) {
    console.log('Usage: rasterize.js URL filename');
    phantom.exit();
} else {
    address = system.args[1];
    output = system.args[2];
		page.paperSize = {
			format: 'A4',
			orientation: 'portrait',
			border: '1.5cm'
		};

    page.onConsoleMessage = function(msg) { console.log(msg); };
    page.settings.userAgent = 'Mozilla/5.0 (Windows NT 6.0; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.75 Safari/535.7';
    page.open(address, function (status) {
        if (status !== 'success') {
            console.log('Unable to load the address!');
        } else {
            window.setTimeout(function () {
                page.render(output);
                phantom.exit();
            }, 50);
        }
    });
}
