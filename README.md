# radio-pad-control

Remotely control [radio-pad](https://github.com/briceburg/radio-pad) through a simple web and/or mobile application.

## Overview

* [redis](https://redis.io/) pub/sub is used as an event-driven communication bus.
  * radio-pad-control (mobile or web) publishes requested stations to the "now playing" channel by calling a google cloud run function.
  * the radio-pad script listens (subscribes) to the "now-playing" channel and plays the requested station on changes.
* [capacitor](https://capacitorjs.com) along with [ionic framework](https://ionicframework.com/) v8 are used to build native mobile apps from the web source. VanillaJS is used instead of react/angular. this is a KISS project.

## Usage

### Configure the Application

```bash
npm install
npx cap add android
```

### Running the Application

**Web/Local Development:**

To run the app in a local web browser for development and testing:

```bash
npm start
```

**Android:**

> requires an Android SDK

To build and run the application on an Android device or emulator:

```bash
npm run build
npx cap run android
```
