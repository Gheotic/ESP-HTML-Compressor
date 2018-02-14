# Project Title

This Python script, minifies and converts HTML,CSS and Javascript files, to an char array of hex values. Which is to be stored in the ESP progmem.

## Getting Started

Create a folder for you HTML, CSS, Javascript files to go and call it "HTML".
Make sure files only use punctuation, for the file extensions. Eg. "jquery-3.3.1.js" is not allowed, change to something like: "jquery-3_3_1.js".
Next run "Convert.py" a file called "output_dir" would appear in the root directory, with the lines of code you need to copy into you ESP32/ESP8266 project.

the lines would look something like this:
```
const char* data_bootstrap_min_css_path PROGMEM = "/bootstrap/css/bootstrap_min.css";   <- The path of the file
const char data_bootstrap_min_css[] PROGMEM = {0X67,0X63,0X61,0X70,0X74....};           <- The array of minifed code
```

Implement the data
```
server.on(data_bootstrap_min_css_path, HTTP_GET, [](AsyncWebServerRequest *request){
    Serial.println("jquery.js requested");
    request->send_P(200, "text/css;charset=UTF-8", data_bootstrap_min_css);
  });
```


### Prerequisites

Only tested: Python 3.5


## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Authors

* **Gheotic** - *Initial work* - [Gheotic](https://github.com/Gheotic)

See also the list of [contributors](https://github.com/Gheotic/ESP-HTML-Compressor/graphs/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

