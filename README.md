# Overview

This repo contains a Flask app as a part of [that](https://github.com/oleg1995petrov/devops-andersen-training/tree/master/HW%202) task.  

The app should receive `json` object and return strings in the following manner:

```bash
# request
curl -XPOST -d '{"animal": "cow", "sound": "mooo", "count": 3}' myvm.localhost

# repsonse
cow says mooo
cow says mooo
cow says mooo
Made with     by %my_name

# request
curl -XPOST -d '{"animal": "elephant", "sound": "whoooaaa", "count": 5}' myvm.localhost

# repsonse
elephant says whoooaaa
elephant says whoooaaa
elephant says whoooaaa
elephant says whoooaaa
elephant says whoooaaa
Made with     by %my_name

```
![logo](https://github.com/oleg1995petrov/fkask-app-for-devops-course/tree/master/logo.png)