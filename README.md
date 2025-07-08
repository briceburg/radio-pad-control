# radio-pad-control

Remotely control [radio-pad](https://github.com/briceburg/radio-pad) through a simple web and/or mobile application.

## Overview

* [redis](https://redis.io/) pub/sub is used as an event-driven communication bus.
  * remote controls (aka radio-pad-control mobile or web clients) publish requested stations to the "station-request" channel by calling the [broadcast](./runfn/broadcast/) function.
  * the [radio-pad](https://github.com/briceburg/radio-pad) script listens (subscribes) to the "station-request" channel and attempts to play the requested station.
  * upon successful station changes, radio-pad will broadcast the currently playing station to the "station-playing" channel.
  * remote controls listen to the "station-playing" channel over websockets connected to the the [switchboard](./runfn/switchboard/) function, and update their UI on changes.
* [capacitor](https://capacitorjs.com) and [ionic framework](https://ionicframework.com/) v8 support native mobile app building from a common the web source.
  * VanillaJS is used instead of react/angular. this is a KISS project.

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
